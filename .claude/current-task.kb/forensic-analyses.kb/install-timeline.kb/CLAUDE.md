# install-timeline.kb — maintenance guide

Analyses that reconstruct **when and how apps were installed**, to place the
infection in time and point at patient zero. See `../CLAUDE.md` for the shared
schema and lifecycle.

Belongs here: timeline/provenance analyses over package + usagestats data. Not
here: artifact/dropper analyses (→ `../dropper-artifacts.kb/`) or capability
abuse (→ `../capability-abuse.kb/`).

Tooling: `scripts/package_dump.py` turns a `package-dump-full.txt` capture into
per-package install-provenance JSONL — installer, `firstInstallTime`, last
update, enabled — one package per line; filter/sort with jq.
