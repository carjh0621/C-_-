"""Markdown 파일 생성 모듈."""
from typing import List


def write_markdown(filename: str, events: List[str]) -> None:
    with open(filename, "a", encoding="utf-8") as f:
        for event in events:
            f.write(f"- {event}\n")
