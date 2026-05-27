# Is the card fraud technically linked to the phone, or social engineering?

Working stance (see `../mission.md`): probably distinct symptoms of the same
risky-behavior pattern. The technical-channel hypothesis has **weakened** — the
one remote-access tool is the user's own (`../findings.kb/teamviewer-is-intentional-not-malware.md`),
there is no rogue SMS interceptor (`../findings.kb/no-rogue-sms-interceptor.md`),
and the active malware is already gone. Social engineering / phishing is now
the leading explanation.

Still to rule out the technical channel: the dropper is now identified as the
Tencent 应用宝 app store (`../findings.kb/dropper-is-tencent-app-store.md`) — a
silent-install/ad gateway, not itself a card-stealer, but it could have
installed one. So recover the removed-apps list (`removed-apps-list.md`) to find
patient zero, and review account-side Google Play **purchase + subscription**
history and Google **Security Checkup** (unknown devices/sessions).
