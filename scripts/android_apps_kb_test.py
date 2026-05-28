"""Tests for android_apps_kb. Fixtures are synthetic — no captured personal data."""

import pytest

from android_apps_kb import classifications, render_md, write_seed


class DescribeRenderMd:
    def it_emits_required_frontmatter_and_body(self):
        md = render_md(
            {
                "package": "com.x.y",
                "verdict": "adware",
                "name": "Foo",
                "source": "http://e",
                "category": "cleaner",
                "confidence": "high",
                "rationale": "does X",
                "last_updated": "2026-05-27",
            }
        )
        assert md.startswith("---\n")
        assert 'package: "com.x.y"' in md
        assert 'verdict: "adware"' in md
        assert 'name: "Foo"' in md
        assert 'source: "http://e"' in md
        assert 'last-updated: "2026-05-27"' in md
        assert md.rstrip().endswith("does X")

    def it_omits_verdict_when_absent(self):
        assert "verdict" not in render_md({"package": "com.x.y"})

    def it_omits_delisted_when_falsey(self):
        assert "delisted" not in render_md({"package": "com.x.y"})

    def it_writes_delisted_true_when_set(self):
        assert "delisted: true" in render_md({"package": "com.x.y", "delisted": True})

    def it_defaults_name_to_package_and_source_to_dash(self):
        md = render_md({"package": "com.x.y"})
        assert 'name: "com.x.y"' in md
        assert 'source: "-"' in md


class DescribeSeedAndList:
    def it_round_trips_verdict_and_delisted(self, tmp_path):
        records = [
            {"package": "com.good.app", "verdict": "legitimate", "name": "Good"},
            {"package": "com.gone.app", "verdict": "unknown", "delisted": True},
        ]
        assert write_seed(tmp_path, records) == 2
        got = {r["package"]: r for r in classifications(tmp_path)}
        assert got == {
            "com.good.app": {"package": "com.good.app", "verdict": "legitimate", "delisted": False},
            "com.gone.app": {"package": "com.gone.app", "verdict": "unknown", "delisted": True},
        }

    def it_files_each_record_flat_at_kb_root(self, tmp_path):
        write_seed(tmp_path, [{"package": "com.a.b", "verdict": "adware", "name": "A"}])
        assert (tmp_path / "com.a.b.md").exists()

    def it_skips_claude_md(self, tmp_path):
        (tmp_path / "CLAUDE.md").write_text("---\nrequires: []\n---\n", encoding="utf-8")
        write_seed(tmp_path, [{"package": "com.a.b", "verdict": "adware"}])
        assert [r["package"] for r in classifications(tmp_path)] == ["com.a.b"]

    def it_reads_an_unquoted_verdict(self, tmp_path):
        (tmp_path / "com.c.d.md").write_text(
            "---\npackage: com.c.d\nverdict: malware\n---\n", encoding="utf-8"
        )
        assert [r["verdict"] for r in classifications(tmp_path)] == ["malware"]


class DescribeWriteSeed:
    def it_rejects_an_unknown_verdict(self, tmp_path):
        with pytest.raises(AssertionError):
            write_seed(tmp_path, [{"package": "com.a.b", "verdict": "bogus"}])
