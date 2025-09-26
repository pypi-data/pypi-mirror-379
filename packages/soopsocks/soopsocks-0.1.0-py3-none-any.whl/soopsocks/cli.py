import argparse, os, sys, asyncio, platform, subprocess

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
    # Relaunch current command as elevated (UAC) using PowerShell
    ps = ["powershell.exe","-NoProfile","-ExecutionPolicy","Bypass","-Command",
          "Start-Process -FilePath '%s' -ArgumentList '%s' -Verb RunAs" % (
              sys.executable.replace("'", "''"),
              ("-m soopsocks " + " ".join(extra_args)).replace("'", "''")
          )]
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

def cmd_service(_args):
    if platform.system() != "Windows":
        print("Windows only."); sys.exit(1)
    try:
        from . import service_windows as svc
    except RuntimeError as e:
        print(str(e)); sys.exit(1)
    svc.handle()

def cmd_auto(_args):
    # Windows: ensure firewall, install service, set delayed-auto, start service
    if platform.system() != "Windows":
        print("`auto`는 Windows에서만 서비스 설치를 수행합니다.")
        print("대신 포그라운드 실행:  soopsocks run --listen 0.0.0.0:1080")
        return

    if not _is_admin_windows():
        print("관리자 권한이 필요합니다. UAC 상승을 시도합니다...")
        _elevate_and_rerun(["auto"])
        return

    # 1) 방화벽 규칙
    ensure_firewall_rules(sys.executable)

    # 2) 서비스 설치/시작
    from . import service_windows as svc
    try:
        svc.handle(["soopsocks","install"])
    except SystemExit:
        pass
    try:
        svc.handle(["soopsocks","start"])
    except SystemExit:
        pass

    # 3) 지연 자동 시작
    try:
        CREATE_NO_WINDOW = 0x08000000
        subprocess.run(["sc","config", SERVICE_NAME, "start=", "delayed-auto"],
                       check=False, creationflags=CREATE_NO_WINDOW,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception:
        pass

    print("서비스 설치 및 시작 완료. (지연 자동 시작 설정됨)")

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
    ps.set_defaults(func=cmd_service)

    pa = sub.add_parser("auto", help="(Windows) Install + start service, set delayed-auto, ensure firewall")
    pa.set_defaults(func=cmd_auto)

    args = p.parse_args(argv)
    if not args.cmd:
        # No subcommand: Windows에서는 자동 설치 모드, 그 외는 도움말
        if platform.system() == "Windows":
            return cmd_auto(args)
        p.print_help(); return
    args.func(args)
