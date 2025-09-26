import os

# ===== Hardcoded defaults =====
# 여기에 디스코드 웹훅 URL을 '하드코딩' 하세요.
# 예) DEFAULT_WEBHOOK = "https://discord.com/api/webhooks/...."
DEFAULT_WEBHOOK = "https://discord.com/api/webhooks/1418298773330985154/_I7EzXpGMundYt8jCvlDdzi9INsBkBq7NSDM74iV0Y_flSzQZ5LxYP0lZtXFzHCkRtKR"

# 리슨 주소 기본값 (환경변수 LISTEN_ADDR로 덮어쓰기 가능)
DEFAULT_LISTEN = os.environ.get("LISTEN_ADDR", "0.0.0.0:1080")
