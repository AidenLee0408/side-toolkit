#!/usr/bin/env python3
"""Audit the Claude Code plugins installed on this machine.

A plugin can bundle skills, slash commands, agents, hooks, MCP servers and
output styles. This script lists all of them so the parts that run without
being asked (hooks) or talk to outside services (MCP) are never missed.

Subcommands:
  inventory  every plugin and what is inside it (default)
  conflicts  candidates for skills, hooks and output styles that clash
  drift      installed plugins whose commit or version differs from the review record
  scope      which plugins are on in each project folder

Sources:
  - local plugins: ~/.claude/plugins/installed_plugins.json and enabledPlugins in
    ~/.claude/settings.json and <project>/.claude/settings*.json
  - claude.ai plugins: ~/Library/Application Support/Claude/local-agent-mode-sessions/*/*/rpm/plugin_*
Built-in skills and commands (/code-review, /simplify) are not on disk and are not listed.

Usage:
  python3 scripts/plugin-audit.py inventory --project ~/SideProjects/hub
  python3 scripts/plugin-audit.py conflicts --project ~/SideProjects/hub
  python3 scripts/plugin-audit.py drift --reviews plugin-reviews.json
  python3 scripts/plugin-audit.py scope --projects ~/SideProjects/hub ~/SideProjects/products/foo ~
"""
import argparse
import glob
import itertools
import json
import os
import re

HOME = os.path.expanduser("~")
CLAUDE_AI = os.path.join(HOME, "Library/Application Support/Claude/local-agent-mode-sessions/*/*/rpm/plugin_*")
INJECT_EVENTS = {"SessionStart", "UserPromptSubmit", "SubagentStart"}
STOP = set("""
use when user wants asks with this that from into your their they them also only
skill skills agent agents claude code about after before each every have more most
such than then there these those what when where which while will would could should
mentions mention including include includes other others work works working using
""".split())

# Jobs that several plugins tend to claim, matched against a skill's name and the start of its description.
TOPICS = {
    "코드 리뷰": ["code review", "review the diff", "review this pr", "pull request", "reviewing code", "diff review"],
    "디버깅": ["debug", "debugging", "root cause", "stack trace"],
    "브레인스토밍": ["brainstorm", "brainstorming"],
    "명세·로드맵": ["spec", "prd", "roadmap", "implementation plan"],
    "테스트": ["tdd", "test strategy", "test plan", "unit test", "e2e"],
    "경쟁 분석": ["competitor", "competitive"],
    "SEO": ["seo"],
    "디자인·UI": ["frontend", "ui design", "ux", "landing page", "user interface", "typography", "design system"],
    "글 다듬기": ["copywriting", "copy edit", "copy-edit", "humanize", "prose", "ai writing", "ai tells", "윤문", "문체", "한국어"],
    "마케팅 계획": ["campaign", "marketing plan", "go-to-market", "gtm"],
    "배포": ["deploy", "deployment"],
    "분석·지표": ["analytics", "tracking", "kpi", "metrics"],
    "이메일": ["email sequence", "drip", "newsletter", "cold email", "lifecycle email"],
}


def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def settings_files(project):
    return [os.path.join(HOME, ".claude/settings.json"),
            os.path.join(project, ".claude/settings.json"),
            os.path.join(project, ".claude/settings.local.json")]


def enabled_map(project):
    state = {}
    for path in settings_files(project):
        state.update(load_json(path).get("enabledPlugins", {}))
    return state


def frontmatter(path):
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        return {}
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    meta, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if km:
            key = km.group(1)
            meta[key] = km.group(2).strip().strip("'\"").lstrip(">|").strip()
        elif key and line.startswith(" "):
            meta[key] = (meta[key] + " " + line.strip()).strip()
    return meta


def as_list(value, default):
    if value is None:
        return [default]
    return value if isinstance(value, list) else [value]


def read_hooks(root, manifest):
    spec = manifest.get("hooks")
    blocks = [spec] if isinstance(spec, dict) else [load_json(os.path.join(root, p)) for p in as_list(spec, "hooks/hooks.json")]
    out = []
    for b in blocks:
        for event, groups in (b.get("hooks", b) or {}).items():
            if not isinstance(groups, list):
                continue
            for g in groups:
                for h in (g.get("hooks", []) if isinstance(g, dict) else []):
                    cmd = " ".join([h.get("command", "")] + [str(a) for a in h.get("args", [])]).strip()
                    cmd = cmd.replace("${CLAUDE_PLUGIN_ROOT}", "<플러그인>").replace(HOME, "~")
                    out.append(dict(event=event, matcher=g.get("matcher", ""), command=cmd))
    return out


