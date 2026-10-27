---
type: playbook
status: proposed
owner: Founder
last_reviewed: 2026-10-27
---

# Plugin Playbook

작업마다 어떤 스킬을 먼저 쓰는지, 어떤 스킬과 훅이 서로 부딪히는지, 언제 스킬 없이 하는지 적는다. 지금 내용은 아직 **가설**이다. `Plugin Reports/`에 실제 결과가 쌓이면 고치고, 근거가 된 리포트 이름을 적는다. 스킬 목록은 [Plugins](Plugins.md)에 있다.

## 1. 작업별 우선순위

한 작업에는 먼저 쓸 스킬을 하나만 정한다. 보조 스킬은 필요할 때만 부른다.

| 작업 | 먼저 쓸 스킬 | 보조 스킬 | 쓰지 않을 스킬 | 근거 |
|---|---|---|---|---|
| 아이디어 고르기와 검증 | product-management `brainstorm` | `deep-research`, `competitive-brief` | 개발 스킬 전부 | 가설 |
| 기능 명세 쓰기 | product-management `write-spec` | superpowers `brainstorming` | ponytail (범위를 지나치게 줄인다) | 가설 |
| 시장 전략과 포지셔닝 | gtm-planner | marketing-skills `product-marketing` | marketing(Anthropic)을 함께 쓰는 것 | 가설 |
| 새 기능 구현 | superpowers `writing-plans` → `test-driven-development` | ponytail lite | caveman `lean-build` (ponytail과 역할이 같다) | 가설 |
| 버그 수정 | superpowers `systematic-debugging` | caveman `surgical-patch` | impeccable | 가설 |
| 코드 정리 | `/simplify` | ponytail `ponytail-review` | — | 가설 |
| 코드 리뷰 | `/code-review` | review-council (큰 변경일 때만) | caveman-review를 함께 쓰는 것 | 가설 |
| 랜딩 페이지 처음 만들기 | taste-skill | ui-ux-pro-max (색과 폰트 데이터만) | impeccable, frontend-design을 함께 쓰는 것 | 가설 |
| 제품 UI (대시보드, 설정 화면) | ui-ux-pro-max | frontend-design | taste-skill | 가설 |
| UI 다듬기와 점검 | impeccable `polish`, `audit` | — | 다른 디자인 스킬 | 가설 |
| 랜딩 페이지 문구 | marketing-skills `copywriting` | writing-quality `writing-enforcer` | — | 가설 |
| 가격과 결제 화면 | marketing-skills `pricing`, `paywalls` | stripe 플러그인 (다시 켠 뒤) | — | 가설 |
| 가입과 온보딩 | marketing-skills `signup`, `onboarding` | — | — | 가설 |
| 런칭 | marketing-skills `launch`, `directory-submissions` | gtm-planner `roadmap` | — | 가설 |
| 배포 전 점검 | engineering `deploy-checklist` | superpowers `verification-before-completion` | — | 가설 |
| 허브 기록과 내부 문서 | 스킬 없이 한다 | — | caveman (보고가 지나치게 짧아진다) | 가설 |
| 한국어 공개 문서 (README, side-toolkit) | fluent-korean으로 처음부터 쓰고(허브와 제품만), 공개 전에 checking-korean-writing으로 점검한다 | humanize-korean (긴 글을 깊게 다듬을 때) | writing-enforcer (한국어를 검사하지 못한다), caveman (문장이 끊긴다) | 창업자 결정 2026-10-27, Plugin Issues #9 |
| 영어 문구 (랜딩, 홍보, 영어 문서) | writing-quality `writing-enforcer` | marketing-skills `copy-editing` (홍보 문구) | — | 창업자 결정 2026-10-27 |

## 2. 부딪히는 조합

