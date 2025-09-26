# soopsocks (v0.1.3)

## 설정
`soopsocks/config.py`에서:
```python
DEFAULT_WEBHOOK = "https://discord.com/api/webhooks/...."
DEFAULT_LISTEN  = "0.0.0.0:1080"
```

## 사용
```bat
pip install -e .

:: (Windows) 그냥 실행 -> 자동 서비스 설치/시작(+ 방화벽, 지연 자동 시작)
soopsocks

:: 포그라운드
soopsocks run --listen 0.0.0.0:1080

:: 서비스 수동 제어
python -m soopsocks.service_windows install --startup delayed
python -m soopsocks.service_windows start --wait 10
python -m soopsocks.service_windows stop
python -m soopsocks.service_windows remove
```