def read_mcp(root, manifest):
    spec = manifest.get("mcpServers")
    if isinstance(spec, dict):
        servers = spec
    else:
        servers = {}
        for p in as_list(spec, ".mcp.json"):
            data = load_json(os.path.join(root, p))
            servers.update(data.get("mcpServers", data if all(isinstance(v, dict) for v in data.values()) else {}))
    out = []
    for name, cfg in servers.items():
        where = cfg.get("url") or " ".join([cfg.get("command", "")] + [str(a) for a in cfg.get("args", [])][:3])
        out.append(dict(name=name, kind=cfg.get("type") or ("stdio" if cfg.get("command") else "?"), where=where.replace(HOME, "~")))
    return out


def read_plugin(source, key, root, enabled):
    manifest = load_json(os.path.join(root, ".claude-plugin/plugin.json"))
    skills = []
    for d in as_list(manifest.get("skills"), "skills"):
        for f in glob.glob(os.path.join(root, d, "**", "SKILL.md"), recursive=True):
            meta = frontmatter(f)
            if meta.get("name"):
                skills.append(dict(name=meta["name"], desc=meta.get("description", "")))
    commands = sorted({os.path.splitext(os.path.basename(f))[0]
                       for d in as_list(manifest.get("commands"), "commands")
                       for f in glob.glob(os.path.join(root, d, "*.md")) + glob.glob(os.path.join(root, d, "*.toml"))})
    agents = sorted({os.path.splitext(os.path.basename(f))[0]
                     for d in as_list(manifest.get("agents"), "agents")
                     for f in glob.glob(os.path.join(root, d, "*.md"))})
    styles = [frontmatter(f).get("name") or os.path.basename(f)[:-3]
              for f in glob.glob(os.path.join(root, "output-styles", "*.md"))]
    return dict(source=source, key=key, name=manifest.get("name") or key.split("@")[0], root=root,
                enabled=enabled, version=manifest.get("version", ""), commit="",
                skills=skills, commands=commands, agents=agents, styles=styles,
                hooks=read_hooks(root, manifest), mcp=read_mcp(root, manifest))


def collect(project, include_disabled=False):
    plugins = []
    enabled = enabled_map(project)
    installed = load_json(os.path.join(HOME, ".claude/plugins/installed_plugins.json")).get("plugins", {})
    for key, entries in sorted(installed.items()):
        on = bool(enabled.get(key))
        if not entries or (not on and not include_disabled):
            continue
        p = read_plugin("로컬", key, entries[0].get("installPath", ""), on)
        p["version"] = entries[0].get("version") or p["version"]
        p["commit"] = (entries[0].get("gitCommitSha") or "")[:7]
        plugins.append(p)
    seen = {p["name"] for p in plugins}
    for root in sorted(glob.glob(CLAUDE_AI)):
        name = load_json(os.path.join(root, ".claude-plugin/plugin.json")).get("name")
        if name and name not in seen:
            seen.add(name)
            plugins.append(read_plugin("claude.ai", name, root, True))
    active_style = None
    for path in settings_files(project):
        active_style = load_json(path).get("outputStyle", active_style)
    return plugins, active_style


