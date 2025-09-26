import asyncio
import ipaddress
import struct
import socket
from typing import Tuple, Optional, Dict

SOCKS_VERSION = 5
NO_AUTH = 0x00

ATYP_IPV4 = 0x01
ATYP_DOMAIN = 0x03
ATYP_IPV6 = 0x04

CMD_CONNECT = 0x01
CMD_BIND = 0x02
CMD_UDP_ASSOC = 0x03

REP_SUCCEEDED = 0x00
REP_GENERAL_FAIL = 0x01
REP_COMMAND_NOT_SUPPORTED = 0x07
REP_ADDR_TYPE_NOT_SUPPORTED = 0x08

class UDPRelay:
    def __init__(self, bind_host="0.0.0.0"):
        self.bind_host = bind_host
        self.transport: Optional[asyncio.DatagramTransport] = None
        self.loop = asyncio.get_event_loop()
        self._client_addr: Optional[Tuple[str, int]] = None

    def connection_made(self, transport: asyncio.DatagramTransport):
        self.transport = transport

    def datagram_received(self, data: bytes, addr: Tuple[str, int]):
        if len(data) < 4:
            return
        rsv, frag, atyp = data[0:2], data[2], data[3]
        if rsv != b"\x00\x00" or frag != 0:
            return

        idx = 4
        dst_addr = None
        if atyp == ATYP_IPV4:
            if len(data) < idx + 4:
                return
            dst_addr = socket.inet_ntoa(data[idx:idx+4])
            idx += 4
        elif atyp == ATYP_DOMAIN:
            if len(data) < idx + 1:
                return
            ln = data[idx]
            idx += 1
            if len(data) < idx + ln:
                return
            dst_addr = data[idx:idx+ln].decode("utf-8", "ignore")
            idx += ln
        elif atyp == ATYP_IPV6:
            if len(data) < idx + 16:
                return
            dst_addr = socket.inet_ntop(socket.AF_INET6, data[idx:idx+16])
            idx += 16
        else:
            return

        if len(data) < idx + 2:
            return
        dst_port = struct.unpack("!H", data[idx:idx+2])[0]
        idx += 2
        payload = data[idx:]

        if self._client_addr is None:
            self._client_addr = addr

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1.5)
            sock.sendto(payload, (dst_addr, dst_port))
            try:
                resp, raddr = sock.recvfrom(65535)
            except socket.timeout:
                resp = None
            finally:
                sock.close()

            if resp is not None and self.transport and self._client_addr:
                try:
                    ipaddress.IPv4Address(raddr[0])
                    atype = ATYP_IPV4
                    packed = socket.inet_aton(raddr[0])
                except ipaddress.AddressValueError:
                    try:
                        ipaddress.IPv6Address(raddr[0])
                        atype = ATYP_IPV6
                        packed = socket.inet_pton(socket.AF_INET6, raddr[0])
                    except ipaddress.AddressValueError:
                        atype = ATYP_DOMAIN
                        domain = raddr[0].encode()
                        packed = bytes([len(domain)]) + domain

                header = b"\x00\x00" + bytes([0]) + bytes([atype])
                header += packed
                header += struct.pack("!H", raddr[1])
                self.transport.sendto(header + resp, self._client_addr)
        except Exception:
            pass

    async def start(self) -> Tuple[str, int]:
        loop = asyncio.get_running_loop()
        transport, _ = await loop.create_datagram_endpoint(lambda: self, local_addr=(self.bind_host, 0))
        self.transport = transport
        sock = transport.get_extra_info("socket")
        return sock.getsockname()

    def close(self):
        if self.transport:
            self.transport.close()


