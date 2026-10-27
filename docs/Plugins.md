---
type: plugins-catalog
status: proposed
owner: Founder
last_reviewed: 2026-10-27
---

# Plugins

설치한 플러그인을 정리한다. 각각 무엇을 하는지, 왜 설치했는지, 지금 어떤 상태인지 적는다. 작업별로 무엇을 먼저 쓰는지는 [Plugin Playbook](Plugin%20Playbook.md)에, 프로젝트에서 써 본 결과는 `Plugin Reports/`에 둔다. 외부 서비스 연결(Stripe, Vercel 등)은 Integrations (운영 허브 문서)에 둔다.

**플러그인에 들어 있는 것**

플러그인 하나에 아래 구성 요소가 함께 들어 있을 수 있다. 검토할 때는 스킬만 보지 않고 모두 본다. 훅은 부르지 않아도 실행되고, MCP는 외부와 통신하기 때문이다.

| 구성 요소 | 하는 일 |
|---|---|
| 스킬 | 상황에 맞으면 Claude가 불러 쓰는 지시서 |
| 명령 | 사람이 `/이름`으로 직접 부르는 기능 |
| 에이전트 | 특정 일을 맡는 별도 Claude |
| 훅 | 세션 시작, 메시지 입력, 파일 수정 후 같은 시점마다 자동으로 실행되는 명령. 대화에 지시를 끼워 넣을 수 있다 |
| MCP 서버 | 외부 서비스나 로컬 프로그램에 연결하는 도구 |
| 출력 스타일 | 답변 방식 전체를 바꾸는 지시 |

플러그인마다 실제로 무엇이 들어 있는지는 `python3 scripts/plugin-audit.py inventory`로 뽑는다. 손으로 적은 표와 실제 설치 상태가 어긋나지 않게, 구성 요소 수와 훅, MCP 목록은 이 명령의 결과를 기준으로 한다. 새 플러그인을 검토하는 순서는 [Plugin Review](Plugin%20Review.md)에 있다.

**상태**는 다섯 가지다.

| 상태 | 뜻 |
|---|---|
| 시험 사용 | 설치해서 써 보는 중이다. 리포트가 쌓이면 채택할지 정한다 |
| 채택 | 계속 쓰기로 했다 |
| 보류 | 설치는 했지만 지금은 쓰지 않는다 |
| 사용 중지 | 설치는 그대로 두고 꺼 두었다. 필요할 때 다시 켠다 |
| 제외 | 검토한 뒤 쓰지 않기로 했다 |

상태를 바꿀 때마다 [Plugin Changelog](Plugin%20Changelog.md)에 한 줄 남긴다.

**설치 경로**는 두 가지다. **claude.ai**는 claude.ai 계정에서 켠 플러그인이고, **로컬**은 `claude plugin install`로 설치한 플러그인이다. 로컬 플러그인은 따로 적지 않으면 모든 프로젝트에 적용된다.

## 1. 개발 절차

| 플러그인 | 설치 경로 | 하는 일 | 설치 이유 | 상태 |
|---|---|---|---|---|
| **superpowers** | claude.ai | 브레인스토밍, 계획, TDD, 디버깅, 검증, 브랜치 마무리까지 개발 절차를 이끈다. 스킬 15개 | 가장 많이 추천되는 개발 절차다. 범위와 완료 기준을 먼저 잡게 한다 | 채택 |
| **engineering** | claude.ai (Anthropic) | 설계 기록(ADR), 시스템 설계, 코드 리뷰, 디버깅, 테스트 전략, 배포 체크리스트, 장애 대응, 문서 작성을 돕는다 | 배포 전에 점검하고 설계를 기록하려고 | 채택 |
| **review-council** | claude.ai | 정확성, 보안, 정책, 테스트 근거, 구조, 인터페이스 여섯 관점으로 리뷰하는 에이전트 | 큰 변경을 머지하기 전에 여러 관점에서 검토하려고 | 시험 사용 |
| **ponytail** 5.3.2 | 로컬 | 가장 작은 변경으로 끝내도록 이끄는 "게으른 시니어" 모드. 기본 단계는 lite | 과설계를 막고 빨리 출시하려고 | 시험 사용 |
| **caveman** 4.0.1 | 로컬 | 답변을 짧게 줄인다. 서브에이전트(cavecrew)와 작업 유형별 스킬(lean-build, surgical-patch 등)이 들어 있다 | 토큰을 아끼려고 | 시험 사용 |