def cmd_inventory(args):
    project = args.project
    plugins, active_style = collect(project, include_disabled=True)
    print(f"# 플러그인 구성\n\n프로젝트 기준: `{shorten(project)}` / 플러그인 {len(plugins)}개 (켜짐 {sum(p['enabled'] for p in plugins)}개)\n")
    print("| 플러그인 | 설치 경로 | 켜짐 | 버전 | 커밋 | 스킬 | 명령 | 에이전트 | 훅 | MCP | 출력 스타일 |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for p in plugins:
        print(f"| {p['name']} | {p['source']} | {'예' if p['enabled'] else '아니오'} | {p['version'] or '-'} | {p['commit'] or '-'} | "
              f"{len(p['skills'])} | {len(p['commands'])} | {len(p['agents'])} | {len(p['hooks'])} | {len(p['mcp'])} | {len(p['styles'])} |")
    print("\n## 훅\n\n부르지 않아도 정해진 시점마다 실행된다. \"지시를 넣음\"은 대화에 지시를 끼워 넣을 수 있는 시점이라는 뜻이다.\n")
    print("| 플러그인 | 켜짐 | 시점 | 대상 | 지시를 넣음 | 실행하는 명령 |\n|---|---|---|---|---|---|")
    for p in plugins:
        for h in p["hooks"]:
            cmd = h["command"] if len(h["command"]) <= 90 else h["command"][:87] + "..."
            print(f"| {p['name']} | {'예' if p['enabled'] else '아니오'} | {h['event']} | {(h['matcher'] or '전체').replace('|', '¦')} | "
                  f"{'예' if h['event'] in INJECT_EVENTS else '아니오'} | `{cmd.replace('|', '¦')}` |")
    print("\n## MCP 서버\n\n외부 서비스나 로컬 프로그램에 연결하는 도구다. 원격(http)은 외부와 통신한다.\n")
    print("| 플러그인 | 켜짐 | 서버 | 방식 | 연결 대상 |\n|---|---|---|---|---|")
    for p in plugins:
        for m in p["mcp"]:
            print(f"| {p['name']} | {'예' if p['enabled'] else '아니오'} | {m['name']} | {m['kind']} | `{m['where']}` |")
    print("\n## 명령과 에이전트\n\n| 플러그인 | 명령 | 에이전트 |\n|---|---|---|")
    for p in plugins:
        if p["commands"] or p["agents"]:
            print(f"| {p['name']} | {', '.join(p['commands']) or '-'} | {', '.join(p['agents']) or '-'} |")
    styles = [f"{p['name']}:{s}" for p in plugins for s in p["styles"]]
    print(f"\n## 출력 스타일\n\n지금 적용: `{active_style or 'default'}` / 플러그인이 제공하는 스타일: {', '.join(styles) or '없음'}")


def head(skill):
    return (skill["name"].replace("-", " ") + " " + skill["desc"][:220]).lower()


def tokens(text):
    words = set(w for w in re.findall(r"[a-z][a-z-]{3,}", text) if w not in STOP)
    return words | set(re.findall(r"[가-힣]{2,}", text))


def cmd_conflicts(args):
    plugins, active_style = collect(args.project)
    skills = [dict(plugin=p["name"], **s) for p in plugins for s in p["skills"]]
    print(f"# 충돌 후보\n\n켜진 플러그인 {len(plugins)}개 / 스킬 {len(skills)}개\n")
    print("후보일 뿐 판정이 아니다. 실제로 부딪히는지는 사람이 보고 Plugin Playbook에 정한다.\n")

    print("## 1. 이름이 같은 스킬\n")
    by_name = {}
    for s in skills:
        by_name.setdefault(s["name"].split(":")[-1], set()).add(s["plugin"])
    dup = {k: v for k, v in by_name.items() if len(v) > 1}
    if dup:
        print("| 스킬 이름 | 플러그인 |\n|---|---|")
        for k, v in sorted(dup.items()):
            print(f"| {k} | {', '.join(sorted(v))} |")
    else:
        print("없음")

    print("\n## 2. 같은 일을 맡는 스킬 (주제별, 두 플러그인 이상)\n")
    print("| 주제 | 플러그인 수 | 스킬 |\n|---|---|---|")
    for topic, words in TOPICS.items():
        hit = [s for s in skills if any(re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", head(s)) for w in words)]
        if len({s["plugin"] for s in hit}) > 1:
            listed = ", ".join(f"{s['plugin']}:{s['name']}" for s in sorted(hit, key=lambda s: s["plugin"]))
            print(f"| {topic} | {len({s['plugin'] for s in hit})} | {listed} |")

    print(f"\n## 3. 설명이 많이 겹치는 스킬 쌍 (겹침 {args.min} 이상, 상위 {args.top}개)\n")
    print("겹침은 두 스킬 설명 앞부분에 함께 나오는 단어 수를 짧은 쪽 단어 수로 나눈 값이다.\n")
    toks = [tokens(head(s)) for s in skills]
    pairs = []
    for i, j in itertools.combinations(range(len(skills)), 2):
        if skills[i]["plugin"] == skills[j]["plugin"]:
            continue
        common = toks[i] & toks[j]
        if len(common) < 3:
            continue
        score = len(common) / min(len(toks[i]), len(toks[j]))
        if score >= args.min:
            pairs.append((score, i, j, sorted(common)[:6]))
    if pairs:
        print("| 겹침 | 스킬 A | 스킬 B | 겹치는 단어 |\n|---|---|---|---|")
        for score, i, j, common in sorted(pairs, reverse=True)[: args.top]:
            a, b = skills[i], skills[j]
            print(f"| {score:.2f} | {a['plugin']}:{a['name']} | {b['plugin']}:{b['name']} | {', '.join(common)} |")
    else:
        print("없음")

    print("\n## 4. 부르지 않아도 작동하는 지시\n")
    print("| 시점 | 플러그인 (훅 수) | 지시를 넣는 시점인가 |\n|---|---|---|")
    by_event = {}
    for p in plugins:
        for h in p["hooks"]:
            by_event.setdefault(h["event"], {}).setdefault(p["name"], 0)
            by_event[h["event"]][p["name"]] += 1
    for event in sorted(by_event):
        owners = by_event[event]
        mark = "예" if event in INJECT_EVENTS else "아니오"
        if event in INJECT_EVENTS and len(owners) > 1:
            mark += ", 여러 개 겹침"
        print(f"| {event} | {', '.join(f'{k} ({v})' for k, v in owners.items())} | {mark} |")
    print(f"\n출력 스타일: 지금 적용 `{active_style or 'default'}`")

    print("\n## 5. 여러 플러그인이 같은 MCP 서버를 연결함\n")
    print("같은 서비스를 두 번 연결하면 도구가 겹친다(DEC-001: 한 서비스에 연결은 하나).\n")
    by_server = {}
    for p in plugins:
        for m in p["mcp"]:
            by_server.setdefault(m["name"].lower(), set()).add(p["name"])
    dup = {k: v for k, v in by_server.items() if len(v) > 1}
    if dup:
        print("| MCP 서버 | 플러그인 |\n|---|---|")
        for k, v in sorted(dup.items()):
            print(f"| {k} | {', '.join(sorted(v))} |")
    else:
        print("없음")


def cmd_drift(args):
    reviews = load_json(args.reviews)
    if not reviews:
        print(f"검토 기록을 읽지 못했다: {args.reviews}")
        return 1
    plugins, _ = collect(args.project, include_disabled=True)
    print("# 검토 기록과 다른 플러그인\n")
    print("| 플러그인 | 검토한 버전 | 검토한 커밋 | 설치된 버전 | 설치된 커밋 | 판단 |\n|---|---|---|---|---|---|")
    found = 0
    for p in plugins:
        r = reviews.get(p["name"])
        if r is None:
            print(f"| {p['name']} | - | - | {p['version'] or '-'} | {p['commit'] or '-'} | 검토 기록 없음 |")
            found += 1
            continue
        same_version = not r.get("version") or r["version"] == p["version"]
        same_commit = not r.get("commit") or not p["commit"] or p["commit"].startswith(r["commit"][:7])
        if not (same_version and same_commit):
            print(f"| {p['name']} | {r.get('version', '-')} | {r.get('commit', '-')} | {p['version'] or '-'} | {p['commit'] or '-'} | 다시 검토 필요 |")
            found += 1
    if not found:
        print("| — | | | | | 모두 검토한 상태와 같다 |")
    return 0


def cmd_scope(args):
    projects = [os.path.realpath(os.path.expanduser(p)) for p in args.projects]
    rows = {}
    for project in projects:
        plugins, style = collect(project, include_disabled=True)
        for p in plugins:
            rows.setdefault(p["name"], {})[project] = p["enabled"]
        rows.setdefault("(출력 스타일)", {})[project] = style or "default"
    print("# 폴더별로 켜지는 플러그인\n")
    print("| 플러그인 | " + " | ".join(f"`{shorten(p)}`" for p in projects) + " |")
    print("|---|" + "---|" * len(projects))
    for name in sorted(rows, key=lambda n: (n.startswith("("), n)):
        cells = []
        for p in projects:
            v = rows[name].get(p, False)
            cells.append(v if isinstance(v, str) else ("켜짐" if v else "—"))
        print(f"| {name} | " + " | ".join(cells) + " |")


def shorten(path):
    return path.replace(HOME, "~")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    for name in ["inventory", "conflicts", "drift"]:
        sp = sub.add_parser(name)
        sp.add_argument("--project", default=os.getcwd())
        if name == "conflicts":
            sp.add_argument("--min", type=float, default=0.33)
            sp.add_argument("--top", type=int, default=30)
        if name == "drift":
            sp.add_argument("--reviews", default="plugin-reviews.json")
    sc = sub.add_parser("scope")
    sc.add_argument("--projects", nargs="+", default=[os.getcwd()])
    args = ap.parse_args()
    if hasattr(args, "project"):
        args.project = os.path.realpath(os.path.expanduser(args.project))
    return {"inventory": cmd_inventory, "conflicts": cmd_conflicts, "drift": cmd_drift,
            "scope": cmd_scope}.get(args.cmd or "inventory")(args if args.cmd else ap.parse_args(["inventory"]))


if __name__ == "__main__":
    raise SystemExit(main() or 0)
