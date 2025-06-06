# 일정 수집 및 Markdown 관리 도구

이 프로젝트는 매일 22:00(한국시간)에 사용자의 일정 정리 여부를 확인한 뒤,
다양한 메시지 서비스에서 일정 관련 내용을 수집하여 Markdown 형식으로
저장하는 간단한 예제입니다.

## 구성 요소
- `aggregator/main.py`: 스케줄러와 수집 로직의 진입점
- `fetchers/`: 각 서비스별 메시지 수집 모듈. Gmail, KakaoTalk, Messenger,
  Instagram, 포털 등에서 직접 메시지를 가져옵니다.
- `parser.py`: 메시지에서 날짜 형식을 찾아 일정 문장으로 추출
- `markdown_writer.py`: Obsidian Vault 등에 저장할 Markdown 파일 작성

## 사용 방법
1. 필요한 라이브러리 설치
   ```bash
   pip install -r requirements.txt
   ```
2. `VAULT_PATH` 환경변수로 Markdown을 저장할 디렉터리를 지정합니다.
3. 서비스별로 필요한 인증 정보를 환경 변수나 설정 파일로 제공합니다.
   주요 변수는 다음과 같습니다.
   - `GMAIL_TOKEN_FILE`: Gmail OAuth 토큰 JSON 파일 경로
   - `KAKAO_EXPORT_PATH`: KakaoTalk 채팅 내보내기 파일 경로
   - `FB_ACCESS_TOKEN`, `FB_THREAD_ID`: Messenger API 토큰과 대화 ID
   - `IG_ACCESS_TOKEN`, `IG_THREAD_ID`: Instagram API 토큰과 스레드 ID
   - `PORTAL_URL`, `PORTAL_USERNAME`, `PORTAL_PASSWORD`: 포털 주소와 로그인 정보
4. `python aggregator/main.py` 실행 후 안내에 따라 일정을 정리합니다.

## 스케줄 동작
프로그램을 실행하면 스케줄러가 매일 22:00까지 대기합니다. 그때까지는
화면에 아무 메시지도 표시되지 않으므로 정지한 것처럼 보일 수 있습니다.

## 빠르게 테스트하기
동작을 바로 확인하려면 다음 방법 중 하나를 사용합니다.

1. `--once` 플래그를 사용해 즉시 한 번만 실행합니다.
   ```bash
   python aggregator/main.py --once
   ```
2. `aggregator/main.py`에서 `schedule.every().day.at("22:00")` 부분을
   가까운 시간으로 임시 수정한 뒤 실행합니다.
