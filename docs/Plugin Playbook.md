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

**표기:** 스킬은 `플러그인:스킬`, 훅은 `플러그인 (훅: 시점)`, 출력 스타일은 `플러그인 (출력 스타일)`로 적는다. 플러그인 이름만 적지 않는다. `/code-review`, `/simplify`는 Claude Code 기본 명령이다.

| 작업 | 먼저 쓸 스킬 | 보조 스킬 | 쓰지 않을 스킬 | 근거 |
|---|---|---|---|---|
| 아이디어 고르기와 검증 | `product-management:brainstorm` | `anthropic-skills:deep-research`, `product-management:competitive-brief` | 개발 스킬 전부 | 가설 |
| 기능 명세 쓰기 | `product-management:write-spec` | `superpowers:brainstorming` | `ponytail:ponytail` (범위를 지나치게 줄인다) | 가설 |
| 시장 전략과 포지셔닝 | `gtm-planner:positioning` (전체는 `gtm-planner:plan`) | `marketing-skills:product-marketing` | `marketing:campaign-plan` | 가설 |
| 새 기능 구현 | `superpowers:writing-plans` → `superpowers:test-driven-development` | `ponytail:ponytail` (lite) | `caveman:lean-build` (`ponytail:ponytail`과 역할이 같다) | 가설 |
| 버그 수정 | `superpowers:systematic-debugging` | `caveman:surgical-patch` | `engineering:debug`, `caveman:investigate-first` | 가설 |
| 코드 정리 | `/simplify` | `ponytail:ponytail-review` | — | 가설 |
| 코드 리뷰 | `/code-review` | `review-council:review-council` (큰 변경일 때만) | `caveman:caveman-review`, `engineering:code-review`, `ponytail:ponytail-review` | 가설 |
| 랜딩 페이지 처음 만들기 | `taste-skill:design-taste-frontend` | `ui-ux-pro-max:ui-ux-pro-max` (색과 폰트 데이터만) | `frontend-design:frontend-design`, `impeccable:impeccable` | 가설 |
| 제품 UI (대시보드, 설정 화면) | `ui-ux-pro-max:ui-ux-pro-max` | `ui-ux-pro-max:design-system`, `frontend-design:frontend-design` | `taste-skill:design-taste-frontend` | 가설 |
| UI 다듬기와 점검 | `impeccable:impeccable` (polish, audit) | — | `taste-skill:design-taste-frontend`, `ui-ux-pro-max:ui-ux-pro-max` | 가설 |
| 랜딩 페이지 문구 | `marketing-skills:copywriting` | `writing-quality:writing-enforcer` | `marketing:draft-content` | 가설 |
| 가격과 결제 화면 | `marketing-skills:pricing`, `marketing-skills:paywalls` | `stripe:stripe-best-practices` (다시 켠 뒤) | — | 가설 |
| 가입과 온보딩 | `marketing-skills:signup`, `marketing-skills:onboarding` | — | — | 가설 |
| 런칭 | `marketing-skills:launch`, `marketing-skills:directory-submissions` | `gtm-planner:roadmap` | `marketing:campaign-plan` | 가설 |
| 배포 전 점검 | `engineering:deploy-checklist` | `superpowers:verification-before-completion` | — | 가설 |
| 허브 기록과 내부 문서 | 스킬 없이 한다 | — | `caveman (훅: 메시지 입력)` 대신 평소 말투 (보고가 지나치게 짧아진다) | 가설 |
| 한국어 공개 문서 (README, side-toolkit) | `fluent-korean (출력 스타일)`로 처음부터 쓰고(허브와 제품만), 공개 전에 `side-skills:checking-korean-writing`으로 점검한다 | `humanize-korean:humanize-korean` (긴 글을 깊게 다듬을 때) | `writing-quality:writing-enforcer` (한국어를 검사하지 못한다) | 창업자 결정 2026-10-27, Plugin Issues #9 |
| 영어 문구 (랜딩, 홍보, 영어 문서) | `writing-quality:writing-enforcer` | `marketing-skills:copy-editing` (홍보 문구) | — | 창업자 결정 2026-10-27 |

