# timeline.kb — maintenance guide

Reconstructed **chain of events** for the infection, one file per moment or
tight grouping. This collection is the time-ordered narrative; the *evidence*
behind each claim lives in `../findings.kb/` and the gitignored captures.

## Filename convention

`<event-time>--<slug>.md` for a single event;
`<start>-<end>--<slug>.md` for a tight grouping or a bounded interval.

- `<event-time>` is the **event's** local timestamp in ISO-8601 to seconds,
  e.g. `2026-05-18T07:09:27`. Files sort chronologically by name.
- **Timezone is omitted from filenames and is always America/Chicago** — CDT
  (−05:00) for all May-2026 events. Stating it here avoids the `-05:00` offset
  colliding with the `start-end` range dash.
- Range entries use a single `-` between the two timestamps and `--` before the
  slug. Slugs are kebab-case.

## What belongs

**Structured data in YAML frontmatter; narrative in the body.** Frontmatter
fields:

- `when:` (single event) **or** `start:`/`end:` (range) — ISO-8601 **with**
  offset, e.g. `2026-05-18T07:09:27-05:00`. (Filenames drop the offset; here it
  is explicit.)
- `sources:` — list of cited artifacts (Takeout paths, a capture file under
  `forensics/<timestamp>/`, or `scripts/myactivity_takeout.py`). Quote paths
  containing spaces.
- `relates-to:` — thread(s): `[adware]`, `[card-fraud]`, `[general]`.

These fields are enforced by `../timeline.jsonschema.yaml` (single-event `when:`
XOR range `start:`/`end:`, offset mandatory); run `bin/llm.kb-validate`.

The body says what happened, in which source it is visible, and what it means
for the chain. Coarse/`Used` Play snapshots bound *that an app ran in a window*,
not when — say so. Keep interpretation labelled as such; keep raw event rows
verbatim.

## Scope (current)

Focused on the **2026-05-18 detonation window** — the last clean state, the
silent trigger gap, and the immediate cascade. Downstream same-day artifacts
(the Tencent APK fetch, the `_.admaster/` residue at 20:36) are recorded in
`../findings.kb/`; add later timeline entries only if they sharpen the chain.
