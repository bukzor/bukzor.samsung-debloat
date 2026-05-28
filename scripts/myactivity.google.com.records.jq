#!/usr/bin/env -S jq -rcf
# Google "My Activity" export (JSONL: one array per line) -> tidy JSONL events.
#
# Companion to myactivity.google.com.jq (which emits human-readable TSV); this
# emits one self-describing JSON object per event for downstream jq — package
# id, action, product, title, device, and the raw microsecond timestamp left
# unformatted so callers can sort/bucket/format as they like.
#
# Known indices in each row:
#   [4]       -> event time, MICROSECONDS since the Unix epoch
#   [7][0]    -> product (e.g. "Google Play Store")
#   [7][1]    -> product url  (carries details?id=<package>)
#   [9][0]    -> title / target
#   [9][2]    -> action ("Used" / "Visited" / "Searched for" / ...)
#   [9][3]    -> target url  (carries details?id=<package>)
#   [18][1]   -> alternate url
#   [19][0][0]-> device label
#
# Usage:
#   ./scripts/myactivity.google.com.records.jq forensics/myactivity.google.com.json
#   jq -rcf scripts/myactivity.google.com.records.jq forensics/myactivity.google.com.json

# package id from the first details?id= url present on the row
def pkg:
  [ .[7][1]?, .[9][3]?, .[18][1]? ]
  | map(select(type == "string") | capture("details\\?id=(?<p>[\\w.]+)").p?)
  | map(select(. != null))
  | (.[0] // null);

{
  when_us: .[4],
  action:  (.[9][2] // null),
  product: (.[7][0] // null),
  title:   (.[9][0] // .[7][0] // null),
  package: pkg,
  device:  (.[19][0][0] // null),
}
