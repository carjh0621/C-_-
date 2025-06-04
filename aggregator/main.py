import os
import pytz
import schedule
import time
from datetime import datetime

from fetchers.gmail_fetcher import fetch_gmail_messages
from fetchers.kakao_fetcher import fetch_kakao_messages
from fetchers.messenger_fetcher import fetch_messenger_messages
from fetchers.instagram_fetcher import fetch_instagram_messages
from fetchers.portal_fetcher import fetch_portal_messages
from parser import extract_events
from markdown_writer import write_markdown

KST = pytz.timezone('Asia/Seoul')
VAULT_PATH = os.environ.get("VAULT_PATH", "vault")


def collect_and_process():
    raw_messages = []
    raw_messages.extend(fetch_gmail_messages())
    raw_messages.extend(fetch_kakao_messages())
    raw_messages.extend(fetch_messenger_messages())
    raw_messages.extend(fetch_instagram_messages())
    raw_messages.extend(fetch_portal_messages())

    events = []
    for msg in raw_messages:
        events.extend(extract_events(msg))

    if events:
        if not os.path.exists(VAULT_PATH):
            os.makedirs(VAULT_PATH)
        timestamp = datetime.now(KST).strftime("%Y-%m-%d")
        filename = os.path.join(VAULT_PATH, f"schedule_{timestamp}.md")
        write_markdown(filename, events)


def daily_task():
    response = input("오늘 일정을 정리했나요? (y/N): ")
    if response.strip().lower() == 'y':
        collect_and_process()
        print("일정을 정리했습니다.")
    else:
        print("다음에 다시 시도합니다.")


def main():
    schedule.every().day.at("22:00").do(daily_task)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
