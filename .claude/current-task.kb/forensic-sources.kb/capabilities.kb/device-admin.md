---
capture-status: captured
captured-as: [device-policy.txt]
needs-device: false
last-updated: "2026-05-27"
---

# device-admin — admins, device/profile owners

`dumpsys device_policy`: active device-admin receivers and any device/profile
owner. A rogue device admin resists uninstall and can lock/wipe the device.

Capture: `adb shell dumpsys device_policy > device-policy.txt`

Reviewed (no rogue admin) — but a deliberate hunt is tracked as an analysis.
