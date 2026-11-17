# Contributing to iOS Rebuilt

Thanks for helping rebuild iOS, one emoji icon at a time! 🎉

## Ground rules
- **One file.** The OS is `index.html`: plain HTML, CSS and JS with no frameworks and no build step. Keep it that way so anyone can download and run it.
- **No Apple assets.** Don't use Apple logos, SF Symbols, or copied artwork. Use emoji, CSS and original art.
- **Privacy first.** Store data with `store` (on-device). Use only free, keyless public APIs.
- **Mobile first.** Test at iPhone size (Chrome DevTools → device toolbar) and with touch.

## Workflow
1. Fork the repo and create a branch: `git checkout -b my-cool-app`
2. Edit `index.html` and test with `python3 -m http.server 8000`
3. Run `python3 build.py` to update `ios-rebuilt.html`
4. If you changed cached files, bump the `CACHE` version in `sw.js`
5. Open a pull request with a screenshot 📸

## Ideas
Check the Roadmap in the README, or open an issue to suggest an app.
