#!/usr/bin/env python3
"""Read and write the android-apps.kb reputation collection.

The kb classifies Android packages by reputation. The kb is flat — one file per
package, named for the package id — and the verdict (legitimate / adware /
malware / unknown) is the `verdict` frontmatter field, per
android-apps.jsonschema.yaml. `delisted` is an orthogonal frontmatter flag (Play
removed the listing).

  android_apps_kb.py list KB_DIR
      JSONL {"package","verdict","delisted"} for every classified package —
      feeds the allowlist + delisted flag into scripts/unknown-apps-timeline.jq.

  android_apps_kb.py seed KB_DIR < records.jsonl
      Write one <package>.md per input record. Each record is
      {"package","verdict","name", optional "category","confidence","source",
      "rationale","delisted","last_updated"}.
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

VERDICTS = ("legitimate", "adware", "malware", "unknown")

_VERDICT = re.compile(r'^verdict:\s*"?(\w+)"?', re.MULTILINE)
_DELISTED = re.compile(r"^delisted:\s*true\b", re.MULTILINE)


def classifications(kb: Path):
    for path in sorted(kb.glob("*.md")):
        if path.name == "CLAUDE.md":
            continue
        text = path.read_text(encoding="utf-8")
        match = _VERDICT.search(text)
        assert match, ("no verdict in frontmatter", path)
        verdict = match.group(1)
        assert verdict in VERDICTS, (verdict, path)
        yield {
            "package": path.stem,
            "verdict": verdict,
            "delisted": bool(_DELISTED.search(text)),
        }


def render_md(record) -> str:
    fields = {
        "package": record["package"],
        "verdict": record.get("verdict"),
        "name": record.get("name") or record["package"],
        "category": record.get("category"),
        "confidence": record.get("confidence"),
        "delisted": True if record.get("delisted") else None,
        "source": record.get("source") or "-",
        "last-updated": record.get("last_updated") or date.today().isoformat(),
    }
    # JSON scalars are valid YAML, so this quotes/escapes correctly.
    front = "\n".join(f"{k}: {json.dumps(v)}" for k, v in fields.items() if v is not None)
    body = (record.get("rationale") or "").strip()
    return f"---\n{front}\n---\n\n{body}\n"


def write_seed(kb: Path, records) -> int:
    count = 0
    for record in records:
        verdict = record["verdict"]
        assert verdict in VERDICTS, verdict
        out = kb / f"{record['package']}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_md(record), encoding="utf-8")
        count += 1
    return count


USAGE = "usage: android_apps_kb.py {list|seed} KB_DIR  (seed reads JSONL on stdin)"


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(USAGE)
    mode, kb_dir = sys.argv[1], sys.argv[2]
    kb = Path(kb_dir)
    match mode:
        case "list":
            for record in classifications(kb):
                print(json.dumps(record))
        case "seed":
            records = (json.loads(line) for line in sys.stdin if line.strip())
            print(f"wrote {write_seed(kb, records)} files under {kb}", file=sys.stderr)
        case _:
            sys.exit(USAGE)


if __name__ == "__main__":
    main()
