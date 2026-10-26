# side-toolkit

1인 사이드 프로젝트에서 쓰는 Claude Code 플러그인과 스킬을 관리하는 저장소입니다. 무엇을 설치했고 왜 설치했는지, 작업마다 어떤 스킬을 먼저 쓰는지, 실제 프로젝트에서 써 보니 어땠는지를 기록합니다.

## 구성

| 경로 | 내용 |
|---|---|
| [docs/Skills.md](docs/Skills.md) | 설치한 플러그인과 스킬 목록, 설치 이유, 상태, 겹침 지도, 오픈소스 검토 기록 |
| [docs/Skill Playbook.md](docs/Skill%20Playbook.md) | 작업별 스킬 우선순위, 서로 부딪히는 조합, 스킬을 쓰지 않아도 되는 경우 |
| [reports/](reports/) | 프로젝트별 스킬 사용 리포트. 양식은 [_Template.md](reports/_Template.md) |
| [scripts/skill-usage.py](scripts/skill-usage.py) | Claude Code 대화 기록에서 스킬, 슬래시 명령, 서브에이전트, MCP 사용 횟수를 집계 |
| [scripts/sync-from-hub.sh](scripts/sync-from-hub.sh) | 원본(개인 운영 허브)에서 문서를 복사 |

## 운영 방식

1. 원본은 개인 운영 허브에 있습니다. 허브에서 문서를 고친 뒤 `scripts/sync-from-hub.sh`로 복사하고 커밋합니다. 이 저장소에서 문서를 직접 고치지 않습니다.
2. 새 플러그인은 설치 전에 설정 파일, 훅, 외부 통신 코드를 읽고, 검토한 커밋을 기록합니다.
3. 프로젝트를 마치면 사용 횟수를 집계하고 리포트를 씁니다.
4. 같은 결과가 두 번 이상 나오면 Playbook의 근거를 "가설"에서 해당 리포트로 바꿉니다.

문서 안의 `[[Integrations]]`, `[[DEC-001 ...]]` 같은 링크는 허브에만 있는 문서를 가리킵니다.

## 사용 횟수 집계

```bash
python3 scripts/skill-usage.py --root ~/SideProjects --since 2026-11-01
```

`--root` 아래에서 실행된 세션만 셉니다. 훅으로만 작동하는 플러그인은 집계되지 않습니다.

## 앞으로

직접 만든 스킬이 쌓이면 이 저장소를 Claude Code 플러그인 마켓플레이스로 구성해 어느 프로젝트에서든 설치할 수 있게 할 계획입니다.