## 2. 기획·전략

| 플러그인 | 설치 경로 | 하는 일 | 설치 이유 | 상태 |
|---|---|---|---|---|
| **product-management** | claude.ai (Anthropic) | 브레인스토밍, 경쟁 분석, 명세(PRD) 작성, 리서치 정리, 로드맵, 지표 검토를 돕는다 | 아이디어를 검증하고 명세를 쓰려고 | 채택 |
| **gtm-planner** | claude.ai | 시장 지도, 포지셔닝, 수요 계획, 90일 로드맵 순서로 시장 진입 전략을 세운다 | "누구에게 무엇을 어떻게 팔까"를 정하려고 | 시험 사용 |
| **aws-startup-advisor** | claude.ai | AWS 구성과 비용, Activate 크레딧, 마이그레이션을 조언한다 | AWS를 쓰게 될 경우에 대비해 두었다. "스타트업 관점" 지시를 넣는 훅이 있지만, 지금 설치본에서는 읽을 파일이 없어 작동하지 않는다 | 시험 사용 |

## 3. 디자인·프론트엔드

| 플러그인 | 설치 경로 | 하는 일 | 설치 이유 | 상태 |
|---|---|---|---|---|
| **frontend-design** | claude.ai (Anthropic) | 뻔한 템플릿 느낌이 나지 않는 UI 방향을 잡는다 | Anthropic이 만든 기본 디자인 스킬이라서 | 채택 |
| **ui-ux-pro-max** 2.15.0 | 로컬 | 스타일 79개, 팔레트 192개, 폰트 조합 74개를 로컬 데이터로 갖고 있다. 디자인 시스템, 배너, 브랜드, 슬라이드 스킬이 들어 있다 | 처음 디자인 시스템을 잡을 때 쓰려고 | 시험 사용 |
| **taste-skill** 2.1.5 | 로컬 | 랜딩 페이지와 제품 페이지의 디자인 방향을 정하고, 실제 브라우저로 보면서 고친다 | AI가 만든 티가 나는 페이지를 피하려고 | 시험 사용 |
| **impeccable** 4.7.1 | 로컬 | 명령 24개(polish, audit, critique 등)와 에이전트 4개로 UI를 점검하고 다듬는다. 파일을 고칠 때마다 훅이 실행된다 | UI를 다듬고 점검하려고 | 시험 사용 (무거운 편) |

## 4. 마케팅·글

| 플러그인 | 설치 경로 | 하는 일 | 설치 이유 | 상태 |
|---|---|---|---|---|
| **marketing-skills** 2.13.4 | 로컬 | 홍보 실행 스킬 52개. 가격, 결제 화면, 가입 흐름, 전환율 개선(CRO), 카피, 런칭, 디렉터리 등록, AI 검색 최적화, 콜드 메일 등을 다룬다 | 1인 SaaS 홍보를 실제로 해 보려고 | 시험 사용 |
| **writing-quality** | claude.ai | AI 문체를 걷어 내고, 비즈니스 문서를 다듬고, 근거 없는 주장을 찾는다. **영어 기준**이라 한국어 글은 검사하지 못한다 | 영어 문구를 점검하려고 | 시험 사용 (영어 전용) |
| **fluent-korean** 1.0.0 | 로컬 | 출력 스타일이다. 조사와 어미를 빠뜨리거나 명사를 이어 붙이지 않게 해서 처음부터 명확한 한국어로 쓰게 한다 | 한국어 문서가 어색하게 나오는 문제를 근본부터 막으려고 | 시험 사용. **허브와 제품 저장소에서만 켠다** (허브 `.claude/settings.json`에서 출력 스타일로 지정) |
| **humanize-korean** 2.3.2 (im-not-ai) | 로컬 | AI가 쓴 한국어의 번역투와 기계적인 문체를 찾아 다듬는다. 패턴 85개, 스킬 4개, 에이전트 9개 | 긴 한국어 글을 공개하기 전에 깊게 다듬으려고 | 시험 사용. **허브와 제품 저장소에서만 켠다** |

