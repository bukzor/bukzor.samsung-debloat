"""Tests for forensic_report. Fixtures are synthetic — no captured personal data."""

from datetime import datetime

from forensic_report import (
    UsageStat,
    download_anomalies,
    is_system_package,
    name_flags,
    parse_appop_holders,
    parse_crashes,
    parse_downloads,
    parse_installer_map,
    parse_logcat_coverage,
    parse_manifest,
    parse_package_list,
    parse_pkg_events,
    parse_ts,
    parse_usagestats,
    removed_app_candidates,
    suspicious_matches,
)


class DescribeParseTs:
    def it_parses_a_plain_timestamp(self):
        assert parse_ts("2026-05-21 12:46:03") == datetime(2026, 5, 21, 12, 46, 3)

    def it_parses_a_millisecond_timestamp(self):
        assert parse_ts("2026-05-21 12:46:03.036") == datetime(2026, 5, 21, 12, 46, 3, 36000)

    def it_treats_the_epoch_sentinel_as_never(self):
        assert parse_ts("1969-12-31 18:00:00") is None

    def it_treats_blank_as_never(self):
        assert parse_ts("   ") is None


class DescribeIsSystemPackage:
    def it_flags_vendor_and_carrier_packages(self):
        assert is_system_package("com.android.settings")
        assert is_system_package("com.samsung.android.lool")
        assert is_system_package("com.verizon.mips.services")

    def it_does_not_flag_third_party_apps(self):
        assert not is_system_package("com.netflix.mediaclient")
        assert not is_system_package("com.forecasts.noaa.live.weather")


class DescribeParsePackageList:
    def it_strips_the_package_prefix(self):
        text = "package:com.netflix.mediaclient\npackage:com.bose.monet\n"
        assert parse_package_list(text) == frozenset(
            {"com.netflix.mediaclient", "com.bose.monet"}
        )


class DescribeParseInstallerMap:
    def it_maps_package_to_installer(self):
        text = (
            "package:com.imdb.mobile  installer=com.android.vending\n"
            "package:com.samsung.android.emergency  installer=null\n"
        )
        result = parse_installer_map(text)
        assert result["com.imdb.mobile"] == "com.android.vending"
        assert result["com.samsung.android.emergency"] == "null"


class DescribeParseAppopHolders:
    def it_reads_bare_package_lines(self):
        assert parse_appop_holders("com.mobile.uhc\ncom.pbs.video\n") == frozenset(
            {"com.mobile.uhc", "com.pbs.video"}
        )

    def it_returns_empty_for_no_operations(self):
        assert parse_appop_holders("No operations.\n") == frozenset()


class DescribeParseUsagestats:
    summary = (
        '      package=com.play2248.block.numbers.merge totalTimeUsed="01:40" '
        'lastTimeUsed="2026-05-25 12:41:29" totalTimeVisible="01:45" '
        'lastTimeVisible="2026-05-25 12:41:29" '
        'lastTimeComponentUsed="2026-05-25 12:40:59" totalTimeFS="00:00" '
        'lastTimeFS="1969-12-31 18:00:00" appLaunchCount=3 \n'
    )
    never = (
        '      package=com.weather.forecast.news totalTimeUsed="00:00" '
        'lastTimeUsed="1969-12-31 18:00:00" totalTimeVisible="00:00" '
        'lastTimeVisible="1969-12-31 18:00:00" '
        'lastTimeComponentUsed="2026-05-26 08:43:12" totalTimeFS="00:00" '
        'lastTimeFS="1969-12-31 18:00:00" appLaunchCount=0 \n'
    )

    def it_records_foregrounded_use_with_launch_count(self):
        stats = parse_usagestats(self.summary)
        merge = stats["com.play2248.block.numbers.merge"]
        assert merge.foregrounded is True
        assert merge.launch_count == 3
        assert merge.last_active == datetime(2026, 5, 25, 12, 41, 29)

    def it_records_background_only_apps_via_component_use(self):
        stats = parse_usagestats(self.never)
        news = stats["com.weather.forecast.news"]
        assert news.foregrounded is False
        assert news.launch_count == 0
        # component-used time still counts as "last active"
        assert news.last_active == datetime(2026, 5, 26, 8, 43, 12)

    def it_takes_the_latest_activity_across_windows(self):
        older = self.summary
        newer = self.summary.replace("2026-05-25 12:41:29", "2026-05-26 09:00:00")
        stats = parse_usagestats(older + newer)
        assert stats["com.play2248.block.numbers.merge"].last_active == datetime(
            2026, 5, 26, 9, 0, 0
        )

    def it_folds_in_the_event_log(self):
        event = (
            '    time="2026-05-25 18:22:23" type=ACTIVITY_RESUMED '
            "package=com.walmart.android class=Foo\n"
        )
        stats = parse_usagestats(event)
        assert stats["com.walmart.android"].foregrounded is True
        assert stats["com.walmart.android"].last_active == datetime(2026, 5, 25, 18, 22, 23)


