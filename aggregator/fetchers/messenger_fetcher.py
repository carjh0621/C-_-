"""Meta Messenger 메시지 수집 모듈."""
from typing import List
import os

from .gmail_fetcher import _read_lines


def fetch_messenger_messages() -> List[str]:
    """샘플 Messenger 메시지를 읽어 반환합니다."""
    data_dir = os.environ.get("DATA_PATH", "data")
    file_path = os.path.join(data_dir, "messenger.txt")
    return _read_lines(file_path)
