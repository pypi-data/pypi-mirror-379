import subprocess, sys

RULE_TCP = "SoopSocks TCP 1080"
RULE_UDP = "SoopSocks UDP 1080"

def _run_hidden(cmd):
    CREATE_NO_WINDOW = 0x08000000
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=CREATE_NO_WINDOW)

def _pwsh_available():
    for exe in ("powershell.exe","pwsh.exe"):
        try:
            subprocess.run([exe,"-NoProfile","-Command","$PSVersionTable.PSVersion.Major"],
                           stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=2)
            return exe
        except Exception:
            continue
    return None

def ensure_firewall_rules(program_path: str):
    exe = _pwsh_available()
    if exe:
        ps = rf"""
$e = '{program_path}'
if (-not (Get-NetFirewallRule -DisplayName '{RULE_TCP}' -ErrorAction SilentlyContinue)) {{
  New-NetFirewallRule -DisplayName '{RULE_TCP}' -Direction Inbound -Action Allow -Protocol TCP -LocalPort 1080 -Program $e -Profile Any | Out-Null
}}
if (-not (Get-NetFirewallRule -DisplayName '{RULE_UDP}' -ErrorAction SilentlyContinue)) {{
  New-NetFirewallRule -DisplayName '{RULE_UDP}' -Direction Inbound -Action Allow -Protocol UDP -LocalPort 1080 -Program $e -Profile Any | Out-Null
}}
"""
        _run_hidden([exe,"-NoProfile","-NonInteractive","-ExecutionPolicy","Bypass","-Command", ps])
        return True
    _run_hidden(["netsh","advfirewall","firewall","add","rule",
                 f"name={RULE_TCP}","dir=in","action=allow","protocol=TCP",
                 "localport=1080",f"program={program_path}","enable=yes","profile=any"])
    _run_hidden(["netsh","advfirewall","firewall","add","rule",
                 f"name={RULE_UDP}","dir=in","action=allow","protocol=UDP",
                 "localport=1080",f"program={program_path}","enable=yes","profile=any"])
    return True
