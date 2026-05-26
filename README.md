# Buck's Samsung Android Debloating

Transform a Samsung phone into a near-Pixel experience by removing bloatware and replacing Samsung apps with Google equivalents, all without root access.

> **⚠️ Status:** This is "works for me" software. I've successfully used these scripts on my Samsung device, but your mileage may vary. Always review scripts before running and maintain backups. Test on your specific device at your own risk.

## What This Does

- Removes ~87 Samsung/carrier bloat packages
- Disables ~8 deeply-integrated Samsung apps
- Installs complete Google/Pixel app suite (15 apps)
- Configures notification priority for family contacts
- Achieves maximum debloat possible without root access

## Quick Start

### Prerequisites

1. **Enable on Phone:**

   - Settings → About phone → Tap "Build number" 7 times (Developer mode)
   - Settings → Developer options → Enable "USB debugging"
   - Settings → Developer options → Enable "Wireless debugging"

2. **Install ADB on Computer:**

   ```bash
   # On Linux/Mac (via Homebrew)
   brew install android-platform-tools

   # Or download from: https://developer.android.com/tools/releases/platform-tools
   ```

### Connect via Wireless ADB

1. **On phone:** Settings → Developer options → Wireless debugging → Pair device with pairing code
2. **Note:** IP, port, and 6-digit pairing code
3. **On computer:**
   ```bash
   adb pair <ip>:<pairing-port> <pairing-code>
   adb connect <ip>:<connection-port>
   adb devices  # Verify connection
   ```

### Run Debloat Script

The master script orchestrates 7 individual phase scripts for clean, modular execution:

```bash
# Run all phases
./scripts/master-debloat.adb.sh 192.168.87.245:44577

# See what would be executed (dry run)
./scripts/master-debloat.adb.sh 192.168.87.245:44577 --dry-run

# Skip Phase 4 (if you want to keep Samsung duplicates temporarily)
./scripts/master-debloat.adb.sh 192.168.87.245:44577 --skip-phase 4

# Run only Phase 1 (initial debloat)
./scripts/master-debloat.adb.sh 192.168.87.245:44577 --only-phase 1

# View all options
./scripts/master-debloat.adb.sh --help
```

**Phases:**

1. Initial debloat (15 packages)
2. Additional bloat (25 packages)
3. Aggressive Samsung (21 packages)
4. Disable duplicates (7 apps)
5. UI overlays (5 packages)
6. Behavior overrides (16 packages)
7. Grant permissions (10 apps)

Individual phase scripts are in `scripts/executed/` and can be run independently if needed.

### Install Google Apps

Open Play Store and install:

1. **Gboard** - Keyboard
2. **Lawnchair** - Launcher (Pixel-like)
3. **Google Phone** - Dialer
4. **Google Contacts** - Contacts
5. **Chrome** - Browser
6. **Google Keep** - Notes
7. **Google Calculator** - Calculator
8. **Google Clock** - Alarms/Timers
9. **Wallpapers by Google** - Pixel wallpapers
10. **Voice Recorder** - Audio recording (third-party alternative)

You likely already have: Messages, Photos, Calendar, Gmail, Files by Google

### Set Defaults

- **Keyboard:** Settings → General management → Keyboard → Gboard
- **Launcher:** Press home button → Lawnchair → Always
- **Phone:** Will prompt when making first call → Google Phone → Always
- **SMS:** Will prompt when sending SMS → Messages → Always

### Configure Family Notifications

1. **Star family contacts:**

   - Open Google Contacts
   - Tap each family member
   - Tap ⭐ star icon

2. **Configure Do Not Disturb:**

   - Settings → Notifications → Do Not Disturb
   - Calls → "Starred contacts only"
   - Messages → "Starred contacts only"
   - Enable "Repeat callers" (safety feature)

3. **Gmail priority (optional):**
   - Gmail → Settings → Your account → Notifications
   - Priority notifications → Star contacts

