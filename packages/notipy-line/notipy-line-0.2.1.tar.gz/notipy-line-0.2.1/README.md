# notipy-line

Minimal LINE Messaging API pusher for Python.

## Install (after publishing)
```bash
pip install notipy-line
```

## Quickstart
```python
from notipy_line import NotiPy

# Option A: set env vars
#   NOTIPY_CHANNEL_ACCESS_TOKEN=... 
#   NOTIPY_USER_ID=...
noti = NotiPy()

# Option B: pass explicitly
# noti = NotiPy(access_token="YOUR_CHANNEL_ACCESS_TOKEN", user_id="LINE_USER_ID")

code, resp = noti.notify_text("✅ Training finished.")
print(code, resp)
```

## Why LINE Notify won't work
LINE Notify has been deprecated. Use LINE Messaging API with a channel access token.
