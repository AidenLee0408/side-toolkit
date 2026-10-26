#!/bin/sh
# Copy the skill docs from the Side Hub (the source of truth) into this repo.
# Usage: scripts/sync-from-hub.sh [hub path]   (default: ../../hub next to products/)
set -eu
repo=$(cd "$(dirname "$0")/.." && pwd)
hub=${1:-$repo/../../hub}
[ -f "$hub/Skills.md" ] || { echo "hub not found: $hub" >&2; exit 1; }
cp "$hub/Skills.md" "$repo/docs/Skills.md"
cp "$hub/Skill Playbook.md" "$repo/docs/Skill Playbook.md"
cp "$hub/Skill Issues.md" "$repo/docs/Skill Issues.md"
cp "$hub/Skill Reports/"*.md "$repo/reports/"
cp "$hub/scripts/skill-usage.py" "$repo/scripts/skill-usage.py"
git -C "$repo" status --short
