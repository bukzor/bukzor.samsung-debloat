#!/bin/bash
# Run the "remove the known" residue+timeline pipeline and print a readable,
# time-sorted table. Residue = My Activity events MINUS system/vendor namespaces
# and kb-`legitimate` apps; each survivor joined to device install metadata
# (scripts/package_dump.py) and its reputation verdict (scripts/android_apps_kb.py).
#
#   scripts/unknown-apps-timeline.sh [PACKAGE_DUMP]
#
# PACKAGE_DUMP defaults to the newest forensics/*/package-dump-full.txt.
# Override the other inputs via env: MYACTIVITY=<json> KB=<android-apps.kb dir>.
# Raw JSON (unformatted) instead of the table: JSON=1 scripts/unknown-apps-timeline.sh
set -euo pipefail
export DEBUG="${DEBUG:-0}"

onerror() {
  error="$?"
  echo >&2 "ERROR($error)"
  exit "$error"
}
trap onerror ERR

here=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
root=$(cd -- "$here/.." && pwd)

MYACTIVITY="${MYACTIVITY:-$root/forensics/myactivity.google.com.json}"
KB="${KB:-$root/.claude/current-task.kb/android-apps.kb}"
JSON="${JSON:-0}"

dump="${1:-}"
if [[ -z "$dump" ]]; then
  [[ -d "$root/forensics" ]] || { echo >&2 "$0: no forensics/ dir; pass a PACKAGE_DUMP path"; exit 1; }
  dump=$(
    find "$root/forensics" -name 'package-dump-full.txt' -printf '%T@\t%p\n' |
      sort -rn |
      sed -n '1p' |
      cut -f2-
  )
fi

[[ -f "$MYACTIVITY" ]] || { echo >&2 "$0: no My Activity json: $MYACTIVITY"; exit 1; }
[[ -f "$dump"       ]] || { echo >&2 "$0: no package dump (pass one as \$1): ${dump:-<none>}"; exit 1; }
[[ -d "$KB"         ]] || { echo >&2 "$0: no kb dir: $KB"; exit 1; }

(( DEBUG > 0 )) && set -x

echo >&2 "myactivity: $MYACTIVITY"
echo >&2 "dump:       $dump"
echo >&2 "kb:         $KB"

# Stream of residue rows (one JSON object per package), already joined.
residue() {
  "$here/myactivity.google.com.records.jq" "$MYACTIVITY" |
    jq -s \
      --slurpfile dump  <("$here/package_dump.py" "$dump") \
      --slurpfile known <("$here/android_apps_kb.py" list "$KB") \
      -f "$here/unknown-apps-timeline.jq"
}

if (( JSON > 0 )); then
  residue | jq -s 'sort_by(.first_seen_us)'
  exit 0
fi

# Tabulate: time-sorted, compact columns, aligned with `column`.
residue |
  jq -rs '
    def pad2:    tostring | if length < 2 then "0" + . else . end;
    def loc:                                                 # UTC ISO -> local ISO, DST-safe
      if . == null then "-"
      else fromdateiso8601 as $e
        | ($e | localtime | mktime - $e) as $off             # local UTC offset, seconds
        | ($off | fabs) as $a
        | ($e | strflocaltime("%Y-%m-%dT%H:%M:%S"))
          + (if $off < 0 then "-" else "+" end)
          + (($a / 3600 | floor) | pad2) + ((($a % 3600) / 60 | floor) | pad2)
      end;
    def flags:   [ (if .delisted then "delisted" else empty end),
                   (if .on_device then "on-dev" else empty end) ]
               | if length == 0 then "-" else join(",") end;
    def instlr:  .installer
               | if . == null then "-" elif . == "com.android.vending" then "play" else . end;
    sort_by(.first_seen_us)
    | (["FIRST_SEEN","LAST_SEEN","VERDICT","FLAGS","USED","VIS","INSTALLER","TITLE","PACKAGE"]),
      (.[] | [ (.first_seen|loc), (.last_seen|loc), .verdict, flags,
               (.used|tostring), (.visited|tostring),
               instlr, (.title // "-"), .package ])
    | @tsv
  ' |
  column -t -s "$(printf '\t')"
