"""Tests for package_dump. Fixtures are synthetic — no captured personal data."""

from package_dump import package_record, parse_user0, records, split_blocks

DUMP = """\
Packages:
  Package [com.example.app] (28d8894):
    versionName=4.53.0
    timeStamp=2026-05-26 16:23:19
    lastUpdateTime=2026-05-26 16:23:20
    installerPackageName=com.android.vending
    codePath=/data/app/~~abc==/com.example.app-xyz==
    User 0: ceDataInode=1 installed=true hidden=false enabled=0 stopped=false
      installReason=4
      firstInstallTime=2026-05-26 15:50:06
      uninstallReason=0
    User 150: ceDataInode=0 installed=false enabled=0
      firstInstallTime=1969-12-31 18:00:00
  Package [com.android.systemstub] (deadbeef):
    versionName=12
    installerPackageName=null
    codePath=/system/app/SystemStub
    User 0: ceDataInode=9 installed=true hidden=false enabled=2 stopped=false
      firstInstallTime=1970-02-14 04:18:20
Hidden system packages:
  Package [com.android.systemstub] (deadbeef):
    versionName=11
"""


class DescribeSplitBlocks:
    def it_yields_each_package_once_keeping_first_occurrence(self):
        names = [pkg for pkg, _ in split_blocks(DUMP)]
        assert names == ["com.example.app", "com.android.systemstub"]

    def it_keeps_the_live_block_not_the_hidden_repeat(self):
        blocks = dict(split_blocks(DUMP))
        assert "versionName=12" in blocks["com.android.systemstub"]
        assert "versionName=11" not in blocks["com.android.systemstub"]


class DescribeParseUser0:
    def it_reads_user0_install_state(self):
        block = dict(split_blocks(DUMP))["com.example.app"]
        assert parse_user0(block) == {
            "installed": True,
            "enabled": "default",
            "first_install_time": "2026-05-26 15:50:06",
        }

    def it_maps_the_enabled_integer_to_a_state(self):
        block = dict(split_blocks(DUMP))["com.android.systemstub"]
        assert parse_user0(block)["enabled"] == "disabled"


class DescribePackageRecord:
    def it_extracts_install_provenance(self):
        block = dict(split_blocks(DUMP))["com.example.app"]
        assert package_record("com.example.app", block) == {
            "package": "com.example.app",
            "version_name": "4.53.0",
            "installer": "com.android.vending",
            "timestamp": "2026-05-26 16:23:19",
            "last_update_time": "2026-05-26 16:23:20",
            "code_path": "/data/app/~~abc==/com.example.app-xyz==",
            "installed": True,
            "enabled": "default",
            "first_install_time": "2026-05-26 15:50:06",
        }

    def it_reports_a_null_installer_as_none(self):
        block = dict(split_blocks(DUMP))["com.android.systemstub"]
        assert package_record("com.android.systemstub", block)["installer"] is None


class DescribeRecords:
    def it_emits_one_record_per_distinct_package(self):
        out = list(records(DUMP))
        assert [r["package"] for r in out] == [
            "com.example.app",
            "com.android.systemstub",
        ]
