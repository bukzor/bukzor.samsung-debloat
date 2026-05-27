--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# forensic-sources.kb — maintenance guide

The **data inventory**: every on-device source worth capturing for this
investigation — what it is, the exact capture command, and the **state of the
local capture** (`capture-status`, `captured-as`, `needs-device`). Schema'd by
`../forensic-sources.jsonschema.yaml`.

Purpose: the single place to answer *"what data exists on the phone, and have we
collected it yet — if not, what's missing?"* It is an **inventory, not a work
queue**, so items persist; when a source is captured, set `capture-status` and
list `captured-as`, don't delete it.

Organized into nested sub-collections by domain — `packages.kb/`, `activity.kb/`,
`capabilities.kb/`, `logs.kb/`, `storage.kb/`, `identity-network.kb/`,
`telephony.kb/`. Each sub-collection carries a **symlinked** copy of the schema
(`<sub>.jsonschema.yaml → ../forensic-sources.jsonschema.yaml`) until
`llm.kb-validate` gains `$ref` support (noted in the sessions.kb entry); on a
*partial* schema match, copy-paste instead and leave a `#TODO`.

Belongs here: a discrete data source + capture command + capture state. Does NOT
belong here: what to *do* with the data (→ `../forensic-analyses.kb/`),
conclusions drawn (→ `../findings.kb/`), or tooling gotchas
(→ `../environment.kb/`). Keep personal data in `forensics/` only — name capture
files, never quote their contents here.
