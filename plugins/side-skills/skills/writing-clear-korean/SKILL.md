---
name: writing-clear-korean
description: Use when writing, reviewing, or naming any text a person will read — README files, documents, issue logs, tables, headings, status names, product screens, buttons, notifications, error and security warnings, feature names — especially in Korean, or when Korean text reads stiff, telegraphic, translated, or full of coined terms. English-only checkers such as writing-enforcer report Korean as clean.
---

# Writing Clear Korean

## Overview
Text people read must be understood without guessing. Two steps: name things literally (any language), then check that the Korean sentences read naturally. A document is "for people" when a person reads it, no matter how it was produced: generated tables and descriptions copied from upstream count too. Meaning never changes; only wording does.

## Modes
- **DETECT** (default): report findings as `줄 | 패턴 | 원문 | 고칠 방향`. Do not edit.
- **REWRITE**: only when the user asks or approves. Smallest edit that removes each finding, then rerun the scanner and report before/after counts.

## Step 1. Name things literally (Korean and English)
For each name, label, or sentence, write what it actually is and what actually happens. No metaphor, personification, abstraction, or coined shorthand. Ask: "Would a first-time reader know this without guessing?"

| 쓰지 않는다 | 쓴다 | 이유 |
|---|---|---|
| 이 페이지의 주인: example.com | 현재 접속 중인 페이지 주소: example.com | 의인화 |
| 스마트 정리 | 30일 지난 파일 삭제 | 추상어. 실제 동작을 쓴다 |
| Something went wrong | Payment failed: card was declined | 무엇이 왜 실패했는지 쓴다 |
| Danger zone | Delete account | 비유 |
| 꺼 둠 | 사용 중지 | 줄여 만든 상태 이름 |
| 겹침 지도, 주력 | 기능이 겹치는 스킬, 먼저 쓰는 스킬 | 비유, 모호한 말 |

- Warnings and errors: what happened, why, what the reader can do. Never soften security or data-loss warnings.
- Feature, setting, and status names: name by what it does or means. Give the literal name first when suggesting names.
- Exception: a brand slogan the owner approved.

## Step 2. Check Korean sentences
1. Run the scanner: `python3 scripts/scan_korean.py FILE` (`--json` for machine output). Hits are candidates, not verdicts.
2. Read every hit in context. Drop false positives (short table labels, proper nouns, quoted examples).
3. Read the text once more for what regex cannot see: wrong particles, mixed 합니다/한다 style, sentences carrying several actions.

| 패턴 | 원문 예 | 고친 예 |
|---|---|---|
| 명사 이어 붙이기 | 6개 관점 리뷰 에이전트 | 여섯 관점으로 리뷰하는 에이전트 |
| 명사로 끝나는 본문 | 페이지 방지, 설계 기록용 | 페이지를 피하려고, 설계를 기록하려고 |
| 명사형(~ㅁ)으로 끝내기 | 결제 붙일 때 켬 | 결제를 붙일 때 다시 켠다 |
| 영어 직역 | 처음 판, 미적 지시 | 지금 기준, 디자인 방향 |
| 영어 문장 섞기 | Review code changes for security. | 코드 변경의 보안을 리뷰한다. |
| 한 문장에 여러 할 일 | 설치 전 읽고, 설치된 커밋을 확인한다 | 할 일마다 문장을 나눈다 |
| 조사 오류 | 이슈를 생길 때마다 | 이슈가 생길 때마다 |
| 빗금으로 잇기 | 추가 / 수정 / 삭제 | 추가, 수정, 삭제 |
| 번역투 | ~을 통해, ~에 있어서, 되어지다 | ~로, ~에서, 되다 |
| 줄표 | A — B | 쉼표나 문장 나누기 |

## Boundaries
- Keep code, commands, paths, links, table structure, quotes, and frontmatter unchanged. Proper nouns stay as they are.
- Do not add facts, claims, or tone the source lacks.
- Table cells may stay short, but say what something does with a verb.

## Common Mistakes
- Treating generated or internal-looking text (tables, status names, copied descriptions) as exempt.
- Trusting a clean scanner run. It cannot see particle errors, style mixing, or new coined terms.
- Rewriting a whole paragraph to fix one phrase.
