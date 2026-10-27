---
name: writing-literal-ui-copy
description: Use when writing, reviewing, or naming text that appears in a product's interface — buttons, labels, menu items, feature names, empty states, notifications, error and security warnings — in Korean or English, or when suggesting names for features, screens, or settings.
---

# Writing Literal UI Copy

## Overview
Interface text names exactly what the user is looking at or about to do. No metaphor, personification, or abstraction. A reader should understand it without interpreting it. This matters most in warnings, where a vague phrase leads to a wrong decision.

## Recipe
For each piece of UI text, write:
1. **What it is**: the actual object or data (주소, 결제 금액, API key, last sync time).
2. **What happens**: the actual action and its result, when there is one (삭제하면 되돌릴 수 없습니다 / This deletes the file permanently).
3. **Nothing else**: no character, mood, or story.

Then ask: "Would a first-time user know what this is without guessing?" If not, name the thing more literally.

## Examples

| 쓰지 않는다 | 쓴다 | 이유 |
|---|---|---|
| 이 페이지의 주인: example.com | 현재 접속 중인 페이지 주소: example.com | 의인화. 실제로는 주소다 |
| 마법 링크로 로그인 | 이메일로 받은 로그인 링크 | 비유 |
| 스마트 정리 | 30일 지난 파일 삭제 | 추상어. 실제 동작을 쓴다 |
| 비서가 정리했어요 | 자동으로 3개 항목을 분류했습니다 | 의인화 |
| Your vault is locked | Encrypted notes are locked. Enter your password to open them. | 비유 (vault) |
| Something went wrong | Payment failed: card was declined | 추상어. 무엇이 왜 실패했는지 쓴다 |
| Danger zone | Delete account | 비유. 무엇을 하는 영역인지 쓴다 |
| Boost | Show this post to more users for 7 days | 추상어 |

## Feature and setting names
- Name by what it does or holds: `자동 백업`, `결제 내역`, `Export to CSV`.
- When suggesting names, give the literal name first. A branded name can only be added next to it, and only with the owner's approval.

## Warnings and errors
- Say what happened, why, and what the user can do, in that order.
- Never soften a security or data-loss warning with a friendly metaphor.

## Exceptions
Brand slogans on marketing pages may use figurative language when the product owner approves. Everything inside the product interface follows the recipe.

## Common Mistakes
- Picking a "friendly" name that hides the action (`정리하기` for a permanent delete).
- Describing the feature's spirit instead of its result (`Peace of mind` instead of `Daily backup at 3 AM`).
- Keeping a vague error because the cause is unknown. Say what is known: `서버에 연결하지 못했습니다. 잠시 후 다시 시도하세요.`
