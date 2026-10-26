---
type: changelog
status: proposed
owner: Founder
last_reviewed: 2026-10-27
---

# Skill Changelog

스킬이나 플러그인에 관한 결정이 바뀔 때마다 **맨 아래에 한 줄씩 추가**한다. 이미 쓴 줄은 고치거나 지우지 않는다. 이 문서에는 "언제, 무엇이, 왜 바뀌었나"만 남긴다. 문제 기록은 [Skill Issues](Skill%20Issues.md), 지금 상태는 [Skills](Skills.md), 지금 우선순위는 [Skill Playbook](Skill%20Playbook.md)에 있다.

- 변경 종류: 설치 / 삭제 / 끄기 / 켜기 / 상태 변경 / 1순위 지정 / 1순위 변경 / 후순위 / 제외 / 규칙
- 근거: Skill Issues 번호, 리포트 이름, 창업자 결정, 또는 `가설`
- 결정자: 창업자 / 에이전트 제안. 제외·삭제는 창업자만 결정한다.

| # | 날짜 | 대상 | 변경 종류 | 이전 → 이후 | 이유 | 근거 | 결정자 |
|---|---|---|---|---|---|---|---|
| 1 | 2026-10-27 | caveman, ui-ux-pro-max, taste-skill, impeccable | 설치 | 없음 → 시험 중 | 토큰 절약, 디자인 품질 | 창업자 결정 | 창업자 |
| 2 | 2026-10-27 | marketing-skills, ponytail | 설치 | 없음 → 시험 중 (ponytail 기본 lite) | 홍보 실행, 과설계 방지 | 창업자 결정 | 창업자 |
| 3 | 2026-10-27 | code-simplifier, ECC, alirezarezvani/claude-skills, rampstackco/claude-skills, pm-skills, claude-mem, context-mode, ralph-loop | 제외 | 후보 → 제외 | 중복, 규모 과다, 라이선스, 위험 | [Skills](Skills.md) 검토 후 제외 표 | 창업자 |
| 4 | 2026-10-27 | claude-seo / geo-seo-claude, context7 로그인 | 상태 변경 | 후보 → 보류 | 랜딩 페이지·코딩 시작 전 | 가설 | 창업자 |
| 5 | 2026-10-27 | stripe, supabase, cloudflare, posthog, playwright, marketing(Anthropic) | 설치 | 미설치 → 시험 중 | 결제·배포·분석·테스트 준비 | Skill Issues #1 | 창업자 |
| 6 | 2026-10-27 | posthog, cloudflare, stripe | 끄기 | 켜짐 → 꺼 둠 | 스킬 수 과다, 지금 단계에 불필요 | Skill Issues #5 | 창업자 |
| 7 | 2026-10-27 | Skill Playbook 작업별 1순위 16개 | 1순위 지정 | 없음 → 첫 판 (랜딩 taste-skill, 제품 UI ui-ux-pro-max, 마케팅 실행 marketing-skills, 과설계 방지 ponytail 등) | 겹침 정리 | 가설 | 에이전트 제안 |
| 8 | 2026-10-27 | 외부 서비스 연결 | 규칙 | 없음 → 플러그인 우선, 없으면 커넥터 | 중복 연결 방지 | DEC-001 | 창업자 |
| 9 | 2026-10-27 | Caveman Cloud 스킬 (`caveman-setup`, `caveman-compress`) | 규칙 | 사용 가능 → 사용 금지 | 외부 전송 | Skill Issues #3 | 에이전트 제안 |
