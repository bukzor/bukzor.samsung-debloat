---
start: "2026-05-18T13:50:09-05:00"
end: "2026-05-18T20:35:33-05:00"
relates-to: [adware]
sources:
  - forensics/myactivity.google.com.json
  - scripts/myactivity.google.com.records.jq
---

# 2026-05-18 13:50 → 20:35 CDT — user fights back: installs real (Norton) antivirus

While the automated PPI cascade ran
(`2026-05-18T07:09:27-2026-05-18T07:36:47--detonation-cascade-and-search-hijack.md`),
the user went and fetched **legitimate, brand-name antivirus herself**. All five
events are device-tagged `samsung SM-S926U` (on the phone, not another of the 5
account devices).

| time (CDT) | action | package | app |
|---|---|---|---|
| 13:50:09 | Visited | `com.symantec.mobilesecurity` | Norton360 Antivirus & Security |
| 16:23:33 | Visited | `com.symantec.securewifi` | Norton VPN |
| ~19:20:00 | **Used** | `com.symantec.mobilesecurity` | Norton360 (installed + ran) |
| ~19:20:00 | **Used** | `com.symantec.securewifi` | Norton VPN (installed + ran) |
| 20:35:33 | Visited | `com.wsandroid.suite` | McAfee Security |

So: visited Norton360 at 13:50, Norton VPN at 16:23, had **both installed and
running by the 19:20 batch**, then looked at McAfee at 20:35.

## Reading

- **This is genuine human remediation**, not cascade noise. Norton/McAfee are
  brand AV (`android-apps.kb` verdict `legitimate`), so they are **filtered out
  of the `unknown-apps-timeline` residue** — which is why that table appears to
  "shift to antivirus" showing only the *fake* AV (AntiVirus Toolkit 16:22,
  DataGuardian 16:23, NexusSecurity 16:26, ViruSweep/AntivirusClean 20:34–20:35).
  Those fake-AV titles arrived via the **automated cascade** (tight intervals,
  same mechanism as the rest of the bundle); the Norton/McAfee fetches here are
  hers.
- **Ordering matters: her real-AV reaction (13:50) precedes the fake-AV cluster
  (16:22+).** She was reacting to the broader infection — popups and the
  "Settings closes itself" symptom — not to the fake AVs. Corroborates her other
  interleaved fingerprints (Play search `settings for android samsung` at 16:08,
  see `../findings.kb/ppi-adware-bundle-detonated-0518.md`).
- **`Used` caveat:** 19:20 is one of the coarse Play usage-snapshot times, so it
  bounds *that Norton ran in the window ending 19:20*, not the exact launch
  second. The `Visited` rows are precise per-page opens.
- **Outcome:** Norton360, Norton VPN, and McAfee are **absent from the 2026-05-26
  package dump** (`package_dump.py` over `package-dump-full.txt`) — she removed
  them too, consistent with the broad uninstall spree that cleared the junk
  (`2026-05-26T08:52:03--cleanup-and-problem-period-end.md`). Her remediation was
  ad-hoc and not retained.
