# Core Samsung bloat
pm uninstall --user 0 com.samsung.android.bixby.agent
pm uninstall --user 0 com.samsung.android.bixby.service
pm uninstall --user 0 com.samsung.android.bixby.wakeup
pm uninstall --user 0 com.samsung.android.bixbyvision.framework
pm uninstall --user 0 com.samsung.android.visionintelligence

# Samsung Daily/Free
pm uninstall --user 0 com.samsung.android.app.spage

# Samsung apps with Google equivalents
pm uninstall --user 0 com.samsung.android.messaging
pm uninstall --user 0 com.samsung.android.calendar
pm uninstall --user 0 com.samsung.android.email.provider
pm uninstall --user 0 com.android.chrome
pm uninstall --user 0 com.sec.android.app.sbrowser

# Game services
pm uninstall --user 0 com.samsung.android.game.gamehome
pm uninstall --user 0 com.samsung.android.game.gametools
pm uninstall --user 0 com.enhance.gameservice
pm uninstall --user 0 com.samsung.android.gametuner.thin

# AR and camera bloat
pm uninstall --user 0 com.samsung.android.arzone
pm uninstall --user 0 com.samsung.android.aremoji
pm uninstall --user 0 com.samsung.android.ardrawing
pm uninstall --user 0 com.samsung.android.aremeji.editor

# Samsung cloud/sync
pm uninstall --user 0 com.samsung.android.scloud
pm uninstall --user 0 com.samsung.android.samsungpass
pm uninstall --user 0 com.samsung.android.samsungpassautofill

# Samsung store/marketing
pm uninstall --user 0 com.sec.android.app.samsungapps
pm uninstall --user 0 com.samsung.android.mateagent
pm uninstall --user 0 com.samsung.android.app.tips

# Samsung media apps (if using Google equivalents)
pm uninstall --user 0 com.samsung.android.gallery3d
pm uninstall --user 0 com.samsung.android.app.notes
pm uninstall --user 0 com.samsung.android.video

# Samsung voice/assistant
pm uninstall --user 0 com.samsung.android.bixby.voiceinput
pm uninstall --user 0 com.samsung.android.app.settings.bixby

# Verizon bloat
pm uninstall --user 0 com.verizon.mips.services
pm uninstall --user 0 com.verizon.services
pm uninstall --user 0 com.vzw.apnlib

# Facebook (if present and unwanted)
pm uninstall --user 0 com.facebook.services
pm uninstall --user 0 com.facebook.system
pm uninstall --user 0 com.facebook.appmanager

# Disable One UI Home (after installing replacement launcher)
pm disable-user --user 0 com.sec.android.app.launcher