| 조합 | 무엇이 부딪히나 | 처리 | 근거 |
|---|---|---|---|
| ponytail ↔ superpowers | "가장 작게 만들라"는 지시와 "계획과 테스트를 먼저 하라"는 지시 | 계획은 superpowers로 세우고, 구현 범위는 ponytail lite로 판단한다 | 가설 |
| ponytail ↔ caveman `lean-build` | 둘 다 과설계를 막는 역할이다 | 리포트로 비교해 하나만 남긴다 | 가설 |
| 디자인 플러그인 4개 (frontend-design, taste-skill, ui-ux-pro-max, impeccable) | 디자인 방향이 서로 다르고, 한 작업에서 함께 불릴 수 있다 | 한 작업에는 하나만 쓴다. 1번 표를 따른다 | 가설 |
| caveman ↔ 창업자 보고 | 설명이 지나치게 짧아진다 | 허브 보고는 평소 말투로 쓴다 | 가설 |
| caveman ↔ fluent-korean | 짧게 줄이라는 지시와 완결된 문장으로 쓰라는 지시가 정반대다 | caveman은 그대로 두고, 한국어 답변은 writing-concise-korean을 따른다(내용만 줄이고 조사와 어미는 지킨다). fluent-korean은 허브와 제품 저장소에서만 켠다 | 창업자 결정 2026-10-27, Plugin Issues #10 |
| impeccable 훅 ↔ UI가 없는 작업 | 파일을 고칠 때마다 훅이 실행되고, 답변 끝에 최대 30초가 걸린다 | 허브나 백엔드 작업에서 느려지면 끈다 | 가설 |
| marketing(Anthropic) ↔ marketing-skills | 하는 일이 겹친다 | 실행은 marketing-skills를 먼저 쓴다. 첫 홍보 작업에서 비교해 하나만 남긴다 | 가설 |
| 코드 리뷰 스킬 6개 | 리뷰를 부탁하면 어느 것이 불릴지 정해져 있지 않다 | `/code-review`를 먼저 쓰고, 큰 변경에만 review-council을 쓴다 | 2026-10-27 충돌 검사 |
| `competitive-brief` (product-management ↔ marketing) | 이름이 같다 | 기획 단계는 product-management, 홍보 단계는 marketing-skills `competitor-profiling`을 쓴다 | 2026-10-27 충돌 검사 |
| `seo-audit` (marketing ↔ marketing-skills) | 이름이 같다 | marketing-skills `seo-audit`을 쓴다 | 2026-10-27 충돌 검사 |
| 브레인스토밍 (superpowers ↔ product-management) | 둘 다 브레인스토밍을 맡는다 | 제품 아이디어는 product-management, 기능 설계 직전은 superpowers `brainstorming`을 쓴다 | 2026-10-27 충돌 검사 |
| 고객 조사 (marketing-skills `customer-research` ↔ product-management `synthesize-research`) | 조사 정리가 겹친다 | 조사 결과 정리는 product-management, 리뷰와 커뮤니티 수집은 marketing-skills를 쓴다 | 2026-10-27 충돌 검사 |
| 세션 시작 훅 5개 (caveman, impeccable, ponytail, aws-startup-advisor, superpowers) | 세션마다 여러 지시가 한꺼번에 들어온다. aws-startup-advisor는 보류 상태인데도 "스타트업 관점" 지시를 넣는다 | aws-startup-advisor는 창업자 결정으로 켜 두고, 답변이 스타트업 관점으로 치우치는지 지켜본다 | 2026-10-27 충돌 검사, 창업자 결정 |

## 3. 스킬을 쓰지 않아도 되는 경우

- 한두 줄 수정, 오타 고치기, 이름 바꾸기
- 질문에 답하기, 파일 몇 개를 읽고 설명하기
- 허브 기록 갱신(Kanban, Portfolio 등)
- 이미 정해진 절차를 그대로 따르는 반복 작업
- 스킬을 불렀더니 결과가 나빠지거나 느려진 작업 (리포트에 남긴다)

판단 기준: 스킬의 절차나 지식이 없으면 결과가 나빠지는 작업에만 쓴다.

## 4. 이 문서를 고치는 방법

1. 작업 중에 스킬 이슈가 생기면 바로 [Plugin Issues](Plugin%20Issues.md)에 한 줄 추가한다. 이 문서의 우선순위나 충돌 표, 또는 [Plugins](Plugins.md)의 상태를 바꾸면 [Plugin Changelog](Plugin%20Changelog.md)에 한 줄 추가한다.
2. 플러그인을 설치하거나 업데이트하면 [Plugin Review](Plugin%20Review.md) 순서로 검토하고, `python3 scripts/plugin-audit.py conflicts`로 충돌 후보를 뽑아 실제 충돌은 2번 표에 추가한다. 주간 리뷰 때는 `plugin-audit.py drift`로 검토하지 않은 업데이트가 있는지 확인한다.
3. 프로젝트나 큰 작업을 마치면 `python3 scripts/skill-usage.py --root <저장소> --since <시작일>`로 사용 횟수를 뽑고, `Plugin Reports/_Template.md`로 리포트를 쓴다.
4. 주간 리뷰 때 새 리포트를 읽는다. 같은 결과가 두 번 이상 나오면 위 표의 근거를 "가설"에서 리포트 이름으로 바꾼다.
5. 스킬 상태(시험 사용 → 채택 또는 제외)는 [Plugins](Plugins.md)에서 바꾼다. 제외는 창업자가 정한다.
6. 월간 재검토 때 전체 집계(`python3 scripts/skill-usage.py --root ~/SideProjects --since <한 달 전>`)로 한 번도 쓰지 않은 플러그인을 찾아 사용 중지 후보로 올린다.
