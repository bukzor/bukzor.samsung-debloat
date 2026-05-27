# Reported history (pre-investigation)

What the user described and did before we connected ADB. Treat as user
testimony, not yet independently verified.

## Symptoms

- **Incessant "your phone is dirty, install to clean!" popup ads** with **zero
  user interaction** — appeared on their own. (Classic overlay adware.)
- When the user opened the app list to find/uninstall the culprit, **Settings
  closed itself automatically** — strongly suggestive of a malicious
  **accessibility service** watching the screen and navigating away to defend
  itself.

## User's prior cleanup

- Uninstalled **~30 assorted apps** in a spree.
- The popups **stopped somewhere between uninstall #20 and #30** — so the
  active culprit is very likely *already removed*, but **which uninstall did
  it is unknown**.
- A reboot was initially assumed — but the user doubted it and **logcat in
  fact retains entries back to 2026-05-21** (see
  `findings.kb/logcat-reaches-back-to-0521.md`). So logcat IS usable for the
  infection-active window; don't treat it as gone.

## Card fraud

- Mother has **recurring trouble keeping people off her Visa card**.
- The user's read: she has likely **given her card number to someone
  unsavory, repeatedly**, via Android — but whether through an installed app
  or social engineering is unknown.

## Timeline anchors

- Adware artifacts in `/sdcard/Download` dated **2026-05-18 to 2026-05-25**.
- Investigation began **2026-05-26**.