## 5. 문서·도구

| 플러그인/스킬 | 설치 경로 | 하는 일 | 설치 이유 | 상태 |
|---|---|---|---|---|
| **context7** | claude.ai | 라이브러리의 최신 문서를 찾아 준다(MCP) | 오래된 API로 코딩하는 실수를 막으려고 | 보류 (로그인 전) |
| **anthropic-skills** | 기본 제공 | docx, pdf, pptx, xlsx 파일 작업, 심층 조사(deep-research), 스킬 만들기(skill-creator) 등 | 문서 파일을 다루고, 조사하고, 스킬을 만들려고 | 채택 |
| 기본 명령 | 기본 제공 | `/simplify`, `/code-review`, `/security-review`, `run`, `schedule`, `loop` | 코드를 정리하고 리뷰하고, 실행해서 확인하려고 | 채택 |

## 6. 외부 서비스 (공식 마켓플레이스에서 로컬 설치, 2026-10-27)

Anthropic 공식 마켓플레이스(`anthropics/claude-plugins-official`, `anthropics/knowledge-work-plugins`)에서 설치했다. 공식 마켓플레이스는 플러그인마다 검토된 커밋을 고정해 둔다. 각 서비스 계정 로그인은 아직 하지 않았다. 연결 규칙은 Integrations (운영 허브 문서)에 있다.

| 플러그인 | 하는 일 | 설치 이유 | 검토 메모 | 상태 |
|---|---|---|---|---|
| **stripe** 0.11.17 | 결제 구현 스킬 10개, `/test-cards`, `/explain-error`, Stripe MCP | 해외 결제를 받으려면 꼭 필요해서 | 훅이 5개 있지만 모두 로컬 Node로 실행되고 외부로 보내는 데이터가 없다. Stripe CLI 사용 통계 전송도 끈 채로 실행한다 | 사용 중지 (결제를 붙일 때 다시 켠다) |
| **supabase** 0.1.16 | DB, 인증, 파일 저장소를 다루는 스킬과 MCP | 1인 SaaS 백엔드 후보라서 | 공식 플러그인(supabase-community) | 시험 사용 (로그인 전) |
| **cloudflare** 1.0.0 | Workers와 Pages 배포, Next.js on Cloudflare, 성능 점검 | 배포 방식 후보라서 | 공식 플러그인(cloudflare/skills) | 사용 중지 (배포 방식을 정할 때 다시 켠다) |
| **posthog** 1.1.67 | 분석, 실험, 기능 플래그, 오류 추적 스킬과 MCP | 출시 후 지표를 보려고 | 훅이 2개다. 하나는 쓰기 작업 전에 확인을 요청하는 안전장치다. 다른 하나는 세션이 끝날 때 작업 기록을 PostHog로 보내는 기능인데 **기본으로 꺼져 있고** 켜지 않는다(`POSTHOG_LLMA_CC_ENABLED`와 키가 있어야 작동) | 사용 중지 (출시 후 다시 켠다) |
| **playwright** | 브라우저 자동화와 E2E 테스트 MCP (Microsoft) | 결제와 가입 흐름을 실제 브라우저로 시험하려고 | 공식 플러그인 | 시험 사용 |
| **marketing** 1.2.0 | 콘텐츠, 캠페인, 브랜드 목소리, 성과 보고 (Anthropic) | 창업자 요청으로 설치했다. marketing-skills와 비교한다 | 공식 플러그인. MCP 서버 13개(Slack, Notion, HubSpot, Canva 등)를 함께 연결한다. 다른 플러그인과 겹치는 연결은 Integrations (운영 허브 문서)에 정리했다 | 시험 사용 (marketing-skills와 비교 중) |

## 7. 자체 제작 플러그인 (side-toolkit)

