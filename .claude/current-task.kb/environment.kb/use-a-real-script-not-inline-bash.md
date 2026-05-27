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

**Pending (requested by the user):** a reusable forensic-report script under
`scripts/` that ingests a `forensics/<capture>/` dir and emits: logcat coverage
+ package install/remove events + crashes by package; usagestats removed-app
candidates (used-but-not-installed) with last-seen; suspicious-name/permission
flags; Downloads anomalies. Build this **first** next session, then use it to
finish the patient-zero hunt. Follow `~/.claude/must-read.kb/before/writing-python-code.md`.