class DescribeParseLogcatCoverage:
    def it_bounds_each_buffer_section(self):
        text = [
            "--------- beginning of crash",
            "2026-05-21 12:46:03.036  8175  8198 E AndroidRuntime: FATAL EXCEPTION: x",
            "2026-05-22 09:00:00.000  1  1 I Tag: y",
            "--------- beginning of main",
            "2026-05-26 19:20:16.350  5740 5740 I Tag: z",
        ]
        cov = {c.buffer: c for c in parse_logcat_coverage(text)}
        assert cov["crash"].first == datetime(2026, 5, 21, 12, 46, 3)
        assert cov["crash"].last == datetime(2026, 5, 22, 9, 0, 0)
        assert cov["main"].first == datetime(2026, 5, 26, 19, 20, 16)


class DescribeParseCrashes:
    def it_attributes_a_fatal_to_the_following_process_line(self):
        lines = [
            "2026-05-21 12:46:03.036  8175  8198 E AndroidRuntime: FATAL EXCEPTION: main",
            "2026-05-21 12:46:03.036  8175  8198 E AndroidRuntime: Process: com.test.weather, PID: 8175",
            "2026-05-21 12:46:03.036  8175  8198 E AndroidRuntime: java.lang.IllegalStateException",
        ]
        crashes = parse_crashes(lines)
        assert crashes == [Crash_("com.test.weather", datetime(2026, 5, 21, 12, 46, 3))]

    def it_reports_unknown_when_no_process_line(self):
        lines = ["2026-05-21 12:46:03.036  1 1 E AndroidRuntime: FATAL EXCEPTION: main"]
        assert parse_crashes(lines)[0].package == "unknown"


class DescribeParsePkgEvents:
    def it_extracts_install_and_remove_lines(self):
        lines = [
            "2026-05-19 10:00:00.000 1 1 I PackageManager: Finished install of com.test.dropper",
            "2026-05-25 11:00:00.000 1 1 I PackageManager: Removing package com.test.adware",
        ]
        events = parse_pkg_events(lines)
        assert [(e.package, e.kind) for e in events] == [
            ("com.test.dropper", "Finished install of"),
            ("com.test.adware", "Removing package"),
        ]


class DescribeParseDownloads:
    listing = (
        "/sdcard/Download:\n"
        "total 32435\n"
        "-rwxrwx--- 1 u0_a316 media_rw 33166208 2026-05-25 10:05 20260519_abc_offset_1.apk\n"
        "-rwxrwx--- 1 u0_a316 media_rw      871 2026-05-24 11:55 AppointmentReminder.ics\n"
        "drwxrws--- 2 u0_a316 media_rw     3452 2026-05-18 20:36 _.admaster\n"
        "\n"
        "/sdcard/Download/_.admaster:\n"
        "total 4\n"
        "-rwxrwx--- 1 u0_a316 media_rw 108 2026-05-18 20:36 ._u_i_d_f_k.txt\n"
    )

    def it_parses_entries_with_their_directory(self):
        entries = parse_downloads(self.listing)
        names = {(e.directory, e.name, e.is_dir) for e in entries}
        assert ("/sdcard/Download", "20260519_abc_offset_1.apk", False) in names
        assert ("/sdcard/Download", "_.admaster", True) in names
        assert ("/sdcard/Download/_.admaster", "._u_i_d_f_k.txt", False) in names

    def it_flags_apk_hidden_names_and_date_drift(self):
        reasons = {r for _, r in download_anomalies(parse_downloads(self.listing))}
        assert any("APK" in r for r in reasons)
        assert any("hidden" in r for r in reasons)
        assert any("filename date 2026-05-19" in r for r in reasons)


class DescribeParseManifest:
    def it_skips_the_header_and_reads_exit_codes(self):
        text = "name\texit\tbytes\tcmd\ngetprop\t0\t60764\tadb shell getprop\nx\t1\t0\tcmd\n"
        assert parse_manifest(text) == [
            ("getprop", 0, "adb shell getprop"),
            ("x", 1, "cmd"),
        ]


class DescribeRemovedAppCandidates:
    def it_returns_active_uninstalled_third_party_apps_newest_first(self):
        usage = {
            "com.test.installed": UsageStat("com.test.installed", datetime(2026, 5, 26, 1, 0), True, 1),
            "com.test.old": UsageStat("com.test.old", datetime(2026, 5, 20, 1, 0), True, 1),
            "com.test.recent": UsageStat("com.test.recent", datetime(2026, 5, 25, 1, 0), False, 0),
            "com.test.never": UsageStat("com.test.never", None, False, 0),
            "com.android.systemthing": UsageStat("com.android.systemthing", datetime(2026, 5, 26, 1, 0), True, 1),
        }
        result = removed_app_candidates(usage, frozenset({"com.test.installed"}))
        assert [s.package for s in result] == ["com.test.recent", "com.test.old"]


class DescribeNameFlags:
    def it_flags_pup_keywords_as_a_weak_signal(self):
        assert "antivirus" in suspicious_matches("com.utils.antivirustoolkit")
        flagged = name_flags(["com.junkeraser.clean", "com.netflix.mediaclient"])
        assert "com.junkeraser.clean" in flagged
        assert "com.netflix.mediaclient" not in flagged


# Small constructor alias so the crash test reads cleanly.
def Crash_(package, when):
    from forensic_report import Crash

    return Crash(package, when)
