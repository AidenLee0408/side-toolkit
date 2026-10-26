---
type: skills-catalog
status: proposed
owner: Founder
last_reviewed: 2026-10-27
---

# Skills

설치한 플러그인과 스킬을 정리한다. 각각 무엇을 하는지, 왜 설치했는지, 지금 어떤 상태인지 적는다. 작업별로 무엇을 먼저 쓰는지는 [Skill Playbook](Skill%20Playbook.md)에, 프로젝트에서 써 본 결과는 `Skill Reports/`에 둔다. 외부 서비스 연결(Stripe, Vercel 등)은 Integrations (운영 허브 문서)에 둔다.

상태: 시험 중 / 채택 / 보류 / 꺼 둠 / 제외. 프로젝트 리포트가 쌓이면 상태를 바꾸고, 바꿀 때마다 [Skill Changelog](Skill%20Changelog.md)에 한 줄 남긴다.
설치 경로: **claude.ai** = claude.ai 계정에서 켠 플러그인, **로컬** = `claude plugin install`로 설치한 플러그인(모든 프로젝트에 적용).

## 1. 개발 절차

| 플러그인 | 설치 경로 | 하는 일 | 설치 이유 | 상태 |
|---|---|---|---|---|
| **superpowers** | claude.ai | 브레인스토밍 → 계획 → TDD → 디버깅 → 검증 → 브랜치 마무리 절차. 스킬 15개 | 가장 많이 추천되는 개발 절차. 범위와 완료 기준을 먼저 잡게 한다 | 채택 |
| **engineering** | claude.ai (Anthropic) | 설계(ADR), 시스템 설계, 코드 리뷰, 디버그, 테스트 전략, 배포 체크리스트, 장애 대응, 문서 | 배포 전 점검과 설계 기록용 | 채택 |
| **review-council** | claude.ai | 정확성, 보안, 정책, 테스트 근거, 구조, 인터페이스 여섯 관점으로 리뷰하는 에이전트 | 큰 변경을 머지하기 전에 여러 관점에서 검토 | 시험 중 |
| **ponytail** 5.3.2 | 로컬 | 가장 작은 변경으로 끝내게 하는 "게으른 시니어" 모드. 기본 lite | 과설계를 막고 빨리 출시하려고 | 시험 중 |
| **caveman** 4.0.1 | 로컬 | 답변을 짧게 압축. 서브에이전트(cavecrew), 작업 유형별 스킬(lean-build, surgical-patch 등) 포함 | 토큰 절약 | 시험 중 |

## 2. 기획·전략

| 플러그인 | 설치 경로 | 하는 일 | 설치 이유 | 상태 |
|---|---|---|---|---|
| **product-management** | claude.ai (Anthropic) | 브레인스토밍, 경쟁 분석, 명세(PRD), 리서치 정리, 로드맵, 지표 검토 | 아이디어 검증과 명세 작성 | 채택 |
| **gtm-planner** | claude.ai | 시장 지도 → 포지셔닝 → 수요 계획 → 90일 로드맵 | "누구에게 무엇을 어떻게 팔까" 전략 | 시험 중 |
| **aws-startup-advisor** | claude.ai | AWS 구성·비용 조언, Activate 크레딧, 마이그레이션 | AWS를 쓸 경우 대비. 지금은 거의 안 씀 | 보류 |

## 3. 디자인·프론트엔드

| 플러그인 | 설치 경로 | 하는 일 | 설치 이유 | 상태 |
|---|---|---|---|---|
| **frontend-design** | claude.ai (Anthropic) | 뻔한 템플릿 느낌이 나지 않는 UI 방향을 잡는다 | 공식 기본 디자인 스킬 | 채택 |
| **ui-ux-pro-max** 2.15.0 | 로컬 | 스타일 79개, 팔레트 192개, 폰트 조합 74개 로컬 DB. 디자인 시스템, 배너, 브랜드, 슬라이드 스킬 | 처음 디자인 시스템을 잡을 때 | 시험 중 |
| **taste-skill** 2.1.5 | 로컬 | 랜딩·제품 페이지 아트 디렉션. 실제 브라우저로 보고 고치는 루프 | AI가 만든 티가 나는 페이지를 피하려고 | 시험 중 |
| **impeccable** 4.7.1 | 로컬 | 명령 24개(polish, audit, critique 등), 에이전트 4개. 편집마다 훅 실행 | UI 다듬기와 점검 | 시험 중 (무거움) |

## 4. 마케팅·글

