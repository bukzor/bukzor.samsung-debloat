#!/bin/bash
# Master Samsung Debloat Script
# Consolidated from all phases - run sequentially
# WARNING: Review each section before running!

DEVICE="$1"
if [ -z "$DEVICE" ]; then
    echo "Usage: $0 <device-ip:port>"
    echo "Example: $0 192.168.87.245:44577"
    exit 1
fi

ADB="adb -s $DEVICE shell"

echo "===== Phase 1: Initial Debloat ====="
echo "Removing Bixby, Samsung Daily, AR Zone, Samsung apps..."
$ADB <<'EOF'
pm uninstall --user 0 com.samsung.android.bixby.agent
pm uninstall --user 0 com.samsung.android.bixby.service
pm uninstall --user 0 com.samsung.android.app.settings.bixby
pm uninstall --user 0 com.samsung.android.visionintelligence
pm uninstall --user 0 com.samsung.android.app.spage
pm uninstall --user 0 com.samsung.android.app.tips
pm uninstall --user 0 com.samsung.android.arzone
pm uninstall --user 0 com.samsung.android.aremoji
pm uninstall --user 0 com.samsung.android.aremeji.editor
pm uninstall --user 0 com.samsung.android.ardrawing
pm uninstall --user 0 com.samsung.android.game.gamehome
pm uninstall --user 0 com.samsung.android.game.gametools
pm uninstall --user 0 com.samsung.android.scloud
pm uninstall --user 0 com.samsung.android.samsungpass
pm uninstall --user 0 com.samsung.android.samsungpassautofill
pm uninstall --user 0 com.sec.android.app.sbrowser
pm uninstall --user 0 com.samsung.android.email.provider
pm uninstall --user 0 com.samsung.android.calendar
pm uninstall --user 0 com.wsomacp
pm uninstall --user 0 com.samsung.android.app.notes
pm uninstall --user 0 com.samsung.android.app.voice
pm uninstall --user 0 com.sec.android.app.popupcalculator
pm uninstall --user 0 com.android.chrome
pm disable-user --user 0 com.sec.android.app.launcher
EOF

echo ""
echo "===== Phase 2: Additional Bloat ====="
echo "Removing Verizon, Microsoft, Samsung services..."
$ADB <<'EOF'
pm uninstall --user 0 com.verizon.obdm
pm uninstall --user 0 com.vzw.ecid
pm uninstall --user 0 com.vzw.hss.myverizon
pm uninstall --user 0 com.vcast.mediamanager
pm uninstall --user 0 com.samsung.vvm
pm uninstall --user 0 com.samsung.vzwapiservice
pm uninstall --user 0 com.verizon.onetalk.dialer
pm uninstall --user 0 com.securityandprivacy.android.verizon.vms
pm uninstall --user 0 com.microsoft.appmanager
pm uninstall --user 0 com.microsoft.skydrive
pm uninstall --user 0 com.samsung.android.themecenter
pm uninstall --user 0 com.samsung.android.themestore
pm uninstall --user 0 com.samsung.storyservice
pm uninstall --user 0 com.samsung.android.app.dressroom
pm uninstall --user 0 com.samsung.android.stickercenter
pm uninstall --user 0 com.samsung.android.aremojieditor
pm uninstall --user 0 com.samsung.android.forest
pm uninstall --user 0 com.samsung.mediasearch
pm uninstall --user 0 com.samsung.cmh
pm uninstall --user 0 com.samsung.android.smartmirroring
pm uninstall --user 0 com.samsung.android.app.interpreter
pm uninstall --user 0 com.samsung.android.mdx
pm uninstall --user 0 com.samsung.android.mdx.kit
pm uninstall --user 0 com.hiya.star
pm uninstall --user 0 com.totalav.android
pm uninstall --user 0 org.chromium.webapk.a46f07ce09aa4da48_v2
pm uninstall --user 0 org.chromium.webapk.a9f973806bafdb35f_v2
pm uninstall --user 0 org.chromium.webapk.aa495f2e2a9b7924c_v2
pm uninstall --user 0 org.chromium.webapk.aed6237980b73fc4d_v2
EOF

echo ""
echo "===== Phase 3: Aggressive Samsung Debloat ====="
echo "Removing behavior overrides (Smart features, Game services, etc.)..."
$ADB <<'EOF'
pm uninstall --user 0 com.samsung.android.smartcallprovider
pm uninstall --user 0 com.samsung.android.smartface
pm uninstall --user 0 com.samsung.android.smartface.overlay
pm uninstall --user 0 com.samsung.android.smartsuggestions
pm uninstall --user 0 com.samsung.android.smartswitchassistant
pm uninstall --user 0 com.samsung.android.smartmirroring
pm uninstall --user 0 com.samsung.android.game.gos
pm uninstall --user 0 com.samsung.gamedriver.sm8650
pm uninstall --user 0 com.samsung.android.spayfw
pm uninstall --user 0 com.samsung.android.app.camera.sticker.facearavatar.preload
pm uninstall --user 0 com.samsung.android.visualars
pm uninstall --user 0 com.samsung.android.aremojieditor
pm uninstall --user 0 com.sec.android.mimage.avatarstickers
pm uninstall --user 0 com.samsung.android.allshare.service.mediashare
pm uninstall --user 0 com.samsung.android.app.parentalcare
pm uninstall --user 0 com.sec.android.app.SecSetupWizard
pm uninstall --user 0 com.sec.android.app.setupwizard
pm uninstall --user 0 com.sec.android.app.setupwizardlegalprovider
pm uninstall --user 0 com.google.android.setupwizard
pm uninstall --user 0 com.samsung.carrier.logcollector
pm uninstall --user 0 com.samsung.android.honeyboard
pm uninstall --user 0 com.samsung.android.app.clipboardedge
pm uninstall --user 0 com.samsung.android.app.sharelive
pm uninstall --user 0 com.samsung.android.inputshare
pm uninstall --user 0 com.samsung.android.appseparation
EOF

