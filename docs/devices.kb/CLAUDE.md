--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
---

# devices.kb — maintenance guide

One file per **physical device** this project has worked on. This is the
registry the devlog refers to — the devlog is *when* things happened; this is
*which hardware* they happened to. It exists because device identity across
sessions was ambiguous (a previous owner's-phone assumption caused a real
error): the same owner can go through several phones over time.

Belongs here: a real device with an owner and a lifecycle (acquired → active →
retired/replaced). Frontmatter per `../devices.jsonschema.yaml`.

Does NOT belong here: session narratives (→ `docs/devlog/`), transient
per-session device notes (→ `.claude/current-task.kb/`), or app/package
decisions (→ README / devlog).

Naming: `<owner>-phone-<NN>-<model-slug>.md`, `NN` ordered by acquisition.
Update `status` to `retired` (with `retired:` date) when a device is replaced;
never delete a retired device — its devlogs still reference it.
