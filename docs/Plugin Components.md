---
type: generated
status: generated
---

# Plugin Components

플러그인마다 들어 있는 스킬, 명령, 에이전트, 훅, MCP 서버, 출력 스타일의 목록이다. `python3 scripts/plugin-audit.py components`로 만든 문서라 손으로 고치지 않는다. 스킬, 명령, 에이전트의 설명은 각 플러그인의 원문을 한국어로 옮긴 것이고(`plugin-descriptions.ko.json`), 훅의 "하는 일"은 검토하면서 `plugin-reviews.json`에 적어 둔 내용이다. 사용 중지한 플러그인은 이름만 적고, 다시 켤 때 번역한다. 왜 설치했는지와 상태는 [Plugins](Plugins.md)에, 어떤 스킬을 먼저 쓰는지는 [Plugin Playbook](Plugin%20Playbook.md)에 있다.

| 플러그인 | 켜짐 | 스킬 | 명령 | 에이전트 | 훅 | MCP | 출력 스타일 |
|---|---|---|---|---|---|---|---|
| [caveman](#caveman) | 예 | 22 | 7 | 3 | 4 | 0 | 0 |
| [cloudflare](#cloudflare) | 아니오 | 14 | 0 | 0 | 0 | 1 | 0 |
| [fluent-korean](#fluent-korean) | 예 | 0 | 0 | 0 | 0 | 0 | 2 |
| [humanize-korean](#humanize-korean) | 예 | 4 | 4 | 9 | 0 | 0 | 0 |
| [impeccable](#impeccable) | 예 | 1 | 0 | 4 | 3 | 0 | 0 |
| [marketing-skills](#marketing-skills) | 예 | 52 | 0 | 0 | 0 | 0 | 0 |
| [marketing](#marketing) | 예 | 8 | 0 | 0 | 0 | 13 | 0 |
| [playwright](#playwright) | 예 | 0 | 0 | 0 | 0 | 1 | 0 |
| [ponytail](#ponytail) | 예 | 6 | 6 | 0 | 3 | 0 | 0 |
| [posthog](#posthog) | 아니오 | 161 | 3 | 1 | 2 | 1 | 0 |
| [side-skills](#side-skills) | 예 | 3 | 0 | 0 | 0 | 0 | 0 |
| [stripe](#stripe) | 아니오 | 10 | 2 | 1 | 7 | 1 | 0 |
| [supabase](#supabase) | 예 | 2 | 0 | 0 | 0 | 1 | 0 |
| [taste-skill](#taste-skill) | 예 | 1 | 0 | 0 | 0 | 0 | 0 |
| [ui-ux-pro-max](#ui-ux-pro-max) | 예 | 7 | 0 | 0 | 0 | 0 | 0 |
| [frontend-design](#frontend-design) | 예 | 1 | 0 | 0 | 0 | 0 | 0 |
| [engineering](#engineering) | 예 | 10 | 0 | 0 | 0 | 10 | 0 |
| [gtm-planner](#gtm-planner) | 예 | 7 | 0 | 4 | 0 | 4 | 0 |
| [aws-startup-advisor](#aws-startup-advisor) | 예 | 9 | 0 | 6 | 1 | 4 | 0 |
| [superpowers](#superpowers) | 예 | 15 | 0 | 0 | 1 | 0 | 0 |
| [review-council](#review-council) | 예 | 1 | 0 | 6 | 1 | 0 | 0 |
| [writing-quality](#writing-quality) | 예 | 4 | 0 | 0 | 0 | 0 | 0 |
| [context7](#context7) | 예 | 0 | 0 | 0 | 0 | 1 | 0 |
| [product-management](#product-management) | 예 | 8 | 1 | 0 | 0 | 16 | 0 |

## caveman

로컬 · 켜짐 · 버전 4.0.1 · 커밋 9b68f7e

> 답변을 아주 짧게 줄이는 대화 모드다.

**스킬 22개**

| 스킬 | 설명 |
|---|---|
| `caveman:cavecrew` | 코드 찾기, 1~2개 파일 수정, 변경 리뷰를 직접 하지 않고 cavecrew 에이전트에게 맡길 때를 알려 준다. |
| `caveman:caveman` | 결론부터 짧게 답하고, 군더더기는 빼되 기술적인 사실은 모두 남긴다. |
| `caveman:caveman-commit` | 의도만 남긴 짧은 Conventional Commits 커밋 메시지를 쓴다. |
| `caveman:caveman-compress` | CLAUDE.md나 할 일 목록 같은 메모 파일을 짧게 압축해 입력 토큰을 줄인다. 원본은 백업해 둔다. (파일 내용을 모델 제공자에게 보낸다) |
| `caveman:caveman-discover` | 저장소의 LLM 사용 흐름을 찾아 이름을 붙여, Caveman Cloud가 비용을 흐름별로 나눠 보게 한다. |
| `caveman:caveman-evidence-review` | Caveman Cloud가 모은 비용, 점수, 지연 시간, 오류, 절감액 기록을 읽기만 하며 검토한다. |
| `caveman:caveman-explore` | 처음 보는 저장소를 파악하거나, 여러 파일에 걸친 코드를 찾거나, 직접 검색이 실패했을 때 쓰는 읽기 전용 탐색기다. |
| `caveman:caveman-help` | caveman 스킬과 명령을 한눈에 정리한 안내를 보여 준다. |
| `caveman:caveman-learn` | 토큰을 많이 쓰는 곳을 정리한 Caveman 보고서를 보고, 비용을 줄이는 수정을 하나씩 동의받아 적용한 뒤 결과를 보고한다. |
| `caveman:caveman-manage` | Caveman Cloud의 실험 진행 상태를 확인하고, 위험한 실행을 막는다. |
| `caveman:caveman-optimize` | Caveman이 찾은 최적화 후보를 고르고, 기준과 비교하는 평가를 준비한다. |
| `caveman:caveman-review` | 발견한 문제마다 위치, 문제, 고칠 방법을 한 줄씩 적는 짧은 코드 리뷰를 한다. |
| `caveman:caveman-setup` | 저장소의 LLM 요청이 Caveman Cloud 게이트웨이를 거치게 연결해, 동작은 그대로 두고 사용량을 측정한다. (외부로 요청을 보낸다) |
| `caveman:caveman-stats` | 지금 Claude Code 세션의 토큰 사용량과 모드별 비중을 보여 준다. |
| `caveman:investigate-first` | 원인이 불분명한 오류는 코드를 고치기 전에 먼저 진단한다. |
| `caveman:lean-build` | 기능을 과하게 만들 위험이 큰 작업을 최소 범위로 만든다. |
| `caveman:megacave` | 답변을 한문(文言文) 문체로 극도로 짧게 쓴다. 기술 용어는 그대로 둔다. |
| `caveman:migration` | 되돌릴 수 있고 호환성을 지키는 방식으로 이전 작업을 한다. |
| `caveman:safe-refactor` | 동작은 그대로 두고 코드 구조만 바꾼다. |
| `caveman:surgical-patch` | 버그와 작은 동작 변경을 가장 좁은 범위에서 고친다. |
| `caveman:ultracave` | 가장 강하게 압축한다. 한 단어로 충분하면 한 단어만 쓰고, 같은 사실은 한 번만 말한다. |
| `caveman:verify-and-stop` | 범위를 넓히지 않고, 이미 한 작업이 완료 조건을 만족하는지만 확인한다. |

**명령 7개**

| 명령 | 설명 |
|---|---|
| `/caveman` | caveman 모드를 켜고 끄거나 상태를 확인한다. |
| `/caveman-commit` | 짧은 caveman 방식 커밋 메시지를 만든다. |
| `/caveman-init` | 모든 IDE 에이전트에 caveman 모드가 항상 켜지도록 저장소에 규칙 파일을 넣는다. |
| `/caveman-review` | 한 줄짜리 코드 리뷰 의견을 단다. |
| `/caveman-stats` | 세션의 토큰 사용량을 보여 준다. |
| `/megacave` | 한문 문체로 압축하는 megacave 모드를 켠다. |
| `/ultracave` | 가장 강하게 압축하는 ultracave 모드를 켠다. |

**에이전트 3개**

| 에이전트 | 설명 |
|---|---|
| `cavecrew-builder` | 1~2개 파일만 정밀하게 고치는 에이전트다. |
| `cavecrew-investigator` | 코드 위치만 찾아 주는 읽기 전용 에이전트다. |
| `cavecrew-reviewer` | 변경, 브랜치, 파일을 리뷰하는 에이전트다. |

**훅 4개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionStart | 전체 | caveman 모드 지시와 설정을 불러와 대화에 넣는다 | 예 |
| SubagentStart | 전체 | 서브에이전트에도 같은 짧은 답변 지시를 넣는다 | 예 |
| UserPromptSubmit | 전체 | 메시지마다 짧게 답하라는 지시를 넣고, /caveman 명령으로 바뀐 모드를 기록한다 | 예 |
| SessionEnd | 전체 | 세션의 토큰 사용 통계를 로컬에 기록한다 | 아니오 |

## cloudflare

로컬 · 꺼짐 · 버전 1.0.0 · 커밋 b052c32

사용 중지한 플러그인이라 이름만 적는다. 다시 켤 때 설명을 번역한다.

스킬 14개, 명령 0개, 에이전트 0개: `cloudflare:agents-sdk`, `cloudflare:cloudflare`, `cloudflare:cloudflare-email-service`, `cloudflare:cloudflare-one`, `cloudflare:cloudflare-one-migrations`, `cloudflare:durable-objects`, `cloudflare:nextjs-on-cloudflare`, `cloudflare:sandbox-migrate-to-next`, `cloudflare:sandbox-next`, `cloudflare:sandbox-stable`, `cloudflare:turnstile-spin`, `cloudflare:web-perf`, `cloudflare:workers-best-practices`, `cloudflare:wrangler`

**MCP 서버 1개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| cloudflare | http | `https://mcp.cloudflare.com/mcp` |

## fluent-korean

로컬 · 켜짐 · 버전 1.0.0 · 커밋 ce8683f

> Claude Code가 유창하고 자연스러운 한국어로 답하게 하는 출력 스타일이다.

**출력 스타일 2개**: `fluent-korean-not-coding`, `fluent-korean`

## humanize-korean

로컬 · 켜짐 · 버전 2.3.2 · 커밋 b37e020

> AI가 쓴 한국어를 사람이 쓴 글처럼 다듬는다. 글 상태에 따라 가볍게(1회), 보통(2회), 깊게(3회 이상) 처리한다.

**스킬 4개**

| 스킬 | 설명 |
|---|---|
| `humanize-korean:humanize` | AI가 쓴 한국어를 자연스럽게 다듬는 시작 명령이다. |
| `humanize-korean:humanize-korean` | ChatGPT, Claude, Gemini 등이 쓴 한국어를 사람이 쓴 글처럼 다듬는 총괄 스킬이다. |
| `humanize-korean:humanize-redo` | 가장 최근에 다듬은 결과를 한 번 더 다듬는다. 특정 유형, 문단, 강도만 조정할 수도 있다. |
| `humanize-korean:humanize-scan` | 한국어 글에 AI 티가 얼마나 있는지 재고, 고치면 어떻게 되는지 표본으로 보여 준다. |

**명령 4개**

| 명령 | 설명 |
|---|---|
| `/humanize` | AI가 쓴 한국어를 다듬는다. |
| `/humanize-korean` | AI가 쓴 한국어를 사람이 쓴 글처럼 다듬는다. |
| `/humanize-redo` | 최근 결과를 한 번 더 다듬는다. |
| `/humanize-scan` | AI 티가 얼마나 있는지 먼저 살펴본다. |

**에이전트 9개**

| 에이전트 | 설명 |
|---|---|
| `humanize-diagnostician` | 정밀 모드의 1단계로, 글을 지배하는 AI 티 패턴 3~6개를 진단한다. |
| `humanize-finalizer` | 정밀 모드의 3단계로, 원문과 다듬은 글을 비교해 의미가 바뀐 곳과 남은 AI 티만 고친다. |
| `humanize-monolith` | 가볍게, 보통, 깊게 모든 경로에서 한 번의 호출로 탐지, 윤문, 자체 검증을 한다. |
| `korean-ai-tell-taxonomist` | AI가 쓴 한국어의 AI 티 패턴을 분류하고, 새 패턴을 검증해 목록에 올린다. |
| `korean-translation-scholar` | 국내외 번역학 연구의 인용 근거를 패턴 분류 체계에 연결한다. |
| `post-editese-metric-engineer` | 번역투의 특징(단순화, 정규화, 간섭)을 한국어 정량 지표로 만들어 회귀 검증에 쓴다. |
| `quick-rules-integrator` | 새 분류 체계와 지표를 간단 규칙집에 반영하고, 검증한 뒤 PR 초안과 변경 기록을 쓴다. |
| `taxonomy-gap-analyzer` | 기존 분류 체계와 외부 연구의 후보 패턴을 비교해, 이미 있는 것, 보강할 것, 새로운 것으로 나눈다. |
| `translationese-research-distiller` | 번역투 연구 보고서를 유형, 체크리스트, 예문으로 나눠 다음 단계가 바로 쓸 수 있는 JSON으로 정리한다. |

## impeccable

로컬 · 켜짐 · 버전 4.7.1 · 커밋 989c484

> 프론트엔드 디자인을 설계하고 점검한다.

**스킬 1개**

| 스킬 | 설명 |
|---|---|
| `impeccable:impeccable` | 웹사이트, 랜딩 페이지, 대시보드, 제품 화면을 설계, 재설계, 비평, 점검, 다듬기, 단순화, 보강, 애니메이션 추가 등으로 개선한다. |

**에이전트 4개**

| 에이전트 | 설명 |
|---|---|
| `impeccable-asset-producer` | 승인된 시안을 바탕으로, 방향은 바꾸지 않고 다시 쓸 수 있는 이미지 에셋을 만든다. |
| `impeccable-documenter` | 완성된 화면에서 디자인 시스템을 뽑아 DESIGN.md로 기록한다. |
| `impeccable-finish-reviewer` | 완성된 화면을 정한 방향, 승인된 시안, 품질 기준과 비교해 고칠 점을 순서대로 정리한다. |
| `impeccable-manual-edit-applier` | 사람이 화면에서 직접 고친 문구를 소스 코드에 반영한다. |

**훅 3개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionStart | 전체 | 디자인 엔진을 준비한다 | 예 |
| PostToolUse | Edit¦Write | 파일을 고친 뒤 UI 변경을 점검한다 | 아니오 |
| Stop | 전체 | 답변이 끝날 때 디자인을 한 번 더 점검한다(최대 30초) | 아니오 |

## marketing-skills

로컬 · 켜짐 · 버전 2.13.4 · 커밋 f90b9d3

> 전환율 개선, 카피, SEO, 광고, 성장을 다루는 마케팅 스킬 모음이다.

**스킬 52개**

| 스킬 | 설명 |
|---|---|
| `marketing-skills:ab-testing` | A/B 테스트나 실험을 계획하고 설계하고 실행한다. 꾸준한 실험 체계도 만든다. |
| `marketing-skills:ad-creative` | 광고 플랫폼용 제목, 설명, 본문, 광고 변형을 만들고 다듬는다. |
| `marketing-skills:ads` | Google, Meta, LinkedIn, X 등의 유료 광고 캠페인 전략, 타깃팅, 입찰, 최적화를 돕는다. |
| `marketing-skills:ai-seo` | AI 검색 엔진에 인용되고 AI 답변에 나오도록 콘텐츠를 최적화한다. |
| `marketing-skills:analytics` | 분석 추적과 측정을 설정하고 개선하고 점검한다. |
| `marketing-skills:aso` | App Store와 Google Play 등록 정보를 점검하고 최적화한다. |
| `marketing-skills:attribution` | 실제로 전환과 매출을 만드는 마케팅을 찾고, 기여 모델을 고르고, 서로 다른 숫자를 맞춘다. |
| `marketing-skills:churn-prevention` | 이탈을 줄인다. 해지 흐름, 붙잡기 제안, 결제 실패 복구, 유지 전략을 만든다. |
| `marketing-skills:co-marketing` | 공동 마케팅 파트너를 찾고, 함께 할 캠페인을 계획한다. |
| `marketing-skills:cold-email` | 답장을 받는 B2B 콜드 메일과 후속 메일, 발송 설정, LinkedIn 연락, 답장 처리까지 맡는다. |
| `marketing-skills:community-marketing` | 온라인 커뮤니티를 만들고 키워 제품 성장과 브랜드 충성도를 높인다. |
| `marketing-skills:competitor-profiling` | 경쟁사 URL을 받아 조사하고 프로필을 만든다. |
| `marketing-skills:competitors` | SEO와 구매자를 위한 경쟁사 비교 페이지와 대안 페이지를 만든다. |
| `marketing-skills:content-strategy` | 콘텐츠 전략을 세우고, 무엇을 만들지와 어떤 주제를 다룰지 정한다. |
| `marketing-skills:conversion-tracking` | 웹사이트 전환 추적을 설정하고, 점검하고, 고친다. |
| `marketing-skills:copy-editing` | 이미 있는 마케팅 문구를 고치고 다듬거나, 낡은 내용을 새로 고친다. |
| `marketing-skills:copywriting` | 홈, 랜딩, 가격, 기능, 소개 페이지 등의 마케팅 문구를 쓰거나 고친다. |
| `marketing-skills:cro` | 마케팅 페이지와 입력 폼의 전환율을 높인다. |
| `marketing-skills:customer-research` | 고객 조사를 진행하고 분석하고 정리한다. |
| `marketing-skills:directory-submissions` | 스타트업, SaaS, AI, MCP 디렉터리 등에 제품을 등록해 백링크와 노출을 얻는다. |
| `marketing-skills:emails` | 이메일 시퀀스, 드립 캠페인, 자동 메일 흐름을 만들고 개선한다. |
| `marketing-skills:events` | 웨비나, 컨퍼런스, 밋업 같은 행사를 계획하고 운영하고, 거기서 잠재 고객을 얻는다. |
| `marketing-skills:free-tools` | 리드 확보, SEO, 인지도를 위한 무료 도구를 기획하고 평가하고 만든다. |
| `marketing-skills:image` | 블로그 대표 이미지, SNS 그래픽, 제품 목업 같은 마케팅 이미지를 만들고 편집하고 최적화한다. |
| `marketing-skills:influencer-marketing` | 인플루언서와 크리에이터 협업을 찾고, 조건을 정하고, 안내하고, 성과를 잰다. |
| `marketing-skills:launch` | 제품 런칭, 기능 발표, 출시 전략을 계획한다. |
| `marketing-skills:lead-magnets` | 이메일 수집과 리드 확보를 위한 리드 마그넷을 기획하고 만든다. |
| `marketing-skills:link-building` | 순위와 AI 인용을 높이는 백링크와 외부 언급을 얻는다. |
| `marketing-skills:marketing-council` | 유명 마케터들의 관점을 흉내 낸 자문단이 마케팅 질문에 여러 의견을 낸다. |
| `marketing-skills:marketing-ideas` | SaaS와 소프트웨어 제품의 마케팅 아이디어와 전략을 제안한다. |
| `marketing-skills:marketing-loops` | AI 에이전트가 주기적으로 돌리는 반복 마케팅 작업을 만든다. |
| `marketing-skills:marketing-plan` | 제품의 종합 마케팅 계획을 세운다. |
| `marketing-skills:marketing-psychology` | 심리학 원리와 행동과학을 마케팅에 적용한다. |
| `marketing-skills:offers` | 실제로 파는 상품의 가치 제시, 보너스, 보증, 희소성 같은 제안 구성을 설계한다. |
| `marketing-skills:onboarding` | 가입 후 온보딩, 첫 사용 경험, 가치를 느끼기까지의 시간을 개선한다. |
| `marketing-skills:paywalls` | 앱 안의 결제 화면, 업그레이드 화면, 기능 잠금을 만들고 개선한다. |
| `marketing-skills:popups` | 전환을 위한 팝업, 모달, 배너를 만들고 개선한다. |
| `marketing-skills:pricing` | 가격 결정, 요금제 구성, 수익화 전략을 돕는다. |
| `marketing-skills:product-marketing` | 제품 마케팅의 기본 맥락 문서(고객, 포지셔닝 등)를 만들거나 고친다. |
| `marketing-skills:programmatic-seo` | 템플릿과 데이터로 SEO 페이지를 대량으로 만든다. |
| `marketing-skills:prospecting` | 연락할 잠재 고객을 찾고 걸러 목록을 만든다. |
| `marketing-skills:public-relations` | 언론 보도, 기자 연락, 미디어 전략을 돕는다. |
| `marketing-skills:referrals` | 추천 프로그램, 제휴 프로그램, 입소문 전략을 만들고 분석한다. |
| `marketing-skills:revops` | 매출 운영, 리드 관리, 마케팅에서 영업으로 넘기는 과정을 다룬다. |
| `marketing-skills:sales-enablement` | 영업 자료, 피치 덱, 한 장 소개서, 반론 대응 문서, 데모 대본을 만든다. |
| `marketing-skills:schema` | 사이트의 구조화 데이터(schema)를 추가하고 고치고 최적화한다. |
| `marketing-skills:seo-audit` | 사이트의 SEO 문제를 점검하고 진단한다. |
| `marketing-skills:signup` | 가입, 계정 생성, 체험 시작 흐름을 개선한다. |
| `marketing-skills:site-architecture` | 웹사이트의 페이지 구조, 메뉴, URL, 내부 링크를 설계하거나 다시 짠다. |
| `marketing-skills:sms` | SMS, MMS, WhatsApp 마케팅을 계획하고 만들고 개선한다. |
| `marketing-skills:social` | LinkedIn, X, Instagram, TikTok, Facebook용 SNS 콘텐츠를 만들고 예약하고 개선한다. |
| `marketing-skills:video` | AI 도구나 코드로 영상 콘텐츠를 만든다. |

## marketing

로컬 · 켜짐 · 버전 1.2.0 · 커밋 33d3dea

> 여러 마케팅 채널에서 콘텐츠를 만들고, 캠페인을 계획하고, 성과를 분석한다.

**스킬 8개**

| 스킬 | 설명 |
|---|---|
| `marketing:brand-review` | 콘텐츠가 브랜드 목소리, 스타일 가이드, 핵심 메시지와 맞는지 검토하고, 어긋난 곳을 고친 예와 함께 알려 준다. |
| `marketing:campaign-plan` | 목표, 대상, 메시지, 채널 전략, 콘텐츠 일정, 성공 지표를 담은 캠페인 계획서를 만든다. |
| `marketing:competitive-brief` | 경쟁사를 조사해 포지셔닝과 메시지를 비교하고, 콘텐츠 빈틈과 기회, 위협을 정리한다. |
| `marketing:content-creation` | 블로그, SNS, 뉴스레터, 랜딩 페이지, 보도자료, 사례 글 등 채널별 마케팅 콘텐츠 초안을 쓴다. |
| `marketing:draft-content` | 채널별 형식과 SEO 제안을 넣어 블로그, SNS, 뉴스레터, 랜딩 페이지 등의 초안을 쓴다. |
| `marketing:email-sequence` | 여러 통으로 이어지는 이메일의 문구, 발송 시점, 분기 조건, 종료 조건을 설계하고 쓴다. |
| `marketing:performance-report` | 핵심 지표, 추세, 잘된 점과 아쉬운 점, 우선 개선 과제를 담은 마케팅 성과 보고서를 만든다. |
| `marketing:seo-audit` | 키워드 조사, 페이지 분석, 콘텐츠 빈틈, 기술 점검, 경쟁사 비교까지 SEO를 종합 점검한다. |

**MCP 서버 13개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| slack | http | `https://mcp.slack.com/mcp` |
| canva | http | `https://mcp.canva.com/mcp` |
| figma | http | `https://mcp.figma.com/mcp` |
| hubspot | http | `https://mcp.hubspot.com/anthropic` |
| amplitude | http | `https://mcp.amplitude.com/mcp` |
| amplitude-eu | http | `https://mcp.eu.amplitude.com/mcp` |
| notion | http | `https://mcp.notion.com/mcp` |
| ahrefs | http | `https://api.ahrefs.com/mcp/mcp` |
| similarweb | http | `https://mcp.similarweb.com` |
| klaviyo | http | `https://mcp.klaviyo.com/mcp` |
| supermetrics | http | `https://mcp.supermetrics.com/mcp` |
| google calendar | http | `-` |
| gmail | http | `-` |

## playwright

로컬 · 켜짐 · 버전 58267944f921 · 커밋 5826794

> Microsoft가 만든 브라우저 자동화와 E2E 테스트용 MCP 서버다.

**MCP 서버 1개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| playwright | stdio | `npx @playwright/mcp@latest` |

## ponytail

로컬 · 켜짐 · 버전 5.3.2 · 커밋 09c434a

> 가장 게으른 시니어 개발자처럼 최소한으로 만드는 모드다.

**스킬 6개**

| 스킬 | 설명 |
|---|---|
| `ponytail:ponytail` | 작업을 완전히 해결하는 가장 작은 변경을 하고, 바쁜 사람이 한 번에 읽을 수 있게 답한다. |
| `ponytail:ponytail-audit` | 저장소 전체를 점검한다. 버그, 보안 구멍, 실제 부하에서 깨질 곳, 테스트 없는 위험한 코드, 느린 부분, 지우거나 합칠 코드를 찾는다. |
| `ponytail:ponytail-debt` | 코드에 남긴 `shortcut:` 주석을 모아 기술 부채 목록을 만든다. |
| `ponytail:ponytail-gain` | ponytail로 줄인 코드량, 비용, 시간을 보여 준다. |
| `ponytail:ponytail-help` | ponytail 단계, 스킬, 명령을 한눈에 안내한다. |
| `ponytail:ponytail-review` | 변경을 점검한다. 로직이 맞는지, 안전한지, 부하를 견디는지, 위험한 코드에 테스트가 있는지, 충분히 빠른지, 모든 줄이 필요한지 본다. |

**명령 6개**

| 명령 | 설명 |
|---|---|
| `/ponytail` | ponytail 단계를 바꾼다(lite, full, ultra, off). |
| `/ponytail-audit` | 저장소 전체의 버그, 보안, 부하, 테스트, 속도, 군살을 점검한다. |
| `/ponytail-debt` | `shortcut:` 주석을 모아 기술 부채 목록으로 만든다. |
| `/ponytail-gain` | 줄인 코드량, 비용, 시간을 점수판으로 보여 준다. |
| `/ponytail-help` | ponytail 단계, 스킬, 명령을 안내한다. |
| `/ponytail-review` | 지금 변경의 버그, 보안, 부하, 테스트, 속도, 군살을 점검한다. |

**훅 3개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionStart | startup¦resume¦clear¦compact | 가장 작게 만들라는 지시를 넣는다 | 예 |
| SubagentStart | 전체 | 서브에이전트에도 같은 지시를 넣는다 | 예 |
| UserPromptSubmit | 전체 | 메시지마다 지시를 넣고, /ponytail 명령으로 바뀐 단계를 기록한다 | 예 |

## posthog

로컬 · 꺼짐 · 버전 1.1.67 · 커밋 e0fbf5e

사용 중지한 플러그인이라 이름만 적는다. 다시 켤 때 설명을 번역한다.

스킬 161개, 명령 3개, 에이전트 1개: `posthog:adding-warehouse-person-properties`, `posthog:analyzing-expensive-users`, `posthog:analyzing-experiment-session-replays`, `posthog:analyzing-task-runs`, `posthog:assessing-heatmaps`, `posthog:auditing-endpoints`, `posthog:auditing-experiments-flags`, `posthog:auditing-warehouse-source-health`, `posthog:auditing-warehouse-view-health`, `posthog:authoring-data-quality-checks`, `posthog:authoring-error-tracking-alerts`, `posthog:authoring-log-alerts`, `posthog:authoring-scouts`, `posthog:building-a-dashboard`, `posthog:building-canvases`, `posthog:building-html-canvases`, `posthog:building-loops`, `posthog:building-react-quill-canvases`, `posthog:building-workflows`, `posthog:checking-deploy-timing`, `posthog:checking-member-access`, `posthog:choosing-trend-or-slope-view`, `posthog:cleaning-up-stale-feature-flags`, `posthog:composing-grid-canvases`, `posthog:configuring-experiment-analytics`, `posthog:configuring-experiment-rollout`, `posthog:consuming-endpoints-from-client-code`, `posthog:context-layer-consolidation`, `posthog:context-layer-dreaming`, `posthog:context-layer-health-check`, `posthog:copying-endpoints-across-projects`, `posthog:copying-flags-across-projects`, `posthog:creating-ai-subscription`, `posthog:creating-an-endpoint`, `posthog:creating-box-plot-insights`, `posthog:creating-experiments`, `posthog:creating-online-evaluations`, `posthog:creating-replay-vision-scanners`, `posthog:creating-surveys`, `posthog:debugging-experiments`, `posthog:debugging-surveys`, `posthog:designing-email-templates`, `posthog:diagnosing-ci-and-merge-bottlenecks`, `posthog:diagnosing-endpoint-performance`, `posthog:diagnosing-experiment-results`, `posthog:diagnosing-failed-warehouse-syncs`, `posthog:diagnosing-missing-recordings`, `posthog:diagnosing-sdk-health`, `posthog:diagnosing-stacktrace-symbolication`, `posthog:downloading-batch-export-files`, `posthog:exploring-ai-failures`, `posthog:exploring-apm-traces`, `posthog:exploring-autocapture-events`, `posthog:exploring-endpoint-execution-logs`, `posthog:exploring-live-traffic`, `posthog:exploring-llm-clusters`, `posthog:exploring-llm-costs`, `posthog:exploring-llm-evaluations`, `posthog:exploring-llm-traces`, `posthog:exploring-mcp-intent-clusters`, `posthog:exploring-mcp-sessions`, `posthog:exploring-mcp-tool-original-user-motive`, `posthog:exploring-mcp-tool-quality`, `posthog:exploring-mcp-tool-usage`, `posthog:exploring-replay-vision-observations`, `posthog:exploring-scouts`, `posthog:feature-usage-feed`, `posthog:filtering-bot-traffic`, `posthog:finding-deleted-feature-flags`, `posthog:finding-experiments`, `posthog:finding-replay-for-issue`, `posthog:finding-sessions-to-watch`, `posthog:formatting-insight-axes`, `posthog:grouping-noisy-errors`, `posthog:inbox-exploration`, `posthog:instrument-error-tracking`, `posthog:instrument-feature-flags`, `posthog:instrument-integration`, `posthog:instrument-llm-analytics`, `posthog:instrument-logs`, `posthog:instrument-metrics`, `posthog:instrument-product-analytics`, `posthog:investigate-metric`, `posthog:investigating-ci-failures`, `posthog:investigating-error-issue`, `posthog:investigating-logs`, `posthog:investigating-metric-anomalies`, `posthog:investigating-replay`, `posthog:managing-endpoint-versions`, `posthog:managing-experiment-lifecycle`, `posthog:managing-path-cleaning-rules`, `posthog:managing-reminders`, `posthog:managing-streamlit-apps`, `posthog:managing-subscriptions`, `posthog:modeling-activation-metrics`, `posthog:modeling-conversion-metrics`, `posthog:modeling-dimension-tables`, `posthog:modeling-product-usage-metrics`, `posthog:modeling-revenue-metrics`, `posthog:modeling-warehouse-foundations`, `posthog:querying-canvas-data`, `posthog:querying-posthog-data`, `posthog:resolving-ingestion-warnings`, `posthog:review-hog-authoring`, `posthog:review-hog-blind-spots-general`, `posthog:review-hog-perspective-contracts-security`, `posthog:review-hog-perspective-logic-correctness`, `posthog:review-hog-perspective-performance-reliability`, `posthog:review-hog-resolution-criteria`, `posthog:review-hog-validation-criteria`, `posthog:scanning-experiments-with-replay-vision`, `posthog:setting-up-a-custom-rest-source`, `posthog:setting-up-a-data-warehouse-source`, `posthog:setting-up-data-catalog`, `posthog:setting-up-warehouse-properties`, `posthog:signals`, `posthog:signals-scout-ai-observability`, `posthog:signals-scout-anomaly-detection`, `posthog:signals-scout-apm`, `posthog:signals-scout-conversations`, `posthog:signals-scout-csp-violations`, `posthog:signals-scout-customer-analytics`, `posthog:signals-scout-customer-analytics-billing-and-usage`, `posthog:signals-scout-data-pipelines`, `posthog:signals-scout-data-warehouse`, `posthog:signals-scout-error-tracking`, `posthog:signals-scout-experiments`, `posthog:signals-scout-feature-flags`, `posthog:signals-scout-general`, `posthog:signals-scout-health-checks`, `posthog:signals-scout-inbox-validation`, `posthog:signals-scout-insight-alerts`, `posthog:signals-scout-logs`, `posthog:signals-scout-mcp-tool-calls`, `posthog:signals-scout-observability-gaps`, `posthog:signals-scout-pr-follow-up`, `posthog:signals-scout-product-analytics`, `posthog:signals-scout-replay-vision`, `posthog:signals-scout-revenue-analytics`, `posthog:signals-scout-session-replay`, `posthog:signals-scout-skills-store`, `posthog:signals-scout-surveys`, `posthog:signals-scout-tasks`, `posthog:signals-scout-web-analytics`, `posthog:signals-scout-web-vitals`, `posthog:signals-scout-workflows`, `posthog:skills-store`, `posthog:suggesting-data-imports`, `posthog:suggesting-path-cleaning-rules`, `posthog:suppressing-noisy-errors`, `posthog:triaging-error-issues`, `posthog:triaging-visual-review-runs`, `posthog:tuning-incremental-sync-config`, `posthog:turning-engineering-analytics-into-insights`, `posthog:understanding-billing-usage`, `posthog:validating-and-publishing-canvases`, `posthog:working-with-scouts`, `posthog:working-with-skills`, `posthog:working-with-task-comments`, `posthog:writing-simplified-technical-english`, `posthog:writing-streamlit-apps`, `/llma-cc-ingest`, `/llma-cc-setup`, `/llma-cc-status`, `error-analyzer`

**훅 2개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionEnd | 전체 | 작업 기록을 PostHog로 보내는 기능. 기본으로 꺼져 있다 | 아니오 |
| PreToolUse | __exec$ | PostHog에 쓰기 작업을 하기 전에 확인을 요청한다 | 아니오 |

**MCP 서버 1개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| posthog | http | `https://mcp.posthog.com/mcp` |

## side-skills

로컬 · 켜짐 · 버전 0.2.0 · 커밋 f79775d

> 자체 제작 스킬 묶음이다. 짧지만 문법이 깨지지 않는 한국어 답변, 한국어 문체 점검, 사실 그대로 쓰는 화면 문구를 맡는다.

**스킬 3개**

| 스킬 | 설명 |
|---|---|
| `side-skills:checking-korean-writing` | 다른 사람이 읽을 한국어 글(README, 문서, 공지, 랜딩 문구, 이슈 기록)을 저장하거나 공개하기 전에 점검하고 다듬는다. 딱딱하거나 끊기거나 번역한 티가 나는 글을 고친다. |
| `side-skills:writing-concise-korean` | 짧게 답하라는 모드(caveman 등)가 켜진 상태에서 한국어로 쓸 때, 조사와 어미가 빠진 명사 나열이 되지 않게 한다. |
| `side-skills:writing-literal-ui-copy` | 제품 화면의 버튼, 메뉴, 기능 이름, 빈 화면 안내, 알림, 오류와 보안 경고를 쓰거나 리뷰할 때, 또는 기능, 화면, 설정의 이름을 제안할 때 쓴다. 비유나 의인화 없이 사실 그대로 쓰게 한다. |

## stripe

로컬 · 꺼짐 · 버전 0.11.17 · 커밋 deae744

사용 중지한 플러그인이라 이름만 적는다. 다시 켤 때 설명을 번역한다.

스킬 10개, 명령 2개, 에이전트 1개: `stripe:connect-recommend`, `stripe:connect-required-verification-information`, `stripe:metronome`, `stripe:stripe-apps`, `stripe:stripe-best-practices`, `stripe:stripe-directory`, `stripe:stripe-docs`, `stripe:stripe-pay`, `stripe:stripe-projects`, `stripe:upgrade-stripe`, `/explain-error`, `/test-cards`, `Company Researcher`

**훅 7개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionStart | startup | Stripe 작업 안내를 넣는다 | 예 |
| PostToolUse | Skill | Stripe 스킬과 에이전트 사용을 로컬에 기록한다 | 아니오 |
| PostToolUse | Agent | Stripe 스킬과 에이전트 사용을 로컬에 기록한다 | 아니오 |
| PostToolUseFailure | Skill | 실패한 Stripe 작업을 로컬에 기록한다 | 아니오 |
| PostToolUseFailure | ^mcp__(?:plugin_stripe_stripe¦stripe)__.*$ | 실패한 Stripe 작업을 로컬에 기록한다 | 아니오 |
| PostToolBatch | 전체 | 작업 묶음이 끝나면 로컬 기록을 정리한다 | 아니오 |
| UserPromptSubmit | 전체 | 메시지에 맞는 Stripe 안내를 넣는다 | 예 |

**MCP 서버 1개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| stripe | http | `https://mcp.stripe.com` |

## supabase

로컬 · 켜짐 · 버전 0.1.16 · 커밋 2c6d02d

> Supabase 공식 플러그인이다. 프로젝트 관리, DB, 인증, 파일 저장소 작업과 Postgres 모범 사례 스킬, MCP 연결을 담고 있다.

**스킬 2개**

| 스킬 | 설명 |
|---|---|
| `supabase:supabase` | Supabase와 관련된 모든 작업에 쓴다. |
| `supabase:supabase-postgres-best-practices` | Supabase가 관리하는 Postgres 모범 사례다. 어디서 돌리는 Postgres에든 쓸 수 있다. |

**MCP 서버 1개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| supabase | http | `https://mcp.supabase.com/mcp` |

## taste-skill

로컬 · 켜짐 · 버전 2.1.5 · 커밋 12af471

> 코딩 에이전트를 위한 디자인 방향 스킬이다. 웹사이트, 제품 페이지, 대시보드, 앱 화면을 실제 브라우저로 확인한다.

**스킬 1개**

| 스킬 | 설명 |
|---|---|
| `taste-skill:design-taste-frontend` | AI가 만든 티가 나지 않는 프론트엔드 디자인 스킬이다. 갤러리 사이트를 연구한 디자인 방향을 고르고, 화면을 보면서 고친다. |

## ui-ux-pro-max

로컬 · 켜짐 · 버전 2.15.0 · 커밋 28b3b8d

> UI/UX 디자인 지식을 담은 플러그인이다.

**스킬 7개**

| 스킬 | 설명 |
|---|---|
| `ui-ux-pro-max:banner-design` | SNS, 광고, 웹사이트 첫 화면, 인쇄용 배너를 디자인한다. |
| `ui-ux-pro-max:brand` | 브랜드 목소리, 시각 정체성, 메시지 체계, 에셋 관리, 브랜드 일관성을 다룬다. |
| `ui-ux-pro-max:design` | 브랜드 정체성, 디자인 토큰, UI 스타일, 로고, 기업 이미지 자료 등 디자인 전반을 다룬다. |
| `ui-ux-pro-max:design-system` | 디자인 토큰 구조, 컴포넌트 규격, 슬라이드를 만든다. |
| `ui-ux-pro-max:slides` | Chart.js와 디자인 토큰으로 반응형 HTML 발표 자료를 만든다. |
| `ui-ux-pro-max:ui-styling` | shadcn/ui와 Tailwind로 보기 좋고 접근성을 갖춘 화면을 만든다. |
| `ui-ux-pro-max:ui-ux-pro-max` | 웹, 모바일, 데스크톱 화면의 UI/UX를 설계한다. |

## frontend-design

claude.ai · 켜짐 · 버전 -

> UI/UX 구현을 위한 프론트엔드 디자인 스킬이다.

**스킬 1개**

| 스킬 | 설명 |
|---|---|
| `frontend-design:frontend-design` | 새 UI를 만들거나 기존 화면을 바꿀 때 뚜렷하고 의도가 있는 디자인을 하도록 안내한다. |

## engineering

claude.ai · 켜짐 · 버전 1.2.0

> 스탠드업, 코드 리뷰, 설계 결정, 장애 대응, 기술 문서 같은 개발 업무를 돕는다.

**스킬 10개**

| 스킬 | 설명 |
|---|---|
| `engineering:architecture` | 설계 결정 기록(ADR)을 만들거나 평가한다. |
| `engineering:code-review` | 코드 변경의 보안, 성능, 정확성을 리뷰한다. |
| `engineering:debug` | 재현, 범위 좁히기, 진단, 수정 순서로 디버깅한다. |
| `engineering:deploy-checklist` | 배포 전 점검표를 만든다. |
| `engineering:documentation` | 기술 문서를 쓰고 관리한다. |
| `engineering:incident-response` | 장애를 분류하고, 상황을 공유하고, 회고를 쓴다. |
| `engineering:standup` | 최근 작업으로 스탠드업 보고를 만든다. |
| `engineering:system-design` | 시스템, 서비스, 아키텍처를 설계한다. |
| `engineering:tech-debt` | 기술 부채를 찾아 분류하고 우선순위를 정한다. |
| `engineering:testing-strategy` | 테스트 전략과 테스트 계획을 세운다. |

**MCP 서버 10개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| slack | http | `https://mcp.slack.com/mcp` |
| linear | http | `https://mcp.linear.app/mcp` |
| asana | http | `https://mcp.asana.com/v2/mcp` |
| atlassian | http | `https://mcp.atlassian.com/v1/mcp` |
| notion | http | `https://mcp.notion.com/mcp` |
| github | http | `https://api.githubcopilot.com/mcp/` |
| pagerduty | http | `https://mcp.pagerduty.com/mcp` |
| datadog | http | `https://mcp.datadoghq.com/api/unstable/mcp-server/mcp` |
| google calendar | http | `-` |
| gmail | http | `-` |

## gtm-planner

claude.ai · 켜짐 · 버전 0.3.3

> 포지셔닝, 수요 계획, 90일 로드맵까지 다섯 단계의 결정을 거쳐 시장 진입 계획을 세운다. 모르는 숫자는 지어내지 않고 질문으로 남긴다.

**스킬 7개**

| 스킬 | 설명 |
|---|---|
| `gtm-planner:demand-plan` | 수요를 만드는 방법과 투자할 홍보 채널을 계획한다. |
| `gtm-planner:intake` | 시장 진입 계획을 시작하며 사업 현황을 정리한다. |
| `gtm-planner:market-map` | 시장과 경쟁사를 조사해 지도처럼 정리하고, 포지셔닝 빈틈을 찾는다. |
| `gtm-planner:plan` | 시장 진입 계획의 다섯 단계를 처음부터 끝까지 진행한다. |
| `gtm-planner:positioning` | 포지셔닝, 카테고리, 핵심 약속, 메시지를 정한다. |
| `gtm-planner:roadmap` | 계획을 실행 과제로 바꾸고, 앞으로 90일 동안 할 일의 우선순위를 정한다. |
| `gtm-planner:setup` | 플러그인을 설치한 직후 필요한 연결을 설정한다. |

**에이전트 4개**

| 에이전트 | 설명 |
|---|---|
| `benchmark-researcher` | 수요 계획 단계에서 업종과 채널별 기준 수치(리드 단가, 전환율 등)를 출처와 함께 조사한다. |
| `market-researcher` | 시장 지도 단계에서 경쟁사와 카테고리 흐름을 공개 웹에서 조사한다. |
| `materials-analyst` | 시작 단계에서 회사 웹사이트, 자료, 문서, 영업 데이터 같은 사용자 자료를 분석한다. |
| `plan-qa` | 로드맵 단계에서 최종 계획을 묶기 전에 다섯 단계의 결과가 서로 맞는지 읽기만 하며 점검한다. |

**MCP 서버 4개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| hubspot | http | `https://mcp.hubspot.com` |
| notion | http | `https://mcp.notion.com/mcp` |
| similarweb | http | `https://mcp.similarweb.com` |
| ahrefs | http | `https://api.ahrefs.com/mcp/mcp` |

## aws-startup-advisor

claude.ai · 켜짐 · 버전 2.0.1

> 35만 개 이상 스타트업의 사례를 바탕으로, 계정 설정부터 운영 인프라까지 AWS 구성, 비용, 보안, 이전을 조언한다.

**스킬 9개**

| 스킬 | 설명 |
|---|---|
| `aws-startup-advisor:agent-advisor` | AWS에서 AI 에이전트를 운영할 환경을 고르고, 이전 계획을 세우고, 시험용 POC를 만든다. |
| `aws-startup-advisor:architect-for-startups` | 회사 단계, 팀 규모, 남은 자금, 크레딧에 맞춰 AWS 아키텍처를 조언한다. |
| `aws-startup-advisor:gcp-to-aws` | Google Cloud의 워크로드를 AI 작업까지 포함해 AWS로 옮긴다. |
| `aws-startup-advisor:heroku-to-aws` | Heroku의 워크로드를 AWS로 옮긴다. |
| `aws-startup-advisor:knowledge-base-for-startups` | AWS Activate FAQ, 크레딧 안내, 지원 프로그램, 예시 아키텍처, 학습 자료를 찾아 준다. |
| `aws-startup-advisor:llm-to-bedrock` | OpenAI, Gemini, Anthropic API를 호출하는 코드를 Amazon Bedrock으로 바꾼다. |
| `aws-startup-advisor:prompt-library-for-startups` | AWS가 고른 AI 코딩 에이전트용 프롬프트(MVP 뼈대, RAG 챗봇, 보안 점검 등)를 제공한다. |
| `aws-startup-advisor:start-building-for-startups` | 선택형 질문으로 요구사항을 모으고 코드를 살펴본 뒤, 프로젝트에 AWS 구성과 구현을 직접 넣는다. |
| `aws-startup-advisor:tf-best-practices` | 이전 작업에서 만든 AWS Terraform의 작성 기준을 안내하고, 읽기 전용으로 정책 검사를 한다. |

**에이전트 6개**

| 에이전트 | 설명 |
|---|---|
| `generic-phase-worker-rw` | 이전 작업의 한 단계를 독립된 환경에서 실행하고 결과 파일을 쓰는 범용 에이전트다. |
| `llm2bedrock-code-analyzer` | 저장소에서 AI 프레임워크와 LLM SDK 호출 위치, 프롬프트, 사용자에게 보이는 동작 차이를 찾는다. |
| `llm2bedrock-code-rewriter` | 별도 브랜치에서 LLM SDK 호출을 Bedrock으로 바꾸고, 의존성과 테스트를 갖춘다. |
| `llm2bedrock-log-ingestor` | LLM API 로그에서 프롬프트와 응답 쌍을 뽑아 평가용 데이터셋을 만든다. |
| `llm2bedrock-prompt-evaluator` | 평가용 프롬프트를 Bedrock 모델에 실행하고, LLM 채점으로 통과율을 보고한다. |
| `llm2bedrock-report-generator` | 앞 단계 결과를 모아 모델 대응, 평가 점수, 코드 변경, 비용 비교를 담은 이전 보고서를 쓴다. |

**훅 1개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionStart | * | "스타트업 관점" 지시를 넣도록 돼 있지만, 읽을 파일이 없어 지금은 작동하지 않는다 | 예 |

**MCP 서버 4개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| awsknowledge | http | `https://knowledge-mcp.global.api.aws` |
| awspricing | stdio | `uvx awslabs.aws-pricing-mcp-server@latest` |
| temporal-docs | http | `https://temporal.mcp.kapa.ai` |
| aws-pricing-calculator | stdio | `npx -y sample-aws-pricing-calculator-mcp@1.2.8` |

## superpowers

claude.ai · 켜짐 · 버전 6.4.2

> Claude Code의 핵심 스킬 모음이다. TDD, 디버깅, 협업 방식 같은 검증된 기법을 담고 있다.

**스킬 15개**

| 스킬 | 설명 |
|---|---|
| `superpowers:brainstorming` | 기능을 만들거나 동작을 바꾸는 창작 작업 전에 반드시 쓴다. 의도와 요구사항, 설계를 먼저 정리한다. |
| `superpowers:diagnosing-superpowers` | superpowers로 진행한 세션이 반복, 계획 무시, 나쁜 결과 등으로 잘못 흘러갔을 때 원인을 진단한다. |
| `superpowers:dispatching-parallel-agents` | 서로 상관없는 작업이 둘 이상일 때 에이전트에게 나눠 동시에 처리한다. |
| `superpowers:executing-plans` | 구현 계획을 지금 세션에서 직접 실행할 때 쓴다. |
| `superpowers:finishing-a-development-branch` | 구현을 마치고 테스트가 통과한 뒤, 작업을 어떻게 합칠지 정한다. |
| `superpowers:receiving-code-review` | 받은 리뷰를 반영하기 전에, 특히 내용이 불분명하거나 기술적으로 의심스러울 때 먼저 검증한다. |
| `superpowers:requesting-code-review` | 작업을 마쳤거나 큰 기능을 구현했거나 머지하기 전에 리뷰를 요청한다. |
| `superpowers:subagent-driven-development` | 독립된 작업이 있는 구현 계획을 서브에이전트에게 나눠 실행한다. |
| `superpowers:systematic-debugging` | 버그, 테스트 실패, 예상과 다른 동작이 생기면 고치기 전에 원인부터 찾는다. |
| `superpowers:test-driven-development` | 기능이나 버그 수정을 구현하기 전에 테스트를 먼저 쓴다. |
| `superpowers:using-git-worktrees` | 작업 공간을 분리해야 하는 기능 작업이나 계획 실행 전에 별도 작업 폴더를 만든다. |
| `superpowers:using-superpowers` | 대화를 시작할 때 스킬을 찾고 쓰는 방법을 정한다. 어떤 답변보다 먼저 스킬을 부르게 한다. |
| `superpowers:verification-before-completion` | 작업이 끝났다거나 고쳐졌다고 말하기 전에, 검증 명령을 실제로 돌려 결과를 확인한다. |
| `superpowers:writing-plans` | 여러 단계가 필요한 작업의 명세나 요구사항이 있으면, 코드를 건드리기 전에 계획을 쓴다. |
| `superpowers:writing-skills` | 스킬을 새로 만들거나 고치거나, 배포 전에 제대로 작동하는지 확인한다. |

**훅 1개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionStart | startup¦clear¦compact | "스킬이 조금이라도 맞으면 반드시 불러라"는 지시(using-superpowers 스킬 전문)를 넣는다 | 예 |

## review-council

claude.ai · 켜짐 · 버전 0.2.4

> 정확성, 보안, 정책, 테스트 근거, 구조, 인터페이스를 맡은 여섯 전문가로 작업 중인 코드나 PR을 리뷰한다.

**스킬 1개**

| 스킬 | 설명 |
|---|---|
| `review-council:review-council` | 머지하기 전에 작업 중인 코드, 변경, GitHub PR을 여러 관점에서 꼼꼼히 리뷰한다. 여섯 리뷰 에이전트를 따로 실행한다. |

**에이전트 6개**

| 에이전트 | 설명 |
|---|---|
| `architecture-reviewer` | 결합도, 계층 위반, 중복 로직, 추상화 누수 같은 구조 문제를 리뷰한다. |
| `correctness-reviewer` | 로직 오류, 경계 조건 버그, 잘못된 흐름을 리뷰한다. |
| `interface-reviewer` | CLI 옵션, API, 출력 형식, 스키마, 오류 메시지처럼 밖으로 드러나는 부분의 변경을 리뷰한다. |
| `policy-boundary-reviewer` | 저장소의 정책 문서(CLAUDE.md, AGENTS.md 등)와 맞는지, 리뷰어를 속이려는 내용이 없는지 확인한다. |
| `security-reviewer` | 인젝션, 인증과 권한 빈틈, 인증 정보 노출 같은 보안 취약점을 리뷰한다. |
| `test-evidence-reviewer` | 동작 변경에 맞는 테스트가 있는지, 통과했다는 주장에 실제 실행 근거가 있는지 확인한다. |

**훅 1개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| PreToolUse | Agent | 저장소의 지침 파일이 기본 브랜치와 다르면 리뷰 에이전트 실행을 막는다 | 아니오 |

## writing-quality

claude.ai · 켜짐 · 버전 0.2.3

> 의도에 맞춰 쓰고, 고치고, 검토만 하고, 주장의 근거를 가르고, 최종 문장을 검증한다. (영어 글 기준)

**스킬 4개**

| 스킬 | 설명 |
|---|---|
| `writing-quality:business-writing-intent-enforcer` | 메모, 명세, PRD, 운영 문서, 요약, 제안서, 프로젝트 계획처럼 독자의 의도와 결정이 중요한 비즈니스 문서에 쓴다. |
| `writing-quality:claim-boundary-checker` | 글에서 근거 있는 주장, 근거 없는 주장, 불확실한 주장, 사실이 아닌 말을 가른다. |
| `writing-quality:writing-enforcer` | 영어 글에서 AI 문체 패턴 47가지를 찾아 고친다. 원래 목소리와 보호할 내용은 그대로 둔다. |
| `writing-quality:writing-quality-router` | 글쓰기 요청을 의도 정리, 고쳐 쓰기, 검토만 하기, 검증 중 맞는 곳으로 보낸다. |

## context7

claude.ai · 켜짐 · 버전 -

> 라이브러리의 최신 문서를 찾아 주는 Upstash Context7 MCP 서버다.

**MCP 서버 1개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| context7 | http | `https://mcp.context7.com/mcp?client=claude-code-plugin` |

## product-management

claude.ai · 켜짐 · 버전 1.2.0

> 기능 명세, 로드맵, 사용자 조사 정리를 빠르게 한다.

**스킬 8개**

| 스킬 | 설명 |
|---|---|
| `product-management:competitive-brief` | 경쟁사 하나 이상이나 특정 기능 영역의 경쟁 분석 보고서를 만든다. |
| `product-management:metrics-review` | 제품 지표를 추세와 함께 분석하고 실행할 수 있는 시사점을 낸다. |
| `product-management:product-brainstorming` | 제품 아이디어를 떠올리고, 문제 영역을 탐색하고, 가정을 따져 보는 대화 상대가 된다. |
| `product-management:roadmap-update` | 제품 로드맵을 만들거나 고치거나 우선순위를 다시 정한다. |
| `product-management:sprint-planning` | 스프린트 범위와 용량을 정하고 목표와 계획 초안을 만든다. |
| `product-management:stakeholder-update` | 받는 사람과 주기에 맞춘 진행 보고를 만든다. |
| `product-management:synthesize-research` | 인터뷰, 설문, 피드백 같은 사용자 조사를 구조화된 인사이트로 정리한다. |
| `product-management:write-spec` | 문제 정의나 기능 아이디어로 기능 명세나 PRD를 쓴다. |

**명령 1개**

| 명령 | 설명 |
|---|---|
| `/brainstorm` | 제품 아이디어, 문제 영역, 전략 질문을 날카로운 대화 상대와 함께 브레인스토밍한다. |

**MCP 서버 16개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| slack | http | `https://mcp.slack.com/mcp` |
| linear | http | `https://mcp.linear.app/mcp` |
| asana | http | `https://mcp.asana.com/v2/mcp` |
| monday | http | `https://mcp.monday.com/mcp` |
| clickup | http | `https://mcp.clickup.com/mcp` |
| atlassian | http | `https://mcp.atlassian.com/v1/mcp` |
| notion | http | `https://mcp.notion.com/mcp` |
| figma | http | `https://mcp.figma.com/mcp` |
| amplitude | http | `https://mcp.amplitude.com/mcp` |
| amplitude-eu | http | `https://mcp.eu.amplitude.com/mcp` |
| pendo | http | `https://app.pendo.io/mcp/v0/shttp` |
| intercom | http | `https://mcp.intercom.com/mcp` |
| fireflies | http | `https://api.fireflies.ai/mcp` |
| google calendar | http | `-` |
| gmail | http | `-` |
| similarweb | http | `https://mcp.similarweb.com/mcp` |
