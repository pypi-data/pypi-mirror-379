import os
import json
import time
import requests
from typing import Optional, Tuple, Dict, Any

LINE_PUSH_URL = "https://api.line.me/v2/bot/message/push"

class NotiPy:
    """
    Minimal LINE Messaging API pusher.

    Provide channel access token and a LINE userId (or group/room id). Defaults
    can be read from env vars:
      - NOTIPY_CHANNEL_ACCESS_TOKEN
      - NOTIPY_USER_ID

    Usage:
        from notipy_line import NotiPy
        noti = NotiPy()  # reads from env
        noti.notify_text("✅ Training finished.")
    """
    def __init__(
        self,
        access_token: Optional[str] = None,
        user_id: Optional[str] = None,
        timeout: int = 15,
    ) -> None:
        self.access_token = (access_token or os.getenv("NOTIPY_CHANNEL_ACCESS_TOKEN","")).strip()
        self.user_id = (user_id or os.getenv("NOTIPY_USER_ID","")).strip()
        self.timeout = int(timeout)
        if not self.access_token or not self.user_id:
            raise ValueError("Missing credentials. Set NOTIPY_CHANNEL_ACCESS_TOKEN and NOTIPY_USER_ID or pass arguments.")

    def _post(self, payload: Dict[str, Any]) -> Tuple[int, str]:
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        resp = requests.post(LINE_PUSH_URL, headers=headers, json=payload, timeout=self.timeout)
        return resp.status_code, resp.text

    def notify_text(self, message: str) -> Tuple[int, str]:
        data = {"to": self.user_id, "messages": [{"type": "text", "text": str(message)}]}
        return self._post(data)

    def notify_on_finish(self, func):
        """
        Decorator that sends a LINE message when a function finishes.
        """
        def wrapper(*args, **kwargs):
            t0 = time.time()
            try:
                result = func(*args, **kwargs)
                secs = time.time() - t0
                self.notify_text(f"✅ {func.__name__} finished in {secs:.2f}s")
                return result
            except Exception as e:
                secs = time.time() - t0
                self.notify_text(f"❌ {func.__name__} failed in {secs:.2f}s: {e}")
                raise
        return wrapper
