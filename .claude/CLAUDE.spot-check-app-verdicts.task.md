---
status: not-started
created: "2026-05-27"
---

# Task: spot-check the agent-produced app verdicts

## Problem

The "remove the known" residue analysis (`scripts/unknown-apps-timeline.jq`, fed
by `scripts/android_apps_kb.py list`) rests on a reputation classification of
every third-party app seen on the subject device. That classification lives in
`current-task.kb/android-apps.kb/` — a flat collection (one file per package),
verdict in frontmatter (`legitimate` / `adware` / `malware` / `unknown`) plus a
`delisted` flag.

The verdicts were produced by LLM web-research sub-agents, in two passes:

1. an initial reputation sweep over every residue package, and
2. a deep-hunt over the `unknown` ones (Exodus Privacy, APK mirrors, the Wayback
   Machine, malware sandboxes) to recover developers, permissions, and trackers.

LLM research is fallible in ways that bite here:

- fabricated or misremembered source URLs;
- developer / identity misattribution;
- conflating a same-named but **different-package** app — rife in this dataset
  (dozens of near-identical "Spades" and generic "Weather"/"Cleaner" titles);
- over- or under-classification — clearing an app as `legitimate` on thin
  evidence, or parking one in `unknown` when a determination was actually available.

These verdicts are load-bearing. A wrong `legitimate` silently removes a bad app
from the residue; a wrong `adware`/`unknown` misdirects attention; and the set
ultimately informs what we conclude about the device and whether anything still
warrants action before the wipe. The classification should not be trusted until
an independent pass has spot-checked it.

## Scope

To be specified later — which verdicts to sample, how to re-verify a verdict,
what distinguishes a confirmed from an overturned one, and how corrections are
recorded back into `android-apps.kb/`.
