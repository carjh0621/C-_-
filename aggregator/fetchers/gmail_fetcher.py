"""Gmail 메시지 수집 모듈."""
from typing import List
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def fetch_gmail_messages() -> List[str]:
    """Gmail API를 통해 최근 메일 메시지를 수집합니다."""
    token_file = os.environ.get("GMAIL_TOKEN_FILE")
    if not token_file or not os.path.exists(token_file):
        return []

    try:
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        service = build("gmail", "v1", credentials=creds)
        results = service.users().messages().list(userId="me", q="newer_than:7d").execute()
        ids = results.get("messages", [])
        messages: List[str] = []
        for msg in ids:
            detail = service.users().messages().get(userId="me", id=msg["id"], format="full").execute()
            snippet = detail.get("snippet")
            if snippet:
                messages.append(snippet)
        return messages
    except HttpError:
        return []
    except Exception:
        return []
