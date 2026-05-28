# Did any surviving "unknown" utility app exercise its category-mismatched permission?

The Play probe (in `android-apps.kb/*.md` frontmatter `probe.permissions`)
found utility apps requesting capabilities their stated function doesn't need —
the malware tell. Per `android-apps.kb/CLAUDE.md`, that only *flags a candidate*;
a `malware` verdict needs device-side proof the op was actually held/used.

Standouts (regenerate the full list from the kb, don't trust this enumeration):

    android_apps_kb.py list <kb> | jq -r 'select(.verdict=="unknown").package' \
      | sed 's#^#.claude/current-task.kb/android-apps.kb/#; s#$#.md#' \
      | xargs -I{} yq -f extract -o=json {} \
      | jq -c 'select(.probe.permissions) | {package, mismatch: [.probe.permissions[]
          | select(test("contacts|directly call|frame buffer|disable your screen lock|take pictures|record audio|phone status"))]}
          | select(.mismatch|length>0)'

- `com.wifiassistant.homescreen.tools` — "read frame buffer" (screen capture) +
  camera + direct-call on a wallpaper/launcher app; throwaway gmail dev + gibberish
  website behind a spoofed "PT. Radjago" name. Highest concern.
- `com.gps.maps.me.city.navigation…weather` — reads + *modifies* contacts, direct-call.
- `com.alarmclock.wakeupalarm`, `com.lightweight.scanning.minatpg`, and the
  "disable your screen lock" network tools (`…bvairpro`, `…uatpreite`, `…mitapouyt`,
  `…mapitop`, `…forakitran`).

## How to resolve (no device needed — captures exist)

Cross-reference each candidate against the captured device state:

- `forensics/<capture>/appops-full.txt` (see `forensic-sources.kb/capabilities.kb/appops.md`)
  — per-package op grants + **last-access timestamps**. A granted/used CAMERA,
  READ_CONTACTS, CALL_PHONE, RECORD_AUDIO op confirms exercise.
- `scripts/package_dump.py` over the package dump — granted runtime permissions
  per package.
- Accessibility is already ruled out (none active — `capabilities.kb/accessibility.md`).

A confirmed exercised-mismatch sets the package's `verdict` to `malware`
(with the appops line as `source`); no evidence of use leaves it `unknown` /
`adware`. Write the outcome into `findings.kb/` and delete this file.
