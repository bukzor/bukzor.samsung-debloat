--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# forensic-analyses.kb — maintenance guide

The **processing backlog**: every analysis worth running over captured data —
its method, the source(s) it `consumes`, the question/thread it `answers`, and
`status`. The analytical judgments (`confidence`, `reaches-window`,
`survives-uninstall`) live here, not on the raw sources. Schema'd by
`../forensic-analyses.jsonschema.yaml`.

Purpose: let an **analysis session** pick up work independently of a
**collection session** — `status: blocked` marks analyses waiting on a
not-yet-captured source (follow `consumes` → `../forensic-sources.kb/`).

Organized into nested sub-collections — `install-timeline.kb/`,
`dropper-artifacts.kb/`, `crashes-persistence.kb/`, `capability-abuse.kb/`,
`card-fraud.kb/`, `synthesis.kb/`. Each carries a **symlinked** copy of the
schema (`<sub>.jsonschema.yaml → ../forensic-analyses.jsonschema.yaml`) until
`llm.kb-validate` gains `$ref` (see the sessions.kb entry).

Belongs here: an analysis task with a method. Does NOT belong here: the raw
sources (→ `../forensic-sources.kb/`) or the conclusions produced (→
`../findings.kb/`; the finding cites the analysis). When an analysis is run,
record its result as a finding and set `status: done` — kept (not removed) for
now, since this collection was brain-dumped exhaustively.
