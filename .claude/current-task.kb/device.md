# Device

The subject phone — **the user's mother's**, the *same owner* as the original
repo sessions (2025-11-12/13). Those sessions worked on her **previous** phone
(a Verizon Samsung), since broken and replaced by this unit. So this is the
**first time on this particular hardware**, but the whole project is about
debloating her phones — the devlog is authoritative for that history.

| Field | Value |
|---|---|
| Model | SM-S926U (Galaxy S24+, Snapdragon US variant, codename `e2q`) |
| ADB serial | `R5CX31TA1RT` |
| Android | 16 (SDK 36) |
| One UI | 8.0 (`ro.build.version.oneui=80500`) |
| Build | `S926USQU5DZDR`, fingerprint `samsung/e2qsqw/e2q:16/BP4A.251205.006/...` |
| Security patch | 2026-04-05 (current) |

Fully patched. Forensically relevant: Android 13+ "restricted settings" makes
it hard for a *sideloaded* app to obtain Accessibility — so accessibility
abuse here implies either a Play-delivered app or a user-performed manual
bypass.

## Connection

Wireless ADB only (see `environment.kb/wireless-adb-only-on-crostini.md`).
Pairing/connection ports change after every reboot.