직접 만든 스킬은 공개 저장소 `products/side-toolkit`의 `plugins/side-skills/skills/`에 둔다. 플러그인 이름은 `side-skills`, 마켓플레이스 이름은 `side-toolkit`이다. 로컬 폴더를 마켓플레이스로 등록해 설치했으므로, 스킬을 고친 뒤에는 버전을 올리고 `claude plugin update side-skills@side-toolkit`을 실행해야 반영된다.

| 스킬 | 하는 일 | 만든 이유 | 검증 | 상태 |
|---|---|---|---|---|
| **writing-concise-korean** | 한국어판 caveman이다. 내용은 줄이되 조사와 어미는 지켜서, 짧게 써도 문장이 깨지지 않게 한다 | caveman을 쓰면서도 한국어 답변이 명사 나열로 깨지지 않게 하려고 | 스킬이 있을 때와 없을 때를 비교하는 시험은 아직 하지 못했다 | 시험 사용 (모든 프로젝트) |
| **checking-korean-writing** | 한국어판 writing-quality다. 명사 나열, 명사로 끝나는 문장, 빗금, 영어 직역, 번역투를 찾아 알려 주고(DETECT), 요청하면 고친다(REWRITE). 스캐너 `scan_korean.py`가 들어 있다 | writing-enforcer가 한국어를 검사하지 못해서 | 이 허브에서 손으로 고쳤던 문서의 수정 전 버전으로 시험했다. 알려진 어색한 표현을 조사 오류 1건만 빼고 모두 찾았다 | 시험 사용 (모든 프로젝트) |

## 폴더별로 켜지는 플러그인

`python3 scripts/plugin-audit.py scope --projects ~/SideProjects/hub ~`로 뽑은 결과를 요약했다. 제품 저장소를 만들면 그 폴더도 추가한다.

| 플러그인 | 허브 | 그 밖의 폴더 |
|---|---|---|
| fluent-korean, humanize-korean | 켜짐 (출력 스타일 fluent-korean) | 꺼짐 |
| posthog, cloudflare, stripe | 꺼짐 | 꺼짐 |
| 나머지 19개 | 켜짐 | 켜짐 |

제품 저장소에서는 한국어 문체 플러그인 2개를 프로젝트 범위로 켜고, 결제·배포·분석 플러그인은 필요해지면 그 저장소에서만 켠다.

## 여러 플러그인이 함께 연결하는 MCP 서버

`plugin-audit.py conflicts`의 5번 결과다. claude.ai 플러그인 4개(engineering, product-management, marketing, gtm-planner)가 같은 서비스를 각자 연결한다. 지금은 모두 로그인하지 않아 실제로 쓰이지는 않는다. 한 서비스를 실제로 쓰게 되면 하나의 플러그인에서만 로그인한다(DEC-001 외부 서비스 연결은 플러그인 우선 (운영 허브 문서)).

| 서비스 | 연결하는 플러그인 |
|---|---|
| Notion | engineering, gtm-planner, marketing, product-management |
| Slack, Gmail, Google Calendar | engineering, marketing, product-management |
| Similarweb | gtm-planner, marketing, product-management |
| Ahrefs, HubSpot | gtm-planner, marketing |
| Amplitude, Figma | marketing, product-management |
| Asana, Atlassian, Linear | engineering, product-management |

## 기능이 겹치는 플러그인 (2026-10-27)

같은 일을 하는 플러그인이 여러 개 있다. 영역마다 **기본으로 쓸 플러그인**을 하나 정하고, 나머지는 리포트로 비교한 뒤 남기거나 끈다. 작업별 순서는 [Plugin Playbook](Plugin%20Playbook.md)에 있다.

