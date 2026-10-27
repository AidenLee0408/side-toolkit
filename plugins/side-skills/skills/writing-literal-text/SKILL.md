---
name: writing-literal-text
description: Use when writing, reviewing, or naming any text a person will read — product screens, buttons, menus, notifications, error and security warnings, README files, documents, headings, table labels, status names, feature and setting names — in Korean or English, or when suggesting names for anything people will see.
---

# Writing Literal Text

## Overview
Text people read names exactly what it refers to. No metaphor, personification, abstraction, or coined shorthand. A first-time reader should understand it without interpreting it. This applies wherever a person reads the text: product screens, documents, README files, tables, and labels alike.

## Recipe
For each name, label, or sentence, write:
1. **What it is**: the actual object, data, or state (주소, 결제 금액, API key, 사용 중지).
2. **What happens**: the actual action and its result, when there is one (삭제하면 되돌릴 수 없습니다 / This deletes the file permanently).
3. **Nothing else**: no character, mood, story, or invented term.

Then ask: "Would a first-time reader know what this is without guessing?" If not, name the thing more literally.

## Examples

**Product screens**

| 쓰지 않는다 | 쓴다 | 이유 |
|---|---|---|
| 이 페이지의 주인: example.com | 현재 접속 중인 페이지 주소: example.com | 의인화. 실제로는 주소다 |
| 마법 링크로 로그인 | 이메일로 받은 로그인 링크 | 비유 |
| 스마트 정리 | 30일 지난 파일 삭제 | 추상어. 실제 동작을 쓴다 |
| 비서가 정리했어요 | 자동으로 3개 항목을 분류했습니다 | 의인화 |
| Your vault is locked | Encrypted notes are locked. Enter your password to open them. | 비유 (vault) |
| Something went wrong | Payment failed: card was declined | 추상어. 무엇이 왜 실패했는지 쓴다 |
| Danger zone | Delete account | 비유 |

**Documents, README, tables**

| 쓰지 않는다 | 쓴다 | 이유 |
|---|---|---|
| 꺼 둠 | 사용 중지 | 줄여 만든 상태 이름 |
| 겹침 지도 | 기능이 겹치는 스킬 | 비유 (지도) |
| 주력, 기본 담당 | 먼저 쓰는 스킬 | 뜻이 모호한 말 |
| 처음 판 | 지금 기준 (아직 가설) | 영어 직역 |
| Source of truth | 원본 | 관용구 |
| Battle-tested | 실제 프로젝트에서 3번 써 봤다 | 비유. 근거를 쓴다 |

## Names for features, settings, sections, and statuses
- Name by what it does, holds, or means: `자동 백업`, `결제 내역`, `Export to CSV`, `사용 중지`.
- Do not coin a new term when a plain phrase exists. If a status needs a short name, define it once in a table.
- When suggesting names, give the literal name first. A branded name can only sit next to it, and only with the owner's approval.

## Warnings and errors
- Say what happened, why, and what the reader can do, in that order.
- Never soften a security or data-loss warning with a friendly metaphor.

## Exceptions
Brand slogans (a tagline on a landing page) may use figurative language only when the owner approves. Everything else follows the recipe, including marketing copy outside the slogan.

## Related skills
- Korean grammar and flow (particles, noun strings, translationese): `checking-korean-writing`.
- This skill decides **what to call things**; that one checks **how the Korean sentence reads**. Use both on Korean documents.

## Common Mistakes
- Picking a "friendly" name that hides the action (`정리하기` for a permanent delete).
- Describing the spirit instead of the result (`Peace of mind` instead of `Daily backup at 3 AM`).
- Treating internal-looking text (tables, status names, generated docs) as exempt. If a person reads it, it follows the recipe.
- Keeping a vague error because the cause is unknown. Say what is known: `서버에 연결하지 못했습니다. 잠시 후 다시 시도하세요.`
