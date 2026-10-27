---
type: issue-log
status: proposed
owner: Founder
last_reviewed: 2026-10-27
---

# Skill Issues

스킬이나 플러그인 관련 이슈가 생길 때마다 **맨 아래에 한 줄씩 추가**한다. 이미 쓴 줄은 내용을 고치거나 지우지 않는다. 처리 결과가 바뀌면 새 줄을 쓰고 이전 번호를 적는다. (2026-10-27에 문서 전체의 표현만 한 번 다듬었다.)

- 종류: 충돌, 엉뚱한 발동, 발동 실패, 느림, 보안, 설치, 설정, 품질
- 상태: 열림, 해결, 관찰 중
- 같은 종류가 두 번 이상 나오면 [Skill Playbook](Skill%20Playbook.md)이나 [Skills](Skills.md)에 반영하고, 반영한 곳을 조치 칸에 적는다.

| # | 날짜 | 스킬/플러그인 | 종류 | 이슈 | 조치 | 상태 |
|---|---|---|---|---|---|---|
| 1 | 2026-10-27 | 카드로 띄운 6개 (Marketing, stripe 등) | 설치 | 설치 카드만 띄우고 실제로 설치됐는지 확인하지 않았다 | `ListPlugins`와 `claude plugin list`로 확인한 뒤 공식 마켓플레이스에서 설치했다. 설치한 뒤에는 목록으로 확인한다 | 해결 |
| 2 | 2026-10-27 | 오픈소스 플러그인 전부 | 보안 | `claude plugin marketplace add`가 특정 커밋 고정을 지원하지 않는다(브랜치와 태그만 된다) | 설치 직후 마켓플레이스 폴더의 커밋이 검토한 커밋과 같은지 확인한다. 업데이트하면 다시 검토한다 | 관찰 중 |
| 3 | 2026-10-27 | caveman | 보안 | 설치 전 검토 때 훅만 보고, 외부로 데이터를 보내는 Caveman Cloud 스킬(`caveman-setup`, `caveman-compress`)을 놓쳤다 | [Skills](Skills.md)에 사용 금지로 기록했다. 검토할 때 스킬 목록도 함께 본다 | 해결 |
| 4 | 2026-10-27 | ponytail | 설정 | 설치할 때 `--config webhookUrl=`처럼 빈 값을 넣으면 거부된다 | 웹훅 관련 값은 지정하지 않았다(비어 있으면 외부로 보내지 않는다). 기본 단계 lite는 `~/.config/ponytail/config.json`에 적었다 | 해결 |
| 5 | 2026-10-27 | posthog | 느림 | 스킬 약 170개가 세션마다 목록에 올라 토큰을 쓰고 엉뚱한 스킬이 불릴 위험이 크다 | 출시 전까지 사용을 중지했다 (cloudflare, stripe도 함께) | 해결 |
| 6 | 2026-10-27 | impeccable | 느림 | 파일을 고칠 때마다 훅이 실행되고, 답변 끝에 최대 30초가 걸린다 | UI가 없는 작업에서 느려지면 끈다. 첫 프로젝트에서 지켜본다 | 관찰 중 |
| 7 | 2026-10-27 | 디자인 플러그인 4개 (frontend-design, taste-skill, ui-ux-pro-max, impeccable) | 충돌 | 한 작업에서 디자인 방향이 서로 다른 지시가 함께 불릴 수 있다 | [Skill Playbook](Skill%20Playbook.md)에 작업별로 먼저 쓸 스킬을 정했다. 첫 랜딩 페이지에서 비교한다 | 관찰 중 |
| 8 | 2026-10-27 | marketing(Anthropic) ↔ marketing-skills | 충돌 | 마케팅 실행에서 하는 일이 겹친다 | marketing-skills를 먼저 쓴다. 첫 홍보 작업에서 비교해 하나만 남긴다 | 관찰 중 |
| 9 | 2026-10-27 | writing-quality `writing-enforcer` | 품질 | 한국어를 검사하지 못한다. 어색했던 초안 문장(조사 오류, 명사 나열, 영어 직역)을 스캐너에 넣었더니 10/10 "Ready to ship"이 나왔다. 패턴 목록이 영어 기준이다 | 한국어 공개 문서를 점검할 도구를 다시 정한다 | 열림 |
| 10 | 2026-10-27 | caveman ↔ fluent-korean | 충돌 | caveman은 답변을 짧게 줄이고 fluent-korean은 완결된 문장을 요구해 지시가 정반대다 | 한국어 글을 쓰는 세션에서는 caveman을 끈다. [Skill Playbook](Skill%20Playbook.md) 충돌 표에 반영했다 | 관찰 중 |
| 11 | 2026-10-27 | writing-quality `writing-enforcer` | 품질 | #9 후속: 한국어 공개 문서 점검을 fluent-korean과 humanize-korean으로 옮기고, writing-enforcer는 영어 전용으로 두었다 | [Skill Playbook](Skill%20Playbook.md)과 UI Wording에 반영했다 | 해결 |
| 12 | 2026-10-27 | caveman ↔ fluent-korean | 충돌 | #10 후속: caveman을 그대로 두기로 했다 | 자체 제작 스킬 writing-concise-korean으로 한국어 답변의 문법을 보완하고, fluent-korean은 허브와 제품 저장소에서만 켠다 | 관찰 중 |
| 13 | 2026-10-27 | checking-korean-writing | 품질 | 공개 문서에 남은 어색한 표현("꺼 둠", "겹침 지도", "기본 담당", "주력")을 창업자가 찾았다. 짧게 줄여 만든 이름이나 상태 표시는 스캐너 패턴에 없어서 걸리지 않았다 | 공개 문서 전체를 다시 다듬었다. 줄여 만든 용어 패턴을 스킬에 추가한다 | 열림 |
| 14 | 2026-10-27 | checking-korean-writing | 품질 | #13 후속: 스캐너에 "줄여 만든 용어"와 "명사형(~ㅁ)으로 끝남" 패턴을 추가했다. 고치기 전 Skills.md에서 각각 24건, 7건을 찾았고, 고친 뒤에는 0건이다 | side-skills 0.1.2 | 해결 |
| 15 | 2026-10-27 | aws-startup-advisor | 충돌 | 상태는 보류인데 세션 시작 훅이 "스타트업 관점으로 모든 답변을 맞추라"는 지시를 계속 넣는다. 첫 스킬 충돌 검사에서 찾았다 | claude.ai에서 사용 중지를 제안했다 | 열림 |
