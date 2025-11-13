# Remove Samsung UI overlays and theming
# Note: Quick settings panel is deeply integrated into Samsung's SystemUI
# Without root/custom ROM, we're limited in what we can change

# Samsung Theme Center (if still present)
pm uninstall --user 0 com.samsung.android.themecenter

# Samsung personalization service
pm uninstall --user 0 com.sec.android.app.personalization

# Samsung quick settings overlay (fast pair)
pm uninstall --user 0 com.sec.android.app.qsfastpairoverlay

# Samsung dynamic lock screen
pm uninstall --user 0 com.samsung.android.dynamiclock

# Samsung live wallpaper
pm uninstall --user 0 com.samsung.android.wallpaper.live
