# Fold app_reputation_probe.py signals into android-apps.kb frontmatter (the
# `probe` object of android-apps.jsonschema.yaml), emitting md-frontmatter-set
# records ({path, "@value"}) — structured data, no prose.
#
# md-frontmatter-set REPLACES a file's frontmatter with `@value` (its leaf-diff
# only minimizes churn; absent keys are deleted), so `@value` must be the FULL
# desired frontmatter. We therefore merge the probe object INTO each file's
# current frontmatter rather than emitting a partial patch.
#
# Driven by scripts/app_reputation_to_kb.sh, which supplies:
#   --slurpfile probe <probe JSONL>   one app_reputation_probe.py record each
#   --slurpfile cur   <current JSONL>  one {package, fm} per existing kb file
#   --arg date <YYYY-MM-DD>            probe date
#   --arg dir  <kb dir/>               e.g. .../android-apps.kb/
# Run with `jq -n`.

( $cur | map({ key: .package, value: .fm }) | from_entries ) as $by_pkg
| $probe[]
| ( $by_pkg[.package] // {} ) as $fm
| ( {
      found,
      developer,
      developer_id,
      developer_email,
      developer_website,
      genre,
      min_installs,
      score,
      ratings,
      ad_supported,
      contains_ads,
      permissions,
    }
    # found:false records carry only `found`; drop the rest
    | with_entries(select(.value != null)) ) as $sig
| {
    path: ($dir + .package + ".md"),
    "@value": ( $fm + {
      "last-updated": $date,
      probe: ({ date: $date } + $sig),
    } ),
  }
