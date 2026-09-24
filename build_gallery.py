#!/usr/bin/env python3
"""Rebuild the baked-in gallery in index.html from images.json.

images.json is the single source of truth. Run this after adding pictures to it,
or the new ones are INVISIBLE: index.html carries the cards, and the runtime
fetch only adds Cloudinary assets that are NOT already in the manifest - so an
entry in images.json without a matching card suppresses its own card.

    python3 build_gallery.py            # rewrite the grid in index.html
    python3 build_gallery.py --check    # report only, change nothing
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'images.json'), encoding='utf-8'))
CLOUD, imgs = d['cloud'], d['images']
BASE = 'https://res.cloudinary.com/%s/image/upload/' % CLOUD

seen, cards, dropped = set(), [], []
for i in imgs:
    if i['branded'] in seen:              # one card per picture, ever
        dropped.append(i['id']); continue
    seen.add(i['branded'])
    h = round(520 * i['h'] / i['w'])
    cards.append(
        '<article class="card" data-slug="%s">'
        '<div class="frame"><img src="%sc_fit,w_520,f_auto,q_auto/%s.png" alt="%s" '
        'width="520" height="%d" loading="lazy"></div>'
        '<p class="cap">%s</p><p class="bk">%s</p>'
        '<div class="acts"><a class="dl" href="%sfl_attachment:%s/%s.png">Download</a>'
        '<a class="buy2" href="%s" rel="noopener">Buy the book</a></div></article>'
        % (i['slug'], BASE, i['branded'], html.escape(i['alt'], quote=True), h,
           html.escape(i['caption']), html.escape(i['book']),
           BASE, i['file'], i['branded'], i['amazon']))

path = os.path.join(HERE, 'index.html')
page = open(path, encoding='utf-8').read()
m = re.search(r'(<div class="grid" id="grid">)(.*?)(\n</div>)', page, re.S)
if not m:
    sys.exit('could not find the grid in index.html - not touching it')
before = m.group(2).count('<article class="card"')
new = m.group(1) + '\n' + '\n'.join(cards) + m.group(3)

print('manifest entries : %d' % len(imgs))
print('cards written    : %d' % len(cards))
print('duplicates skipped: %s' % (', '.join(dropped) if dropped else 'none'))
print('cards before     : %d' % before)
if '--check' in sys.argv:
    print('\n--check: index.html not modified')
    sys.exit(0)
open(path, 'w', encoding='utf-8').write(page[:m.start()] + new + page[m.end():])
print('\nrewrote the grid in index.html')
