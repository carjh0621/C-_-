"""Meta Messenger 메시지 수집 모듈."""
from typing import List
import os
import requests


def fetch_messenger_messages() -> List[str]:
    """Graph API를 이용해 Messenger 대화 메시지를 수집합니다."""
    token = os.environ.get("FB_ACCESS_TOKEN")
    thread_id = os.environ.get("FB_THREAD_ID")
    if not token or not thread_id:
        return []

    url = f"https://graph.facebook.com/v18.0/{thread_id}/messages"
    params = {"access_token": token}
    try:
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code != 200:
            return []
        data = resp.json()
        return [m["message"] for m in data.get("data", []) if "message" in m]
    except Exception:
        return []
