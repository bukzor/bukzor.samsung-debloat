# Samsung "Auto Blocker" greys out USB debugging

On One UI 6.1+/Android 14+, Samsung's **Auto Blocker** is a *setting* (not an
app — it cannot be uninstalled). One of its functions, "Block harmful commands
& software via USB cable," **greys out the USB-debugging toggle** in Developer
options.

To enable ADB over USB you must first turn it off:
**Settings → Security and privacy → Auto Blocker → off**
(some builds: Security and privacy → More security settings → Auto Blocker).

Two caveats:
- Since we use **wireless** ADB anyway (see
  `wireless-adb-only-on-crostini.md`), Auto Blocker does **not** need to be off
  for our workflow — it only blocks USB.
- Auto Blocker is a **good** anti-malware control (blocks sideloading and USB
  attacks). Plan to leave it **on** as part of the post-wipe lockdown. The user
  disabled it for 30 minutes during the USB detour; that timer is irrelevant to
  wireless work.
