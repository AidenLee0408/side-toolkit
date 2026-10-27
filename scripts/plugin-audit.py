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
  usage      how often skills, commands, agents and MCP servers were used (from transcripts)
  summary    counts for the side-toolkit README
  components every skill, command, agent, hook, MCP server and output style per plugin
             (writes the "Plugin Components" document)

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
  python3 scripts/plugin-audit.py usage --root ~/SideProjects --since 2026-11-01
  python3 scripts/plugin-audit.py summary --projects ~/SideProjects/hub ~
  python3 scripts/plugin-audit.py components > "Plugin Components.md"
"""
import argparse
import collections
import glob
import hashlib
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


def toml_desc(path):
    try:
        m = re.search(r'^description\s*=\s*"(.*)"', open(path, encoding="utf-8").read(), re.M)
    except OSError:
        return ""
    return m.group(1) if m else ""


def first_sentence(text, limit=160):
    text = re.sub(r"\s+", " ", text or "").strip()
    m = re.match(r"(.+?[.!?。])(\s|$)", text)
    text = m.group(1) if m else text
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text.replace("|", "¦")


def read_plugin(source, key, root, enabled):
    manifest = load_json(os.path.join(root, ".claude-plugin/plugin.json"))
    skills = []
    for d in as_list(manifest.get("skills"), "skills"):
        for f in glob.glob(os.path.join(root, d, "**", "SKILL.md"), recursive=True):
            meta = frontmatter(f)
            if meta.get("name"):
                skills.append(dict(name=meta["name"], desc=meta.get("description", "")))
    commands, command_desc = set(), {}
    for d in as_list(manifest.get("commands"), "commands"):
        for f in glob.glob(os.path.join(root, d, "*.md")) + glob.glob(os.path.join(root, d, "*.toml")):
            name = os.path.splitext(os.path.basename(f))[0]
            commands.add(name)
            command_desc.setdefault(name, frontmatter(f).get("description", "") if f.endswith(".md") else toml_desc(f))
    commands = sorted(commands)
    agents, agent_desc = set(), {}
    for d in as_list(manifest.get("agents"), "agents"):
        for f in glob.glob(os.path.join(root, d, "*.md")):
            meta = frontmatter(f)
            name = meta.get("name") or os.path.splitext(os.path.basename(f))[0]
            agents.add(name)
            agent_desc[name] = meta.get("description", "")
    agents = sorted(agents)
    styles = [frontmatter(f).get("name") or os.path.basename(f)[:-3]
              for f in glob.glob(os.path.join(root, "output-styles", "*.md"))]
    return dict(source=source, key=key, name=manifest.get("name") or key.split("@")[0], root=root,
                enabled=enabled, version=manifest.get("version", ""), commit="",
                description=manifest.get("description", ""),
                skills=skills, commands=commands, agents=agents, styles=styles,
                command_desc=command_desc, agent_desc=agent_desc,
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
            listed = ", ".join(f"`{s['plugin']}:{s['name']}`" for s in sorted(hit, key=lambda s: s["plugin"]))
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
    gaps = translation_gaps(plugins, load_json(args.ko))
    print("\n## 한국어 설명이 없거나 낡은 항목 (켜진 플러그인)\n")
    if gaps:
        print("| 항목 | 상태 |\n|---|---|")
        for key, state in gaps:
            print(f"| `{key.replace('|', ' / ').rstrip(' /')}` | {state} |")
    else:
        print("없음")
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


COMMAND_RE = re.compile(r"<command-name>/?([^<\s]+)</command-name>")


def cmd_usage(args):
    """Count use from ~/.claude/projects transcripts whose working directory is under --root."""
    root = os.path.realpath(os.path.expanduser(args.root))
    skills, commands, agents, mcp = (collections.Counter() for _ in range(4))
    sessions = set()
    for path in glob.glob(os.path.join(HOME, ".claude/projects/*/*.jsonl")):
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except json.JSONDecodeError:
                    continue
                cwd = d.get("cwd") or ""
                if not (cwd == root or cwd.startswith(root + os.sep)):
                    continue
                day = (d.get("timestamp") or "")[:10]
                if (args.since and day < args.since) or (args.until and day > args.until):
                    continue
                content = (d.get("message") or {}).get("content")
                if d.get("type") == "user":
                    text = content if isinstance(content, str) else json.dumps(content)
                    for m in COMMAND_RE.findall(text or ""):
                        commands[m] += 1
                        sessions.add(d.get("sessionId"))
                if not isinstance(content, list):
                    continue
                for c in content:
                    if c.get("type") != "tool_use":
                        continue
                    name, inp = c.get("name", ""), c.get("input") or {}
                    if name == "Skill" and inp.get("skill"):
                        skills[inp["skill"]] += 1
                    elif name == "Agent":
                        agents[inp.get("subagent_type") or "general-purpose"] += 1
                    elif name.startswith("mcp__") and not name.startswith("mcp__ccd_"):
                        mcp[name.split("__")[1]] += 1
                    else:
                        continue
                    sessions.add(d.get("sessionId"))

    def owner(name):
        return name.split(":", 1)[0] if ":" in name else "(기본)"

    by_plugin = collections.Counter()
    for counter in (skills, commands, agents):
        for k, v in counter.items():
            by_plugin[owner(k)] += v
    for k, v in mcp.items():
        by_plugin[k.replace("plugin_", "").split("_")[0]] += v
    period = f"{args.since or '처음'} ~ {args.until or '지금'}"
    print(f"# 사용 집계\n\n범위: `{shorten(root)}` / 기간: {period} / 사용이 있던 세션: {len(sessions)}\n")
    print("훅과 출력 스타일은 부르지 않아도 작동하므로 집계되지 않는다.\n")
    for title, counter in [("플러그인별 합계", by_plugin), ("스킬 (Claude가 부름)", skills),
                           ("슬래시 명령 (사람이 입력)", commands), ("서브에이전트", agents), ("MCP 서버", mcp)]:
        print(f"## {title}\n")
        if not counter:
            print("없음\n")
            continue
        print("| 이름 | 횟수 |\n|---|---|")
        for k, v in counter.most_common():
            print(f"| {k} | {v} |")
        print()
    plugins, _ = collect(root)
    unused = [p["name"] for p in plugins if p["name"] not in by_plugin and (p["skills"] or p["commands"] or p["agents"] or p["mcp"])]
    print("## 켜져 있지만 이 기간에 한 번도 쓰지 않은 플러그인\n")
    print(", ".join(sorted(unused)) or "없음")
    print("\n(훅이나 출력 스타일로만 작동하는 플러그인은 쓰지 않은 것처럼 보일 수 있다.)")


def cmd_summary(args):
    """Counts across folders: on everywhere, on in some folders only, off everywhere."""
    projects = [os.path.realpath(os.path.expanduser(p)) for p in args.projects]
    state, info = {}, {}
    for project in projects:
        plugins, _ = collect(project, include_disabled=True)
        for p in plugins:
            state.setdefault(p["name"], []).append(p["enabled"])
            info[p["name"]] = p
    everywhere = [n for n, v in state.items() if all(v)]
    some = [n for n, v in state.items() if any(v) and not all(v)]
    off = [n for n, v in state.items() if not any(v)]
    on = [info[n] for n in everywhere]
    print(f"모든 폴더에서 사용 중: {len(on)}개 (claude.ai {sum(p['source'] == 'claude.ai' for p in on)}개, "
          f"로컬 {sum(p['source'] == '로컬' for p in on)}개)")
    print(f"일부 폴더에서만 사용: {len(some)}개 ({', '.join(sorted(some)) or '없음'})")
    print(f"사용 중지: {len(off)}개 ({', '.join(sorted(off)) or '없음'})")
    print(f"모든 폴더에서 켜진 스킬 {sum(len(p['skills']) for p in on)}개, 훅 {sum(len(p['hooks']) for p in on)}개, "
          f"MCP 서버 {sum(len(p['mcp']) for p in on)}개, 에이전트 {sum(len(p['agents']) for p in on)}개")

def src_hash(text):
    return hashlib.sha1((text or "").encode()).hexdigest()[:10]


def korean(ko, key, source):
    """Korean description for key; flags missing or outdated translations."""
    entry = ko.get(key)
    if not entry:
        return "(번역 없음)"
    if entry.get("src") != src_hash(source):
        return entry["ko"] + " (원문이 바뀌어 번역 다시 필요)"
    return entry["ko"]


def translation_gaps(plugins, ko):
    gaps = []
    for p in plugins:
        if not p["enabled"]:
            continue
        items = [(f"{p['name']}|plugin|", p["description"])]
        items += [(f"{p['name']}|skill|{s['name'].split(':')[-1]}", s["desc"]) for s in p["skills"]]
        items += [(f"{p['name']}|command|{c}", p["command_desc"].get(c, "")) for c in p["commands"]]
        items += [(f"{p['name']}|agent|{a}", p["agent_desc"].get(a, "")) for a in p["agents"]]
        for key, source in items:
            entry = ko.get(key)
            if not entry:
                gaps.append((key, "번역 없음"))
            elif entry.get("src") != src_hash(source):
                gaps.append((key, "원문이 바뀌어 번역 다시 필요"))
    return gaps


def cmd_components(args):
    plugins, _ = collect(args.project, include_disabled=True)
    reviews = load_json(args.reviews)
    ko = load_json(args.ko)
    print("---\ntype: generated\nstatus: generated\n---\n")
    print("# Plugin Components\n")
    print("플러그인마다 들어 있는 스킬, 명령, 에이전트, 훅, MCP 서버, 출력 스타일의 목록이다. "
          "`python3 scripts/plugin-audit.py components`로 만든 문서라 손으로 고치지 않는다. "
          "스킬, 명령, 에이전트의 설명은 각 플러그인의 원문을 한국어로 옮긴 것이고(`plugin-descriptions.ko.json`), "
          "훅의 \"하는 일\"은 검토하면서 `plugin-reviews.json`에 적어 둔 내용이다. "
          "사용 중지한 플러그인은 이름만 적고, 다시 켤 때 번역한다. "
          "왜 설치했는지와 상태는 [[Plugins]]에, 어떤 스킬을 먼저 쓰는지는 [[Plugin Playbook]]에 있다.\n")
    print("| 플러그인 | 켜짐 | 스킬 | 명령 | 에이전트 | 훅 | MCP | 출력 스타일 |\n|---|---|---|---|---|---|---|---|")
    for p in plugins:
        anchor = p["name"]
        print(f"| [{p['name']}](#{anchor}) | {'예' if p['enabled'] else '아니오'} | {len(p['skills'])} | {len(p['commands'])} | "
              f"{len(p['agents'])} | {len(p['hooks'])} | {len(p['mcp'])} | {len(p['styles'])} |")
    for p in plugins:
        state = "켜짐" if p["enabled"] else "꺼짐"
        print(f"\n## {p['name']}\n")
        print(f"{p['source']} · {state} · 버전 {p['version'] or '-'}" + (f" · 커밋 {p['commit']}" if p["commit"] else ""))
        if not p["enabled"]:
            names = [f"`{p['name']}:{sk['name'].split(':')[-1]}`" for sk in sorted(p["skills"], key=lambda x: x["name"])]
            names += [f"`/{c}`" for c in p["commands"]] + [f"`{a}`" for a in p["agents"]]
            print("\n사용 중지한 플러그인이라 이름만 적는다. 다시 켤 때 설명을 번역한다.")
            if names:
                print(f"\n스킬 {len(p['skills'])}개, 명령 {len(p['commands'])}개, 에이전트 {len(p['agents'])}개: " + ", ".join(names))
        else:
            print(f"\n> {korean(ko, p['name'] + '|plugin|', p['description'])}")
        if p["enabled"] and p["skills"]:
            print(f"\n**스킬 {len(p['skills'])}개**\n\n| 스킬 | 설명 |\n|---|---|")
            for sk in sorted(p["skills"], key=lambda x: x["name"]):
                short = sk["name"].split(":")[-1]
                print(f"| `{p['name']}:{short}` | {korean(ko, p['name'] + '|skill|' + short, sk['desc'])} |")
        if p["enabled"] and p["commands"]:
            print(f"\n**명령 {len(p['commands'])}개**\n\n| 명령 | 설명 |\n|---|---|")
            for c in p["commands"]:
                print(f"| `/{c}` | {korean(ko, p['name'] + '|command|' + c, p['command_desc'].get(c, ''))} |")
        if p["enabled"] and p["agents"]:
            print(f"\n**에이전트 {len(p['agents'])}개**\n\n| 에이전트 | 설명 |\n|---|---|")
            for a in p["agents"]:
                print(f"| `{a}` | {korean(ko, p['name'] + '|agent|' + a, p['agent_desc'].get(a, ''))} |")
        if p["hooks"]:
            notes = reviews.get(p["name"], {}).get("hooks", {})
            print(f"\n**훅 {len(p['hooks'])}개** (부르지 않아도 정해진 시점마다 실행된다)\n\n| 시점 | 대상 | 하는 일 | 대화에 지시를 넣을 수 있음 |\n|---|---|---|---|")
            for h in p["hooks"]:
                note = notes.get(h["event"]) or f"`{(h['command'][:60] + '...') if len(h['command']) > 60 else h['command']}`".replace("|", "¦")
                print(f"| {h['event']} | {(h['matcher'] or '전체').replace('|', '¦')} | {note} | {'예' if h['event'] in INJECT_EVENTS else '아니오'} |")
        if p["mcp"]:
            print(f"\n**MCP 서버 {len(p['mcp'])}개**\n\n| 서버 | 방식 | 연결 대상 |\n|---|---|---|")
            for m in p["mcp"]:
                print(f"| {m['name']} | {m['kind']} | `{m['where'] or '-'}` |")
        if p["styles"]:
            print(f"\n**출력 스타일 {len(p['styles'])}개**: " + ", ".join(f"`{x}`" for x in p["styles"]))
        if not any([p["skills"], p["commands"], p["agents"], p["hooks"], p["mcp"], p["styles"]]):
            print("\n구성 요소를 찾지 못했다.")


def shorten(path):
    return path.replace(HOME, "~")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    for name in ["inventory", "conflicts", "drift", "components"]:
        sp = sub.add_parser(name)
        sp.add_argument("--project", default=os.getcwd())
        if name == "conflicts":
            sp.add_argument("--min", type=float, default=0.33)
            sp.add_argument("--top", type=int, default=30)
        if name in ("drift", "components"):
            sp.add_argument("--reviews", default="plugin-reviews.json")
            sp.add_argument("--ko", default="plugin-descriptions.ko.json")
    sc = sub.add_parser("scope")
    sc.add_argument("--projects", nargs="+", default=[os.getcwd()])
    us = sub.add_parser("usage")
    us.add_argument("--root", default=os.getcwd())
    us.add_argument("--since", help="YYYY-MM-DD, inclusive")
    us.add_argument("--until", help="YYYY-MM-DD, inclusive")
    sm = sub.add_parser("summary")
    sm.add_argument("--projects", nargs="+", default=[os.path.join(HOME, "SideProjects/hub"), HOME])
    args = ap.parse_args()
    if hasattr(args, "project"):
        args.project = os.path.realpath(os.path.expanduser(args.project))
    return {"inventory": cmd_inventory, "conflicts": cmd_conflicts, "drift": cmd_drift,
            "scope": cmd_scope, "usage": cmd_usage, "summary": cmd_summary,
            "components": cmd_components}.get(args.cmd or "inventory")(args if args.cmd else ap.parse_args(["inventory"]))


if __name__ == "__main__":
    raise SystemExit(main() or 0)
