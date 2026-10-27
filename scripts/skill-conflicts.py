#!/usr/bin/env python3
"""List skill conflict candidates across the Claude Code plugins enabled here.

Claude picks a skill by reading every enabled skill's description. When two
plugins describe the same job, the wrong one can fire. This script collects
enabled skills, hooks and output styles, then prints candidates for a person
to judge. It never decides that something is a conflict.

Sources:
  - local plugins: ~/.claude/plugins/installed_plugins.json, filtered by
    enabledPlugins in ~/.claude/settings.json and <project>/.claude/settings*.json
  - claude.ai plugins: ~/Library/Application Support/Claude/local-agent-mode-sessions/*/*/rpm/plugin_*
Built-in skills and commands (/code-review, /simplify) are not on disk and are not listed.

Usage:
  python3 scripts/skill-conflicts.py                  # project = current directory
  python3 scripts/skill-conflicts.py --project ~/SideProjects/products/foo
  python3 scripts/skill-conflicts.py --min 0.18 --top 40
"""
import argparse
import glob
import itertools
import json
import os
import re

HOME = os.path.expanduser("~")
INJECT_EVENTS = {"SessionStart", "UserPromptSubmit", "SubagentStart"}
STOP = set("""
use when user wants asks with this that from into your their they them also only
skill skills agent agents claude code about after before each every have more most
such than then there these those what when where which while will would could should
mentions mention including include includes other others work works working using
""".split())

# Jobs that several plugins tend to claim. Each topic lists words that signal it.
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


def enabled_map(project):
    state = {}
    for path in [os.path.join(HOME, ".claude/settings.json"),
                 os.path.join(project, ".claude/settings.json"),
                 os.path.join(project, ".claude/settings.local.json")]:
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


def plugin_hooks(root, manifest):
    spec = manifest.get("hooks")
    files = []
    if isinstance(spec, dict):
        blocks = [spec]
    else:
        blocks = []
        paths = spec if isinstance(spec, list) else [spec] if isinstance(spec, str) else ["hooks/hooks.json"]
        for p in paths:
            files.append(os.path.normpath(os.path.join(root, p)))
        blocks = [load_json(f) for f in files]
    events = {}
    for b in blocks:
        for event, groups in (b.get("hooks", b) or {}).items():
            if isinstance(groups, list):
                events[event] = events.get(event, 0) + sum(len(g.get("hooks", [])) for g in groups if isinstance(g, dict))
    return events


def collect(project):
    plugins = []
    enabled = enabled_map(project)
    installed = load_json(os.path.join(HOME, ".claude/plugins/installed_plugins.json")).get("plugins", {})
    for key, entries in installed.items():
        if not enabled.get(key) or not entries:
            continue
        root = entries[0].get("installPath", "")
        plugins.append(("로컬", key.split("@")[0], root))
    seen = {p[1] for p in plugins}
    pattern = os.path.join(HOME, "Library/Application Support/Claude/local-agent-mode-sessions/*/*/rpm/plugin_*")
    for root in sorted(glob.glob(pattern)):
        name = load_json(os.path.join(root, ".claude-plugin/plugin.json")).get("name")
        if name and name not in seen:
            seen.add(name)
            plugins.append(("claude.ai", name, root))

    skills, hooks, styles = [], [], []
    for source, name, root in plugins:
        manifest = load_json(os.path.join(root, ".claude-plugin/plugin.json"))
        skill_dirs = manifest.get("skills") or "skills"
        skill_dirs = skill_dirs if isinstance(skill_dirs, list) else [skill_dirs]
        for d in skill_dirs:
            for f in glob.glob(os.path.join(root, d, "**", "SKILL.md"), recursive=True):
                meta = frontmatter(f)
                if meta.get("name"):
                    skills.append(dict(plugin=name, source=source, name=meta["name"], desc=meta.get("description", "")))
        for event, count in plugin_hooks(root, manifest).items():
            hooks.append(dict(plugin=name, event=event, count=count))
        for f in glob.glob(os.path.join(root, "output-styles", "*.md")):
            styles.append(dict(plugin=name, name=frontmatter(f).get("name") or os.path.basename(f)[:-3]))
    active_style = None
    for path in [os.path.join(HOME, ".claude/settings.json"), os.path.join(project, ".claude/settings.json"),
                 os.path.join(project, ".claude/settings.local.json")]:
        active_style = load_json(path).get("outputStyle", active_style)
    return plugins, skills, hooks, styles, active_style