## What Gets Removed

### Bloatware (~87 packages)

- Bixby (all components)
- Samsung Daily/Tips/AR Zone
- Samsung Cloud/Pass/Pay
- Samsung Store/Members/Kids/Free
- Samsung themes/stickers/customization
- Game Launcher/Game Optimizer
- Verizon/carrier bloat (8 packages)
- Microsoft apps (OneDrive, App Manager)
- PWA wrappers, various bloat apps

### Behavior Overrides (~20 packages)

- Smart features (call, face, suggestions)
- Settings helper/interception
- Audio routing overrides
- Clipboard/input sharing
- Usage tracking services
- Privacy dashboard override
- Carrier customization

### Samsung Duplicates (disabled, not removed)

- Samsung Dialer → Google Phone
- Samsung Contacts → Google Contacts
- Samsung Gallery → Google Photos
- Samsung Files → Files by Google
- Samsung Calculator → Google Calculator
- Samsung Notes → Google Keep
- Samsung Internet → Chrome

## What Stays (Required)

~100-120 essential Samsung packages must remain:

- Network stack & telephony framework
- Samsung Knox (security)
- WiFi/NFC/Bluetooth drivers
- Camera SDK services
- Biometrics (fingerprint/face)
- Core system framework
- Hardware-specific services

## Limitations Without Root

**Cannot change:**

- Quick settings visual appearance (One UI style remains)
- Notification shade design
- Status bar appearance
- Core SystemUI framework

**To change these requires:**

- Unlocked bootloader
- Custom ROM (LineageOS, GrapheneOS, etc.)
- Full device wipe
- Warranty void

## Results

**Before:**

- 531 packages installed
- Samsung bloat throughout
- One UI experience

**After:**

- ~440 packages remaining
- Minimal Samsung interference
- Near-Pixel experience
- Google app ecosystem
- Clean, fast interface

## Project Structure

```
.
├── README.md                           # This file
├── CLAUDE.md                           # Project context for Claude
├── scripts/
│   ├── master-debloat.adb.sh          # Consolidated debloat script
│   ├── executed/                       # Individual scripts (for reference)
│   └── reference/                      # Unused reference scripts
├── docs/
│   └── devlog/
│       └── 2025-11-12-000-initial-debloat.md  # Complete session documentation
├── packages-install-dates.json         # Package analysis data
└── current-packages.txt                # Final package list
```

## Safety Notes

- All removals use `--user 0` flag (not system-wide)
- Factory reset restores all removed apps
- Disabled apps can be re-enabled: `adb shell pm enable <package>`
- Some features (Samsung DeX, smart features) may be wanted by some users
- Core telephony and framework packages left untouched

## Troubleshooting

### Reconnecting After Reboot

Wireless ADB requires re-pairing after reboot:

```bash
adb pair <ip>:<new-pairing-port> <new-pairing-code>
adb connect <ip>:<new-connection-port>
```

### Re-enable Samsung App

If you need a Samsung app back:

```bash
adb shell pm enable <package-name>
```

### Check Current Defaults

```bash
# Current keyboard
adb shell settings get secure default_input_method

# Current launcher
adb shell cmd role get-role-holders android.app.role.HOME

# Current phone app
adb shell cmd role get-role-holders android.app.role.DIALER

# Current SMS app
adb shell cmd role get-role-holders android.app.role.SMS
```

## Additional Resources

- [Android Developer - Platform Tools](https://developer.android.com/tools/releases/platform-tools)
- [Universal Android Debloater](https://github.com/0x192/universal-android-debloater)
- [ADB Commands Reference](https://developer.android.com/tools/adb)
- [Lawnchair Launcher](https://lawnchair.app/)

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) file for details.

## Credits

Session documented in `docs/devlog/2025-11-12-000-initial-debloat.md` - complete step-by-step process, commands, and analysis.

🤖 Created with [Claude Code](https://claude.com/claude-code)
