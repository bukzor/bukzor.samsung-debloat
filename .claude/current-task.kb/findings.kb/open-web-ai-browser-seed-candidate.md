---
status: ruled-out
confidence: high
relates-to: [adware]
last-updated: "2026-05-28"
---

# `com.open.web.ai.browser` ("AI Browser") — RULED OUT as seed/controller

Earlier (2026-05-27) this was the *leading* seed candidate, on the premise it was
an **off-Play sideload** that drove the cascade and the Yahoo search-hijack.
Re-probed 2026-05-28 (after `google-play-scraper` was added this session) — **the
premise is false on every count**:

1. **Not off-Play.** It's a live, long-listed Play app: AdPulse INC, **10M
   installs, 4.7★**, on Play since 2025-06 (8 Wayback snapshots, status 200),
   updated 2026-05-25. The original "off-Play / sideloaded" call mistook *"no Play
   telemetry on this device"* for *"not a Play app"* — a guess the reputation
   probe (not runnable when the finding was written) refutes in one call.
2. **Lacks the capability to be the controller.** The observed behaviour —
   zero-interaction overlays *over other apps*, "Settings closes itself", silent
   installs — needs `SYSTEM_ALERT_WINDOW` + accessibility + install permission. It
   holds **none** (17 perms: location/camera/mic/accounts/storage/network). Its
   ads are **in-app interstitials only** (per reviews), exactly a no-overlay app's
   ceiling.
3. **Doesn't explain the Yahoo hijack.** Reviews say it wraps **Google** (behind
   forced ads), and with no system permissions it cannot change Chrome's default
   search.

**What it actually is:** aggressive adware / PUA browser — relentless in-app ads,
scareware ad creatives, identifier harvesting, planted 5★ reviews inflating the
score. Reclassified there: `../android-apps.kb/com.open.web.ai.browser.md`
(verdict `adware`, full probe).

**What survives (consistent with adware, not seed):** it was on the device,
**Samsung Device Care SuspiciousApps flagged it**, and it was uninstalled
2026-05-26 08:52 (`../timeline.kb/2026-05-26T08:52:03--cleanup-and-problem-period-end.md`).
Samsung flagging abusive adware ≠ it being the controller.

**Consequence:** patient zero / the controller is **unnamed again**. The
silent-window conclusion (trigger left no synced trace) stands on its own and
does not depend on this app. The best *surviving* overlay/accessibility holder is
`com.sunteame.superhomescreen`, but it appeared mid-cascade (07:16:40), so it is
not the initial seed either.

**Method lesson (3rd instance):** a candidate was anchored on a name/archetype
("AI browser click-fraud trojan") and an unverified provenance guess, never
checked against the live Play listing — exactly the false-lead pattern in
`install-source-of-survivors.md`. Probe the listing before believing a name.
