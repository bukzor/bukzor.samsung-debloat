---
capture-status: captured
captured-as: [roles.txt]
needs-device: false
last-updated: "2026-05-27"
---

# default-roles — SMS / dialer / browser / home / assistant holders

`cmd role get-role-holders <role>` for each role. A hijacked default (esp. SMS,
browser, assistant) is a redirection/interception vector.

Capture (loop over roles):

    for r in sms dialer browser home assistant emergency; do
      adb shell cmd role get-role-holders android.app.role.${r^^}; done > roles.txt

This capture: defaults are legitimate (SMS = Google Messages, browser = Chrome).
