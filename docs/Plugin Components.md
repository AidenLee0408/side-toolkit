---
type: generated
status: generated
---

# Plugin Components

플러그인마다 들어 있는 스킬, 명령, 에이전트, 훅, MCP 서버, 출력 스타일의 목록이다. `python3 scripts/plugin-audit.py components`로 만든 문서라 손으로 고치지 않는다. 스킬, 명령, 에이전트의 설명은 각 플러그인이 적어 둔 원문(대부분 영어)의 첫 문장이고, 훅의 "하는 일"은 검토하면서 `plugin-reviews.json`에 적어 둔 내용이다. 왜 설치했는지와 상태는 [Plugins](Plugins.md)에, 어떤 스킬을 먼저 쓰는지는 [Plugin Playbook](Plugin%20Playbook.md)에 있다.

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
| [side-skills](#side-skills) | 예 | 2 | 0 | 0 | 0 | 0 | 0 |
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

> Ultra-compressed communication mode.

**스킬 22개**

| 스킬 | 설명 |
|---|---|
| `caveman:cavecrew` | When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder` (1-2 file edit) or `cavecrew-reviewer` (diff review) instead of working inline or… |
| `caveman:caveman` | Terse caveman voice: answer first, fluff gone, every technical fact kept. |
| `caveman:caveman-commit` | Write a Conventional Commits message compressed to intent only. |
| `caveman:caveman-compress` | Compress a memory file such as CLAUDE.md or a todo list into caveman format to save input tokens, keeping a readable backup. |
| `caveman:caveman-discover` | Find and label every LLM workflow in the repository so Caveman Cloud groups spend by workflow instead of one bucket. |
| `caveman:caveman-evidence-review` | Read-only review of Caveman Cloud evidence: cost, Cave Score, workflows, traces, latency, errors, routing, savings. |
| `caveman:caveman-explore` | Read-only repository explorer for cold-start orientation, broad cross-file localization, or when a direct search failed. |
| `caveman:caveman-help` | Quick-reference card for the three caveman skills and their commands. |
| `caveman:caveman-learn` | Act on a Caveman learn report - review the ranked token sinks, apply cost-lowering fixes with per-edit consent, and report what those fixes returned. |
| `caveman:caveman-manage` | Inspect Caveman Cloud's experiment lifecycle and block unsafe execution. |
| `caveman:caveman-optimize` | Turn a Caveman optimization observation into an operator-chosen candidate with a paired baseline evaluation. |
| `caveman:caveman-review` | Compressed code review - one line per finding with location, problem and fix. |
| `caveman:caveman-setup` | Wire a repository through the Caveman Cloud gateway so every LLM request is measured, with no behavior change. |
| `caveman:caveman-stats` | Show recorded output and cache-read token usage and mode attribution for the current Claude Code session, or locate the host's native usage report. |
| `caveman:investigate-first` | Diagnose ambiguous failures before editing. |
| `caveman:lean-build` | Build feature work with high overbuilding risk. |
| `caveman:megacave` | Caveman in Classical Chinese: 文言文 register, far fewer characters, technical terms verbatim. |
| `caveman:migration` | Implement reversible compatibility-safe transitions. |
| `caveman:safe-refactor` | Restructure code while preserving behavior. |
| `caveman:surgical-patch` | Fix bugs and small behavior changes at the narrowest responsible layer. |
| `caveman:ultracave` | Caveman at maximum compression: fragments, one word when one word is enough, each fact once. |
| `caveman:verify-and-stop` | Prove existing work meets acceptance conditions without expanding scope. |

**명령 7개**

| 명령 | 설명 |
|---|---|
| `/caveman` | Caveman voice: answer first, fluff gone, every technical fact kept (/caveman, /caveman off, /caveman status) |
| `/caveman-commit` | Generate terse caveman-style commit message |
| `/caveman-init` | Drop the always-on caveman activation rule into the current repo for every IDE agent |
| `/caveman-review` | One-line code review comments |
| `/caveman-stats` | Find Gemini CLI session token usage; Caveman savings remain unknown. |
| `/megacave` | Megacave: caveman in Classical Chinese (文言文), technical terms verbatim |
| `/ultracave` | Ultracave: caveman at maximum compression (fragments, one word when one word is enough, each fact once) |

**에이전트 3개**

| 에이전트 | 설명 |
|---|---|
| `cavecrew-builder` | Surgical 1-2 file edit. |
| `cavecrew-investigator` | Read-only code locator. |
| `cavecrew-reviewer` | Diff/branch/file reviewer. |

**훅 4개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionStart | 전체 | caveman 모드 지시와 설정을 불러와 대화에 넣는다 | 예 |
| SubagentStart | 전체 | 서브에이전트에도 같은 짧은 답변 지시를 넣는다 | 예 |
| UserPromptSubmit | 전체 | 메시지마다 짧게 답하라는 지시를 넣고, /caveman 명령으로 바뀐 모드를 기록한다 | 예 |
| SessionEnd | 전체 | 세션의 토큰 사용 통계를 로컬에 기록한다 | 아니오 |

## cloudflare

로컬 · 꺼짐 · 버전 1.0.0 · 커밋 b052c32

> Build, test, and deploy applications on Cloudflare with platform guidance Skills and the Cloudflare MCP server.

**스킬 14개**

| 스킬 | 설명 |
|---|---|
| `cloudflare:agents-sdk` | Build, debug, or review Cloudflare Agents SDK applications using the agents package. |
| `cloudflare:cloudflare` | Discover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security. |
| `cloudflare:cloudflare-email-service` | Implement or troubleshoot Cloudflare Email Sending and Email Routing integrations and their delivery configuration. |
| `cloudflare:cloudflare-one` | Design, configure, troubleshoot, or review Cloudflare One Zero Trust and SASE deployments. |
| `cloudflare:cloudflare-one-migrations` | Assess and plan migrations from existing VPN, SWG, or SASE platforms to Cloudflare One, including policy mapping, parity gaps, and rollout. |
| `cloudflare:durable-objects` | Build, debug, or review Cloudflare Durable Objects code for persistent state and coordination. |
| `cloudflare:nextjs-on-cloudflare` | Build, migrate, and deploy Next.js apps on Cloudflare Workers with vinext. |
| `cloudflare:sandbox-migrate-to-next` | Migrate Cloudflare Sandbox apps from stable @cloudflare/sandbox to @cloudflare/sandbox@next (SDK 1.0 preview). |
| `cloudflare:sandbox-next` | Build or maintain Cloudflare Sandbox apps on @cloudflare/sandbox@next (SDK 1.0 preview). |
| `cloudflare:sandbox-stable` | Build or maintain Cloudflare Sandbox apps on the stable @cloudflare/sandbox package. |
| `cloudflare:turnstile-spin` | Set up, repair, or migrate to Cloudflare Turnstile bot verification in an existing frontend and backend, including server-side Siteverify. |
| `cloudflare:web-perf` | Audit, diagnose, or optimize website loading and interaction performance, Core Web Vitals, and Lighthouse performance scores. |
| `cloudflare:workers-best-practices` | Cloudflare Workers best practices for production applications. |
| `cloudflare:wrangler` | Run or troubleshoot Wrangler CLI commands and configure Worker projects for local development, deployment, and Cloudflare resource management. |

**MCP 서버 1개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| cloudflare | http | `https://mcp.cloudflare.com/mcp` |

## fluent-korean

로컬 · 켜짐 · 버전 1.0.0 · 커밋 ce8683f

> Claude Code가 유창하고 자연스러운 한국어로 응답하게 하는 출력 스타일.

**출력 스타일 2개**: `fluent-korean-not-coding`, `fluent-korean`

## humanize-korean

로컬 · 켜짐 · 버전 2.3.2 · 커밋 b37e020

> AI가 쓴 한글 텍스트를 사람이 쓴 글처럼 윤문 — route_hint 3경로(light 1콜 · standard 2콜 · heavy 3+콜).

**스킬 4개**

| 스킬 | 설명 |
|---|---|
| `humanize-korean:humanize` | AI가 쓴 한글 텍스트를 자연스럽게 윤문하는 진입 명령. |
| `humanize-korean:humanize-korean` | AI(ChatGPT·Claude·Gemini 등)가 쓴 한글 텍스트를 "사람이 쓴 글처럼" 윤문해주는 오케스트레이터 스킬. |
| `humanize-korean:humanize-redo` | 가장 최근 윤문 결과를 2차로 다시 다듬는다 — 특정 카테고리·문단·강도 조정도 가능. |
| `humanize-korean:humanize-scan` | 한글 글에 AI 티가 얼마나 있는지 재고, 실제로 고치면 어떻게 되는지 표본으로 보여주는 정찰 스킬. |

**명령 4개**

| 명령 | 설명 |
|---|---|
| `/humanize` |  |
| `/humanize-korean` |  |
| `/humanize-redo` |  |
| `/humanize-scan` |  |

**에이전트 9개**

| 에이전트 | 설명 |
|---|---|
| `humanize-diagnostician` | 정밀(strict) 모드 1단계 진단 에이전트. |
| `humanize-finalizer` | 정밀(strict) 모드 3단계 마무리 에이전트. |
| `humanize-monolith` | 전 경로(light·standard·heavy) 공용 단일 호출 윤문 에이전트. |
| `korean-ai-tell-taxonomist` | AI가 생성한 한글 글의 "AI 티" 패턴을 체계적으로 분류·확장·버전 관리하는 도메인 전문가. |
| `korean-translation-scholar` | 한국 번역학계(이근희·김정우·김도훈·김순영·김혜영·이영옥·곽은주·조의연)와 국제 번역학(Baker·Toury·Laviosa·Chesterman·Toral·Sarti)의 학술 인용 계보를 Humanize KR 본진 SSOT(taxonomy.md)와 외부 references/scholar… |
| `post-editese-metric-engineer` | Toral 2019 post-editese 3축(단순화·정규화·간섭)을 한국어 정량 지표로 구체화하고, 보고서 8유형 검출 시그널을 metrics.py에 추가해 회귀 검증 가능 상태로 만드는 정량 엔지니어. |
| `quick-rules-integrator` | 신규 분류 체계 v2.0과 metrics·playbook 패치를 quick-rules.md(monolith 전용 슬림 룰북, 126줄 → ≤180줄)에 안착하고 monolith 도구 호출 3회 캡(v1.6.1) 회귀를 검증한 뒤, GitHub PR 초안과 CHANGELOG를 작성하는… |
| `taxonomy-gap-analyzer` | Humanize KR 본진 v1.6 분류 체계(10대 카테고리·61+ 패턴)와 외부 학술 보고서 후보 풀(translationese-research-distiller 산출물)을 3-축 매트릭스(이미 본진·보강·신규)로 매핑해 분류학자에게 승격 결정 입력을 제공하는 갭 분석가. |
| `translationese-research-distiller` | 한국어 번역투(translationese) 학술 보고서를 8유형·15항목 PE 체크리스트·post-editese 3축·학술 인용 계보·예문 코퍼스로 분해해 후속 분류·승격 단계가 직접 소비할 수 있는 구조화 JSON으로 증류하는 도메인 추출가. |

## impeccable

로컬 · 켜짐 · 버전 4.7.1 · 커밋 989c484

> Design fluency for frontend development.

**스킬 1개**

| 스킬 | 설명 |
|---|---|
| `impeccable:impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, simplify, harden, animate, or otherwise improve a frontend interface: websites, la… |

**에이전트 4개**

| 에이전트 | 설명 |
|---|---|
| `impeccable-asset-producer` | Produces clean reusable raster assets from approved Impeccable mock references without redesigning the direction. |
| `impeccable-documenter` | Records DESIGN.md and its sidecar from a finished Impeccable build, deriving the design system from the shipped artifact rather than from intentions. |
| `impeccable-finish-reviewer` | Reviews a finished Impeccable build against its direction contract, the approved comp, and the chosen world's quality bar, returning an ordered list of materia… |
| `impeccable-manual-edit-applier` | Applies leased Impeccable live manual copy-edit batches to source and returns canonical Apply results. |

**훅 3개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionStart | 전체 | 디자인 엔진을 준비한다 | 예 |
| PostToolUse | Edit¦Write | 파일을 고친 뒤 UI 변경을 점검한다 | 아니오 |
| Stop | 전체 | 답변이 끝날 때 디자인을 한 번 더 점검한다(최대 30초) | 아니오 |

## marketing-skills

로컬 · 켜짐 · 버전 2.13.4 · 커밋 f90b9d3

> Marketing skills for AI agents — conversion optimization, copywriting, SEO, paid ads, ad creative, and growth

**스킬 52개**

| 스킬 | 설명 |
|---|---|
| `marketing-skills:ab-testing` | When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. |
| `marketing-skills:ad-creative` | When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad variations — for any paid advertising platfo… |
| `marketing-skills:ads` | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms. |
| `marketing-skills:ai-seo` | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. |
| `marketing-skills:analytics` | When the user wants to set up, improve, or audit analytics tracking and measurement. |
| `marketing-skills:aso` | When the user wants to audit or optimize an App Store or Google Play listing. |
| `marketing-skills:attribution` | When the user wants to figure out which marketing actually drives conversions and revenue, choose or interpret an attribution model, or reconcile conflicting n… |
| `marketing-skills:churn-prevention` | When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implement retention strategies. |
| `marketing-skills:co-marketing` | When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. |
| `marketing-skills:cold-email` | Write and run B2B cold outbound that gets replies, from cold emails and follow-ups to sending setup, LinkedIn, multichannel cadences, and reply handling. |
| `marketing-skills:community-marketing` | Build and leverage online communities to drive product growth and brand loyalty. |
| `marketing-skills:competitor-profiling` | When the user wants to research, profile, or analyze competitors from their URLs. |
| `marketing-skills:competitors` | When the user wants to create competitor comparison or alternative pages for SEO and buyer-facing use. |
| `marketing-skills:content-strategy` | When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. |
| `marketing-skills:conversion-tracking` | Set up, audit, verify, or fix website conversion tracking. |
| `marketing-skills:copy-editing` | When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. |
| `marketing-skills:copywriting` | When the user wants to write, rewrite, or improve marketing copy for any page, including homepage, landing pages, pricing pages, feature pages, about pages, or… |
| `marketing-skills:cro` | When the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage, landing pages, pricing pages, feature pag… |
| `marketing-skills:customer-research` | When the user wants to conduct, analyze, or synthesize customer research. |
| `marketing-skills:directory-submissions` | When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backlinks, domain rating, and discovery. |
| `marketing-skills:emails` | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. |
| `marketing-skills:events` | When the user wants to plan, run, sponsor, speak at, or get pipeline from events — webinars, conferences, trade shows, meetups, dinners, workshops, virtual sum… |
| `marketing-skills:free-tools` | When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness. |
| `marketing-skills:image` | When the user wants to create, generate, edit, or optimize images for marketing — blog heroes, social graphics, product mockups, profile banners, listing visua… |
| `marketing-skills:influencer-marketing` | When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and vetting partners, structuring deals, briefing… |
| `marketing-skills:launch` | When the user wants to plan a product launch, feature announcement, or release strategy. |
| `marketing-skills:lead-magnets` | When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. |
| `marketing-skills:link-building` | When the user wants to earn backlinks or third-party mentions that lift rankings and AI citations. |
| `marketing-skills:marketing-council` | When the user wants multiple expert perspectives on a marketing question — a simulated board of advisors staffed by legendary marketers (Seth Godin, David Ogil… |
| `marketing-skills:marketing-ideas` | When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. |
| `marketing-skills:marketing-loops` | When the user wants to set up a recurring, self-running marketing workflow — a repeatable loop an AI agent runs on a cadence (weekly, daily, on a trigger) rath… |
| `marketing-skills:marketing-plan` | When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product. |
| `marketing-skills:marketing-psychology` | When the user wants to apply psychological principles, mental models, or behavioral science to marketing. |
| `marketing-skills:offers` | When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing, bonus stacking, guarantee design, scarc… |
| `marketing-skills:onboarding` | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. |
| `marketing-skills:paywalls` | When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. |
| `marketing-skills:popups` | When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. |
| `marketing-skills:pricing` | When the user wants help with pricing decisions, packaging, or monetization strategy. |
| `marketing-skills:product-marketing` | When the user wants to create or update their product marketing context document. |
| `marketing-skills:programmatic-seo` | When the user wants to create SEO-driven pages at scale using templates and data. |
| `marketing-skills:prospecting` | When the user wants to find, qualify, and build a list of prospects to reach out to, across B2B SaaS, general B2B, or local small businesses. |
| `marketing-skills:public-relations` | When the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy (not pull requests). |
| `marketing-skills:referrals` | When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. |
| `marketing-skills:revops` | When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. |
| `marketing-skills:sales-enablement` | When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. |
| `marketing-skills:schema` | When the user wants to add, fix, or optimize schema markup and structured data on their site. |
| `marketing-skills:seo-audit` | When the user wants to audit, review, or diagnose SEO issues on their site. |
| `marketing-skills:signup` | When the user wants to optimize signup, registration, account creation, or trial activation flows. |
| `marketing-skills:site-architecture` | When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. |
| `marketing-skills:sms` | When the user wants to plan, build, or optimize SMS, MMS, or WhatsApp marketing — including welcome flows, abandoned cart texts, post-purchase, win-back, promo… |
| `marketing-skills:social` | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, or Facebook, or wants to do socia… |
| `marketing-skills:video` | When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. |

## marketing

로컬 · 켜짐 · 버전 1.2.0 · 커밋 33d3dea

> Create content, plan campaigns, and analyze performance across marketing channels.

**스킬 8개**

| 스킬 | 설명 |
|---|---|
| `marketing:brand-review` | Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. |
| `marketing:campaign-plan` | Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics. |
| `marketing:competitive-brief` | Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. |
| `marketing:content-creation` | Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies. |
| `marketing:draft-content` | Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO recommendations. |
| `marketing:email-sequence` | Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. |
| `marketing:performance-report` | Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations. |
| `marketing:seo-audit` | Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison. |

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

> Browser automation and end-to-end testing MCP server by Microsoft.

**MCP 서버 1개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| playwright | stdio | `npx @playwright/mcp@latest` |

## ponytail

로컬 · 켜짐 · 버전 5.3.2 · 커밋 09c434a

> Lazy senior dev mode.

**스킬 6개**

| 스킬 | 설명 |
|---|---|
| `ponytail:ponytail` | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. |
| `ponytail:ponytail-audit` | Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or split. |
| `ponytail:ponytail-debt` | List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. |
| `ponytail:ponytail-gain` | Show ponytail's measured savings (code, cost, speed) from the benchmark. |
| `ponytail:ponytail-help` | Quick reference for ponytail levels, skills and commands. |
| `ponytail:ponytail-review` | Quality review of a change: is the logic right, is it safe, does it hold under real load, is risky code tested, is it fast enough, and is every line needed. |

**명령 6개**

| 명령 | 설명 |
|---|---|
| `/ponytail` | Switch ponytail intensity level (lite/full/ultra/off) |
| `/ponytail-audit` | Quality audit of the whole repo: bugs, security, load, tests, speed, bloat |
| `/ponytail-debt` | Harvest shortcut: comments into a tracked debt ledger |
| `/ponytail-gain` | Show ponytail's measured impact scoreboard (less code, cost, time) |
| `/ponytail-help` | Quick reference for ponytail levels, skills, and commands |
| `/ponytail-review` | Quality review of the current changes: bugs, security, load, tests, speed, bloat |

**훅 3개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionStart | startup¦resume¦clear¦compact | 가장 작게 만들라는 지시를 넣는다 | 예 |
| SubagentStart | 전체 | 서브에이전트에도 같은 지시를 넣는다 | 예 |
| UserPromptSubmit | 전체 | 메시지마다 지시를 넣고, /ponytail 명령으로 바뀐 단계를 기록한다 | 예 |

## posthog

로컬 · 꺼짐 · 버전 1.1.67 · 커밋 e0fbf5e

> Access PostHog analytics, feature flags, experiments, error tracking, and insights directly from your AI coding tool.

**스킬 161개**

| 스킬 | 설명 |
|---|---|
| `posthog:adding-warehouse-person-properties` | Sync columns from a synced data warehouse table onto PostHog person or group properties, so warehouse data becomes usable anywhere person and group properties… |
| `posthog:analyzing-expensive-users` | Analyze the most expensive users in AI observability and explain why they cost so much. |
| `posthog:analyzing-experiment-session-replays` | Analyze session replay patterns across experiment variants to understand user behavior differences. |
| `posthog:analyzing-task-runs` | - Split a completed PostHog task run into activity records — what the agent tried, whether it worked, what blocked it — and record each one through the report_… |
| `posthog:assessing-heatmaps` | Assesses what a page's heatmap is telling you and recommends concrete changes. |
| `posthog:auditing-endpoints` | Audit every endpoint in a PostHog project for staleness, failed materialisations, and unused materialised versions. |
| `posthog:auditing-experiments-flags` | Audit PostHog experiments and feature flags for configuration issues, staleness, and best-practice violations. |
| `posthog:auditing-warehouse-source-health` | Audit the health of a PostHog project's data warehouse sources and syncs — find every broken or degraded source connection, sync schema, and webhook channel. |
| `posthog:auditing-warehouse-view-health` | Audit the health of a PostHog project's materialized views (saved queries) — find every failed materialization and flag unused or stale materialized views that… |
| `posthog:authoring-data-quality-checks` | Adds and runs data quality checks (dbt-test style assertions) on a project's warehouse tables and saved-query views, and HogQL catalog metrics: not-null, uniqu… |
| `posthog:authoring-error-tracking-alerts` | Author error tracking alerts that fire when an issue is created, reopened, or starts spiking. |
| `posthog:authoring-log-alerts` | Author useful, low-noise log alerts on services in a PostHog project. |
| `posthog:authoring-scouts` | Write, edit, and adapt PostHog Signals scouts: scheduled agents that scan a project and report findings. |
| `posthog:building-a-dashboard` | Build a new dashboard, or update an existing one, from a set of insights — the same job the in-app assistant does with its upsert-dashboard tool, but over MCP. |
| `posthog:building-canvases` | Create or edit a PostHog freeform canvas — a sandboxed browser application (data board, document, form, small tool, graphics experiment) stored in PostHog and… |
| `posthog:building-html-canvases` | Author a PostHog canvas with semantic HTML, CSS, and direct browser APIs — documents, articles, generative graphics, 2D canvas and WebGL experiences, and focus… |
| `posthog:building-loops` | - Build a Loop for PostHog Desktop: a workflow that creates an AI task each time its trigger fires, optionally followed by a Slack or email notification with t… |
| `posthog:building-react-quill-canvases` | Author the React + Quill implementation of a PostHog canvas: the single-component contract, the allowed imports, Quill (PostHog's design system) component and… |
| `posthog:building-workflows` | Build, edit, test, enable, and monitor PostHog workflows over MCP. |
| `posthog:checking-deploy-timing` | Determine when a PostHog code change reached a given environment by reading the hidden GIT deploy annotations in the project and correlating them with the merg… |
| `posthog:checking-member-access` | Explains what a member or a role can do in a PostHog project, using the access control MCP tools. |
| `posthog:choosing-trend-or-slope-view` | Clarify how to visualize change over a time range before building a trend. |
| `posthog:cleaning-up-stale-feature-flags` | Identify stale feature flags in a PostHog project and clean up the code that checks them. |
| `posthog:composing-grid-canvases` | Compose PostHog grid canvases — widget grids (including the user's home canvas) built from reusable component canvases. |
| `posthog:configuring-experiment-analytics` | Configures the analytics side of a PostHog experiment — exposure criteria (server-resolved default exposure event vs custom exposure events), primary and secon… |
| `posthog:configuring-experiment-rollout` | Configures the rollout shape of a PostHog experiment — the variant split (50/50, 80/20, A/B/C ratios), the overall rollout percentage that gates how many users… |
| `posthog:consuming-endpoints-from-client-code` | Wire a PostHog endpoint into a client app or SDK. |
| `posthog:context-layer-consolidation` | Keep the context wiki coherent using the deterministic lint report queue |
| `posthog:context-layer-dreaming` | Synthesizes recent organizational activity into a durable context wiki. |
| `posthog:context-layer-health-check` | Semantic review of context wiki quality after deterministic consolidation |
| `posthog:copying-endpoints-across-projects` | Copy a PostHog endpoint (a saved HogQL/insight query exposed as an API route) to another project in the same organization, or duplicate it under a new name in… |
| `posthog:copying-flags-across-projects` | Copy a feature flag from one PostHog project to one or more target projects in the same organization. |
| `posthog:creating-ai-subscription` | Create a recurring AI-generated PostHog report — schedule a free-text prompt to run on a cron, with the LLM-synthesized markdown delivered to email, Slack, or… |
| `posthog:creating-an-endpoint` | Create a PostHog endpoint with the right shape on the first try — covers query kind choice, name conventions, what to expose as variables (HogQL code_name vs i… |
| `posthog:creating-box-plot-insights` | - Creates product analytics or SQL-backed box plot insights in PostHog. |
| `posthog:creating-experiments` | Guides agents through experiment creation: reading the project's setup with experiment-setup-context, defining the hypothesis, configuring rollout and bucketin… |
| `posthog:creating-online-evaluations` | Author continuously-running online evaluations in PostHog AI observability, grounded in real failure modes you've identified. |
| `posthog:creating-replay-vision-scanners` | Guides agents through creating and safely sizing a Replay Vision scanner: choosing the scanner type (monitor/classifier/scorer/summarizer), shaping the Recordi… |
| `posthog:creating-surveys` | Creates and launches PostHog surveys through MCP, including NPS/CSAT popovers, hosted feedback forms, and headless surveys. |
| `posthog:debugging-experiments` | - Debug and support PostHog Experiments (A/B tests) for a customer looking at their own results. |
| `posthog:debugging-surveys` | - Diagnose PostHog Surveys configuration and responses across all five SDKs (web/posthog-js, iOS, Android, Flutter, React Native). |
| `posthog:designing-email-templates` | Author, save, and edit email templates in the PostHog workflows library — compose email design JSON with Liquid personalization and create and round-trip-edit… |
| `posthog:diagnosing-ci-and-merge-bottlenecks` | Diagnoses CI and pull-request pipeline health for a GitHub repo using the engineering analytics MCP tools — pull-requests (PR list with CI status), workflow-he… |
| `posthog:diagnosing-endpoint-performance` | Diagnose why a PostHog endpoint is slow or expensive and propose a concrete fix — bump the cache TTL, enable materialisation, restructure variables, or rewrite… |
| `posthog:diagnosing-experiment-results` | Diagnoses bias, anomalies, and strange results on a PostHog experiment. |
| `posthog:diagnosing-failed-warehouse-syncs` | Diagnose why a data warehouse sync is failing and recommend the right recovery action. |
| `posthog:diagnosing-missing-recordings` | Diagnoses why a session recording is missing or was not captured. |
| `posthog:diagnosing-sdk-health` | Diagnoses the health of a project's PostHog SDK integrations — which SDKs are out of date and how to fix them. |
| `posthog:diagnosing-stacktrace-symbolication` | Help users debug PostHog Error Tracking stack-trace symbolication for any supported platform — JavaScript/TypeScript web, React Native (Hermes), Android (Progu… |
| `posthog:downloading-batch-export-files` | Export PostHog events, persons, sessions, or the results of a HogQL query on demand and download the resulting files. |
| `posthog:exploring-ai-failures` | Find where an AI/LLM application is failing in production and surface the failure patterns, working from real traces. |
| `posthog:exploring-apm-traces` | Investigates distributed application performance using PostHog APM (OpenTelemetry span) data via MCP. |
| `posthog:exploring-autocapture-events` | Guides exploration of $autocapture events captured by posthog-js to understand user interactions, find CSS selectors (especially data-attr attributes), evaluat… |
| `posthog:exploring-endpoint-execution-logs` | Explore and diagnose a PostHog endpoint's execution logs — error messages, failed runs, cache misses, slow runs, or unexpected row counts during endpoint invoc… |
| `posthog:exploring-live-traffic` | Inspects PostHog Web analytics Live tab data — current users online, last-30-minutes pageviews, top pages, referrers, devices, browsers, countries, bot traffic… |
| `posthog:exploring-llm-clusters` | Investigate AI observability clusters — understand usage patterns in AI/LLM traffic, compare cluster behavior, compute cost/latency metrics, and drill into ind… |
| `posthog:exploring-llm-costs` | Investigate LLM spend in PostHog — total cost over time, cost by model, provider, user, trace, or custom dimension, token and cache-hit economics, and cost reg… |
| `posthog:exploring-llm-evaluations` | Investigate AI observability evaluations — `hog` (deterministic code-based), `llm_judge` (LLM-prompt-based), and `sentiment` (user-message sentiment). |
| `posthog:exploring-llm-traces` | Debug and inspect LLM/AI agent traces using PostHog's MCP tools. |
| `posthog:exploring-mcp-intent-clusters` | Explore PostHog MCP intent clusters — agent goals grouped by semantic similarity, with each cluster's tool distribution and error rates, plus the tool-centric… |
| `posthog:exploring-mcp-sessions` | Investigate individual PostHog MCP sessions — the sequence of tool calls a single agent made in one run, what it was trying to do, and where it went wrong. |
| `posthog:exploring-mcp-tool-original-user-motive` | Build a starting-point taxonomy for an MCP tool — what users were trying to accomplish before they reached the tool — and publish it as a PostHog notebook. |
| `posthog:exploring-mcp-tool-quality` | Investigate the quality of PostHog MCP tool calls — error rates, latency, reach, and which tools are failing or slow. |
| `posthog:exploring-mcp-tool-usage` | Starting point for exploring how a PostHog MCP server's tools are used — routes a broad question to the typed tool that answers it. |
| `posthog:exploring-replay-vision-observations` | Guides agents through pulling a Replay Vision scanner's observations, reading the findings, and acting on them — summarizing patterns across sessions, drilling… |
| `posthog:exploring-scouts` | How to explore and make sense of PostHog Signals scouts — the scheduled agents that scan a project and write reports into the Signals inbox. |
| `posthog:feature-usage-feed` | Set up an LLM-judge evaluation that extracts canonical use cases for a PostHog feature at scale and streams the results to a Slack channel as a live feed. |
| `posthog:filtering-bot-traffic` | Identify, measure, and exclude bot / crawler / AI-agent traffic in PostHog web and product analytics using the traffic classification surface (the isLikelyBot… |
| `posthog:finding-deleted-feature-flags` | Find feature flags that were soft-deleted in the active project within a recent time window. |
| `posthog:finding-experiments` | Resolves a PostHog experiment reference from natural language to a concrete experiment ID by browsing `experiment-list` (not feature-flag tools), with disambig… |
| `posthog:finding-replay-for-issue` | Finds the most informative session recording linked to an error tracking issue. |
| `posthog:finding-sessions-to-watch` | Guides a user from "I want to watch recordings but don't know which ones" to a short, high-signal list of sessions worth watching. |
| `posthog:formatting-insight-axes` | Pick the right y-axis unit when creating or updating an insight via `posthog:insight-create` or `posthog:insight-update` — both TrendsQuery (`trendsFilter.aggr… |
| `posthog:grouping-noisy-errors` | Consolidate PostHog error tracking issues that are the same actual error reported under different fingerprints. |
| `posthog:inbox-exploration` | Explore PostHog's Inbox and act on what it surfaces — the place where signal reports cluster into actionable issues and trends. |
| `posthog:instrument-error-tracking` | - Add PostHog error tracking to capture and monitor exceptions. |
| `posthog:instrument-feature-flags` | - Add PostHog feature flags to gate new functionality. |
| `posthog:instrument-integration` | - Add PostHog SDK integration to your application. |
| `posthog:instrument-llm-analytics` | - Add PostHog AI Observability to trace AI model usage. |
| `posthog:instrument-logs` | - Add PostHog log capture to track application logs. |
| `posthog:instrument-metrics` | - Add PostHog metric capture to track counters, gauges, and histograms. |
| `posthog:instrument-product-analytics` | - Add PostHog product analytics events to track user behavior. |
| `posthog:investigate-metric` | Diagnose why a product metric changed (dropped, spiked, or plateaued) by orchestrating breakdowns, actors, paths, lifecycle, retention, and annotations queries. |
| `posthog:investigating-ci-failures` | Investigates a specific CI failure to a verdict: whose fault, which commit, who wrote it, and whether it's fixed. |
| `posthog:investigating-error-issue` | Investigates a single PostHog error tracking issue end-to-end. |
| `posthog:investigating-logs` | Investigate logs in a PostHog project: verify a service or deployment is healthy, explain an error spike, triage an incident, or understand what a log stream i… |
| `posthog:investigating-metric-anomalies` | Investigates server/infrastructure metric anomalies in PostHog Metrics — from "this metric is rising/dropping/spiking" or a fired alert to a probable cause wit… |
| `posthog:investigating-replay` | Investigates a session recording by gathering metadata, person profile, same-session events, and linked error tracking issues in one pass. |
| `posthog:managing-endpoint-versions` | Work safely with endpoint versions — preview a draft in the playground, roll back to an older version, update settings on one version without bumping query his… |
| `posthog:managing-experiment-lifecycle` | Guides experiment state transitions: launching, pausing, resuming, freezing/unfreezing exposure, ending, shipping variants, archiving, resetting, duplicating,… |
| `posthog:managing-path-cleaning-rules` | Inspects URL paths and proposes, tests, orders, and applies project-level path cleaning rules so dynamic segments (numeric IDs, UUIDs, slugs, dates) collapse i… |
| `posthog:managing-reminders` | Create and manage PostHog reminders — private, human-paced nudges that fire as in-app notifications on a schedule, optionally linked to a PostHog resource. |
| `posthog:managing-streamlit-apps` | Create, deploy, and operate Streamlit apps in PostHog via the streamlit-apps MCP tools — create an app, set its source, start and stop its sandbox, poll status… |
| `posthog:managing-subscriptions` | Create and manage scheduled PostHog subscriptions for insight snapshots, dashboard snapshots, and AI prompt reports. |
| `posthog:modeling-activation-metrics` | Build reusable activation models — an activation-rate metric and a per-user/per-account activated flag — on either PostHog data-warehouse views (HogQL) or an e… |
| `posthog:modeling-conversion-metrics` | Build reusable conversion models — funnel/step conversion rates, drop-off, and time-to-convert — on either PostHog data-warehouse views (HogQL) or an external… |
| `posthog:modeling-dimension-tables` | Build reusable dimension / lookup tables for a star schema — country/region, timezone, currency, date, plan/product, and other descriptive attributes — on eith… |
| `posthog:modeling-product-usage-metrics` | Build reusable product-usage and engagement models — retention, stickiness, and lifecycle — on either PostHog data-warehouse views (HogQL) or an external dbt p… |
| `posthog:modeling-revenue-metrics` | Build reusable revenue models — MRR, ARR, gross revenue, new/expansion/contraction/churn, ARPU, LTV, and per-customer/per-account revenue — on either PostHog d… |
| `posthog:modeling-warehouse-foundations` | Shared foundations for building reusable data models in PostHog, on either of two stacks: PostHog-native data-warehouse views / materialized views (HogQL, via… |
| `posthog:querying-canvas-data` | Get PostHog data into a canvas correctly: the host-injected `ph` SDK (loadInsight, query, capture, state, connectors, openExternal, navigate), the data hierarc… |
| `posthog:querying-posthog-data` | Explains how to query PostHog data, defaulting to typed runners for supported product analytics. |
| `posthog:resolving-ingestion-warnings` | Diagnoses and resolves PostHog ingestion warnings — problems recorded while ingesting events (dropped events, rejected person merges, oversized payloads, inval… |
| `posthog:review-hog-authoring` | How to author custom PostHog Review skills: the review perspectives, blind-spot checks, validation criteria, and resolution criteria that drive PostHog Review'… |
| `posthog:review-hog-blind-spots-general` | The general blind-spot check for PostHog Review, the final sweep that runs after every enabled review perspective has reviewed a chunk. |
| `posthog:review-hog-perspective-contracts-security` | The Contracts & Security review perspective for PostHog Review. |
| `posthog:review-hog-perspective-logic-correctness` | The Logic & Correctness review perspective for PostHog Review. |
| `posthog:review-hog-perspective-performance-reliability` | The Performance & Reliability review perspective for PostHog Review. |
| `posthog:review-hog-resolution-criteria` | The resolution criteria for PostHog Review's resolution stage: the bar for deciding, per unresolved review thread, whether the ask is worth implementing and sa… |
| `posthog:review-hog-validation-criteria` | The validation criteria for PostHog Review, the bar for deciding whether a flagged PR issue is worth keeping. |
| `posthog:scanning-experiments-with-replay-vision` | Provisions a Replay Vision scanner scoped to one experiment's exposed sessions: sets `experiment_targeting` so the API derives the person-scoped exposure filte… |
| `posthog:setting-up-a-custom-rest-source` | Connect an arbitrary REST API to the PostHog data warehouse as a Custom source by authoring a JSON manifest, with no per-source code. |
| `posthog:setting-up-a-data-warehouse-source` | Guide the user through connecting a new data warehouse source — Postgres, MySQL, Stripe, Hubspot, MongoDB, Salesforce, BigQuery, Snowflake, and so on. |
| `posthog:setting-up-data-catalog` | Populates and maintains a project's data catalog (semantic layer): canonical metrics, trust marks (certifications) on warehouse tables/views, and reviewed tabl… |
| `posthog:setting-up-warehouse-properties` | Populate person or group properties from a data warehouse table or materialized view, so warehouse columns become properties usable in feature flags, cohorts,… |
| `posthog:signals` | How to query the document_embeddings table for raw signal data using HogQL. |
| `posthog:signals-scout-ai-observability` | Signals scout for PostHog AI observability. |
| `posthog:signals-scout-anomaly-detection` | Signals scout that watches the project's most-viewed dashboards and insights for anomalies — bursts, drops, flat-lines, and trend breaks — against each insight… |
| `posthog:signals-scout-apm` | Signals scout for PostHog distributed tracing (APM / OpenTelemetry spans). |
| `posthog:signals-scout-conversations` | Signals scout for PostHog Conversations (support inbox). |
| `posthog:signals-scout-csp-violations` | Signals scout for Content Security Policy violations. |
| `posthog:signals-scout-customer-analytics` | Signals scout for PostHog Customer analytics (Accounts). |
| `posthog:signals-scout-customer-analytics-billing-and-usage` | Signals scout for per-account product-mix shifts. |
| `posthog:signals-scout-data-pipelines` | Signals scout for PostHog data pipelines — CDP destinations and transformations, batch exports, and hog flows. |
| `posthog:signals-scout-data-warehouse` | Signals scout for warehouse imports. |
| `posthog:signals-scout-error-tracking` | Signals scout for PostHog error tracking. |
| `posthog:signals-scout-experiments` | Signals scout for PostHog A/B experiments. |
| `posthog:signals-scout-feature-flags` | Signals scout for PostHog feature flags. |
| `posthog:signals-scout-general` | Cross-product Signals scout. |
| `posthog:signals-scout-health-checks` | Signals scout over PostHog's own health checks. |
| `posthog:signals-scout-inbox-validation` | Follow-up Signals scout for the inbox itself. |
| `posthog:signals-scout-insight-alerts` | Signals scout over the project's configured insight alerts. |
| `posthog:signals-scout-logs` | Signals scout for PostHog logs. |
| `posthog:signals-scout-mcp-tool-calls` | Signals scout for PostHog MCP tool calls. |
| `posthog:signals-scout-observability-gaps` | Signals scout for observability gaps — significant event volumes with no insight, dashboard, or alert coverage. |
| `posthog:signals-scout-pr-follow-up` | Follow-up Signals scout for recently merged pull requests. |
| `posthog:signals-scout-product-analytics` | Signals scout for core product-analytics flows — funnels, retention, lifecycle, stickiness, and paths. |
| `posthog:signals-scout-replay-vision` | Signals scout for PostHog Replay Vision scanners. |
| `posthog:signals-scout-revenue-analytics` | Signals scout for PostHog revenue analytics. |
| `posthog:signals-scout-session-replay` | Signals scout for PostHog session replay. |
| `posthog:signals-scout-skills-store` | Skill-hygiene scout for the team's PostHog skills store. |
| `posthog:signals-scout-surveys` | Signals scout for PostHog surveys. |
| `posthog:signals-scout-tasks` | Signals scout for PostHog Tasks. |
| `posthog:signals-scout-web-analytics` | Signals scout for PostHog web traffic. |
| `posthog:signals-scout-web-vitals` | Signals scout for Core Web Vitals (`$web_vitals`). |
| `posthog:signals-scout-workflows` | Signals scout for PostHog workflows. |
| `posthog:skills-store` | - Discover and use shared team skills stored in PostHog. |
| `posthog:suggesting-data-imports` | Use when the user asks about revenue, payments, subscriptions, billing, CRM deals, support tickets, ad spend, production database tables, or other data PostHog… |
| `posthog:suggesting-path-cleaning-rules` | Runs and reasons about the automated AI health check that suggests path-cleaning rules for web-analytics teams. |
| `posthog:suppressing-noisy-errors` | Create PostHog error tracking suppression rules to drop high-volume, low-value errors at ingestion. |
| `posthog:triaging-error-issues` | Triage PostHog error tracking issues during a daily or on-call review. |
| `posthog:triaging-visual-review-runs` | Inspects PostHog Visual Review (VR) runs that gate PR merges with screenshot regression checks. |
| `posthog:tuning-incremental-sync-config` | Change the sync configuration of an existing data warehouse schema — switch sync_type, pick a different incremental_field, set primary_key_columns, choose cdc_… |
| `posthog:turning-engineering-analytics-into-insights` | Converts engineering analytics (PR / CI) data into saved PostHog insights, dashboards, and subscriptions, and explains how to query the product data directly w… |
| `posthog:understanding-billing-usage` | Explains PostHog billing usage and spend from the customer's visible Billing MCP tools. |
| `posthog:validating-and-publishing-canvases` | Validate and publish a canvas source project safely: the source-project shape, declared capabilities, reading the current version pointer, iterating on validat… |
| `posthog:working-with-scouts` | Work with PostHog Signals scouts: scheduled agents that monitor a project and write reports into the Signals inbox. |
| `posthog:working-with-skills` | - Best practices for agents managing PostHog skills via the MCP `skill-*` tools — how to discover, read, create, update, and refactor skills efficiently, espec… |
| `posthog:working-with-task-comments` | - Read and use comments attached to the current PostHog task, its artifacts, and its canvases through the PostHog MCP exec dispatcher. |
| `posthog:writing-simplified-technical-english` | Write English that a reader cannot misread: one meaning per word, active voice, simple tenses, one idea per sentence, short sentences. |
| `posthog:writing-streamlit-apps` | Write Streamlit app source code that runs well in a PostHog sandbox — the posthog_apps.query() bridge for reading PostHog data, the packages baked into the san… |

**명령 3개**

| 명령 | 설명 |
|---|---|
| `/llma-cc-ingest` | Manually send a Claude Code session log to PostHog LLM Analytics |
| `/llma-cc-setup` | Set up PostHog LLM Analytics to capture Claude Code sessions |
| `/llma-cc-status` | Check if Claude Code sessions are being sent to PostHog LLM Analytics |

**에이전트 1개**

| 에이전트 | 설명 |
|---|---|
| `error-analyzer` | Analyze multiple PostHog errors in parallel to identify patterns, root causes, and prioritize fixes based on user impact. |

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

로컬 · 켜짐 · 버전 0.1.3 · 커밋 d41e4b7

> 자체 제작 스킬 묶음: 짧지만 문법이 깨지지 않는 한국어 답변(writing-concise-korean), 한국어 문체 점검(checking-korean-writing)

**스킬 2개**

| 스킬 | 설명 |
|---|---|
| `side-skills:checking-korean-writing` | Use when Korean prose others will read (README, docs, release notes, landing copy, issue logs) needs a review or cleanup before saving or publishing, or when K… |
| `side-skills:writing-concise-korean` | Use when answering or writing in Korean while a brevity mode (caveman, terse, "짧게") is active, or when Korean replies come out as telegraphic noun fragments wi… |

## stripe

로컬 · 꺼짐 · 버전 0.11.17 · 커밋 deae744

> Stripe development plugin for Claude

**스킬 10개**

| 스킬 | 설명 |
|---|---|
| `stripe:connect-recommend` | - Use this skill when the user asks about Stripe Connect configuration, charge patterns, Dashboard access, or how to get started with Connect, is building a ma… |
| `stripe:connect-required-verification-information` | - Use this skill when the user asks what information a Stripe Connect connected account must provide for verification, onboarding, KYC, or account requirements… |
| `stripe:metronome` | - Guides Metronome usage-based billing integration decisions — event ingestion (single and batch, idempotency, billable metrics), contract design (rate cards,… |
| `stripe:stripe-apps` | - Build, modify, or review Stripe Apps and extensions using the relevant documentation and reference guides. |
| `stripe:stripe-best-practices` | - Guides Stripe integration decisions across development and test environment planning (separate sandboxes vs the shared test mode sandbox), API selection (Che… |
| `stripe:stripe-directory` | - Identifies external providers, merchants, nonprofits, platforms, APIs, and software services, and resolves the documented way to engage them — to pay, donate… |
| `stripe:stripe-docs` | - Use when the user or agent needs to read, search, or look up Stripe documentation or API reference. |
| `stripe:stripe-pay` | - Helps users send funds to another Stripe business, transfer money to a Stripe Profile handle or network ID, or ask whether an agent can pay a Stripe business. |
| `stripe:stripe-projects` | Use when the user wants to provision infrastructure or third-party services using Stripe Projects. |
| `stripe:upgrade-stripe` | - Guide for upgrading Stripe API versions, webhook endpoints, server-side SDKs, Stripe.js, and mobile SDKs |

**명령 2개**

| 명령 | 설명 |
|---|---|
| `/explain-error` | Explain Stripe error codes and provide solutions with code examples |
| `/test-cards` | Display Stripe test card numbers for various testing scenarios |

**에이전트 1개**

| 에이전트 | 설명 |
|---|---|
| `Company Researcher` | Research a company from its URL or description to infer Stripe Connect integration shape |

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

> Official Supabase plugin for Claude Code with bundled Supabase skills and MCP access for project management, database work, auth, storage, and Postgres best practices.

**스킬 2개**

| 스킬 | 설명 |
|---|---|
| `supabase:supabase` | Use when doing ANY task involving Supabase. |
| `supabase:supabase-postgres-best-practices` | Postgres best practices maintained by Supabase, for Postgres running anywhere. |

**MCP 서버 1개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| supabase | http | `https://mcp.supabase.com/mcp` |

## taste-skill

로컬 · 켜짐 · 버전 2.1.5 · 커밋 12af471

**스킬 1개**

| 스킬 | 설명 |
|---|---|
| `taste-skill:design-taste-frontend` | - tasteskill v2, the anti-slop frontend skill. |

## ui-ux-pro-max

로컬 · 켜짐 · 버전 2.15.0 · 커밋 28b3b8d

> UI/UX design intelligence.

**스킬 7개**

| 스킬 | 설명 |
|---|---|
| `ui-ux-pro-max:banner-design` | Design banners for social media, ads, website heroes, creative assets, and print. |
| `ui-ux-pro-max:brand` | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. |
| `ui-ux-pro-max:design` | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAPI AI), corporate identity progra… |
| `ui-ux-pro-max:design-system` | Token architecture, component specifications, and slide generation. |
| `ui-ux-pro-max:slides` | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. |
| `ui-ux-pro-max:ui-styling` | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based vis… |
| `ui-ux-pro-max:ui-ux-pro-max` | UI/UX design intelligence for web, mobile, and desktop. |

## frontend-design

claude.ai · 켜짐 · 버전 -

> Frontend design skill for UI/UX implementation

**스킬 1개**

| 스킬 | 설명 |
|---|---|
| `frontend-design:frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. |

## engineering

claude.ai · 켜짐 · 버전 1.2.0

> Streamline engineering workflows — standups, code review, architecture decisions, incident response, and technical documentation.

**스킬 10개**

| 스킬 | 설명 |
|---|---|
| `engineering:architecture` | Create or evaluate an architecture decision record (ADR). |
| `engineering:code-review` | Review code changes for security, performance, and correctness. |
| `engineering:debug` | Structured debugging session — reproduce, isolate, diagnose, and fix. |
| `engineering:deploy-checklist` | Pre-deployment verification checklist. |
| `engineering:documentation` | Write and maintain technical documentation. |
| `engineering:incident-response` | Run an incident response workflow — triage, communicate, and write postmortem. |
| `engineering:standup` | Generate a standup update from recent activity. |
| `engineering:system-design` | Design systems, services, and architectures. |
| `engineering:tech-debt` | Identify, categorize, and prioritize technical debt. |
| `engineering:testing-strategy` | Design test strategies and test plans. |

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

> Build a defensible go-to-market plan — positioning, demand engines and a 90-day roadmap — through five gated decisions, with open questions instead of invented data.

**스킬 7개**

| 스킬 | 설명 |
|---|---|
| `gtm-planner:demand-plan` | This skill should be used when the user asks to \"design my demand plan\", \"how do we generate demand\", \"which channels should we invest in\", \"build our d… |
| `gtm-planner:intake` | This skill should be used when the user wants to start a go-to-market plan, says \"start my GTM plan\", \"build a business snapshot\", \"run intake\", \"/gtm-p… |
| `gtm-planner:market-map` | This skill should be used when the user asks to \"map my market\", \"analyze my competitors\", \"who do we really compete with\", \"find positioning gaps\", \"… |
| `gtm-planner:plan` | This skill should be used when the user asks to \"build my GTM plan\", \"run the whole journey\", \"do the full go-to-market plan\", \"take me through all five… |
| `gtm-planner:positioning` | This skill should be used when the user asks to \"define my positioning\", \"choose a category\", \"craft our core promise\", \"build our messaging\", \"/gtm-p… |
| `gtm-planner:roadmap` | This skill should be used when the user asks to \"build my roadmap\", \"turn the plan into actions\", \"what do we do in the next 90 days\", \"prioritize initi… |
| `gtm-planner:setup` | This skill should be used right after installing the Go-to-Market Planner plugin, when the user asks to \"set up gtm planner\", \"configure the planner\", \"co… |

**에이전트 4개**

| 에이전트 | 설명 |
|---|---|
| `benchmark-researcher` | Use this agent during the demand-plan step to research sector and channel benchmarks (CPLs, conversion rates, volumes) with cited sources, enriched by Ahrefs,… |
| `market-researcher` | Use this agent during the market-map step to autonomously research competitors and category dynamics on the public web, enriched with Similarweb traffic data a… |
| `materials-analyst` | Use this agent during GTM intake to analyze the user's own materials — company website, uploaded decks and documents, Google Drive files, and HubSpot funnel da… |
| `plan-qa` | Use this agent at the roadmap step, before consolidating the final GTM Plan, to run a transversal coherence check across all five step outputs — read-only.\n\n… |

**MCP 서버 4개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| hubspot | http | `https://mcp.hubspot.com` |
| notion | http | `https://mcp.notion.com/mcp` |
| similarweb | http | `https://mcp.similarweb.com` |
| ahrefs | http | `https://api.ahrefs.com/mcp/mcp` |

## aws-startup-advisor

claude.ai · 켜짐 · 버전 2.0.1

> Personalized AWS guidance built on patterns from 350,000+ startups—architecture, cost, security, and migration, from day-one account setup to production-ready infrastructure.

**스킬 9개**

| 스킬 | 설명 |
|---|---|
| `aws-startup-advisor:agent-advisor` | Unified entry point for AI-agent work on AWS: evaluate and pick a runtime, generate a full migration plan (for existing workloads), and build an executable POC… |
| `aws-startup-advisor:architect-for-startups` | Startup-tailored AWS architecture advice that adjusts recommendations to the company''s stage (pre-revenue through Series B+), team size, runway, and available… |
| `aws-startup-advisor:gcp-to-aws` | Migrate workloads from Google Cloud Platform to AWS — including AI and agentic workloads regardless of cloud provider. |
| `aws-startup-advisor:heroku-to-aws` | Migrate workloads from Heroku to AWS. |
| `aws-startup-advisor:knowledge-base-for-startups` | AWS Startups reference content — Activate FAQ, credits guide, programs, partner offers, sample architectures, and hundreds of learn articles spanning generativ… |
| `aws-startup-advisor:llm-to-bedrock` | Use when the user wants to migrate code that calls OpenAI, Gemini/Google AI, or the Anthropic API to Amazon Bedrock — a pure model/SDK rewrite. |
| `aws-startup-advisor:prompt-library-for-startups` | AWS-curated copy-paste prompts for AI coding agents (MVP scaffolding, RAG chatbot with Claude on Bedrock, security baseline evaluation, cost anomaly detection,… |
| `aws-startup-advisor:start-building-for-startups` | Interactive discovery + implementation workflow that gathers requirements through picker-based questions (intent, scope, constraints, preferences), scans the c… |
| `aws-startup-advisor:tf-best-practices` | Best-practice authoring guidance AND a read-only policy gate for AWS Terraform generated by a migration skill. |

**에이전트 6개**

| 에이전트 | 설명 |
|---|---|
| `generic-phase-worker-rw` | Generic, phase-AGNOSTIC worker that runs ONE migration phase's work (its fragments + assembler) in an isolated context and writes the phase's artifact(s) to di… |
| `llm2bedrock-code-analyzer` | Analyze the local source repo, detect the AI framework and LLM SDK usage, map all call sites, identify prompts, and enumerate user-visible behavior-deltas for… |
| `llm2bedrock-code-rewriter` | Rewrite LLM SDK calls to Amazon Bedrock on a dedicated git branch, swap dependencies, generate tests, and apply the user-confirmed behavior-delta decisions. |
| `llm2bedrock-log-ingestor` | Parse LLM API logs from the local repo, extract prompt/response pairs, and build a golden dataset (prompts.jsonl) for evaluation. |
| `llm2bedrock-prompt-evaluator` | Run each golden prompt against the target Bedrock model via the pinned uv harness, score with LLM-as-judge, and report a pass rate. |
| `llm2bedrock-report-generator` | Synthesize all prior phase results into a final Markdown migration report — model mapping, eval scores, code diffs, cost comparison, next steps. |

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

> Core skills library for Claude Code: TDD, debugging, collaboration patterns, and proven techniques

**스킬 15개**

| 스킬 | 설명 |
|---|---|
| `superpowers:brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. |
| `superpowers:diagnosing-superpowers` | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't… |
| `superpowers:dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `superpowers:executing-plans` | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool i… |
| `superpowers:finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| `superpowers:receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical… |
| `superpowers:requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `superpowers:subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| `superpowers:systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `superpowers:test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code |
| `superpowers:using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via… |
| `superpowers:using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions |
| `superpowers:verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output b… |
| `superpowers:writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |
| `superpowers:writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |

**훅 1개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| SessionStart | startup¦clear¦compact | "스킬이 조금이라도 맞으면 반드시 불러라"는 지시(using-superpowers 스킬 전문)를 넣는다 | 예 |

## review-council

claude.ai · 켜짐 · 버전 0.2.4

> Six-specialist code review orchestrator (correctness, security, policy/trust-boundary, test-evidence, architecture, interface) for a working tree or pull request diff

**스킬 1개**

| 스킬 | 설명 |
|---|---|
| `review-council:review-council` | Use when the user asks for a thorough, multi-angle code review of a working tree, git diff, or GitHub pull request before merging — dispatches six independent… |

**에이전트 6개**

| 에이전트 | 설명 |
|---|---|
| `architecture-reviewer` | Use this agent to review a git diff or working tree for structural issues — coupling, layering violations, duplicated logic, and abstraction leaks — rather tha… |
| `correctness-reviewer` | Use this agent to review a git diff or working tree for logic errors, edge-case bugs, and incorrect control flow. |
| `interface-reviewer` | Use this agent to review a git diff or working tree for changes to public-facing surfaces — CLI flags, HTTP/API endpoints, output formats, schemas, and error m… |
| `policy-boundary-reviewer` | Use this agent to check a git diff or working tree against the target repository's own trusted policy documents (CLAUDE.md, AGENTS.md, CONTRIBUTING.md, or simi… |
| `security-reviewer` | Use this agent to review a git diff or working tree for security vulnerabilities such as injection, authentication/authorization gaps, credential exposure, and… |
| `test-evidence-reviewer` | Use this agent to check whether a git diff or working tree has adequate test coverage for its behavioral changes, and to verify that any claims of passing chec… |

**훅 1개** (부르지 않아도 정해진 시점마다 실행된다)

| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |
|---|---|---|---|
| PreToolUse | Agent | 저장소의 지침 파일이 기본 브랜치와 다르면 리뷰 에이전트 실행을 막는다 | 아니오 |

## writing-quality

claude.ai · 켜짐 · 버전 0.2.3

> Intent-aware drafting, rewriting, detect-only review, claim boundaries, and final prose validation.

**스킬 4개**

| 스킬 | 설명 |
|---|---|
| `writing-quality:business-writing-intent-enforcer` | Use for memos, specs, PRDs, operating docs, executive summaries, proposals, project plans, and structured business deliverables where reader intent, decisions,… |
| `writing-quality:claim-boundary-checker` | Separates supported, unsupported, uncertain, and non-factual statements in prose. |
| `writing-quality:writing-enforcer` | Applies the complete local 47-pattern Unslop method to ordinary prose while preserving source-backed voice and exact protected material. |
| `writing-quality:writing-quality-router` | Routes writing requests to intent architecture, rewriting, detect-only review, or validation. |

## context7

claude.ai · 켜짐 · 버전 -

> Upstash Context7 MCP server for up-to-date documentation lookup.

**MCP 서버 1개**

| 서버 | 방식 | 연결 대상 |
|---|---|---|
| context7 | http | `https://mcp.context7.com/mcp?client=claude-code-plugin` |

## product-management

claude.ai · 켜짐 · 버전 1.2.0

> Write feature specs, plan roadmaps, and synthesize user research faster.

**스킬 8개**

| 스킬 | 설명 |
|---|---|
| `product-management:competitive-brief` | Create a competitive analysis brief for one or more competitors or a feature area. |
| `product-management:metrics-review` | Review and analyze product metrics with trend analysis and actionable insights. |
| `product-management:product-brainstorming` | Brainstorm product ideas, explore problem spaces, and challenge assumptions as a thinking partner. |
| `product-management:roadmap-update` | Update, create, or reprioritize your product roadmap. |
| `product-management:sprint-planning` | Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan. |
| `product-management:stakeholder-update` | Generate a stakeholder update tailored to audience and cadence. |
| `product-management:synthesize-research` | Synthesize user research from interviews, surveys, and feedback into structured insights. |
| `product-management:write-spec` | Write a feature spec or PRD from a problem statement or feature idea. |

**명령 1개**

| 명령 | 설명 |
|---|---|
| `/brainstorm` | Brainstorm a product idea, problem space, or strategic question with a sharp thinking partner |

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
