# Residue analysis: My Activity events MINUS the known-legitimate = apps to review.
#
# "Remove the known": drop OS/vendor namespaces (below) and any package the
# android-apps.kb reputation collection marks `legitimate`. What survives is the
# problem set (adware + still-unclassified), each row tagged with its verdict and
# joined to device install metadata. Residue membership is the ABSENCE of a
# known-good explanation, not a verdict.
#
# Input : My Activity events JSONL on stdin (from myactivity.google.com.records.jq)
# Joins : --slurpfile dump  <package_dump.py output>          (device metadata)
#         --slurpfile known <android_apps_kb.py list output>  (reputation verdicts)
# Output: one JSONL row per residue package; callers sort (see usage).
#
# Usage:
#   scripts/myactivity.google.com.records.jq forensics/myactivity.google.com.json \
#     | jq -s \
#         --slurpfile dump  <(scripts/package_dump.py forensics/<cap>/package-dump-full.txt) \
#         --slurpfile known <(scripts/android_apps_kb.py list .claude/current-task.kb/android-apps.kb) \
#         -f scripts/unknown-apps-timeline.jq \
#     | jq -s 'sort_by(.first_seen_us)'

def is_system($p):
  [ "android", "com.android.", "com.google.", "com.samsung", "com.sec.",
    "com.qualcomm.", "com.qti.", "qcom.", "vendor.", "org.codeaurora.",
    "com.skms.", "com.knox", "com.monotype.", "com.dsi.ant", "com.osp.app",
    "com.wssyncmldm", "com.wssnps", "com.sktelecom.", "com.verizon.",
    "com.vzw.", "com.vcast.", "com.synchronoss." ]
  | any(. as $pre | $p | startswith($pre));

def iso: if . == null then null else (. / 1000000 | floor | todate) end;

( reduce $dump[]  as $r ({}; .[$r.package] = $r) )  as $by_pkg
| ( reduce $known[] as $k ({}; .[$k.package] = $k) ) as $known_by
| group_by(.package)[]
| select(.[0].package != null)
| (.[0].package) as $p
| ($known_by[$p].verdict // "unclassified") as $v
| select(is_system($p) | not)
| select($v != "legitimate")
# first real title: skip nulls, the bare "Google Play Store", and store-URL titles
# (delisted deeplink visits log the play.google.com URL as their title)
| ( map(.title)
    | map(select(. != null and . != "Google Play Store" and (test("^https?://") | not)))
    | (.[0] // null) ) as $title
| ( map(.when_us) | min ) as $first
| ( map(.when_us) | max ) as $last
| {
    package: $p,
    verdict: $v,
    delisted: ($known_by[$p].delisted // false),
    title: $title,
    first_seen: ($first | iso),
    last_seen:  ($last  | iso),
    first_seen_us: $first,
    used:    ( map(select(.action == "Used"))    | length ),
    visited: ( map(select(.action == "Visited")) | length ),
    events:  length,
    devices: ( map(.device) | map(select(. != null)) | unique ),
    on_device:            ( $by_pkg | has($p) ),
    installer:            ( $by_pkg[$p].installer // null ),
    device_first_install: ( $by_pkg[$p].first_install_time // null ),
    enabled:              ( $by_pkg[$p].enabled // null ),
    version:              ( $by_pkg[$p].version_name // null ),
  }
