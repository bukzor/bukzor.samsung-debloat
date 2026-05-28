# Non-trivial data processing goes in a committed, reusable script

The moment work stops being one safe command — parsing a dump, decoding a
protobuf, aggregating activity, diffing package lists — **write a committed
script under `scripts/`**, not ephemeral inline code. This means *any* language:
a bash heredoc, `python3 -c '…'`, and `python3 - <<'PY'` are all the same
anti-pattern. (This rule started life as "not inline *bash*"; that was
overspecified — the session that wrote it then violated it with inline *Python*
heredocs. The language is irrelevant; throw-away-ness is the problem.)

Inline code is unreviewable, untested, and discarded the turn it runs. A
committed script is diffable, testable, and reusable by the next agent — and you
stop re-deriving the same parser every time the question shifts slightly.

## Reusability: emit JSONL, explore with jq

Separate the stable part from the ad-hoc part:

- The **script** does the hard, stable work — parse the messy source *once* and
  emit **JSONL** (one self-describing record per line) to stdout. Bake in no
  filtering, ranking, or presentation.
- **jq** does the ad-hoc work — filter, join, aggregate, histogram, sort. A new
  question is a new jq one-liner, not an edit to the script.

Payoff: the parser stops churning, intermediate results stay greppable/diffable,
and exploration leaves no untracked code behind.

## Bash-specific gotchas (one instance of the general rule)

The interactive shell runs `set -e -o pipefail`, so casual one-liners abort on
*expected* conditions, wasting turns:

- `var=$(grep … | …)` dies when `grep` finds nothing (no-match = exit 1,
  pipefail propagates, `set -e` aborts).
- `sort -t'≈'` fails: `-t` needs a single-byte delimiter. `printf '--- …'`
  parses `--` as an option terminator.
- Per-item shell loops over big dumps are fragile and slow.

## Build it tested; announce it where it'll be found

Each capture analysis is its own tested extractor under `scripts/`: JSONL out,
jq for the rest; pure parsers with I/O only in `main`; `pyproject.toml` enables
the `Describe`/`it_` pytest convention. Run tests: `uv run pytest`. Follow
`~/.claude/must-read.kb/before/writing-python-code.md`.

A script worth reusing earns one line in the `CLAUDE.md` nearest where the next
agent will reach for it — the kb or directory it serves — so they inherit the
tool, not the blank slate.