| 플러그인 | 설치 경로 | 하는 일 | 설치 이유 | 상태 |
|---|---|---|---|---|
| **marketing-skills** 2.13.4 | 로컬 | 실행 스킬 52개: 가격, 결제 화면, 가입 흐름, CRO, 카피, 런칭, 디렉터리 등록, AI 검색 최적화, 콜드 메일 등 | 1인 SaaS 홍보 실행 | 시험 중 |
| **writing-quality** | claude.ai | AI 문체 제거, 비즈니스 문서, 근거 없는 주장 점검 | 랜딩 문구와 문서 품질 | 시험 중 |

## 5. 문서·도구

| 플러그인/스킬 | 설치 경로 | 하는 일 | 설치 이유 | 상태 |
|---|---|---|---|---|
| **context7** | claude.ai | 라이브러리 최신 문서 조회(MCP) | 오래된 API로 코딩하는 실수 방지 | 보류 (로그인 전) |
| **anthropic-skills** | 기본 제공 | docx, pdf, pptx, xlsx, deep-research, skill-creator 등 | 문서 파일, 조사, 스킬 만들기 | 채택 |
| 기본 명령 | 기본 제공 | `/simplify`, `/code-review`, `/security-review`, `run`, `schedule`, `loop` | 코드 정리·리뷰, 실행 확인 | 채택 |

## 6. 외부 서비스·공식 마켓플레이스 (2026-10-27 로컬 설치)

Anthropic 공식 마켓플레이스(`anthropics/claude-plugins-official`, `anthropics/knowledge-work-plugins`)에서 설치했다. 공식 마켓플레이스는 플러그인마다 검토된 커밋을 고정해 둔다. 서비스 로그인은 아직 하지 않았다. 연결 규칙은 Integrations (운영 허브 문서).

| 플러그인 | 하는 일 | 설치 이유 | 검토 메모 | 상태 |
|---|---|---|---|---|
| **stripe** 0.11.17 | 결제 구현 스킬 10개, `/test-cards`, `/explain-error`, Stripe MCP | 해외 결제의 핵심 | 훅 5개, 로컬 Node, 외부 전송 없음. Stripe CLI 텔레메트리 끔 | 꺼 둠 (결제 붙일 때 켬) |
| **supabase** 0.1.16 | DB, 인증, 저장소 스킬과 MCP | 1인 SaaS 백엔드 후보 | 공식(supabase-community) | 시험 중 (로그인 전) |
| **cloudflare** 1.0.0 | Workers/Pages 배포, Next.js on Cloudflare, 성능 | 배포 후보 | 공식(cloudflare/skills) | 꺼 둠 (배포 방식 정할 때 켬) |
| **posthog** 1.1.67 | 분석, 실험, 기능 플래그, 오류 추적 스킬과 MCP | 출시 후 지표 | 훅 2개: 쓰기 작업 전 확인 요청(안전장치), 세션 종료 시 LLM 분석 전송은 **기본 꺼짐**(`POSTHOG_LLMA_CC_ENABLED`와 키가 있어야 작동). 켜지 않는다 | 꺼 둠 (출시 후 켬) |
| **playwright** | 브라우저 자동화·E2E 테스트 MCP (Microsoft) | 결제·가입 흐름 실제 테스트 | 공식 | 시험 중 |
| **marketing** 1.2.0 | 콘텐츠, 캠페인, 브랜드 목소리, 성과 보고 (Anthropic) | 창업자 요청으로 설치. marketing-skills와 비교 | 공식 | 시험 중 (marketing-skills와 중복 비교) |

## 겹침 지도 (2026-10-27)

같은 일을 하는 플러그인이 여러 개 있다. 영역마다 **기본 담당**을 하나 두고, 나머지는 리포트로 비교한 뒤 남기거나 끈다. 작업별 순서는 [Skill Playbook](Skill%20Playbook.md)에 있다.

| 영역 | 기본 담당 | 겹치는 것 | 비교할 점 |
|---|---|---|---|
| 개발 절차 | superpowers | ponytail, caveman 작업 스킬(lean-build, surgical-patch 등) | ponytail lite가 계획·TDD를 방해하는가 |
| 과설계 방지 | ponytail (lite) | caveman `lean-build` | 둘 중 하나만 남긴다 |
| 코드 리뷰 | `/code-review` | review-council, caveman-review, engineering `code-review` | 큰 변경에서 review-council이 더 찾는가 |
| 코드 정리 | `/simplify` | ponytail-review | — |
| 랜딩·마케팅 페이지 디자인 | taste-skill | frontend-design, impeccable, ui-ux-pro-max | 첫 랜딩에서 결과 비교 |
| 제품 UI 디자인 | ui-ux-pro-max | frontend-design, impeccable | — |
| UI 점검·다듬기 | impeccable | ui-ux-pro-max | impeccable 훅 비용 대비 효과 |
| 시장 전략 | gtm-planner | product-management, marketing(Anthropic) `campaign-plan` | — |
| 마케팅 실행 | marketing-skills | marketing(Anthropic) | 하나만 남긴다 |
| 경쟁 분석 | product-management `competitive-brief` | marketing(Anthropic) `competitive-brief`, marketing-skills `competitor-profiling` | — |
| SEO | marketing-skills `seo-audit`, `ai-seo` | marketing(Anthropic) `seo-audit` | 보류 중인 claude-seo가 필요한가 |
| 글 다듬기 | writing-quality | marketing-skills `copy-editing` | 랜딩 문구는 copy-editing, 문서는 writing-quality |
| 브라우저 테스트 | playwright | 앱 내장 브라우저, taste-skill 검사기 | — |