class Socks5Server:
    def __init__(self, host: str = "0.0.0.0", port: int = 1080, no_auth: bool = True):
        self.host = host
        self.port = port
        self.no_auth = no_auth
        self._server: Optional[asyncio.base_events.Server] = None
        self._udp_relays: Dict[asyncio.StreamWriter, UDPRelay] = {}

    async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        try:
            ver = (await reader.readexactly(1))[0]
            if ver != SOCKS_VERSION:
                writer.close(); await writer.wait_closed(); return
            nmethods = (await reader.readexactly(1))[0]
            methods = await reader.readexactly(nmethods)
            if self.no_auth and NO_AUTH in methods:
                writer.write(bytes([SOCKS_VERSION, NO_AUTH])); await writer.drain()
            else:
                writer.write(bytes([SOCKS_VERSION, 0xFF])); await writer.drain()
                writer.close(); await writer.wait_closed(); return

            req = await reader.readexactly(4)
            ver, cmd, _rsv, atyp = req
            if ver != SOCKS_VERSION:
                writer.close(); await writer.wait_closed(); return

            if atyp == ATYP_IPV4:
                addr = socket.inet_ntoa(await reader.readexactly(4))
            elif atyp == ATYP_DOMAIN:
                ln = (await reader.readexactly(1))[0]
                addr = (await reader.readexactly(ln)).decode("utf-8", "ignore")
            elif atyp == ATYP_IPV6:
                addr = socket.inet_ntop(socket.AF_INET6, await reader.readexactly(16))
            else:
                await self._reply(writer, REP_ADDR_TYPE_NOT_SUPPORTED, "0.0.0.0", 0)
                writer.close(); await writer.wait_closed(); return

            port = struct.unpack("!H", await reader.readexactly(2))[0]

            if cmd == CMD_CONNECT:
                await self._handle_connect(addr, port, reader, writer)
            elif cmd == CMD_UDP_ASSOC:
                await self._handle_udp_associate(reader, writer)
            else:
                await self._reply(writer, REP_COMMAND_NOT_SUPPORTED, "0.0.0.0", 0)
                writer.close(); await writer.wait_closed()
        except asyncio.IncompleteReadError:
            try:
                writer.close(); await writer.wait_closed()
            except Exception:
                pass
        except Exception:
            try:
                writer.close(); await writer.wait_closed()
            except Exception:
                pass
        finally:
            relay = self._udp_relays.pop(writer, None)
            if relay:
                relay.close()

    async def _handle_connect(self, addr: str, port: int, reader, writer):
        try:
            r = await asyncio.open_connection(addr, port)
        except Exception:
            await self._reply(writer, REP_GENERAL_FAIL, "0.0.0.0", 0)
            writer.close(); await writer.wait_closed(); return

        sock = r[1].get_extra_info("socket")
        lhost, lport = sock.getsockname()[:2]
        await self._reply(writer, REP_SUCCEEDED, lhost, lport)

        remote_reader, remote_writer = r

        async def pipe(src, dst):
            try:
                while True:
                    data = await src.read(65536)
                    if not data:
                        break
                    dst.write(data); await dst.drain()
            except Exception:
                pass
            finally:
                try:
                    dst.close(); await dst.wait_closed()
                except Exception:
                    pass

        await asyncio.gather(
            pipe(reader, remote_writer),
            pipe(remote_reader, writer),
        )

    async def _handle_udp_associate(self, reader, writer):
        relay = UDPRelay(bind_host="0.0.0.0")
        bind_host, bind_port = await relay.start()
        self._udp_relays[writer] = relay
        await self._reply(writer, REP_SUCCEEDED, bind_host, bind_port)
        try:
            await reader.read()
        finally:
            relay.close()

    async def _reply(self, writer, rep_code: int, bnd_addr: str, bnd_port: int):
        try:
            ip = ipaddress.ip_address(bnd_addr)
            atyp = ATYP_IPV6 if ip.version == 6 else ATYP_IPV4
        except ValueError:
            atyp = ATYP_DOMAIN

        resp = bytearray([SOCKS_VERSION, rep_code, 0x00])
        if atyp == ATYP_IPV4:
            resp += bytes([ATYP_IPV4]) + socket.inet_aton(bnd_addr)
        elif atyp == ATYP_IPV6:
            resp += bytes([ATYP_IPV6]) + socket.inet_pton(socket.AF_INET6, bnd_addr)
        else:
            domain = bnd_addr.encode("utf-8")
            resp += bytes([ATYP_DOMAIN, len(domain)]) + domain
        resp += struct.pack("!H", bnd_port)
        writer.write(resp); await writer.drain()

    async def start(self):
        self._server = await asyncio.start_server(self.handle_client, self.host, self.port)
        return self._server

    async def serve_forever(self):
        srv = await self.start()
        addrs = ", ".join(str(s.getsockname()) for s in (srv.sockets or []))
        print(f"SOCKS5 listening on {addrs}")
        async with srv:
            await srv.serve_forever()


async def main(listen: str = "0.0.0.0:1080", no_auth: bool = True):
    host, port = listen.split(":")
    port = int(port)
    server = Socks5Server(host, port, no_auth=no_auth)
    await server.serve_forever()
