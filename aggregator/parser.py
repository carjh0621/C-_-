"""메시지에서 일정 및 할 일 추출 모듈."""
from typing import List
import re
from datetime import datetime

DATE_PATTERN = re.compile(r"(\d{4}-\d{2}-\d{2})")


def extract_events(text: str) -> List[str]:
    events = []
    for line in text.splitlines():
        match = DATE_PATTERN.search(line)
        if match:
            date_str = match.group(1)
            try:
                datetime.strptime(date_str, "%Y-%m-%d")
                events.append(line.strip())
            except ValueError:
                continue
    return events
