---
type: checklist
status: proposed
owner: Founder
last_reviewed: 2026-10-27
---

# Plugin Review

새 플러그인을 설치하기 전과 설치한 플러그인이 업데이트됐을 때 이 순서로 검토한다. 검토를 마치면 [Plugins](Plugins.md)에 메모를 남기고, `plugin-reviews.json`에 검토한 버전과 커밋을 적는다.

## 1. 출처를 정한다

| 출처 | 검토 범위 |
|---|---|
| Anthropic 공식 마켓플레이스 (`claude-plugins-official`, `knowledge-work-plugins`) | 훅과 MCP만 본다. 마켓플레이스가 검토된 커밋을 고정해 둔다 |
| claude.ai 플러그인 디렉터리 | 훅과 MCP만 본다. 설치는 claude.ai에서 한다 |
| 그 밖의 오픈소스 저장소 | 아래 2~7번을 모두 본다 |
| 자체 제작 (side-skills) | 고칠 때마다 직접 시험한다 |

## 2. 저장소를 받아 둔다

- 설치 전에 저장소를 작업 폴더(스크래치패드)에 받아서 읽는다.
- 검토한 커밋을 적어 둔다. 설치 도구가 커밋 고정을 지원하지 않으므로, 설치한 뒤 마켓플레이스 폴더의 커밋과 비교한다.

## 3. 구성 요소를 모두 확인한다

`.claude-plugin/plugin.json`과 기본 폴더(`skills/`, `commands/`, `agents/`, `hooks/`, `output-styles/`, `.mcp.json`)를 모두 연다.

| 구성 요소 | 확인할 것 |
|---|---|
| 스킬 | 이름과 설명. 이미 있는 스킬과 같은 일을 맡는지. 외부 서비스로 데이터를 보내는 스킬이 있는지 (caveman의 Cloud 스킬을 놓친 적이 있다) |
| 명령 | 이름이 기존 명령과 겹치는지 |
| 에이전트 | 쓸 수 있는 도구 범위 |
| 훅 | 어느 시점에 무엇을 실행하는지. 대화에 지시를 넣는지(세션 시작, 메시지 입력, 서브에이전트 시작). 실행하는 스크립트를 열어 본다 |
| MCP 서버 | 원격(http)이면 연결 주소, 로컬(stdio)이면 실행하는 프로그램. 같은 서비스가 이미 연결돼 있는지 |
| 출력 스타일 | 무엇을 바꾸는지. `force-for-plugin`으로 설정을 덮어쓰는지 |

## 4. 외부 통신과 파일 쓰기를 찾는다

- 스크립트에서 `fetch`, `http`, `curl`, `wget`, `requests`, `urllib`를 찾고, 무엇을 어디로 보내는지 읽는다.
- 웹훅이나 원격 기록 기능이 기본으로 켜져 있는지 본다.
- 홈 폴더(`~/.claude`, `~/.config`)에 무엇을 쓰는지 본다.
- 실행 파일을 내려받는다면 출처와 검증 방법(sha256 등)을 확인한다.

## 5. 라이선스와 관리 상태를 본다

- 라이선스가 오픈소스인지 (Elastic License처럼 오픈소스가 아닌 경우가 있다)
- 마지막 커밋 날짜, 별 수, 기여자 수

## 6. 충돌 후보를 뽑는다

설치한 뒤 `python3 scripts/plugin-audit.py conflicts`를 실행한다. 실제 충돌은 [Plugin Playbook](Plugin%20Playbook.md)의 2번 표에 추가한다.

충돌은 플러그인끼리 적지 않고, 실제로 부딪히는 구성 요소끼리 적는다. 스킬은 `플러그인:스킬`, 훅은 `플러그인 (훅: 시점)`, 출력 스타일은 `플러그인 (출력 스타일)`로 쓰고, 한 줄에 한 쌍만 적는다.

## 7. 기록한다

- [Plugins](Plugins.md): 하는 일, 설치 이유, 상태, 검토 메모
- `plugin-reviews.json`의 `hooks`: 훅마다 하는 일을 한 줄로 적는다
- `plugin-descriptions.ko.json`: 켜는 플러그인의 소개, 스킬, 명령, 에이전트 설명을 한국어로 옮긴다. 사용 중지한 플러그인은 다시 켤 때 옮긴다. `plugin-audit.py drift`의 "한국어 설명이 없거나 낡은 항목"이 비어 있어야 한다
- [Plugin Components](Plugin%20Components.md): `python3 scripts/plugin-audit.py components > "Plugin Components.md"`로 다시 만든다
- `plugin-reviews.json`: 버전, 커밋, 검토 날짜, 검토 근거
- [Plugin Changelog](Plugin%20Changelog.md): 설치 기록 한 줄
- 문제를 찾았으면 [Plugin Issues](Plugin%20Issues.md)에 한 줄

## 업데이트를 확인할 때

주간 리뷰 때 `python3 scripts/plugin-audit.py drift --reviews plugin-reviews.json`을 실행한다. "다시 검토 필요"나 "검토 기록 없음"이 나오면, 바뀐 부분을 2~7번 순서로 다시 검토한다.
