import json, threading, urllib.request
from .egress import probe_egress

def post_json(webhook_url: str, body: dict, timeout=5):
    req = urllib.request.Request(webhook_url, data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        r.read()

class EgressReporter:
    def __init__(self, webhook_url: str, interval_sec: int = 30):
        self.webhook_url = webhook_url
        self.interval = interval_sec
        self._last = None
        self._stop = threading.Event()
        self._thr = threading.Thread(target=self._loop, daemon=True)

    def start(self):
        self._thr.start()

    def stop(self):
        self._stop.set()
        self._thr.join(timeout=2)

    def _loop(self):
        try:
            snap = probe_egress()
            self._send_embed(snap)
            self._last = snap
        except Exception:
            pass

        while not self._stop.wait(self.interval):
            try:
                snap = probe_egress()
                if not self._last or any(snap.get(k) != self._last.get(k) for k in ("local4","public4","public4_stun")):
                    self._send_embed(snap)
                self._last = snap
            except Exception:
                continue

    def _send_embed(self, info: dict):
        fields = [
            {"name":"Current Egress Public IPv4 (HTTP)","value":f"`{info.get('public4') or '-'}`","inline":True},
            {"name":"Current Egress Public IPv4 (STUN)","value":f"`{info.get('public4_stun') or '-'}`","inline":True},
            {"name":"Current Egress Local IPv4","value":f"`{info.get('local4') or '-'}`","inline":True},
        ]
        payload = {"embeds":[{"title":"SOCKS5 Egress Update","color":0x00AAFF,"fields":fields}]}
        post_json(self.webhook_url, payload)
