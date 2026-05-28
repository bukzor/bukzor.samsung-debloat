#!/usr/bin/env -S jq -srf
# Gap analysis for a Google "My Activity" export (JSONL, one array per line).
#
# Reports the time span covered and every gap between consecutive events that
# meets a threshold, so silent windows stand out.
#
# Event time is index [4], MICROSECONDS since the Unix epoch.
# Times are rendered in local zone ($TZ / /etc/localtime). jq's %z/%Z are
# unreliable (see myactivity.google.com.jq), so the numeric offset is derived:
# mktime reads a broken-down array as UTC, so (mktime(localtime) - epoch) is
# exactly the local UTC offset in seconds.
#
# Usage (the -S shebang slurps the whole file with -s):
#   ./scripts/myactivity.google.com.gap-analysis.jq forensics/myactivity.google.com.json
#   jq -srf scripts/myactivity.google.com.gap-analysis.jq forensics/myactivity.google.com.json
# Override the gap threshold (hours; default 2):
#   ./scripts/myactivity.google.com.gap-analysis.jq --argjson gap_hours 4 forensics/myactivity.google.com.json

(($ARGS.named.gap_hours // 2) | tonumber) as $threshold_h

| def pad2: tostring | ("0" + .)[-2:];

  def fmt:
    (. / 1000000 | floor) as $sec
    | ($sec | localtime) as $lt
    | (($lt | mktime) - $sec) as $off
    | (if $off < 0 then "-" else "+" end) as $sign
    | ($off | fabs) as $a
    | ($lt | strftime("%Y-%m-%dT%H:%M:%S"))
      + $sign + ($a / 3600 | floor | pad2)
      + ":"  + (($a % 3600) / 60 | floor | pad2);

  def hours: . / 1000000 / 3600;

  ([.[] | .[4]] | sort) as $t
  | ($t | length) as $n
  | "events:   \($n)",
    "earliest: \($t[0]  | fmt)",
    "latest:   \($t[-1] | fmt)",
    "span:     \(($t[-1] - $t[0] | hours / 24 * 100 | round / 100)) days",
    "",
    "gaps >= \($threshold_h)h:",
    ( [ range(1; $n)
        | { gap: ($t[.] - $t[.-1]), after: ($t[.-1] | fmt), before: ($t[.] | fmt) }
      ]
      | map(select(.gap | hours >= $threshold_h))
      | if length == 0 then "  (none)"
        else .[] | "  \(.gap | hours * 10 | round / 10)h\t\(.after)  ->  \(.before)"
        end )
