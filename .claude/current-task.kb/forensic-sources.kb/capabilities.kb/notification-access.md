---
capture-status: partial
captured-as: [notification-listeners.txt]
needs-device: false
last-updated: "2026-05-27"
---

# notification-access — listeners and posted-notification log

Notification-listener access lets an app read every notification. The dump also
carries a recent log of posted notifications, naming the posting package.

    adb shell settings get secure enabled_notification_listeners > notification-listeners.txt
    adb shell dumpsys notification --noredact                    > notification-dump.txt

Listeners captured (only legit holders). The `--noredact` post log (which could
name a popup-poster) is not yet captured.