## 2. 부딪히는 조합

한 줄에 부딪히는 쌍 하나만 적는다. 같은 플러그인끼리 여러 쌍이 부딪히면 줄을 나눈다.

**개발**

| 조합 | 무엇이 부딪히나 | 처리 | 근거 |
|---|---|---|---|
| `ponytail (훅: 메시지 입력)` ↔ `superpowers:writing-plans` | "가장 작게 만들라"는 지시와 "계획을 먼저 세우라"는 지시 | 계획은 `superpowers:writing-plans`로 세우고, 구현 범위는 ponytail lite로 판단한다 | 가설 |
| `ponytail (훅: 메시지 입력)` ↔ `superpowers:test-driven-development` | "가장 작게"와 "테스트를 먼저 쓰라" | 테스트는 생략하지 않는다. ponytail은 구현 코드에만 적용한다 | 가설 |
| `ponytail:ponytail` ↔ `caveman:lean-build` | 둘 다 과설계를 막는다 | 리포트로 비교해 하나만 남긴다 | 가설 |
| `superpowers:systematic-debugging` ↔ `engineering:debug` ↔ `caveman:investigate-first` | 셋 다 원인부터 찾는 디버깅 절차다 | `superpowers:systematic-debugging`을 쓴다 | 2026-10-27 충돌 검사 |
| `/code-review` ↔ `engineering:code-review` ↔ `caveman:caveman-review` ↔ `ponytail:ponytail-review` | 리뷰를 부탁하면 어느 것이 불릴지 정해져 있지 않다 | `/code-review`를 먼저 쓴다 | 2026-10-27 충돌 검사 |
| `caveman:caveman-review` ↔ `ponytail:ponytail-review` | 설명이 가장 많이 겹친다(겹침 0.44) | 둘 다 쓰지 않는다 | 2026-10-27 충돌 검사 |
| `review-council:review-council` ↔ `superpowers:requesting-code-review` | 둘 다 여러 관점의 리뷰를 맡긴다 | 큰 변경에만 `review-council:review-council`을 쓴다 | 2026-10-27 충돌 검사 |
| `superpowers:brainstorming` ↔ `product-management:brainstorm`, `product-management:product-brainstorming` | 셋 다 브레인스토밍을 맡는다 | 제품 아이디어는 `product-management:brainstorm`, 기능 설계 직전은 `superpowers:brainstorming`을 쓴다 | 2026-10-27 충돌 검사 |

**디자인**

| 조합 | 무엇이 부딪히나 | 처리 | 근거 |
|---|---|---|---|
| `taste-skill:design-taste-frontend` ↔ `frontend-design:frontend-design` | 둘 다 랜딩 페이지의 디자인 방향을 잡는다 | 랜딩은 `taste-skill:design-taste-frontend`를 쓴다 | 가설 |
| `taste-skill:design-taste-frontend` ↔ `ui-ux-pro-max:ui-ux-pro-max` | 디자인 방향을 정하는 기준이 다르다(갤러리 연구 대 스타일 데이터) | 랜딩은 taste-skill, 제품 UI는 ui-ux-pro-max를 쓴다 | 가설 |
| `ui-ux-pro-max:ui-ux-pro-max` ↔ `frontend-design:frontend-design` | 둘 다 제품 UI를 설계한다 | `ui-ux-pro-max:ui-ux-pro-max`를 먼저 쓴다 | 가설 |
| `ui-ux-pro-max:design-system` ↔ `impeccable:impeccable` (document) | 둘 다 디자인 시스템 문서를 만든다 | 처음 만들 때는 `ui-ux-pro-max:design-system`, 완성된 화면에서 뽑을 때는 impeccable을 쓴다 | 가설 |
| `impeccable (훅: 파일 수정 후, 답변 끝)` ↔ UI가 없는 작업 | 파일을 고칠 때마다 훅이 실행되고, 답변 끝에 최대 30초가 걸린다 | 허브나 백엔드 작업에서 느려지면 끈다 | 가설 |

