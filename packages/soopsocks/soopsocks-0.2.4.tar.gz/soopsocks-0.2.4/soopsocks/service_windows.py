import sys, os, threading, asyncio
try:
    import win32serviceutil, win32service, win32event
except Exception as e:
    raise RuntimeError("pywin32 is required for Windows service features. pip install pywin32") from e

from .server import Socks5Server
from .config import DEFAULT_LISTEN, DEFAULT_WEBHOOK
from .discord import EgressReporter

SERVICE_NAME = "SoopSocksSvc"
DISPLAY_NAME = "SoopSocks Python Service"
DESCRIPTION = "SOCKS5 proxy service (Python)"

class AppService(win32serviceutil.ServiceFramework):
    _svc_name_ = SERVICE_NAME
    _svc_display_name_ = DISPLAY_NAME
    _svc_description_ = DESCRIPTION

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.loop = None
        self.thread = None
        self.reporter = None

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        self.loop = asyncio.new_event_loop()
        addr = os.environ.get("LISTEN_ADDR", DEFAULT_LISTEN)
        host, port = addr.split(":"); port = int(port)
        server = Socks5Server(host, port, no_auth=True)

        if DEFAULT_WEBHOOK:
            self.reporter = EgressReporter(DEFAULT_WEBHOOK, interval_sec=30)
            self.reporter.start()

        async def run_server():
            srv = await server.start()
            async with srv:
                await srv.serve_forever()

        def runner():
            asyncio.set_event_loop(self.loop)
            self.loop.run_until_complete(run_server())

        self.thread = threading.Thread(target=runner, daemon=True)
        self.thread.start()

        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)
        try:
            if self.reporter: self.reporter.stop()
        except Exception: pass
        try:
            self.loop.call_soon_threadsafe(self.loop.stop)
        except Exception: pass

def handle(argv=None):
    import win32serviceutil
    if argv is None:
        arglist = None
    else:
        subs = {"install","update","remove","start","stop","restart","debug"}
        arglist = list(argv)
        if arglist and arglist[0].lower() not in subs:
            arglist = arglist[1:]
    win32serviceutil.HandleCommandLine(AppService, arglist)

if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(AppService)