def head(skill):
    """Skill name plus the start of its description, where the job is stated."""
    return (skill["name"].replace("-", " ") + " " + skill["desc"][:220]).lower()


def tokens(text):
    text = text.lower()
    words = set(w for w in re.findall(r"[a-z][a-z-]{3,}", text) if w not in STOP)
    words |= set(re.findall(r"[가-힣]{2,}", text))
    return words


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default=os.getcwd())
    ap.add_argument("--min", type=float, default=0.33, help="minimum overlap (shared words / smaller set) for a pair")
    ap.add_argument("--top", type=int, default=30)
    args = ap.parse_args()
    project = os.path.realpath(os.path.expanduser(args.project))
    plugins, skills, hooks, styles, active_style = collect(project)

    print(f"# 스킬 충돌 후보\n\n프로젝트: `{project}` / 켜진 플러그인 {len(plugins)}개 / 스킬 {len(skills)}개\n")
    print("후보일 뿐 판정이 아니다. 실제로 부딪히는지는 사람이 보고 Skill Playbook에 정한다.\n")

    print("## 1. 같은 이름의 스킬\n")
    by_name = {}
    for s in skills:
        by_name.setdefault(s["name"].split(":")[-1], []).append(s)
    dup = {k: v for k, v in by_name.items() if len({s["plugin"] for s in v}) > 1}
    if dup:
        print("| 스킬 이름 | 플러그인 |\n|---|---|")
        for k, v in sorted(dup.items()):
            print(f"| {k} | {', '.join(sorted({s['plugin'] for s in v}))} |")
    else:
        print("없음")
    print()

    print("## 2. 같은 일을 맡는 스킬 (주제별, 두 플러그인 이상)\n")
    print("| 주제 | 플러그인 수 | 스킬 |\n|---|---|---|")
    for topic, words in TOPICS.items():
        hit = [s for s in skills if any(re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", head(s)) for w in words)]
        owners = {s["plugin"] for s in hit}
        if len(owners) > 1:
            listed = ", ".join(f"{s['plugin']}:{s['name']}" for s in sorted(hit, key=lambda s: s["plugin"]))
            print(f"| {topic} | {len(owners)} | {listed} |")
    print()

    print(f"## 3. 설명이 많이 겹치는 스킬 쌍 (겹침 {args.min} 이상, 상위 {args.top}개)\n")
    print("겹침은 두 스킬 설명 앞부분에 함께 나오는 단어 수를 짧은 쪽 단어 수로 나눈 값이다.\n")
    pairs = []
    toks = [tokens(head(s)) for s in skills]
    for i, j in itertools.combinations(range(len(skills)), 2):
        if skills[i]["plugin"] == skills[j]["plugin"] or not toks[i] or not toks[j]:
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
    print()

    print("## 4. 부르지 않아도 작동하는 지시\n")
    print("메시지나 세션마다 지시를 넣는 훅과 출력 스타일이다. 같은 시점에 여러 개가 있으면 지시가 서로 부딪힐 수 있다.\n")
    print("| 시점 | 플러그인 (훅 수) | 지시를 넣는 시점인가 |\n|---|---|---|")
    by_event = {}
    for h in hooks:
        by_event.setdefault(h["event"], []).append(h)
    for event in sorted(by_event):
        owners = ", ".join(f"{h['plugin']} ({h['count']})" for h in by_event[event])
        mark = "예" if event in INJECT_EVENTS else "아니오"
        if event in INJECT_EVENTS and len(by_event[event]) > 1:
            mark += ", 여러 개 겹침"
        print(f"| {event} | {owners} | {mark} |")
    print(f"\n출력 스타일: 지금 적용 `{active_style or 'default'}` / 플러그인이 제공하는 스타일 "
          + (", ".join(f"{s['plugin']}:{s['name']}" for s in styles) or "없음"))


if __name__ == "__main__":
    main()
