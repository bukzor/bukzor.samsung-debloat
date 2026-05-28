# android-apps.kb — maintenance guide

One file per **Android app package**, recording a reputation verdict so the
residue tooling can "remove the known" and zoom in on the concerning apps.

The kb is **flat**: one file per package, the filename is the **package id**
(unique — app names are not, and collide heavily in this data). The verdict is
the frontmatter **`verdict`** field, one of:

- `legitimate` — a real app from an identifiable developer doing its stated
  job. May be ad-supported. Not a concern.
- `adware` — "normal bad software": intrusive ads, after-call ad injection,
  scareware popups, launcher/home-screen hijack, deceptive monetization.
  Abusive and annoying, but operating *within* (or merely over-using) the
  permissions it was granted. **Not the primary concern.**
- `malware` — **the concern**: abuse that goes **beyond ad-spam** — covert
  capability abuse evading the app's permission scope (accessibility
  keylogging, SMS interception, hidden device-admin, remote control, covert
  charges, dropping apps / blocking uninstall). Reserve it for **real
  evidence**: device-side proof (appops, accessibility, APK) or corroborated
  high-signal user reports (weighted Play reviews — `scripts/app_reviews_probe.py`),
  not a generic AV label or one angry review. How strong the evidence is rides
  on `confidence`.
- `unknown` — researched, but evidence is insufficient to place.

Orthogonal axis — frontmatter `confidence` (strength of the evidence behind the
verdict, *not* how bad the app is):

- `high` — device-side proof, or a body of corroborated high-signal reports;
  the call would survive scrutiny.
- `medium` — a live Play listing whose metadata (developer, installs,
  permissions, reviews) fits the verdict, but no behavioural proof.
- `low` — thin or absent source: a name match, a single glance, or inference.

Orthogonal flag — frontmatter `delisted: true`: the exact package no longer
resolves to a live Play Store listing, although it *was* Play-served when the
subject visited it (per My Activity). High signal — Play removed it —
independent of the behaviour verdict; a delisted app may sit in any bucket.

Filename = exact package id + `.md` (e.g. `com.spotify.music.md`). Frontmatter
conforms to `../android-apps.jsonschema.yaml`; cite the `source` that justifies
the verdict.

Belongs here: a per-package reputation judgement with a cited source. Does NOT
belong here: device-specific forensic conclusions (→ `../findings.kb/`) or the
residue/timeline method itself (→ `../environment.kb/`).

## Spot-checking an app — the probe toolkit

To research a package's verdict (the off-device half; device-side proof still
trumps all), `scripts/` has four token-cheap probes that hit real JSON
endpoints, no HTML scraping. Each is self-documenting — read its module
docstring for purpose + runnable usage:

- `scripts/app_reputation_probe.py` — Play metadata as JSONL: developer
  identity, install scale, rating, ad posture, full permission list. The
  bread-and-butter `unknown` → verdict move. `found: false` ⇒ no *live* listing.
- `scripts/app_reviews_probe.py` — weighted Play user reviews (one record per
  review, with `thumbs_up`). The adware-vs-`malware` discriminator: a heavily
  upvoted "it sent texts / charged my card" review is the malware tell.
- `scripts/wayback_probe.py` — Wayback CDX capture history of the Play listing.
  Pairs with the reputation probe's `found: false` to split **delisted** (was on
  Play, now gone — set `delisted: true`) from **never-on-Play** (sideloaded).
- `scripts/app_reputation_probe.frontmatter.jq` — folds reputation-probe signals
  into each file's `probe` frontmatter object (see `../android-apps.jsonschema.yaml`).

Reclassify by editing the `verdict` field and bumping `last-updated`. Consumed
by `scripts/android_apps_kb.py list`, which feeds the verdicts + delisted flag
into `scripts/unknown-apps-timeline.jq`.
