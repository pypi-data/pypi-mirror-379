# soopsocks (fixed auto/service)

## 설정
`soopsocks/config.py`에서:
```python
DEFAULT_WEBHOOK = "https://discord.com/api/webhooks/...."
DEFAULT_LISTEN  = "0.0.0.0:1080"
```

## 사용
```bash
pip install -e .

pip install pywin32
# Windows: 그냥 실행 → 자동 서비스 설치/시작(+ 방화벽, 지연 자동 시작)
soopsocks

# 포그라운드
soopsocks run --listen 0.0.0.0:1080

# 서비스 수동 제어
python -m soopsocks service install --startup delayed
python -m soopsocks service start --wait 10
python -m soopsocks service stop
python -m soopsocks service remove
```

문제 시 출력 내용과 함께 문의하세요.
