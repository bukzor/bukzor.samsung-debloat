---
status: confirmed
confidence: high
relates-to: [adware]
last-updated: "2026-05-26"
---

# `_.admaster/` adware artifact in Downloads

`downloads-listing.txt` shows a hidden-style directory in `/sdcard/Download`:

```
drwxrws--- _.admaster/
  -rwxrwx--- ._u_i_d_f_k.txt   108 B   (mtime 2026-05-18 20:36)
```

The leading-dot/underscore naming hides it from the gallery/file UI — typical
adware behavior. Pulled to `pulled/admaster_uidfk.txt`; its contents are a
single base64-looking blob (likely an encrypted device/ad identifier):

```
gpMi8QJ3DheAfPfBZPaqBRGqXaiivpiz1p3VNVGERJ6oQHEMYBxoVdjTDBne/okeIUMeWLqqkZva5r0AHVvcgPnsMrpcU9ccfxxIpLwE9Qw=
```

"admaster" connotes ad/attribution tooling. The **2026-05-18** timestamp is
the earliest infection anchor and predates the dropper APK (2026-05-25),
suggesting the ad component was active for at least a week.

This is residue left behind after the user's uninstalls — the owning app may
already be gone. Decode attempted: the 96-byte blob is high-entropy and is not
valid base64→text, consistent with an encrypted identifier — so it does **not**
name the owning app. Confirms an ad-fraud/adware family was present; does not by
itself name it.
