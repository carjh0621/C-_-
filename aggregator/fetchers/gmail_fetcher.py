"""Gmail 메시지 수집 모듈."""
from typing import List
import os


def _read_lines(path: str) -> List[str]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def fetch_gmail_messages() -> List[str]:
    """샘플 Gmail 메시지를 읽어 반환합니다."""
    data_dir = os.environ.get("DATA_PATH", "data")
    file_path = os.path.join(data_dir, "gmail.txt")
    return _read_lines(file_path)