echo ""
echo "===== Phase 4: Disable Samsung Duplicates ====="
echo "Disabling (not uninstalling) deeply-integrated Samsung apps..."
$ADB <<'EOF'
pm disable-user --user 0 com.samsung.android.dialer
pm disable-user --user 0 com.samsung.android.app.contacts
pm disable-user --user 0 com.sec.android.gallery3d
pm disable-user --user 0 com.sec.android.app.soundalive
pm disable-user --user 0 com.sec.android.app.myfiles
pm disable-user --user 0 com.samsung.app.newtrim
pm disable-user --user 0 com.samsung.android.app.routines
EOF

echo ""
echo "===== Phase 5: UI Overlays & Behavior Overrides ====="
echo "Removing UI customizations and behavior modifications..."
$ADB <<'EOF'
pm uninstall --user 0 com.samsung.android.themecenter
pm uninstall --user 0 com.sec.android.app.personalization
pm uninstall --user 0 com.sec.android.app.qsfastpairoverlay
pm uninstall --user 0 com.samsung.android.dynamiclock
pm uninstall --user 0 com.samsung.android.wallpaper.live
pm uninstall --user 0 com.samsung.internal.systemui.navbar.gestural_no_hint
pm uninstall --user 0 com.samsung.internal.systemui.navbar.sec_gestural
pm uninstall --user 0 com.samsung.internal.systemui.navbar.sec_gestural_no_hint
pm uninstall --user 0 com.samsung.android.ConnectivityOverlay
pm uninstall --user 0 com.samsung.android.ConnectivityUxOverlay
pm uninstall --user 0 com.samsung.android.settingshelper
pm uninstall --user 0 com.samsung.unifiedsettingservice
pm uninstall --user 0 com.samsung.android.inputshare
pm uninstall --user 0 com.samsung.android.aware.service
pm uninstall --user 0 com.samsung.android.setting.multisound
pm uninstall --user 0 com.samsung.android.app.soundpicker
pm uninstall --user 0 com.samsung.android.secsoundpicker
pm uninstall --user 0 com.samsung.android.app.taskedge
pm uninstall --user 0 com.samsung.android.app.routines
pm uninstall --user 0 com.samsung.android.internal.overlay.config.default_contextual_search
pm uninstall --user 0 com.sec.android.app.qsfastpairoverlay
pm uninstall --user 0 com.samsung.android.svcagent
pm uninstall --user 0 com.samsung.android.app.omcagent
pm uninstall --user 0 com.samsung.android.lool
pm uninstall --user 0 com.samsung.android.privacydashboard
EOF

echo ""
echo "===== Phase 6: Grant App Permissions ====="
echo "Granting essential permissions to Google apps..."
$ADB <<'EOF'
pm grant com.google.android.dialer android.permission.READ_CONTACTS
pm grant com.google.android.dialer android.permission.WRITE_CONTACTS
pm grant com.google.android.dialer android.permission.READ_CALL_LOG
pm grant com.google.android.dialer android.permission.WRITE_CALL_LOG
pm grant com.google.android.dialer android.permission.CALL_PHONE
pm grant com.google.android.dialer android.permission.READ_PHONE_STATE
pm grant com.google.android.dialer android.permission.CAMERA
pm grant com.google.android.contacts android.permission.READ_CONTACTS
pm grant com.google.android.contacts android.permission.WRITE_CONTACTS
pm grant com.google.android.contacts android.permission.GET_ACCOUNTS
pm grant com.google.android.apps.messaging android.permission.READ_SMS
pm grant com.google.android.apps.messaging android.permission.SEND_SMS
pm grant com.google.android.apps.messaging android.permission.RECEIVE_SMS
pm grant com.google.android.apps.messaging android.permission.READ_CONTACTS
pm grant com.google.android.apps.messaging android.permission.CAMERA
pm grant com.google.android.apps.photos android.permission.READ_MEDIA_IMAGES
pm grant com.google.android.apps.photos android.permission.READ_MEDIA_VIDEO
pm grant com.google.android.apps.photos android.permission.ACCESS_MEDIA_LOCATION
pm grant com.google.android.apps.photos android.permission.CAMERA
pm grant com.google.android.apps.nbu.files android.permission.READ_EXTERNAL_STORAGE
pm grant com.google.android.apps.nbu.files android.permission.WRITE_EXTERNAL_STORAGE
pm grant com.google.android.calendar android.permission.READ_CALENDAR
pm grant com.google.android.calendar android.permission.WRITE_CALENDAR
pm grant com.google.android.calendar android.permission.READ_CONTACTS
pm grant com.google.android.gm android.permission.GET_ACCOUNTS
pm grant com.google.android.gm android.permission.READ_CONTACTS
pm grant com.android.chrome android.permission.ACCESS_FINE_LOCATION
pm grant com.android.chrome android.permission.CAMERA
pm grant com.google.android.keep android.permission.RECORD_AUDIO
pm grant com.google.android.keep android.permission.CAMERA
pm grant com.google.android.deskclock android.permission.RECORD_AUDIO
EOF

echo ""
echo "===== Complete! ====="
echo "Total packages removed: ~87"
echo "Total packages disabled: ~8"
echo ""
echo "Next steps:"
echo "1. Install Google apps from Play Store (see README.md)"
echo "2. Set defaults: Gboard, Lawnchair, Google Phone, Google Messages"
echo "3. Star family contacts in Google Contacts"
echo "4. Configure Do Not Disturb priority notifications"
