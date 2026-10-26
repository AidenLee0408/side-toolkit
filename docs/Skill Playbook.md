---
type: playbook
status: proposed
owner: Founder
last_reviewed: 2026-10-27
---

# Skill Playbook

작업마다 어떤 스킬을 먼저 쓰는지, 어떤 스킬끼리 부딪히는지, 언제 스킬 없이 하는지 적는다. 지금 내용은 아직 **가설**이다. `Skill Reports/`에 실제 결과가 쌓이면 고치고, 근거가 된 리포트 이름을 적는다. 스킬 목록은 [Skills](Skills.md)에 있다.

## 1. 작업별 우선순위

한 작업에는 주력 스킬을 하나만 둔다. 보조 스킬은 필요할 때만 부른다.

| 작업 | 1순위 | 보조 | 쓰지 않는 것 | 근거 |
|---|---|---|---|---|
| 아이디어 고르기·검증 | product-management `brainstorm` | `deep-research`, `competitive-brief` | 개발 스킬 전부 | 가설 |
| 기능 명세 | product-management `write-spec` | superpowers `brainstorming` | ponytail (범위를 너무 줄임) | 가설 |
| 시장 전략·포지셔닝 | gtm-planner | marketing-skills `product-marketing` | marketing(Anthropic) 동시 사용 | 가설 |
| 새 기능 구현 | superpowers `writing-plans` → `test-driven-development` | ponytail lite | caveman `lean-build` (ponytail과 중복) | 가설 |
| 버그 수정 | superpowers `systematic-debugging` | caveman `surgical-patch` | impeccable | 가설 |
| 코드 정리 | `/simplify` | ponytail `ponytail-review` | — | 가설 |
| 코드 리뷰 | `/code-review` | review-council (큰 변경만) | caveman-review와 동시 사용 | 가설 |
| 랜딩 페이지 처음 만들기 | taste-skill | ui-ux-pro-max (색·폰트 데이터만) | impeccable, frontend-design 동시 사용 | 가설 |
| 제품 UI(대시보드, 설정) | ui-ux-pro-max | frontend-design | taste-skill | 가설 |
| UI 다듬기·점검 | impeccable `polish`/`audit` | — | 다른 디자인 스킬 | 가설 |
| 랜딩 문구 | marketing-skills `copywriting` | writing-quality `writing-enforcer` | — | 가설 |
| 가격·결제 화면 | marketing-skills `pricing`, `paywalls` | stripe 플러그인(설치 후) | — | 가설 |
| 가입·온보딩 | marketing-skills `signup`, `onboarding` | — | — | 가설 |
| 런칭 | marketing-skills `launch`, `directory-submissions` | gtm-planner `roadmap` | — | 가설 |
| 배포 전 점검 | engineering `deploy-checklist` | superpowers `verification-before-completion` | — | 가설 |
| 허브 기록·문서 | 스킬 없음 | writing-quality (외부 공개 글만) | caveman (보고가 너무 짧아짐) | 가설 |

## 2. 부딪히는 조합

| 조합 | 무엇이 부딪히나 | 처리 | 근거 |
|---|---|---|---|
| ponytail ↔ superpowers | "가장 작게"와 "계획·TDD 먼저" | 계획은 superpowers, 구현 범위 판단은 ponytail lite | 가설 |
| ponytail ↔ caveman `lean-build` | 같은 역할(과설계 방지) | 하나만 남긴다. 리포트로 비교 | 가설 |
| 디자인 4종 (frontend-design, taste-skill, ui-ux-pro-max, impeccable) | 디자인 방향이 서로 다르고, 함께 발동할 수 있음 | 한 작업에 하나만. 위 표 기준 | 가설 |
| caveman ↔ 창업자 보고 | 설명이 지나치게 짧아짐 | 허브 보고는 평소 말투로 쓴다 | 가설 |
| impeccable 훅 ↔ UI 없는 작업 | 편집마다 실행, 답변 끝에 최대 30초 | 허브·백엔드 작업에서 느리면 끈다 | 가설 |
| marketing(Anthropic) ↔ marketing-skills | 영역 중복 | 실행은 marketing-skills 우선. 첫 홍보 작업에서 비교해 하나만 남긴다 | 가설 |

## 3. 스킬을 쓰지 않아도 되는 경우
- 한두 줄 수정, 오타, 이름 바꾸기
- 질문에 답하기, 파일 몇 개 읽고 설명하기
- 허브 기록 갱신(Kanban, Portfolio 등)
- 이미 정해진 절차를 그대로 따르는 반복 작업
- 스킬을 불렀더니 결과가 나빠지거나 느려진 작업 (리포트에 남긴다)

판단 기준: 스킬의 절차나 지식이 없으면 결과가 나빠지는 작업에만 쓴다.

## 4. 이 문서를 고치는 방법
1. 작업 중 스킬 이슈가 생기면 바로 [Skill Issues](Skill%20Issues.md)에 한 줄 추가한다. 이 문서의 1순위·충돌 표나 [Skills](Skills.md)의 상태를 바꾸면 [Skill Changelog](Skill%20Changelog.md)에 한 줄 추가한다.
2. 프로젝트(또는 큰 작업)를 마치면 `python3 scripts/skill-usage.py --root <저장소> --since <시작일>`로 사용 횟수를 뽑고, `Skill Reports/_Template.md`로 리포트를 쓴다.
3. 주간 리뷰 때 새 리포트를 읽고, 같은 결과가 두 번 이상 나오면 위 표의 근거를 "가설"에서 리포트 이름으로 바꾼다.
4. 스킬 상태(시험 중 → 채택/제외)는 [Skills](Skills.md)에서 바꾼다. 제외는 창업자가 정한다.
5. 월간 재검토 때 전체 집계(`python3 scripts/skill-usage.py --root ~/SideProjects --since <한 달 전>`)로 한 번도 안 쓴 플러그인을 찾아 끄기 후보로 올린다.
