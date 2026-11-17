# iOS Rebuilt 📱

An iOS-style home screen you can install on your iPhone as a web app (PWA). No Xcode, no App Store.

## v1 features
- Lock screen with live clock (swipe up / tap to unlock, re-locks when you leave the app)
- Home screen + dock; long-press an icon to jiggle, tap two icons to swap them
- Control Center (swipe down from the top): toggles, working brightness slider, flashlight
- Apps: Calculator, Notes (saved on device), Stopwatch, Weather (live, Open-Meteo), Settings (wallpapers), Camera → set a photo as wallpaper
- Works offline once installed

## Install on iPhone
1. Host these files over HTTPS (GitHub Pages: Settings → Pages → deploy from this branch, root).
2. Open the URL in **Safari** → Share → **Add to Home Screen**.
3. Tap the new icon. Enjoy your bootleg OS.

## Run locally
`python3 -m http.server 8000` then open http://localhost:8000