### 부담이 큰 플러그인
2026-10-27 창업자 결정: posthog, cloudflare, stripe는 필요할 때까지 꺼 둔다. 다시 켤 때는 `claude plugin enable <이름>@claude-plugins-official` (제품 저장소에서만 쓰려면 `--scope project`).

Claude는 세션마다 스킬 설명을 모두 읽는다. 그래서 스킬이 많을수록 토큰을 더 쓰고, 엉뚱한 스킬을 부를 가능성도 커진다.

| 플러그인 | 스킬 수 | 부담 | 제안 |
|---|---|---|---|
| posthog | 약 170 | 매우 큼 | 출시 전까지 끄고, 출시 후 그 제품 저장소에서만 켠다 |
| marketing-skills | 52 | 큼 | 유지 (홍보 핵심) |
| cloudflare | 14 | 보통 | 배포 방식 정할 때까지 끈다 |
| stripe | 10 + 훅 5 | 보통 | 결제 붙일 때 켠다 |
| impeccable | 훅 3 | 편집마다 실행 | UI 작업이 없는 저장소에서는 끈다 |

## 오픈소스 플러그인 검토 기록
오픈소스 플러그인은 설치하기 전에 설정 파일, 훅, 외부 통신 코드를 읽는다. 설치한 뒤에는 설치된 커밋이 검토한 커밋과 같은지 확인하고, 업데이트하면 다시 검토한다.

| 플러그인 | 저장소 (라이선스) | 검토 커밋 | 검토 메모 |
|---|---|---|---|
| caveman | JuliusBrussee/caveman (Apache-2.0) | 9b68f7e | 훅 4개, 로컬 Node, 네트워크 없음. `~/.claude`, `~/.config/caveman`에 기록. **Caveman Cloud 스킬(`caveman-setup`, `caveman-compress`)은 외부 전송이 있어 쓰지 않는다** |
| ui-ux-pro-max | nextlevelbuilder/ui-ux-pro-max-skill (MIT) | 28b3b8d | 훅·MCP 없음. 로컬 Python 스크립트 |
| taste-skill | Leonxlnx/taste-skill (MIT) | 12af471 | 훅 없음. 쓸 때 공개 이미지 모음에서 사진을 받음 |
| impeccable | pbakaus/impeccable (Apache-2.0) | 989c484 | 훅 3개(SessionStart, Edit/Write 후, Stop 최대 30초). 처음 실행 때 GitHub 릴리스에서 엔진 바이너리를 받아 sha256 검증 |
| marketing-skills | coreyhaines31/marketingskills (MIT) | f90b9d3 | 훅·MCP 없음, 스킬만 |
| ponytail | DietrichGebert/ponytail (MIT) | 09c434a | 훅 3개, 로컬에서만 실행. 매 턴 기록을 `~/.config/ponytail/band/`에 CSV로 저장. 웹훅 비움. 기본 lite |

### 검토 후 제외
| 후보 | 이유 |
|---|---|
| code-simplifier (Anthropic) | `/simplify`와 겹침. 에이전트에 특정 코딩 스타일이 고정돼 있음 |
| ECC, alirezarezvani/claude-skills, rampstackco/claude-skills | 스킬 수백~천 개. 충돌과 토큰 낭비 |
| phuryn/pm-skills | product-management, gtm-planner와 겹침 |
| claude-mem | 모든 작업 기록, 로컬 서버. "상태는 파일에" 규칙과 맞지 않음 |
| context-mode | Elastic License 2.0(오픈소스 아님), 훅 6개 |
| ralph-loop / Ralph Wiggum | 자율 반복 루프. 비용과 통제 위험 |

### 보류
| 후보 | 다시 볼 시점 |
|---|---|
| AgriciDaniel/claude-seo 또는 zubair-trabzada/geo-seo-claude | 랜딩 페이지가 생긴 뒤, 제품 저장소에만 설치 |
