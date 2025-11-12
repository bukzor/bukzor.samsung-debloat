# Additional Verizon bloat
pm uninstall --user 0 com.verizon.obdm
pm uninstall --user 0 com.vzw.ecid
pm uninstall --user 0 com.vzw.hss.myverizon
pm uninstall --user 0 com.vcast.mediamanager
pm uninstall --user 0 com.samsung.vvm
pm uninstall --user 0 com.samsung.vzwapiservice
pm uninstall --user 0 com.verizon.onetalk.dialer
pm uninstall --user 0 com.securityandprivacy.android.verizon.vms

# Microsoft bloat
pm uninstall --user 0 com.microsoft.appmanager
pm uninstall --user 0 com.microsoft.skydrive

# Samsung theme/customization bloat
pm uninstall --user 0 com.samsung.android.themecenter
pm uninstall --user 0 com.samsung.android.themestore
pm uninstall --user 0 com.samsung.storyservice
pm uninstall --user 0 com.samsung.android.app.dressroom
pm uninstall --user 0 com.samsung.android.stickercenter
pm uninstall --user 0 com.samsung.android.aremojieditor

# Samsung services (non-essential)
pm uninstall --user 0 com.samsung.android.forest
pm uninstall --user 0 com.samsung.mediasearch
pm uninstall --user 0 com.samsung.cmh
pm uninstall --user 0 com.samsung.android.smartmirroring
pm uninstall --user 0 com.samsung.android.app.interpreter

# Samsung DeX (if not used)
pm uninstall --user 0 com.samsung.android.mdx
pm uninstall --user 0 com.samsung.android.mdx.kit

# Other bloat
pm uninstall --user 0 com.hiya.star
pm uninstall --user 0 com.totalav.android

# PWAs/Web wrappers (chromium webapk - usually safe to remove if not used)
pm uninstall --user 0 org.chromium.webapk.a46f07ce09aa4da48_v2
pm uninstall --user 0 org.chromium.webapk.a9f973806bafdb35f_v2
pm uninstall --user 0 org.chromium.webapk.aa495f2e2a9b7924c_v2
pm uninstall --user 0 org.chromium.webapk.aed6237980b73fc4d_v2
