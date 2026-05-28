#!/usr/bin/env -S jq -rf
# Prettify Google "My Activity" export rows into readable local-time records.
#
# The export is JSONL: one array per line. Known indices:
#   [4]    -> event time, MICROSECONDS since the Unix epoch
#   [7][0] -> product (e.g. "Google Play Store")
#   [9][0] -> title / target
#   [9][2] -> action (e.g. "Visited")
#   [9][3] -> url (when present)
#
# Output: TSV of  local-time \t product \t action \t title \t url
#
# Usage (local time honours $TZ / /etc/localtime):
#   ./scripts/myactivity.google.com.jq forensics/myactivity.google.com.json
#   jq -rf scripts/myactivity.google.com.jq forensics/myactivity.google.com.json
#
# Note: jq's strftime("%z"/"%Z") is unreliable here — %z prints +0000 and %Z
# ignores DST (prints CST in summer). We derive the numeric offset ourselves:
# feeding a localtime broken-down array to mktime reinterprets it as UTC, so
# (that epoch - the real epoch) is exactly the local UTC offset in seconds.

def pad2: tostring | ("0" + .)[-2:];

def fmt_local:
  (. % 1000000) as $us
  | (. / 1000000 | floor) as $sec
  | ($sec | localtime) as $lt
  | (($lt | mktime) - $sec) as $off
  | (if $off < 0 then "-" else "+" end) as $sign
  | ($off | fabs) as $a
  | ($lt | strftime("%Y-%m-%dT%H:%M:%S"))
    + "." + (("000000" + ($us | tostring)) | .[-6:])
    + $sign + ($a / 3600 | floor | pad2)
    + ":"  + (($a % 3600) / 60 | floor | pad2);

[ (.[4] | fmt_local),
  (.[7][0] // ""),
  (.[9][2] // ""),
  (.[9][0] // ""),
  (.[9][3] // "")
] | @tsv