| 영역 | 기본으로 쓸 것 | 겹치는 것 | 비교할 점 |
|---|---|---|---|
| 개발 절차 | superpowers | ponytail, caveman의 작업 스킬(lean-build, surgical-patch 등) | ponytail lite가 계획이나 TDD를 방해하는가 |
| 과설계 방지 | ponytail (lite) | caveman `lean-build` | 둘 중 하나만 남긴다 |
| 코드 리뷰 | `/code-review` | review-council, caveman-review, engineering `code-review` | 큰 변경에서 review-council이 문제를 더 찾는가 |
| 코드 정리 | `/simplify` | ponytail-review | — |
| 랜딩·마케팅 페이지 디자인 | taste-skill | frontend-design, impeccable, ui-ux-pro-max | 첫 랜딩 페이지에서 결과를 비교한다 |
| 제품 UI 디자인 | ui-ux-pro-max | frontend-design, impeccable | — |
| UI 점검·다듬기 | impeccable | ui-ux-pro-max | 훅 때문에 느려지는 만큼 효과가 있는가 |
| 시장 전략 | gtm-planner | product-management, marketing(Anthropic) `campaign-plan` | — |
| 마케팅 실행 | marketing-skills | marketing(Anthropic) | 하나만 남긴다 |
| 경쟁 분석 | product-management `competitive-brief` | marketing(Anthropic) `competitive-brief`, marketing-skills `competitor-profiling` | — |
| SEO | marketing-skills `seo-audit`, `ai-seo` | marketing(Anthropic) `seo-audit` | 보류 중인 claude-seo가 필요한가 |
| 한국어 글 | fluent-korean(쓸 때, 허브와 제품만) + checking-korean-writing(공개 전) | humanize-korean(긴 글을 깊게 다듬을 때) | caveman은 writing-concise-korean으로 보완한다 |
| 영어 글 다듬기 | writing-quality | marketing-skills `copy-editing` | 랜딩 문구는 copy-editing, 그 밖의 영어 글은 writing-quality로 다듬는다 |
| 브라우저 테스트 | playwright | 앱 내장 브라우저, taste-skill 검사기 | — |

### 부담이 큰 플러그인

2026-10-27 창업자 결정: posthog, cloudflare, stripe는 필요할 때까지 사용을 중지한다. 다시 켤 때는 `claude plugin enable <이름>@claude-plugins-official`을 실행한다. 제품 저장소에서만 쓰려면 `--scope project`를 붙인다.

Claude는 세션마다 스킬 설명을 모두 읽는다. 그래서 스킬이 많을수록 토큰을 더 쓰고, 엉뚱한 스킬을 부를 가능성도 커진다.

| 플러그인 | 스킬 수 | 부담 | 처리 |
|---|---|---|---|
| posthog | 약 170 | 매우 크다 | 출시 전까지 사용을 중지하고, 출시 후에는 그 제품 저장소에서만 켠다 |
| marketing-skills | 52 | 크다 | 홍보에 꼭 필요해서 그대로 둔다 |
| cloudflare | 14 | 보통이다 | 배포 방식을 정할 때까지 사용을 중지한다 |
| stripe | 10 + 훅 5 | 보통이다 | 결제를 붙일 때 다시 켠다 |
| impeccable | 훅 3 | 파일을 고칠 때마다 실행된다 | UI 작업이 없는 저장소에서는 끈다 |

## 오픈소스 플러그인 검토 기록

오픈소스 플러그인은 설치하기 전에 설정 파일, 훅, 외부 통신 코드를 읽는다. 설치한 뒤에는 설치된 커밋이 검토한 커밋과 같은지 확인하고, 업데이트하면 다시 검토한다.

