---
package: "com.open.web.ai.browser"
name: "AI Browser"
category: "browser"
confidence: "high"
source: "https://play.google.com/store/apps/details?id=com.open.web.ai.browser + weighted Play reviews"
last-updated: "2026-05-28"
verdict: adware
probe:
  date: "2026-05-28"
  found: true
  developer: AdPulse INC
  developer_id: AdPulse+INC
  developer_email: Georgemartinezz2002@gmail.com
  developer_website: https://hb-website.optiword.com
  genre: Tools
  min_installs: 10000000
  score: 4.7289886
  ratings: 244230
  ad_supported: false
  contains_ads: false
  permissions:
    - add or remove accounts
    - approximate location (network-based)
    - control flashlight
    - control vibration
    - create accounts and set passwords
    - find accounts on the device
    - full network access
    - modify or delete the contents of your USB storage
    - precise location (GPS and network-based)
    - prevent device from sleeping
    - read the contents of your USB storage
    - receive data from Internet
    - record audio
    - take pictures and videos
    - toggle sync on and off
    - view Wi-Fi connections
    - view network connections
---

Aggressive adware / PUA browser by **AdPulse INC** (gmail dev contact). Live,
long-listed Play app — **10M installs, 4.7★, updated 2026-05-25** — but the
rating is propped up by apparently-planted 5★ marketing reviews; the
heavily-upvoted genuine reviews are damning: relentless in-app ad interstitials
("ads after every single thing you do", "opens to a TikTok ad", 1653/1262/827
👍), **scareware ad creatives** that mimic virus/system warnings and deep-link to
installs (240👍), device-identifier harvesting (362👍), and it merely wraps
Google search behind forced ads (627👍).

**Ruled out as the infection's controller/seed** — see
`../findings.kb/open-web-ai-browser-seed-candidate.md`. It requests **no**
`SYSTEM_ALERT_WINDOW`, **no** accessibility, **no** install permission (17 perms:
location/camera/mic/accounts/storage/network), so it cannot throw system-wide
overlays, self-defend Settings, or silently install — its ads are in-app only.
On the subject device only as a 2026-05-26 uninstall token (Device Care
SuspiciousApps); no Play "Used"/"Visited", Library, or Installs hit.
