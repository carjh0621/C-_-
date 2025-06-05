"""Instagram DM 수집 모듈."""
from typing import List
import os
import requests


def fetch_instagram_messages() -> List[str]:
    """Instagram Graph API를 이용해 최근 DM을 수집합니다."""
    token = os.environ.get("IG_ACCESS_TOKEN")
    thread_id = os.environ.get("IG_THREAD_ID")
    if not token or not thread_id:
        return []

    url = f"https://graph.facebook.com/v18.0/{thread_id}/messages"
    params = {"access_token": token}
    try:
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code != 200:
            return []
        data = resp.json()
        return [m.get("text") or m.get("message") for m in data.get("data", []) if m.get("text") or m.get("message")]
    except Exception:
        return []
