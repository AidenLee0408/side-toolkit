---
type: changelog
status: proposed
owner: Founder
last_reviewed: 2026-10-27
---

# Plugin Changelog

플러그인과 그 안의 스킬, 훅, MCP에 관한 결정이 바뀔 때마다 **맨 아래에 한 줄씩 추가**한다. 이미 쓴 줄은 내용을 고치거나 지우지 않는다. 이 문서에는 "언제, 무엇이, 왜 바뀌었나"만 남긴다. 문제 기록은 [Plugin Issues](Plugin%20Issues.md), 지금 상태는 [Plugins](Plugins.md), 지금 우선순위는 [Plugin Playbook](Plugin%20Playbook.md)에 있다. (2026-10-27에 문서 전체의 표현만 한 번 다듬었다.)

- 변경 종류: 설치, 삭제, 사용 중지, 다시 켜기, 상태 변경, 우선순위 지정, 우선순위 변경, 후순위로 내림, 제외, 규칙
- 근거: Plugin Issues 번호, 리포트 이름, 창업자 결정, 또는 `가설`
- 결정한 사람: 창업자 또는 에이전트 제안. 제외와 삭제는 창업자만 결정한다.

| # | 날짜 | 대상 | 변경 종류 | 이전 → 이후 | 이유 | 근거 | 결정한 사람 |
|---|---|---|---|---|---|---|---|
| 1 | 2026-10-27 | caveman, ui-ux-pro-max, taste-skill, impeccable | 설치 | 없음 → 시험 사용 | 토큰 절약, 디자인 품질 | 창업자 결정 | 창업자 |
| 2 | 2026-10-27 | marketing-skills, ponytail | 설치 | 없음 → 시험 사용 (ponytail 기본 단계 lite) | 홍보 실행, 과설계 방지 | 창업자 결정 | 창업자 |
| 3 | 2026-10-27 | code-simplifier, ECC, alirezarezvani/claude-skills, rampstackco/claude-skills, pm-skills, claude-mem, context-mode, ralph-loop | 제외 | 후보 → 제외 | 기능 중복, 지나치게 큰 규모, 라이선스, 위험 | [Plugins](Plugins.md)의 "검토 후 제외" 표 | 창업자 |
| 4 | 2026-10-27 | claude-seo 또는 geo-seo-claude, context7 로그인 | 상태 변경 | 후보 → 보류 | 랜딩 페이지와 코딩을 시작하기 전이라서 | 가설 | 창업자 |
| 5 | 2026-10-27 | stripe, supabase, cloudflare, posthog, playwright, marketing(Anthropic) | 설치 | 미설치 → 시험 사용 | 결제, 배포, 분석, 테스트 준비 | Plugin Issues #1 | 창업자 |
| 6 | 2026-10-27 | posthog, cloudflare, stripe | 사용 중지 | 사용 중 → 사용 중지 | 스킬이 너무 많고, 지금 단계에는 필요 없다 | Plugin Issues #5 | 창업자 |
| 7 | 2026-10-27 | Plugin Playbook 작업별 우선순위 16개 | 우선순위 지정 | 없음 → 첫 기준 (랜딩 taste-skill, 제품 UI ui-ux-pro-max, 마케팅 실행 marketing-skills, 과설계 방지 ponytail 등) | 겹치는 플러그인 정리 | 가설 | 에이전트 제안 |
| 8 | 2026-10-27 | 외부 서비스 연결 | 규칙 | 없음 → 공식 플러그인이 있으면 플러그인, 없으면 커넥터 | 같은 서비스를 두 번 연결하지 않으려고 | DEC-001 | 창업자 |
| 9 | 2026-10-27 | Caveman Cloud 스킬 (`caveman-setup`, `caveman-compress`) | 규칙 | 사용 가능 → 사용 금지 | 외부로 데이터를 보낸다 | Plugin Issues #3 | 에이전트 제안 |
| 10 | 2026-10-27 | 공개 문서 문장 | 규칙 | 없음 → UI Wording.md에 공개 문서 규칙 추가, 공개 전 writing-quality 점검, 주간 반영에 문장 점검 단계 추가 | 초안 문장이 어색해 전체를 다시 다듬었다 | 창업자 결정 | 창업자 |
| 11 | 2026-10-27 | fluent-korean, humanize-korean (im-not-ai) | 설치 | 없음 → 시험 사용 | 한국어 문체 개선 | Plugin Issues #9 | 창업자 |
| 12 | 2026-10-27 | 한국어 공개 문서 점검 | 우선순위 변경 | writing-enforcer → fluent-korean(쓸 때) + humanize-korean(공개 전 점검) | writing-enforcer가 한국어를 검사하지 못한다 | Plugin Issues #9 | 창업자 |
| 13 | 2026-10-27 | writing-enforcer | 상태 변경 | 공개 문서 점검 → 영어 문구 점검 전용 | 패턴 목록이 영어 기준이다 | Plugin Issues #9 | 창업자 |
| 14 | 2026-10-27 | fluent-korean, humanize-korean | 상태 변경 | 모든 프로젝트 → 허브(프로젝트 범위)와 제품 저장소에서만 켬. 허브의 출력 스타일을 fluent-korean으로 지정 | 문서 작업과 제품에서만 쓰기로 했다 | 창업자 결정 | 창업자 |
| 15 | 2026-10-27 | writing-concise-korean, checking-korean-writing (side-skills) | 설치 | 없음 → 시험 사용 (자체 제작 스킬, 모든 프로젝트) | 한국어판 caveman과 한국어판 writing-quality | Plugin Issues #9, #10 | 창업자 |
| 16 | 2026-10-27 | 한국어 공개 문서 점검 | 우선순위 변경 | humanize-korean → checking-korean-writing (humanize-korean은 긴 글 보조) | 우리 규칙에 맞춘 점검과 스캐너가 있다 | 가설 | 에이전트 제안 |
| 17 | 2026-10-27 | 문서 용어 | 규칙 | 자작 스킬 → 자체 제작 스킬 | 용어 정리 | 창업자 결정 | 창업자 |
| 18 | 2026-10-27 | 문서 용어 | 규칙 | 시험 중 → 시험 사용, 꺼 둠 → 사용 중지, 겹침 지도 → 기능이 겹치는 플러그인, 기본 담당·주력·1순위 → 먼저 쓸 스킬 | 줄여 만든 어색한 용어 정리 | 창업자 결정, Plugin Issues #13 | 창업자 |
| 19 | 2026-10-27 | 스킬 충돌 검사 | 규칙 | 없음 → 설치·업데이트 때와 월간 재검토 때 `plugin-audit.py conflicts`로 검사하고, 실제 충돌은 Playbook에 반영 | 플러그인 단위가 아니라 스킬 단위로 부딪힌다 | 창업자 결정 | 창업자 |
| 20 | 2026-10-27 | 코드 리뷰, competitive-brief, seo-audit, 브레인스토밍, 고객 조사 | 우선순위 지정 | 없음 → Playbook 충돌 표에 먼저 쓸 스킬 지정 | 첫 충돌 검사 결과 | 2026-10-27 충돌 검사 | 에이전트 제안 |
| 21 | 2026-10-27 | aws-startup-advisor | 상태 변경 | 보류 → 시험 사용 | 우선 써 보면서 세션 시작 훅의 영향을 지켜보기로 했다 | 창업자 결정, Plugin Issues #15 | 창업자 |
| 22 | 2026-10-27 | 관리 범위 | 규칙 | 스킬 중심 → 플러그인과 그 구성 요소(스킬, 명령, 에이전트, 훅, MCP, 출력 스타일) 전체. 문서 이름을 Skill에서 Plugin으로 변경 | 훅과 MCP가 관리에서 빠져 있었다 | 창업자 결정 | 창업자 |
| 23 | 2026-10-27 | 검토 절차 | 규칙 | 없음 → Plugin Review 체크리스트, plugin-reviews.json 검토 기록, 주간 리뷰 때 drift 확인 | 검토 항목이 매번 달랐다 | 창업자 결정 | 창업자 |
| 24 | 2026-10-27 | 플러그인 운영 문서 | 규칙 | CLAUDE.md에 흩어진 운영 규칙 → Plugin Playbook "5. 운영 규칙", "6. 주간 점검"으로 모음 | 허브 지침이 무거워지고 주간 할 일이 흩어져 있었다 | 창업자 결정 (문서 점검 13건) | 창업자 |
| 25 | 2026-10-27 | skill-usage.py | 규칙 | 별도 스크립트 → `plugin-audit.py usage`로 합침. `summary` 추가 | 점검 도구를 하나로 모음 | 창업자 결정 (문서 점검 13건) | 창업자 |
| 26 | 2026-10-27 | side-skills | 상태 변경 | 0.1.2 → 0.1.3 (스캐너가 "켜 둔", "켜짐", "꺼짐"을 잘못 걸러 내지 않게 함) | 오탐 정리 | 창업자 결정 (문서 점검 13건) | 창업자 |
| 27 | 2026-10-27 | DEC-001 | 상태 변경 | proposed → accepted | 창업자가 결정한 내용이다 | 창업자 결정 | 창업자 |
| 28 | 2026-10-27 | Plugin Playbook 1번, 2번 표 | 규칙 | 플러그인 단위로 적힌 줄 → `플러그인:스킬`, `플러그인 (훅: 시점)`, `플러그인 (출력 스타일)` 단위로 나눠 적음. 2번 표를 개발, 디자인, 마케팅, 글, 세션 시작으로 묶음 | 실제로 부딪히는 것은 플러그인이 아니라 스킬과 훅이다 | 창업자 결정 | 창업자 |
