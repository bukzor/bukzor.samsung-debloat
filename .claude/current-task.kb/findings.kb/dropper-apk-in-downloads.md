---
status: needs-investigation
confidence: high
relates-to: [adware]
last-updated: "2026-05-26"
---

# Suspicious 33 MB APK in Downloads (likely dropper/payload)

`downloads-listing.txt` shows, in `/sdcard/Download`:

```
20260519_39cc25247bafa76987de194541c77c41_offset_32641024.apk   33,166,208 B   (mtime 2026-05-25 10:05)
```

The `<date>_<md5>_offset_<n>.apk` naming is a hallmark of **auto-downloaded
ad-SDK / silent-install payloads**, not a user-chosen download. It sits beside
the `_.admaster/` adware dir (see `admaster-adware-artifact.md`).

Pulled to `forensics/20260526-182045-SM-S926U/pulled/dropper.apk` (verified
`file` = "Android package (APK), with AndroidManifest.xml"). **Inert on disk —
not installed.**

Next step (`../open-question.kb/dropper-apk-identity.md`): identify package
name, signer certificate, and requested permissions. No `aapt`/`keytool`/`java`
on the host yet; plan to use `uv run --with androguard` or `unzip` + cert
inspection.

Attribution caveat: the file's owner UID (`u0_a316` = MediaProvider) does
**not** identify the downloading app — see
`../environment.kb/scoped-storage-ownership-not-attributable.md`.
