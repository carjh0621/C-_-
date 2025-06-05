"""학교/회사 포털 일정 수집 모듈."""
from typing import List
import os
import requests
from bs4 import BeautifulSoup


def fetch_portal_messages() -> List[str]:
    """포털 사이트에서 일정 관련 메시지를 스크래핑합니다."""
    base_url = os.environ.get("PORTAL_URL")
    username = os.environ.get("PORTAL_USERNAME")
    password = os.environ.get("PORTAL_PASSWORD")

    if not base_url or not username or not password:
        return []

    session = requests.Session()
    try:
        login_resp = session.post(f"{base_url}/login", data={"username": username, "password": password}, timeout=10)
        if login_resp.status_code != 200:
            return []
        resp = session.get(f"{base_url}/messages", timeout=10)
        if resp.status_code != 200:
            return []
        soup = BeautifulSoup(resp.text, "html.parser")
        return [item.get_text(strip=True) for item in soup.select(".message")]
    except Exception:
        return []
