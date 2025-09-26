import subprocess, platform

TASK_NAME = "SoopSocksAuto"

def _run(cmd):
    CREATE_NO_WINDOW = 0x08000000
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          creationflags=CREATE_NO_WINDOW if platform.system()=="Windows" else 0, check=False)

def ensure_task(command_line: str, ru_system: bool=True, onstart: bool=True, onlogon: bool=True):
    if platform.system() != "Windows":
        return False, "Windows only"

    _run(["schtasks","/Delete","/TN",TASK_NAME,"/F"])

    ok = False
    msgs = []

    if onstart:
        cmd = ["schtasks","/Create","/TN",TASK_NAME,"/SC","ONSTART","/TR",command_line,"/F"]
        if ru_system:
            cmd += ["/RU","SYSTEM"]
        r = _run(cmd)
        msgs.append((b"START", r.stdout, r.stderr))
        ok = ok or (r.returncode==0)

    if onlogon:
        cmd = ["schtasks","/Create","/TN",TASK_NAME,"/SC","ONLOGON","/TR",command_line,"/RL","HIGHEST","/F"]
        if ru_system:
            cmd += ["/RU","SYSTEM"]
        r = _run(cmd)
        msgs.append((b"LOGON", r.stdout, r.stderr))
        ok = ok or (r.returncode==0)

    if ok:
        _run(["schtasks","/Run","/TN",TASK_NAME])
        return True, msgs
    return False, msgs
