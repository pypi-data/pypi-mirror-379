import socket, time, struct, ipaddress, urllib.request, contextlib

PUBLIC_IP_ENDPOINTS = [
    "https://api.ipify.org",
    "https://ifconfig.me/ip",
    "https://checkip.amazonaws.com",
    "https://ipinfo.io/ip",
]

def pick_local_ipv4_by_route(timeout=2.0):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(timeout)
    try:
        s.connect(("1.1.1.1", 80))
        return s.getsockname()[0]
    finally:
        s.close()

def fetch_public_ipv4_http(timeout=3.0):
    for url in PUBLIC_IP_ENDPOINTS:
        try:
            with contextlib.closing(urllib.request.urlopen(url, timeout=timeout)) as r:
                ip = r.read().decode().strip()
                ipaddress.IPv4Address(ip)
                return ip
        except Exception:
            continue
    return ""

def fetch_public_ipv4_stun(lip: str, server=("stun.l.google.com", 19302), timeout=2.0):
    try:
        txid = b"PYSTUNXOR12"
        msg_type = 0x0001; msg_len = 0; cookie = 0x2112A442
        header = struct.pack("!HHI12s", msg_type, msg_len, cookie, txid)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); sock.bind((lip, 0)); sock.settimeout(timeout)
        sock.sendto(header, server)
        data, _ = sock.recvfrom(2048); sock.close()
        if len(data) < 20: return ""
        body = memoryview(data)[20:]
        while len(body) >= 4:
            atype, alen = struct.unpack_from("!HH", body, 0); body = body[4:]
            aval = body[:alen]; body = body[(alen + 3) & ~3:]
            if atype == 0x0020:  # XOR-MAPPED-ADDRESS
                fam = aval[1]; _ = struct.unpack_from("!H", aval, 2)[0] ^ (cookie >> 16)
                if fam == 0x01 and len(aval) >= 8:
                    raw = struct.unpack_from("!I", aval, 4)[0] ^ cookie
                    return socket.inet_ntoa(struct.pack("!I", raw))
        return ""
    except Exception:
        return ""

def probe_egress():
    loc = pick_local_ipv4_by_route() or ""
    pub = fetch_public_ipv4_http() or ""
    stun = fetch_public_ipv4_stun(loc) if loc else ""
    return {"local4": loc, "public4": pub, "public4_stun": stun, "time": time.time()}
