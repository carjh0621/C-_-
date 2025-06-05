"""KakaoTalk 메시지 수집 모듈."""
from typing import List
import os


def fetch_kakao_messages() -> List[str]:
    """내보낸 KakaoTalk 채팅 파일에서 메시지를 읽어 반환합니다."""
    export_path = os.environ.get("KAKAO_EXPORT_PATH")
    if not export_path or not os.path.exists(export_path):
        return []

    with open(export_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
