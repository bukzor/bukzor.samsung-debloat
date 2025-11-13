# Focus on Samsung packages that OVERRIDE default Android behaviors
# Quick settings, notifications, system UI, etc.

# Samsung SystemUI overlays (navbar customization)
pm uninstall --user 0 com.samsung.internal.systemui.navbar.gestural_no_hint
pm uninstall --user 0 com.samsung.internal.systemui.navbar.sec_gestural
pm uninstall --user 0 com.samsung.internal.systemui.navbar.sec_gestural_no_hint

# Samsung connectivity overlays (network behavior overrides)
pm uninstall --user 0 com.samsung.android.ConnectivityOverlay
pm uninstall --user 0 com.samsung.android.ConnectivityUxOverlay

# Samsung settings helper (intercepts settings changes)
pm uninstall --user 0 com.samsung.android.settingshelper

# Samsung unified setting service (behavior customization)
pm uninstall --user 0 com.samsung.unifiedsettingservice

# Samsung input share (clipboard/input override)
pm uninstall --user 0 com.samsung.android.inputshare

# Samsung aware service (usage pattern tracking/behavior modification)
pm uninstall --user 0 com.samsung.android.aware.service

# Samsung multisound (audio routing override)
pm uninstall --user 0 com.samsung.android.setting.multisound

# Samsung sound picker (replaces system sound picker)
pm uninstall --user 0 com.samsung.android.app.soundpicker
pm uninstall --user 0 com.samsung.android.secsoundpicker

# Samsung edge panels/features (UI overlay)
pm uninstall --user 0 com.samsung.android.app.taskedge

# Samsung contextual search overlay
pm uninstall --user 0 com.samsung.android.internal.overlay.config.default_contextual_search

# Samsung service agent (background behavior modifier)
pm uninstall --user 0 com.samsung.android.svcagent

# Samsung OMC agent (carrier customization)
pm uninstall --user 0 com.samsung.android.app.omcagent

# Samsung Device Care services (behavior throttling/optimization)
pm uninstall --user 0 com.samsung.android.lool

# Samsung privacy dashboard (replaces Android privacy dashboard)
pm uninstall --user 0 com.samsung.android.privacydashboard

# Note: The core SystemUI (com.android.systemui) cannot be removed or replaced
# without root access. These removals eliminate Samsung's behavior overrides
# but the base quick settings UI will still be Samsung's.
