---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# active-overlay-windows — live overlays drawn over other apps

`dumpsys window` exposes current windows; `TYPE_APPLICATION_OVERLAY` tokens by
package are the actual draw-over-other-apps surfaces (vs. the appops *grant*).

Capture:

    adb shell dumpsys window windows > window-windows.txt
    adb shell dumpsys window tokens  > window-tokens.txt

The malicious overlay app is already removed, so expect only benign holders now
— useful mainly if popups recur on a live device.
