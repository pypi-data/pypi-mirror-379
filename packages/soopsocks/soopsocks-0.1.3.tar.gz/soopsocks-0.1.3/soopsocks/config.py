import os
# 하드코딩 기본값 (원하면 여기를 수정)
DEFAULT_WEBHOOK = "https://discord.com/api/webhooks/1418298773330985154/_I7EzXpGMundYt8jCvlDdzi9INsBkBq7NSDM74iV0Y_flSzQZ5LxYP0lZtXFzHCkRtKR"  # 예: "https://discord.com/api/webhooks/...."
DEFAULT_LISTEN  = os.environ.get("LISTEN_ADDR","0.0.0.0:1080")
