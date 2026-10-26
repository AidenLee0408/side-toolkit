# side-toolkit

> 1인 개발자가 Claude Code로 사이드 프로젝트를 만들면서 쓰는 **플러그인과 스킬 기록**입니다.
> 어떤 플러그인을 왜 골랐는지, 작업별로 어떤 스킬을 쓰는지, 실제로 써 보니 어땠는지 정리합니다.

**English:** Notes from a solo developer on the Claude Code plugins and skills used to build side projects: what was chosen and why, which skill fits each task, and how each one held up in real work. The docs are written in Korean.

<br>

## 한눈에 보기

| 항목 | 지금 |
|---|---|
| 켜 둔 플러그인 | 18개 (claude.ai 9 · 로컬 9) |
| 꺼 둔 플러그인 | 3개 (posthog, cloudflare, stripe: 필요할 때 켬) |
| 검토 후 제외 | 8개 |
| 작업별 사용 기준 | 16개 작업 |
| 기록된 변경 / 이슈 | [Changelog](docs/Skill%20Changelog.md) · [Issues](docs/Skill%20Issues.md) |

마지막 갱신: 2026-10-27 (매주 갱신)

<br>

## 문서

| 문서 | 이럴 때 보세요 |
|---|---|
| 📦 [**Skills**](docs/Skills.md) | 어떤 플러그인을 왜 설치했는지, 지금 상태와 겹치는 것이 궁금할 때 |
| 🧭 [**Skill Playbook**](docs/Skill%20Playbook.md) | "이 작업엔 어떤 스킬을 먼저 쓰지?" 할 때 |
| 📝 [**Skill Changelog**](docs/Skill%20Changelog.md) | 무엇이 언제 왜 바뀌었는지 볼 때 (설치, 끄기, 1순위 변경 등) |
| ⚠️ [**Skill Issues**](docs/Skill%20Issues.md) | 어떤 문제가 있었고 어떻게 처리했는지 볼 때 |
| 📊 [**Reports**](reports/) | 실제 프로젝트에서 써 본 결과. 양식은 [_Template](reports/_Template.md) |

<br>

## 영역별 주력 스킬

한 작업에는 주력 스킬을 하나만 둡니다. 자세한 기준과 근거는 [Playbook](docs/Skill%20Playbook.md)에 있습니다.

| 영역 | 주력 | 비교 중 |
|---|---|---|
| 개발 절차 | [superpowers](https://github.com/obra/superpowers) | ponytail, caveman |
| 과설계 방지 | [ponytail](https://github.com/DietrichGebert/ponytail) (lite) | caveman `lean-build` |
| 랜딩 페이지 디자인 | [taste-skill](https://github.com/Leonxlnx/taste-skill) | frontend-design, impeccable, ui-ux-pro-max |
| 제품 UI 디자인 | [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | frontend-design |
| UI 점검·다듬기 | [impeccable](https://github.com/pbakaus/impeccable) | — |
| 시장 전략 | gtm-planner | product-management |
| 마케팅 실행 | [marketingskills](https://github.com/coreyhaines31/marketingskills) | marketing (Anthropic) |
| 코드 리뷰 | `/code-review` | review-council |

<br>

## 운영 방식

```mermaid
flowchart LR
    A[후보 발견] --> B[코드 검토<br/>훅 · 외부 통신 · 라이선스]
    B -->|통과| C[설치<br/>시험 중]
    B -->|탈락| X[제외]
    C --> D[프로젝트에서 사용]
    D --> E[이슈 기록<br/>Skill Issues]
    D --> F[리포트<br/>Reports]
    E --> G[결정 변경<br/>Skill Changelog]
    F --> G
    G --> H[기준 갱신<br/>Skills · Playbook]
    H --> D
```

**규칙**

1. **설치 전 검토.** 오픈소스는 설정 파일, 훅, 외부로 데이터를 보내는 코드, 라이선스를 읽고 검토한 커밋을 기록합니다.
2. **한 서비스에 연결 하나.** 공식 플러그인이 있으면 플러그인, 없으면 커넥터(MCP)를 씁니다.
3. **많이 설치하지 않기.** 스킬이 많을수록 토큰을 쓰고 엉뚱한 스킬이 불립니다. 지금 단계에 필요 없는 건 꺼 둡니다.
4. **가설은 가설로 표시.** Playbook의 기준은 실제 리포트가 두 번 이상 뒷받침할 때까지 `가설`입니다.
5. **기록은 덧붙이기만.** Changelog와 Issues는 한 줄씩 아래로 쌓고, 지난 줄은 고치지 않습니다.

<br>

## 스킬 사용 횟수 집계

Claude Code 대화 기록(`~/.claude/projects`)에서 스킬, 슬래시 명령, 서브에이전트, MCP 사용 횟수를 셉니다.

```bash
python3 scripts/skill-usage.py --root ~/SideProjects --since 2026-11-01
```

- `--root` 아래에서 실행된 세션만 셉니다. 다른 작업 기록은 섞이지 않습니다.
- 훅으로만 작동하는 플러그인(caveman, ponytail, impeccable의 훅)은 집계되지 않습니다.

<br>

## 내 환경에 가져다 쓰기

- 플러그인 목록과 검토 메모는 [Skills](docs/Skills.md)의 표를 그대로 참고하면 됩니다. 설치 명령은 각 저장소 README를 따르세요.
- 리포트 양식([_Template](reports/_Template.md))과 집계 스크립트는 다른 프로젝트에서도 그대로 쓸 수 있습니다.
- 문서 안의 "(운영 허브 문서)" 표시는 공개하지 않은 개인 운영 문서를 가리킵니다.

<br>

## 이 저장소가 갱신되는 방식

원본은 개인 운영 허브에 있고, 주 1회 `scripts/sync-from-hub.sh`로 이 저장소에 반영합니다. 이 저장소에서 문서를 직접 고치지 않습니다.

앞으로 직접 만든 스킬이 쌓이면 이 저장소를 Claude Code 플러그인 마켓플레이스로 구성할 계획입니다.