**마케팅**

| 조합 | 무엇이 부딪히나 | 처리 | 근거 |
|---|---|---|---|
| `product-management:competitive-brief` ↔ `marketing:competitive-brief` | 이름이 같다 | 기획 단계는 `product-management:competitive-brief`를 쓴다 | 2026-10-27 충돌 검사 |
| `marketing:competitive-brief` ↔ `marketing-skills:competitor-profiling` | 둘 다 경쟁사를 조사한다 | 홍보 단계는 `marketing-skills:competitor-profiling`을 쓴다 | 2026-10-27 충돌 검사 |
| `marketing:seo-audit` ↔ `marketing-skills:seo-audit` | 이름이 같다 | `marketing-skills:seo-audit`을 쓴다 | 2026-10-27 충돌 검사 |
| `marketing:campaign-plan` ↔ `marketing-skills:marketing-plan`, `marketing-skills:launch` | 둘 다 캠페인과 런칭을 계획한다 | marketing-skills 쪽을 쓴다 | 가설 |
| `marketing:email-sequence` ↔ `marketing-skills:emails` | 둘 다 자동 메일 시퀀스를 만든다 | `marketing-skills:emails`를 쓴다 | 가설 |
| `marketing:content-creation`, `marketing:draft-content` ↔ `marketing-skills:copywriting`, `marketing-skills:content-strategy` | 둘 다 콘텐츠와 카피를 쓴다 | marketing-skills 쪽을 쓴다 | 가설 |
| `marketing:performance-report` ↔ `marketing-skills:analytics`, `product-management:metrics-review` | 셋 다 지표를 정리한다 | 출시 후 첫 지표 검토 때 비교한다 | 2026-10-27 충돌 검사 |
| `marketing:brand-review` ↔ `ui-ux-pro-max:brand` | 둘 다 브랜드 일관성을 다룬다 | 브랜드를 정할 때 비교한다 | 가설 |
| `marketing-skills:customer-research` ↔ `product-management:synthesize-research` | 조사 결과 정리가 겹친다 | 정리는 product-management, 리뷰와 커뮤니티 수집은 marketing-skills를 쓴다 | 2026-10-27 충돌 검사 |

**글과 답변 방식**

| 조합 | 무엇이 부딪히나 | 처리 | 근거 |
|---|---|---|---|
| `caveman (훅: 메시지 입력)` ↔ `fluent-korean (출력 스타일)` | 짧게 줄이라는 지시와 완결된 문장으로 쓰라는 지시가 정반대다 | caveman은 그대로 두고, 한국어 답변은 `side-skills:writing-concise-korean`을 따른다. fluent-korean은 허브와 제품 저장소에서만 켠다 | 창업자 결정 2026-10-27, Plugin Issues #10 |
| `caveman (훅: 메시지 입력)` ↔ 창업자 보고 | 설명이 지나치게 짧아진다 | 허브 보고는 평소 말투로 쓴다 | 가설 |
| `side-skills:checking-korean-writing` ↔ `humanize-korean:humanize-korean` | 둘 다 한국어 문체를 고친다 | 공개 전 점검은 checking-korean-writing, 긴 글을 깊게 다듬을 때만 humanize-korean을 쓴다 | 가설 |
| `writing-quality:writing-enforcer` ↔ `marketing-skills:copy-editing` | 둘 다 영어 글의 AI 문체를 걷어 낸다 | 홍보 문구는 copy-editing, 그 밖의 영어 글은 writing-enforcer를 쓴다 | 가설 |

**세션 시작 때 들어오는 지시**

