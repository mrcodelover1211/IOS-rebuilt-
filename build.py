"""Builds ios-rebuilt.html: a single self-contained file (icon inlined, no service worker needed).
Run: python3 build.py"""
import base64
html = open('index.html', encoding='utf-8').read()
icon = base64.b64encode(open('icons/icon-180.png', 'rb').read()).decode()
html = html.replace('<link rel="manifest" href="manifest.json">\n', '')
html = html.replace('href="icons/icon-180.png"', f'href="data:image/png;base64,{icon}"')
open('ios-rebuilt.html', 'w', encoding='utf-8').write(html)
print('Built ios-rebuilt.html')
