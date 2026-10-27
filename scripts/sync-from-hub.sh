#!/bin/sh
# Copy the skill docs from the Side Hub (the source of truth) into this repo.
# Obsidian [[wiki links]] become GitHub links; links to hub-only docs become plain text.
# Usage: scripts/sync-from-hub.sh [hub path]   (default: ../../hub next to products/)
set -eu
repo=$(cd "$(dirname "$0")/.." && pwd)
hub=${1:-$repo/../../hub}
[ -f "$hub/Skills.md" ] || { echo "hub not found: $hub" >&2; exit 1; }

copy() { python3 - "$1" "$2" "$3" <<'EOF'
import re, sys
src, dst, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
docs = {"Skills", "Skill Playbook", "Skill Issues", "Skill Changelog"}
def link(m):
    name = m.group(1)
    if name in docs:
        return f"[{name}]({prefix}{name.replace(' ', '%20')}.md)"
    return f"{name} (운영 허브 문서)"
text = re.sub(r"\[\[([^\]|]+)\]\]", link, open(src, encoding="utf-8").read())
open(dst, "w", encoding="utf-8").write(text)
EOF
}

for d in "Skills" "Skill Playbook" "Skill Issues" "Skill Changelog"; do
  copy "$hub/$d.md" "$repo/docs/$d.md" ""
done
for f in "$hub/Skill Reports/"*.md; do
  copy "$f" "$repo/reports/$(basename "$f")" "../docs/"
done
cp "$hub/scripts/skill-usage.py" "$repo/scripts/skill-usage.py"
cp "$hub/scripts/skill-conflicts.py" "$repo/scripts/skill-conflicts.py"
git -C "$repo" status --short