| 조합 | 무엇이 부딪히나 | 처리 | 근거 |
|---|---|---|---|
| `superpowers (훅: 세션 시작)` ↔ 모든 스킬 | "스킬이 조금이라도 맞으면 반드시 불러라"는 지시 때문에, 스킬이 많을수록 엉뚱한 스킬이 불린다 | 쓰지 않는 플러그인은 사용을 중지해 스킬 수를 줄인다 | 2026-10-27 충돌 검사 |
| `caveman (훅: 세션 시작, 메시지 입력)` ↔ `ponytail (훅: 세션 시작, 메시지 입력)` | 둘 다 매번 지시를 넣는다. 방향은 같다(짧게, 작게) | 창업자 결정으로 모두 켜 두고, 답변이 한쪽으로 치우치는지 지켜본다 | 2026-10-27 충돌 검사 |
| `aws-startup-advisor (훅: 세션 시작)` | "스타트업 관점" 지시를 넣도록 돼 있지만, 읽을 파일이 없어 지금은 작동하지 않는다 | 업데이트로 파일이 생기면 다시 확인한다 | Plugin Issues #18 |

## 3. 스킬을 쓰지 않아도 되는 경우

- 한두 줄 수정, 오타 고치기, 이름 바꾸기
- 질문에 답하기, 파일 몇 개를 읽고 설명하기
- 허브 기록 갱신(Kanban, Portfolio 등)
- 이미 정해진 절차를 그대로 따르는 반복 작업
- 스킬을 불렀더니 결과가 나빠지거나 느려진 작업 (리포트에 남긴다)

판단 기준: 스킬의 절차나 지식이 없으면 결과가 나빠지는 작업에만 쓴다.

## 4. 이 문서를 고치는 방법

1. 작업 중에 스킬 이슈가 생기면 바로 [Plugin Issues](Plugin%20Issues.md)에 한 줄 추가한다. 이 문서의 우선순위나 충돌 표, 또는 [Plugins](Plugins.md)의 상태를 바꾸면 [Plugin Changelog](Plugin%20Changelog.md)에 한 줄 추가한다.
2. 플러그인을 설치하거나 업데이트하면 [Plugin Review](Plugin%20Review.md) 순서로 검토하고, `python3 scripts/plugin-audit.py conflicts`로 충돌 후보를 뽑아 실제 충돌은 2번 표에 추가한다.
3. 프로젝트나 큰 작업을 마치면 `python3 scripts/plugin-audit.py usage --root <저장소> --since <시작일>`로 사용 횟수를 뽑고, `Plugin Reports/_Template.md`로 리포트를 쓴다.
4. 주간 리뷰 때는 아래 "6. 주간 점검"을 따른다.
5. 스킬 상태(시험 사용 → 채택 또는 제외)는 [Plugins](Plugins.md)에서 바꾼다. 제외는 창업자가 정한다.

## 5. 운영 규칙

**설치와 업데이트**
- 새 플러그인은 [Plugin Review](Plugin%20Review.md) 순서로 검토한 뒤 설치하고, `plugin-reviews.json`에 검토한 버전과 커밋을 적는다.
- 같은 서비스는 한 플러그인에서만 로그인한다(DEC-001 외부 서비스 연결은 플러그인 우선 (운영 허브 문서)).
- 지금 단계에 필요 없는 플러그인은 `claude plugin disable <이름>`으로 사용을 중지한다. 다시 켤 때는 `claude plugin enable <이름>`을 실행하고, 한 저장소에서만 쓰려면 `--scope project`를 붙인다. 다시 켜면 그 플러그인의 설명을 `plugin-descriptions.ko.json`에 한국어로 옮긴다.

**폴더별 적용 범위**
- 한국어 문체 플러그인(fluent-korean, humanize-korean)은 허브와 제품 저장소에서만 켠다. 새 제품 저장소를 만들면 그 저장소에서 아래 두 명령을 실행하고, `.claude/settings.json`에 `"outputStyle": "fluent-korean"`을 넣는다.
  - `claude plugin enable fluent-korean@fluent-korean --scope project`
  - `claude plugin enable humanize-korean@im-not-ai --scope project`
- 결제, 배포, 분석 플러그인(stripe, cloudflare, posthog)은 필요해지면 그 제품 저장소에서만 켠다.

