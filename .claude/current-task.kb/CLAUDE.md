--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# Current-task knowledge base

Durable memory for the **in-progress** task: forensic investigation of a
family member's compromised Samsung phone, then a factory wipe, then a
de-Samsung/debloat pass. Write facts here as they are established so they
survive context compaction and the device wipe. See `README.md` for the
current layout.

This kb is **transient**. When the task is fully done, delete
`current-task.kb/` or distil it into a `docs/devlog/` entry — do not let it
masquerade as permanent project documentation.

## Collections

- `findings.kb/` — evidence-backed forensic findings, one per file, schema'd by
  `findings.jsonschema.yaml`.
- `forensic-sources.kb/` — inventory of on-device data sources + capture state,
  in domain sub-collections; schema'd by `forensic-sources.jsonschema.yaml`.
- `forensic-analyses.kb/` — analysis backlog over that data (method, consumed
  sources, status), in sub-collections; schema'd by `forensic-analyses.jsonschema.yaml`.
- `environment.kb/` — operational facts/gotchas for working this task (how to
  connect, toolchain quirks, data-handling, method caveats).
- `open-questions.kb/` — currently-open known-unknowns, one per file; remove a
  file when its question is answered and write the answer into `findings.kb/`.
- `android-apps.kb/` — per-package reputation verdicts (legitimate / adware /
  malware / unknown, plus a `delisted` flag), one flat file per package with the
  verdict in frontmatter; schema'd by `android-apps.jsonschema.yaml`. Feeds the
  "remove the known" residue tooling (`scripts/unknown-apps-timeline.jq` via
  `scripts/android_apps_kb.py list`).

Single-topic root `.md` files (mission, device, history) hold context that
isn't a homogeneous collection; promote one to a `.kb/` only under growth
pressure.

## Maintenance

Cite the captured artifact a finding rests on (captures live under the
gitignored `forensics/<timestamp>/`). When evidence shifts a finding, edit it
in place and bump `last-updated`; flip `status` to `ruled-out` rather than
deleting a dismissed hypothesis. Keep personal data (identity, account names,
phone/card numbers) in `forensics/` only — never in this kb or any committed
file.
