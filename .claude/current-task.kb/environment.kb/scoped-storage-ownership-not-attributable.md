# `/sdcard` file owner UID does not name the creating app

Forensic-method caveat learned this session. Files under `/sdcard` (emulated
storage) on modern Android (FUSE + scoped storage) show the **MediaProvider**
UID, not the app that wrote them.

Concretely: the dropper APK and `_.admaster/` in `/sdcard/Download` are owned
by `u0_a316`, which `package-dump-full.txt` maps to
`com.google.android.providers.media.module` (appId 10316) — a **system
component**, not the malware. Do **not** conclude MediaProvider downloaded
anything.

To attribute a file to an app instead:

- Analyze the file itself (APK package name / signer cert).
- Cross-reference install/download timestamps against app install times and
  `usagestats` events.
- These artifacts persist after the writing app is uninstalled, which is why
  the owner UID is uninformative.

Separately: `find /sdcard -iname '*.apk'` returned nothing while
`ls -laR /sdcard/Download` clearly showed the APK — `find` traversal under the
FUSE mount as the `shell` user is unreliable. **Prefer `ls -laR` for /sdcard
enumeration.**