**자체 제작 스킬**
- `products/side-toolkit/plugins/side-skills/skills/`에 만든다.
- 고친 뒤에는 `plugins/side-skills/.claude-plugin/plugin.json`과 `.claude-plugin/marketplace.json`의 버전을 올리고, `claude plugin marketplace update side-toolkit`과 `claude plugin update side-skills@side-toolkit`을 실행한다.
- 실제 작업에서 놓친 패턴이 보이면 [Plugin Issues](Plugin%20Issues.md)에 남기고 스킬에 추가한다.

**공개 저장소 반영**
- 플러그인 문서(`Plugins.md`, `Plugin Components.md`, `plugin-descriptions.ko.json`, `Plugin Review.md`, `Plugin Playbook.md`, `Plugin Changelog.md`, `Plugin Issues.md`, `Plugin Reports/`, `plugin-reviews.json`, `scripts/plugin-audit.py`)는 허브가 원본이다. 평소에는 허브에서만 고친다.
- 공개 저장소 `products/side-toolkit`에는 주간 점검 때 한 번에 반영한다. 공개 저장소이므로 실제 사용자 정보, 키, 개인 경로를 쓰지 않는다.

## 6. 주간 점검

주간 리뷰 때 이 순서로 한다. 결과는 그 주의 `Weekly Reviews/YYYY-Www.md`에 짧게 남긴다.

0. **구성 요소 목록 갱신:** `python3 scripts/plugin-audit.py components > "Plugin Components.md"`로 [Plugin Components](Plugin%20Components.md)를 다시 만든다.
1. **업데이트 확인:** `python3 scripts/plugin-audit.py drift --reviews plugin-reviews.json`. "다시 검토 필요"나 "검토 기록 없음"이 나오면 [Plugin Review](Plugin%20Review.md) 순서로 검토한다. "한국어 설명이 없거나 낡은 항목"이 나오면 `plugin-descriptions.ko.json`에 옮기고 0번을 다시 한다.
2. **충돌 확인:** 지난주에 플러그인을 설치하거나 업데이트했다면 `python3 scripts/plugin-audit.py conflicts`를 실행하고, 실제 충돌은 2번 표에 추가한다.
3. **공식 플러그인 출시 확인:** Integrations (운영 허브 문서)의 커넥터 서비스마다 공식 플러그인이 나왔는지 플러그인 디렉터리에서 검색하고, 결과를 같은 문서의 "공식 플러그인 출시 확인 기록"에 한 줄 남긴다. 나왔으면 창업자에게 설치를 제안한다.
4. **리포트 반영:** 새 리포트를 읽고, 같은 결과가 두 번 이상 나왔으면 1번, 2번 표의 근거를 "가설"에서 리포트 이름으로 바꾼다. 바꾼 내용은 [Plugin Changelog](Plugin%20Changelog.md)에 남긴다.
5. **이슈 정리:** [Plugin Issues](Plugin%20Issues.md)에서 "열림", "관찰 중"인 줄을 훑고, 처리할 수 있는 것은 처리한다.
6. **공개 저장소 반영:** `products/side-toolkit`에서 순서대로 한다.
   1. `scripts/sync-from-hub.sh`로 허브 문서를 복사한다.
   2. 키와 개인 정보가 들어갔는지 검사한다.
   3. 바뀐 문서를 **모두** 점검한다. 스크립트로 다시 만든 Plugin Components도 포함한다. 한국어는 `checking-korean-writing`, 영어는 `writing-quality`를 쓰고, 고칠 곳은 허브 원본에서 고친 뒤 다시 복사한다.
   4. `python3 scripts/plugin-audit.py summary`로 숫자를 뽑아 README "한눈에 보기"를 맞춘다.
   5. 커밋하고 푸시한다.

월간 재검토 때는 `python3 scripts/plugin-audit.py usage --root ~/SideProjects --since <한 달 전>`으로 한 번도 쓰지 않은 플러그인을 찾아 사용 중지 후보로 올린다.
