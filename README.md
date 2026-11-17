# 📱 iOS Rebuilt

**An open-source, iOS-style operating system that runs in your browser and installs on your iPhone home screen.**
One HTML file. No frameworks, no build step, no App Store, and no Mac required.

> Fan project for learning and fun. Not affiliated with or endorsed by Apple.

## ✨ Features

**System**
- 🔒 Lock screen with live clock, notifications, flashlight and camera shortcuts, plus an optional **4-digit passcode**
- 🏠 Home screen with multiple swipeable pages, **widgets** (clock/calendar and weather), a dock and notification badges
- ✏️ **Jiggle mode**: long-press an icon, tap two icons to swap them, tap − to delete
- 🎛️ **Control Center**: toggles, Focus, dark mode, flashlight, brightness, volume and music controls
- 🔀 **App Switcher**: swipe up on the home bar, then flick cards away to close apps
- 🔍 Spotlight search, banner notifications, and a Dynamic Island on larger screens
- 🌗 Light and dark mode, plus wallpapers (including your own photos)
- ☁️ **Cloud**: an iCloud-style account with automatic backups, a storage breakdown, and backup files you can download or restore to move to another device

**28 apps** (incl. Translate, Stocks, Tiles game, FaceTime, Magnifier, in-app Safari)
| | | | |
|---|---|---|---|
| 📞 Phone (real calls) | 💬 Messages + Siri bot | 🧭 Safari | 🎵 Music (synth + your files) |
| 📷 Camera (live) | 🌸 Photos | 📝 Notes | ☑️ Reminders |
| 📅 Calendar | ⏰ Clock (world/alarm/stopwatch/timer) | ⛅ Weather (live, 7-day) | 🗺️ Maps (OpenStreetMap) |
| 🧮 Calculator | 👤 Contacts | 🧭 Compass | 🎙️ Voice Memos |
| 📁 Files | ❤️ Health | 📰 News | 💡 Tips |
| ⚙️ Settings | ☁️ Cloud | 🛍️ App Store | |

Original iOS-style vector icons (glyphs from [Lucide](https://lucide.dev), ISC) — live Clock & Calendar icons.

All data stays **on your device** (localStorage). Nothing is sent anywhere except public API calls for weather, maps and news.

## 🚀 Get it

### Option A: Download and run (easiest)
Download **[`ios-rebuilt.html`](ios-rebuilt.html)** and open it in any browser. That's it.

### Option B: Install on iPhone as an app
1. Host the repo with GitHub Pages: go to **Settings → Pages → Source: GitHub Actions** (the included workflow deploys `main`).
2. On your iPhone, open the Pages URL in **Safari**.
3. Tap **Share → Add to Home Screen**.
4. Launch it from the icon. It runs full-screen and works offline, and updates install automatically.

### Run locally
```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## 🛠️ Contributing: add your own app in ~20 lines

Everything lives in `index.html`. Find `APP REGISTRY` and add:

```js
defineApp('hello', {
  name: 'Hello', icon: '👋', bg: 'linear-gradient(#ff9a9e,#fad0c4)',
  render(win) {
    const body = page(win, 'Hello');               // large-title page
    body.appendChild(list([                         // iOS-style list
      { title: 'Say hi', onclick: () => notify('hello', 'Hello', 'Hi there! 👋') }
    ]));
  }
});
```

Then add `'hello'` to a page in `DEFAULT_LAYOUT` (or install it from the App Store).
Helpers: `page()`, `list()`, `switchEl()`, `store.get/set()`, `notify()`, `toast()`, `pickImage()`, `cloudSync()`.

After editing, run `python3 build.py` to regenerate the single-file download. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 🗺️ Roadmap
- [ ] Drag-and-drop icon rearranging
- [ ] Folders on the home screen
- [ ] Real cross-device Cloud sync (optional backend)
- [ ] Lock screen customization
- [ ] More apps: Podcasts, Stocks, Translate, Measure, Games
- [ ] Localization

## 📄 License
MIT. Do whatever you want, just keep the license.
