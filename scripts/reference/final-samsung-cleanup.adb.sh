# Final Samsung cleanup - safe removals
# Focus on bloat that doesn't affect core functionality

# Bixby (on-device language packs)
pm uninstall --user 0 com.samsung.android.bixby.ondevice.enus
pm uninstall --user 0 com.samsung.android.bixby.ondevice.esus

# Samsung Pay (if confirmed not used)
pm uninstall --user 0 com.samsung.android.spayfw

# Samsung Game Optimizer (if still present)
pm uninstall --user 0 com.samsung.android.game.gos

# Samsung Apps/Services (non-essential)
pm uninstall --user 0 com.samsung.android.app.routines
pm uninstall --user 0 com.samsung.android.app.sketchbook
pm uninstall --user 0 com.samsung.android.app.smartcapture
pm uninstall --user 0 com.samsung.android.app.dofviewer
pm uninstall --user 0 com.samsung.android.oneconnect
pm uninstall --user 0 com.samsung.android.app.galaxyregistry
pm uninstall --user 0 com.samsung.petservice

# Samsung background telemetry/analytics
pm uninstall --user 0 com.samsung.android.knox.analytics.uploader
pm uninstall --user 0 com.samsung.android.da.daagent
pm uninstall --user 0 com.samsung.android.dqagent

# Samsung AI/ML services (if not using Samsung camera features)
pm uninstall --user 0 com.samsung.android.aicore
pm uninstall --user 0 com.samsung.android.vision.model

# Samsung keyboard/input (already removed, but check)
pm uninstall --user 0 com.samsung.android.sdk.handwriting

# Samsung theme/UI (remaining)
pm uninstall --user 0 com.samsung.android.themecenter
pm uninstall --user 0 com.samsung.android.widget.pictureframe

# Samsung accessory managers (if not using Samsung accessories)
pm uninstall --user 0 com.samsung.accessory.budsunitemgr
pm uninstall --user 0 com.samsung.android.app.watchmanagerstub
pm uninstall --user 0 com.samsung.gpuwatchapp

# Samsung cloud/sync services
pm uninstall --user 0 com.samsung.android.scs

# Samsung AR (likely already removed)
pm uninstall --user 0 com.samsung.android.aircommandmanager

# Video editor
pm uninstall --user 0 com.samsung.app.newtrim

# Samsung voice services
pm uninstall --user 0 com.samsung.android.intellivoiceservice

# Translation services (if not used)
pm uninstall --user 0 com.samsung.SMT
pm uninstall --user 0 com.samsung.SMT.lang_en_us_l03
pm uninstall --user 0 com.samsung.SMT.lang_es_us_l01
pm uninstall --user 0 com.samsung.android.nmt.apps.t2t.languagepack.enesus
