# 일정 수집 및 Markdown 관리 도구

이 프로젝트는 매일 22:00(한국시간)에 사용자의 일정 정리 여부를 확인한 뒤,
다양한 메시지 서비스에서 일정 관련 내용을 수집하여 Markdown 형식으로
저장하는 간단한 예제입니다.

## 구성 요소
- `aggregator/main.py`: 스케줄러와 수집 로직의 진입점
- `fetchers/`: 각 서비스별 메시지 수집 모듈. 기본 구현은 `DATA_PATH`\
  환경 변수(기본값 `data`)로 지정된 디렉터리에서 텍스트 파일을 읽어
  메시지를 가져옵니다.
- `parser.py`: 메시지에서 날짜 형식을 찾아 일정 문장으로 추출
- `markdown_writer.py`: Obsidian Vault 등에 저장할 Markdown 파일 작성

## 사용 방법
1. 필요한 라이브러리 설치
   ```bash
   pip install schedule pytz
   ```
2. `VAULT_PATH` 환경변수로 Markdown을 저장할 디렉터리를 지정합니다.
3. `DATA_PATH` 환경변수로 메시지 텍스트 파일이 위치한 디렉터리를
   지정할 수 있습니다. 기본값은 프로젝트의 `data/` 폴더입니다.
4. `python aggregator/main.py` 실행 후 안내에 따라 일정을 정리합니다.

실제 서비스 연동이 필요하다면 각 fetcher 모듈을 API 호출 코드로
교체하면 됩니다.
