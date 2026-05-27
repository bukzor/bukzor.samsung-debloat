# Use a real script for non-trivial parsing — not inline bash

Hard-won this session. The interactive shell here runs **`set -e -o pipefail`**,
so casual one-liners abort in ways that waste turns and frustrate the user:

- `var=$(grep ... | ...)` dies when `grep` finds nothing (no-match = exit 1,
  pipefail propagates, `set -e` aborts — even though "no match" is expected).
- `sort -t'≈'` fails: `-t` needs a single-byte delimiter.
- `printf '--- ...'` parses `--` as an option terminator.
- Per-item shell loops over big dumps are fragile and slow.

Rule: the moment analysis stops being a trivial one-liner (parsing
`usagestats.txt`, multi-buffer `logcat`, diffing package lists), **write a
committed, tested script** — Python preferred for parsing. Inline bash is for
one safe command, not data processing.

**Built:** `scripts/forensic_report.py` (+ `forensic_report_test.py`, and a root
`pyproject.toml` enabling the `Describe`/`it_` pytest convention). Pure parsers,
I/O only in `main()`, 23 tests green. It ingests a `forensics/<capture>/` dir and
reports: logcat buffer coverage, crashes-by-package, package install/remove
events (none present — buffers too shallow), usagestats removed-app candidates,
name-heuristic flags, third-party appop holders, and Download anomalies.

Rule going forward: each new **analysis** that parses a capture
(`../forensic-analyses.kb/`) gets its own tested parser in
`scripts/forensic_report.py`, never inline bash. Run the report:
`python3 scripts/forensic_report.py forensics/<capture>`. Run tests:
`uv run --no-project --with pytest pytest scripts/`. Follow
`~/.claude/must-read.kb/before/writing-python-code.md`.
