#!/usr/bin/env python3
"""Count skill, slash command, subagent and MCP tool use in Claude Code transcripts.

Reads ~/.claude/projects/*/*.jsonl and keeps only sessions whose working
directory is under --root (default: $SKILL_USAGE_ROOT, else the current
directory), so sessions from unrelated work are never counted. Prints
Markdown tables for a Skill Report.

Usage:
  python3 scripts/skill-usage.py --root ~/SideProjects        # every side project
  python3 scripts/skill-usage.py --root ~/SideProjects/products/foo
  python3 scripts/skill-usage.py --since 2026-11-01 --until 2026-11-14
"""
import argparse
import collections
import glob
import json
import os
import re

COMMAND_RE = re.compile(r"<command-name>/?([^<\s]+)</command-name>")


def plugin_of(name):
    return name.split(":", 1)[0] if ":" in name else "(기본)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.environ.get("SKILL_USAGE_ROOT") or os.getcwd())
    ap.add_argument("--since", help="YYYY-MM-DD, inclusive")
    ap.add_argument("--until", help="YYYY-MM-DD, inclusive")
    args = ap.parse_args()
    root = os.path.realpath(os.path.expanduser(args.root))

    skills = collections.Counter()
    commands = collections.Counter()
    agents = collections.Counter()
    mcp = collections.Counter()
    sessions = set()

    for path in glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl")):
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
                if args.since and day < args.since:
                    continue
                if args.until and day > args.until:
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

    period = f"{args.since or '처음'} ~ {args.until or '지금'}"
    print(f"# 스킬 사용 집계\n\n범위: `{root}` / 기간: {period} / 사용이 있던 세션: {len(sessions)}\n")
    by_plugin = collections.Counter()
    for k, v in skills.items():
        by_plugin[plugin_of(k)] += v
    for k, v in commands.items():
        by_plugin[plugin_of(k)] += v
    for title, counter in [
        ("플러그인별 (스킬 + 명령)", by_plugin),
        ("스킬 (Claude가 부름)", skills),
        ("슬래시 명령 (사람이 입력)", commands),
        ("서브에이전트", agents),
        ("MCP 서버", mcp),
    ]:
        print(f"## {title}\n")
        if not counter:
            print("없음\n")
            continue
        print("| 이름 | 횟수 |\n|---|---|")
        for k, v in counter.most_common():
            print(f"| {k} | {v} |")
        print()


if __name__ == "__main__":
    main()
