#!/bin/bash
# Fold app_reputation_probe.py JSONL (stdin) into the frontmatter of the
# android-apps.kb files (flat, one per package), emitting md-frontmatter-set
# records on stdout (inspect, then pipe to md-frontmatter-set):
#
#   scripts/app_reputation_probe.py $(pkgs) \
#     | scripts/app_reputation_to_kb.sh .claude/current-task.kb/android-apps.kb/ \
#     | md-frontmatter-set
#
# The probe `permissions`/identity/ad-posture land in the schema's `probe`
# object; verdict + name/category/confidence/source/body are untouched.
set -euo pipefail
export DEBUG="${DEBUG:-0}"

onerror() {
  error="$?"
  echo >&2 "ERROR($error)"
  exit "$error"
}
trap onerror ERR

usage() {
  echo >&2 "usage: app_reputation_probe.py ... | $0 <kb-dir/> [date] | md-frontmatter-set"
  exit 2
}

[[ "${1:-}" ]] || usage
dir=$1
date=${2:-$(date +%F)}
[[ -d "$dir" ]] || { echo >&2 "$0: not a directory: $dir"; exit 1; }
(( DEBUG > 0 )) && set -x

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
probe=$(mktemp)
cur=$(mktemp)
trap 'rm -f "$probe" "$cur"' EXIT

cat > "$probe"

# Current frontmatter of each kb file, as {package, fm} JSONL — the base we
# merge the probe object into (md-frontmatter-set replaces, so we need it whole).
# CLAUDE.md is the kb's maintenance guide, not a package — skip it.
find "$dir" -maxdepth 1 -name '*.md' -not -name 'CLAUDE.md' -print0 \
  | while IFS= read -r -d '' f; do
      yq -f extract -o=json -I=0 '{"package": .package, "fm": .}' "$f"
    done > "$cur"

jq -c -n --arg date "$date" --arg dir "$dir" \
  --slurpfile probe "$probe" \
  --slurpfile cur "$cur" \
  -f "$script_dir/app_reputation_probe.frontmatter.jq"
