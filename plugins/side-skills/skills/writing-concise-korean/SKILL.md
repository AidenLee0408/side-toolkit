---
name: writing-concise-korean
description: Use when answering or writing in Korean while a brevity mode (caveman, terse, "짧게") is active, or when Korean replies come out as telegraphic noun fragments with missing particles and endings.
---

# Writing Concise Korean

## Overview
A Korean counterpart to caveman. Short Korean is made by cutting **content**, not by cutting **grammar**. English brevity drops articles and verbs; doing the same in Korean drops particles and endings and breaks the sentence.

## Output shape
Each Korean reply is:
1. **결론 한 문장.** First sentence answers the question.
2. **필요한 근거만.** Bullets or a small table. Each bullet is a complete short sentence that ends with a verb, never with a bare noun or `~함`/`~됨`.
3. **남은 일 한 줄** only if something is pending.

Every sentence keeps its particles (은/는/이/가/을/를/에/로) and ends with a verb ending (`~다`, `~요`, `~니다`). Pick one style per reply: 합니다체 for the user, 한다체 for internal docs.

## What to cut
| 자르는 것 | 예 |
|---|---|
| 인사, 맞장구, 반복 | "좋은 질문입니다", "말씀하신 대로" |
| 했던 일 서술 | "먼저 파일을 읽어 보았습니다" |
| 같은 말 두 번 | 표와 본문에 같은 내용 |
| 불필요한 수식어 | "매우", "정말", "기본적으로" |

## What never to cut
| 남기는 것 | 틀린 예 | 맞는 예 |
|---|---|---|
| 조사 | 설정 파일 수정 완료 | 설정 파일을 고쳤습니다 |
| 어미 | 훅 없음, 외부 전송 없음 | 훅이 없고 외부로 보내는 것도 없습니다 |
| 주어가 바뀔 때 주어 | 실패. 재시도 필요 | 빌드가 실패했습니다. 다시 실행해야 합니다 |
| 기술 용어, 코드, 경로, 숫자 | — | 그대로 둔다 |

## Quick check before sending
- Does any line end in a bare noun (`방지`, `완료`, `필요`, `확인`)? Add the verb.
- Are three or more nouns in a row without a particle? Split with particles.
- Is there a slash list in prose? Use commas.

## Common Mistakes
- Treating caveman's English rules as Korean rules. Korean needs its particles to stay readable.
- Making the reply short by deleting the reason. Keep one reason; delete the narration.
- Switching between 합니다 and 한다 inside one reply.
