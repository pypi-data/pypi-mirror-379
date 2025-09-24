import os
import time
from contextlib import contextmanager
from typing import Tuple, Optional, Dict, Any, Callable
import requests
from functools import wraps

LINE_PUSH_URL = "https://api.line.me/v2/bot/message/push"

class NotiPy:
    """LINE Messaging API only."""
    def __init__(
        self,
        channel_access_token: Optional[str] = None,
        user_id: Optional[str] = None,
    ):
        self.token = (channel_access_token or os.getenv("NOTIPY_CHANNEL_ACCESS_TOKEN", "")).strip()
        self.user_id = (user_id or os.getenv("NOTIPY_USER_ID", "")).strip()
        if not self.token:
            raise ValueError("channel_access_token required. Set arg or NOTIPY_CHANNEL_ACCESS_TOKEN.")
        if not self.user_id:
            raise ValueError("user_id required. Set arg or NOTIPY_USER_ID.")

    # ---------------- Core send ----------------
    def _post(self, payload: Dict[str, Any]) -> Tuple[int, str]:
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        resp = requests.post(LINE_PUSH_URL, headers=headers, json=payload, timeout=15)
        return resp.status_code, resp.text

    def notify_text(self, text: str) -> Tuple[int, str]:
        if not text or not text.strip():
            raise ValueError("text is empty.")
        return self._post({"to": self.user_id, "messages": [{"type": "text", "text": text}]})

    def notify_image(self, original_url: str, preview_url: Optional[str] = None) -> Tuple[int, str]:
        if not original_url or not original_url.strip():
            raise ValueError("original_url required.")
        msg = {
            "type": "image",
            "originalContentUrl": original_url,
            "previewImageUrl": preview_url or original_url
        }
        return self._post({"to": self.user_id, "messages": [msg]})

    # --------------- Helpers -------------------
    def notify_success(self, text: str) -> Tuple[int, str]:
        return self.notify_text(f"✅ {text}")

    def notify_error(self, text: str) -> Tuple[int, str]:
        return self.notify_text(f"❌ {text}")

    def notify_on_finish(self, msg_ok: str = "✅ {func} finished in {secs:.2f}s", msg_err: str = "❌ {func} failed: {exc}") -> Callable:
        """Decorator that sends a LINE message on completion or error.
        Placeholders: {func}, {secs}, {exc}
        """
        def decorator(fn: Callable) -> Callable:
            @wraps(fn)
            def wrapper(*args, **kwargs):
                t0 = time.time()
                try:
                    result = fn(*args, **kwargs)
                    secs = time.time() - t0
                    self.notify_text(msg_ok.format(func=fn.__name__, secs=secs))
                    return result
                except Exception as exc:
                    secs = time.time() - t0
                    self.notify_text(msg_err.format(func=fn.__name__, secs=secs, exc=exc))
                    raise
            return wrapper
        return decorator

    @contextmanager
    def notify_context(self, label: str = "Task"):
        """Context manager that notifies start/finish and errors."""
        self.notify_text(f"▶️ {label} started")
        t0 = time.time()
        try:
            yield
            secs = time.time() - t0
            self.notify_text(f"✅ {label} finished in {secs:.2f}s")
        except Exception as exc:
            secs = time.time() - t0
            self.notify_text(f"❌ {label} failed after {secs:.2f}s: {exc}")
            raise