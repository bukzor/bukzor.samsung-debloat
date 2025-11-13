# Disable Samsung duplicates AFTER installing Google equivalents
# Run this ONLY after: Gboard, Lawnchair, Google Phone, Google Clock, Google Recorder are installed

# Samsung Dialer (replaced by Google Phone)
pm disable-user --user 0 com.samsung.android.dialer

# Samsung Contacts (replaced by Google Contacts)
pm disable-user --user 0 com.samsung.android.app.contacts

# Samsung Gallery (replaced by Google Photos)
pm disable-user --user 0 com.sec.android.gallery3d

# Samsung sound/audio effects (optional - only if you don't use them)
pm disable-user --user 0 com.sec.android.app.soundalive

# Samsung Files (replaced by Files by Google - you already have it)
pm disable-user --user 0 com.sec.android.app.myfiles

# Samsung Video Editor
pm disable-user --user 0 com.samsung.app.newtrim

# Samsung Routines (if you don't use automation)
pm disable-user --user 0 com.samsung.android.app.routines

# Note: We're using disable-user instead of uninstall for these
# because they're more deeply integrated. This is safer.
# They can be re-enabled if needed: pm enable <package>
