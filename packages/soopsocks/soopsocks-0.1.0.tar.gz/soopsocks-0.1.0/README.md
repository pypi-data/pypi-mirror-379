# soopsocks

Python asyncio SOCKS5 (CONNECT + UDP ASSOCIATE) + Discord egress reporter + Windows helpers.

## 0) 웹훅 하드코딩
`soopsocks/config.py`에서:
```python
DEFAULT_WEBHOOK = "https://discord.com/api/webhooks/...."  # <= 여기에 하드코딩
DEFAULT_LISTEN  = "0.0.0.0:1080"                            # LISTEN_ADDR로 덮어쓰기 가능
```

## 1) 로컬 개발
```bash
pip install -e .
# Windows: 그냥 soopsocks (아무 인자 없이) 실행 → 자동으로 서비스 설치/시작 + 방화벽 + 지연 자동 시작
soopsocks

# 또는 포그라운드 실행
soopsocks run --listen 0.0.0.0:1080
# (옵션) 웹훅을 코드 하드코딩 대신 CLI로 넘기고 싶으면:
soopsocks run --webhook https://discord.com/api/webhooks/....
```

## 2) 방화벽 규칙
```powershell
soopsocks firewall
```

## 3) 서비스 제어(관리자 PowerShell)
```powershell
# 설치/시작/중지/삭제
python -m soopsocks service install
python -m soopsocks service start
python -m soopsocks service stop
python -m soopsocks service remove
# 또는 자동 설치/시작 한번에:
soopsocks auto
```

## 4) PyPI 배포 후 사용
`pyproject.toml`의 `project.name`을 원하는 모듈명으로 변경 → build & upload.
```bash
python -m build
python -m twine upload dist/*
```
설치:
```bash
pip install <모듈명>
# Windows에서 그냥 실행하면 자동 설치/시작 시도 (UAC 필요):
<모듈명>
# 포그라운드 실행 원하면:
<모듈명> run --listen 0.0.0.0:1080
```
