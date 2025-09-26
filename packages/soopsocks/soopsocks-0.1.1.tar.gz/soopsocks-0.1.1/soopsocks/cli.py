import argparse, os, sys, asyncio, platform, subprocess, shlex

from .server import main as run_server_main
from .firewall import ensure_firewall_rules
from .egress import probe_egress
from .discord import EgressReporter
from .config import DEFAULT_WEBHOOK, DEFAULT_LISTEN

SERVICE_NAME = "SoopSocksSvc"

def _is_admin_windows():
    if platform.system() != "Windows":
        return False
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

def _elevate_and_rerun(extra_args):
    args = ["-m", "soopsocks"] + extra_args
    cmd = " ".join(shlex.quote(a) for a in args)
    ps = ["powershell.exe","-NoProfile","-ExecutionPolicy","Bypass","-Command",
          f"Start-Process -FilePath '{sys.executable}' -ArgumentList '{cmd}' -Verb RunAs"]
    subprocess.run(ps, check=False)

def cmd_run(args):
    listen = args.listen or DEFAULT_LISTEN
    webhook = args.webhook or DEFAULT_WEBHOOK
    reporter = None
    if webhook:
        reporter = EgressReporter(webhook, interval_sec=30)
        reporter.start()
    try:
        asyncio.run(run_server_main(listen, True))
    finally:
        if reporter:
            reporter.stop()

def cmd_firewall(_args):
    prog = sys.executable
    ensure_firewall_rules(prog)
    print("Firewall rules ensured for port 1080.")

def cmd_egress(_args):
    print(probe_egress())

def cmd_service(args):
    try:
        from . import service_windows as svc
    except RuntimeError as e:
        print(str(e)); sys.exit(1)
    argv = ["soopsocks"] + (args.svcargs or [])
    svc.handle(argv)

def _run_and_check(cmdlist, hide=True):
    CREATE_NO_WINDOW = 0x08000000
    kw = dict(check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if hide and platform.system() == "Windows":
        kw["creationflags"] = CREATE_NO_WINDOW
    return subprocess.run(cmdlist, **kw)

def _service_running():
    if platform.system() != "Windows":
        return False
    r = _run_and_check(["sc","query", SERVICE_NAME])
    txt = (r.stdout or b"").decode(errors="ignore")
    return "RUNNING" in txt

def cmd_auto(_args):
    if platform.system() != "Windows":
        print("`auto`는 Windows에서만 서비스 설치를 수행합니다.")
        print("대신 포그라운드 실행:  soopsocks run --listen 0.0.0.0:1080")
        return

    if not _is_admin_windows():
        print("관리자 권한이 필요합니다. UAC 상승을 시도합니다...")
        _elevate_and_rerun(["auto"])
        return

    ensure_firewall_rules(sys.executable)

    install = _run_and_check([sys.executable,"-m","soopsocks","service","install","--startup","delayed"], hide=True)
    start   = _run_and_check([sys.executable,"-m","soopsocks","service","start","--wait","10"], hide=True)

    if _service_running():
        print("서비스 설치 및 시작 완료. (지연 자동 시작 설정됨)")
    else:
        print("서비스 설치/시작에 실패했습니다.")
        print("설치 출력:\n", (install.stdout or b'').decode(errors="ignore"))
        print("설치 에러:\n", (install.stderr or b'').decode(errors="ignore"))
        print("시작 출력:\n", (start.stdout or b'').decode(errors="ignore"))
        print("시작 에러:\n", (start.stderr or b'').decode(errors="ignore"))
        print("수동 실행 예시:")
        print("  python -m soopsocks service install --startup delayed")
        print("  python -m soopsocks service start --wait 10")

def main(argv=None):
    p = argparse.ArgumentParser(prog="soopsocks",
        description="SOCKS5 server (Python) with optional Discord egress reporter")
    sub = p.add_subparsers(dest="cmd")

    prun = sub.add_parser("run", help="Run SOCKS5 server in foreground")
    prun.add_argument("--listen", default=DEFAULT_LISTEN,
                      help="Listen address, default from LISTEN_ADDR or 0.0.0.0:1080")
    prun.add_argument("--webhook", help="Discord webhook URL to send egress updates")
    prun.set_defaults(func=cmd_run)

    pfw = sub.add_parser("firewall", help="Add inbound firewall rules for TCP/UDP 1080")
    pfw.set_defaults(func=cmd_firewall)

    pe = sub.add_parser("egress", help="Print current egress info (HTTP+STUN)")
    pe.set_defaults(func=cmd_egress)

    ps = sub.add_parser("service", help="Windows service control (install/start/stop/remove via pywin32)")
    ps.add_argument("svcargs", nargs=argparse.REMAINDER, help="pass-through to pywin32: install|start|stop|remove ...")
    ps.set_defaults(func=cmd_service)

    pa = sub.add_parser("auto", help="(Windows) Install + start service, set delayed-auto, ensure firewall")
    pa.set_defaults(func=cmd_auto)

    args = p.parse_args(argv)
    if not args.cmd:
        if platform.system() == "Windows":
            return cmd_auto(args)
        p.print_help(); return
    args.func(args)
