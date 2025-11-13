# Samsung Debloat Project

Transform Samsung phones into Pixel-like experience by removing bloatware via ADB without root.

## Project Context

This is a completed debloat session documented in `docs/devlog/2025-11-12.md`. The phone was successfully transformed with ~87 packages removed, ~8 disabled, and complete Google app suite installed.

## Key Files

- `scripts/master-debloat.adb.sh` - Consolidated debloat script for future use
- `scripts/executed/` - Individual scripts from original session (reference)
- `packages-install-dates.json` - Complete package analysis with install date clustering
- `current-packages.txt` - Final state after debloat
- `README.md` - User-facing documentation
- `docs/devlog/2025-11-12.md` - Complete session documentation

## Approach

1. **Install date clustering** - Factory apps have `2021-12-31` timestamp, reliably identifying bloat
2. **Progressive phases** - Started with obvious bloat, progressed to behavior overrides
3. **Safe methods** - Used `disable-user` for deeply-integrated apps, `uninstall --user 0` for bloat
4. **Categorization** - Analyzed 190 Samsung packages by function to identify removable vs essential

## Key Findings

- **190 Samsung packages** remain after debloat
- **~100-120 are essential** (telephony, Knox, WiFi, hardware drivers)
- **~70-80 are low-priority bloat** (diminishing returns)
- **SystemUI cannot be replaced** without root - quick settings retain Samsung appearance
- **Behavior overrides removed** - Smart features, settings interception, usage tracking
- **Google Recorder is Pixel-exclusive** - used third-party alternative

## Device Connection

Wireless ADB via:
```bash
adb pair <ip>:<pairing-port> <pairing-code>
adb connect <ip>:<connection-port>
```

After reboot, requires fresh pairing with new ports.

## App Replacements

| Samsung | Google | Status |
|---------|--------|--------|
| Samsung Keyboard | Gboard | Uninstalled |
| One UI Home | Lawnchair | Disabled |
| Samsung Dialer | Google Phone | Disabled |
| Samsung Contacts | Google Contacts | Disabled |
| Samsung Gallery | Google Photos | Disabled |
| Samsung Files | Files by Google | Disabled |
| Samsung Internet | Chrome | Uninstalled |
| Samsung Notes | Google Keep | Uninstalled |
| Samsung Calculator | Google Calculator | Uninstalled |
| Samsung Voice Recorder | Voice Recorder (3rd party) | Uninstalled |

## Limitations

Without root/custom ROM, cannot change:
- Core SystemUI appearance (quick settings, notification shade)
- Status bar design
- System UI framework
- Some deeply-integrated Samsung services

## Future Tasks

If resuming work on this project:
- Test debloat script on fresh Samsung device
- Explore GCam ports for specific Samsung models
- Document custom ROM options (LineageOS, GrapheneOS)
- Create automated permission grant verification
- Add package restore scripts for specific features

## Commands Reference

```bash
# List packages
adb shell pm list packages | grep samsung

# Uninstall for user 0
adb shell pm uninstall --user 0 <package>

# Disable
adb shell pm disable-user --user 0 <package>

# Re-enable
adb shell pm enable <package>

# Grant permission
adb shell pm grant <package> <permission>

# Check defaults
adb shell cmd role get-role-holders <role>

# Open app in Play Store
adb shell am start -a android.intent.action.VIEW -d 'market://details?id=<package>'
```

## Safety Notes

- All changes are user-level only (`--user 0`)
- Factory reset restores everything
- No warranty void, no bootloader unlock needed
- Carrier config packages kept to avoid cellular issues
- Core framework untouched

## Session Stats

- **Duration:** Full day session (2025-11-12)
- **Packages analyzed:** 531 initial packages
- **Packages removed:** ~87 uninstalled, ~8 disabled
- **Google apps installed:** 15
- **Final package count:** ~440
- **Phases completed:** 6

Phase breakdown:
1. Initial debloat (15 packages)
2. Additional bloat (28 packages)
3. Aggressive Samsung debloat (22 packages)
4. Disable duplicates (7 apps)
5. UI overlays & behavior overrides (22 packages)
6. Permissions & notification config

## Lessons Learned

1. Install date clustering is highly effective for bloat identification
2. `disable-user` safer than `uninstall` for system apps
3. Behavior overrides more impactful than simple bloat removal
4. Samsung keyboard must be replaced before removal (Gboard)
5. Samsung launcher must be replaced before disabling (Lawnchair)
6. Google Recorder has device restrictions on Samsung
7. SystemUI replacement requires root - this is the hard limit
