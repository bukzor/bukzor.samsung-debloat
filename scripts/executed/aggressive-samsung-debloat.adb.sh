# Samsung Smart* features (behavior overrides - worst offenders)
pm uninstall --user 0 com.samsung.android.smartcallprovider
pm uninstall --user 0 com.samsung.android.smartface
pm uninstall --user 0 com.samsung.android.smartface.overlay
pm uninstall --user 0 com.samsung.android.smartsuggestions
pm uninstall --user 0 com.samsung.android.smartswitchassistant
pm uninstall --user 0 com.samsung.android.smartmirroring

# Samsung Game services (behavior overrides for games)
pm uninstall --user 0 com.samsung.android.game.gos
pm uninstall --user 0 com.samsung.gamedriver.sm8650

# Samsung Pay (unless you use it)
pm uninstall --user 0 com.samsung.android.spayfw

# Samsung AR/Avatar/Stickers (camera bloat)
pm uninstall --user 0 com.samsung.android.app.camera.sticker.facearavatar.preload
pm uninstall --user 0 com.samsung.android.visualars
pm uninstall --user 0 com.samsung.android.aremojieditor
pm uninstall --user 0 com.sec.android.mimage.avatarstickers

# Samsung AllShare (media sharing)
pm uninstall --user 0 com.samsung.android.allshare.service.mediashare

# Parental controls
pm uninstall --user 0 com.samsung.android.app.parentalcare

# Setup wizards (already completed)
pm uninstall --user 0 com.sec.android.app.SecSetupWizard
pm uninstall --user 0 com.sec.android.app.setupwizard
pm uninstall --user 0 com.sec.android.app.setupwizardlegalprovider
pm uninstall --user 0 com.google.android.setupwizard

# Carrier telemetry
pm uninstall --user 0 com.samsung.carrier.logcollector

# Samsung keyboard (replaced by Gboard)
pm uninstall --user 0 com.samsung.android.honeyboard

# Other Samsung behavior overrides
pm uninstall --user 0 com.samsung.android.app.clipboardedge
pm uninstall --user 0 com.samsung.android.app.sharelive
pm uninstall --user 0 com.samsung.android.inputshare
pm uninstall --user 0 com.samsung.android.appseparation
