# Is the card fraud technically linked to the phone, or social engineering?

Working stance (see `../mission.md`): probably distinct symptoms of the same
risky-behavior pattern. The technical-channel hypothesis has **weakened** — the
one remote-access tool is the user's own (`../findings.kb/teamviewer-is-intentional-not-malware.md`),
there is no rogue SMS interceptor (`../findings.kb/no-rogue-sms-interceptor.md`),
and the active malware is already gone. Social engineering / phishing is now
the leading explanation.

Still to rule out the technical channel: identify the dropper APK
(`dropper-apk-identity.md`) in case it is an info-stealer; recover the
removed-apps list (`removed-apps-list.md`); and review account-side Google Play
**purchase + subscription** history and Google **Security Checkup** (unknown
devices/sessions).
