---
type: issue-log
status: proposed
owner: Founder
last_reviewed: 2026-10-27
---

# Skill Issues

스킬이나 플러그인 관련 이슈가 생길 때마다 **맨 아래에 한 줄씩 추가**한다. 이미 쓴 줄은 고치거나 지우지 않는다. 처리 결과가 바뀌면 새 줄을 쓰고 이전 번호를 적는다.

- 종류: 충돌 / 엉뚱한 발동 / 발동 실패 / 느림 / 보안 / 설치 / 설정 / 품질
- 상태: 열림 / 해결 / 관찰 중
- 같은 종류가 두 번 이상 나오면 [Skill Playbook](Skill%20Playbook.md)이나 [Skills](Skills.md)에 반영하고, 반영한 곳을 조치 칸에 적는다.

| # | 날짜 | 스킬/플러그인 | 종류 | 이슈 | 조치 | 상태 |
|---|---|---|---|---|---|---|
| 1 | 2026-10-27 | 카드 설치 6종 (Marketing, stripe 등) | 설치 | 설치 카드만 띄우고 실제로 설치됐는지 확인하지 않았다 | `ListPlugins`, `claude plugin list`로 확인 후 공식 마켓플레이스에서 설치. 설치 뒤엔 목록으로 확인한다 | 해결 |
| 2 | 2026-10-27 | 오픈소스 플러그인 전부 | 보안 | `claude plugin marketplace add`가 커밋 고정을 지원하지 않는다(브랜치·태그만) | 설치 직후 마켓플레이스 폴더의 커밋이 검토한 커밋과 같은지 확인. 업데이트 시 재검토 | 관찰 중 |
| 3 | 2026-10-27 | caveman | 보안 | 설치 전 검토 때 훅만 보고, 외부로 보내는 Caveman Cloud 스킬(`caveman-setup`, `caveman-compress`)을 놓쳤다 | 사용 금지로 [Skills](Skills.md)에 기록. 검토 범위에 스킬 목록 포함 | 해결 |
| 4 | 2026-10-27 | ponytail | 설정 | 설치 시 `--config webhookUrl=` 빈 값이 거부됨 | 웹훅 관련 값은 지정하지 않음(비어 있으면 외부 전송 없음). 기본 단계는 `~/.config/ponytail/config.json`에 lite | 해결 |
| 5 | 2026-10-27 | posthog | 느림 | 스킬 약 170개가 매 세션 목록에 올라 토큰과 오발동 위험이 큼 | 출시 전까지 끔 (cloudflare, stripe도 함께) | 해결 |
| 6 | 2026-10-27 | impeccable | 느림 | 편집마다 훅 실행, 답변 끝에 최대 30초 | UI 없는 작업에서 느리면 끈다. 첫 프로젝트에서 관찰 | 관찰 중 |
| 7 | 2026-10-27 | 디자인 4종 (frontend-design, taste-skill, ui-ux-pro-max, impeccable) | 충돌 | 같은 작업에 서로 다른 미적 지시가 동시에 발동할 수 있음 | [Skill Playbook](Skill%20Playbook.md)에 작업별 1순위 지정. 첫 랜딩에서 비교 | 관찰 중 |
| 8 | 2026-10-27 | marketing(Anthropic) ↔ marketing-skills | 충돌 | 마케팅 실행 영역 중복 | marketing-skills 우선. 첫 홍보 작업에서 하나만 남긴다 | 관찰 중 |
