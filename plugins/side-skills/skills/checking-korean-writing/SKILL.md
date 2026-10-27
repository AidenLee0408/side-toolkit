---
name: checking-korean-writing
description: Use when Korean prose others will read (README, docs, release notes, landing copy, issue logs) needs a review or cleanup before saving or publishing, or when Korean text reads stiff, telegraphic, or translated. English-only checkers such as writing-enforcer report Korean as clean.
---

# Checking Korean Writing

## Overview
A Korean counterpart to writing-quality. Reads Korean prose for the patterns that make agent-written Korean feel broken: dropped particles, noun strings, noun-ending sentences, clipped coined labels, slash lists, and translationese. Meaning never changes; only wording does.

## Modes
- **DETECT** (default): list findings with line, pattern, and suggested direction. Do not edit.
- **REWRITE**: only when the user asks or approves. Smallest edit that removes the finding.

## Method
1. Decide the reader: public text gets full sentences; internal tables may stay short.
2. Run the scanner for evidence: `python3 scripts/scan_korean.py FILE` (`--json` for machine output). Hits are candidates, not verdicts.
3. Read every hit in context. Drop false positives (short table labels, proper nouns).
4. Read the prose once more yourself for what regex cannot see: wrong particles (`이슈를 생길 때` → `이슈가 생길 때`), mixed 합니다/한다 style, sentences carrying several actions, and coined shorthand terms that a first-time reader would not understand.
5. DETECT: report a table `줄 | 패턴 | 원문 | 고칠 방향`. REWRITE: apply edits, rerun the scanner, report before/after counts.

## Patterns

| 패턴 | 원문 예 | 고친 예 |
|---|---|---|
| 명사 이어 붙이기 | 6개 관점 리뷰 에이전트 | 여섯 관점으로 리뷰하는 에이전트 |
| 명사로 끝나는 본문 | 페이지 방지 / 설계 기록용 | 페이지를 피하려고 / 설계를 기록하려고 |
| 영어 직역 | 처음 판, 미적 지시 | 지금 내용, 디자인 방향 |
| 한 문장에 여러 할 일 | 설치 전 읽고, 설치된 커밋을 확인한다 | 할 일마다 문장을 나눈다 |
| 조사 오류 | 이슈를 생길 때마다 | 이슈가 생길 때마다 |
| 빗금으로 잇기 | 추가 / 수정 / 삭제 | 추가, 수정, 삭제 |
| 번역투 | ~을 통해, ~에 있어서, 되어지다, ~것이 가능하다 | ~로, ~에서, 되다, ~할 수 있다 |
| 줄표 | A — B | 쉼표나 문장 나누기 |
| 줄여 만든 용어 | 꺼 둠, 겹침 지도, 기본 담당, 주력 | 사용 중지, 기능이 겹치는 플러그인, 먼저 쓸 스킬 |
| 명사형(~ㅁ)으로 끝내기 | 설치함, 결제 붙일 때 켬 | 설치했다, 결제를 붙일 때 다시 켠다 |
| 영어 문장 섞기 | (한국어 문서 안에) Review code changes for security. | 코드 변경의 보안을 리뷰한다. |

## Boundaries
- Keep code, commands, paths, links, tables' structure, quotes, and frontmatter unchanged.
- Do not add facts, claims, or tone the source lacks.
- Table cells may stay short, but write what something does with a verb.
- A Korean document is public prose no matter how it was produced. Generated tables and descriptions copied from upstream must be Korean too.

## Common Mistakes
- Trusting a clean scanner run. It cannot see particle errors or style mixing; step 4 is required.
- Rewriting whole paragraphs to fix one pattern. Change the phrase, not the paragraph.
- Turning every table cell into a sentence. Only public prose needs full sentences.