| 플러그인 | 저장소 (라이선스) | 검토 커밋 | 검토 메모 |
|---|---|---|---|
| caveman | JuliusBrussee/caveman (Apache-2.0) | 9b68f7e | 훅 4개가 로컬 Node로 실행되고 네트워크를 쓰지 않는다. `~/.claude`와 `~/.config/caveman`에 기록을 남긴다. **Caveman Cloud 스킬(`caveman-setup`, `caveman-compress`)은 외부로 데이터를 보내므로 쓰지 않는다** |
| ui-ux-pro-max | nextlevelbuilder/ui-ux-pro-max-skill (MIT) | 28b3b8d | 훅과 MCP가 없고, 로컬 Python 스크립트만 있다 |
| taste-skill | Leonxlnx/taste-skill (MIT) | 12af471 | 훅이 없다. 스킬을 쓸 때 공개 이미지 모음에서 사진을 받아 온다 |
| impeccable | pbakaus/impeccable (Apache-2.0) | 989c484 | 훅 3개(세션 시작, 파일 수정 후, 답변 종료 시 최대 30초). 처음 실행할 때 GitHub 릴리스에서 엔진 실행 파일을 받아 sha256으로 검증한다 |
| marketing-skills | coreyhaines31/marketingskills (MIT) | f90b9d3 | 훅과 MCP 없이 스킬만 있다 |
| fluent-korean | snflkd/fluent-korean (MIT) | ce8683f | 출력 스타일 문서 2개가 전부다. 훅, MCP, 스크립트가 없다 |
| humanize-korean | epoko77-ai/im-not-ai (MIT) | b37e020 | 스킬 4개, 에이전트 9개, 명령 4개. 훅과 MCP가 없고, 플러그인이 실제로 쓰는 부분에는 외부 통신 코드가 없다 |
| ponytail | DietrichGebert/ponytail (MIT) | 09c434a | 훅 3개가 로컬에서만 실행된다. 매 턴 작업 기록을 `~/.config/ponytail/band/`에 CSV로 저장한다. 웹훅은 비워 두었다. 기본 단계는 lite |

## claude.ai 플러그인 검토 메모

claude.ai 디렉터리 플러그인은 코드를 고정할 수 없어서, 훅과 MCP만 확인한다. `plugin-audit.py inventory`로 찾은 내용이다.

| 플러그인 | 훅 | MCP 서버 | 메모 |
|---|---|---|---|
| superpowers 6.4.2 | 세션 시작 1개 | 없음 | 세션마다 "스킬이 조금이라도 맞으면 반드시 불러라"는 지시(using-superpowers 스킬 전문)를 넣는다. 스킬이 많을수록 엉뚱한 스킬이 불릴 가능성이 커진다 |
| aws-startup-advisor 2.0.1 | 세션 시작 1개 | 4개 (AWS 문서, 가격 2개, Temporal 문서) | 훅은 `scripts/startup-context.txt`를 읽어 "스타트업 관점" 지시를 넣도록 돼 있다. 그런데 지금 설치본에는 이 파일이 없어서 실제로는 아무것도 넣지 않는다. 업데이트로 파일이 생기면 다시 확인한다 |
| review-council 0.2.4 | 에이전트 실행 전 1개 | 없음 | 저장소의 CLAUDE.md 같은 지침 파일이 기본 브랜치와 다르면 리뷰 에이전트 실행을 막는다. 안전장치다 |
| engineering 1.2.0 | 없음 | 10개 (Slack, Notion, GitHub, Linear 등) | 다른 플러그인과 겹치는 연결이 많다 |
| product-management 1.2.0 | 없음 | 16개 | 가장 많은 서비스를 연결한다 |
| gtm-planner 0.3.3 | 없음 | 4개 (HubSpot, Notion, Similarweb, Ahrefs) | — |
| context7 | 없음 | 1개 (Context7 문서) | 로그인 전 |
| writing-quality 0.2.3, frontend-design | 없음 | 없음 | 스킬만 있다 |

### 검토 후 제외

| 후보 | 이유 |
|---|---|
| code-simplifier (Anthropic) | `/simplify`와 기능이 겹치고, 에이전트에 특정 코딩 스타일이 고정돼 있다 |
| ECC, alirezarezvani/claude-skills, rampstackco/claude-skills | 스킬이 수백에서 천 개가 넘어 서로 충돌하고 토큰을 낭비한다 |
| phuryn/pm-skills | product-management, gtm-planner와 겹친다 |
| claude-mem | 모든 작업을 기록하고 로컬 서버를 띄운다. "상태는 파일에 둔다"는 허브 규칙과 맞지 않는다 |
| context-mode | 라이선스가 Elastic License 2.0이라 오픈소스가 아니고, 훅이 6개다 |
| ralph-loop / Ralph Wiggum | 사람 없이 스스로 반복 실행하는 루프라 비용과 통제 위험이 크다 |

### 보류

| 후보 | 다시 볼 시점 |
|---|---|
| AgriciDaniel/claude-seo 또는 zubair-trabzada/geo-seo-claude | 랜딩 페이지가 생긴 뒤 제품 저장소에만 설치한다 |
