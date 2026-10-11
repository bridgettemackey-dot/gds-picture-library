#!/usr/bin/env python3
"""Check a week's schedule BEFORE it is queued. Passing does not guarantee that
Instagram will publish, but failing guarantees a loss.

    python3 sched/verify.py sched/wk47.py

Handles both slot shapes: a single picture, and a COLLAGE DAY where Facebook and
Instagram carry a carousel of panels and Pinterest carries one composited collage.
On a collage day every panel is checked the same way a single picture would be,
plus: all panels from the same book, one alt per panel, and the collage image
itself reachable.
"""
import importlib.util, io, sys, urllib.request
from PIL import Image

spec = importlib.util.spec_from_file_location('wk', sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
bad = 0


def check_image(std_url, ig_url, label, problems):
    try:
        r = urllib.request.urlopen(std_url, timeout=90)
        if r.status != 200 or not r.headers['content-type'].startswith('image/'):
            problems.append('%s std %s %s' % (label, r.status, r.headers['content-type']))
    except Exception as e:
        problems.append('%s std fetch failed: %s' % (label, e))
    if not ig_url:
        return None
    try:
        im = Image.open(io.BytesIO(urllib.request.urlopen(ig_url, timeout=90).read()))
        if im.mode != 'RGB':
            problems.append('%s IG mode %s' % (label, im.mode))
        ratio = im.size[0] / im.size[1]
        if not 0.8 <= ratio <= 1.91:
            problems.append('%s IG ratio %.3f' % (label, ratio))
        return ratio
    except Exception as e:
        problems.append('%s IG fetch failed: %s' % (label, e))
        return None


for s in m.S:
    problems = []
    panels = s.get('panels')
    if panels:
        alts = s.get('alts') or []
        pad = s.get('pad_panels') or [False] * len(panels)
        if len(alts) != len(panels):
            problems.append('%d panels but %d alts' % (len(panels), len(alts)))
        if len({p.split('/')[1] for p in panels}) != 1:
            problems.append('panels span more than one book')
        if not s.get('collage'):
            problems.append('collage day with no composited collage for Pinterest')
        for i, p in enumerate(panels):
            check_image(m.STD(p), (m.IGP if pad[i] else m.IGC)(p), 'panel%d' % (i + 1), problems)
        for i, a in enumerate(alts):
            if len(a) > 500:
                problems.append('panel%d alt %d' % (i + 1, len(a)))
        if s.get('collage'):
            check_image(m.STD(s['collage']), None, 'collage', problems)
        shown = 'COLLAGE x%d' % len(panels)
    else:
        check_image(m.STD(s['pid']), (m.IGP if s['pad'] else m.IGC)(s['pid']), 'img', problems)
        shown = s['pid'].rsplit('/', 1)[-1]
    if len(s['alt']) > 500:
        problems.append('alt %d' % len(s['alt']))
    for k in ('fb', 'ig', 'pin'):
        if m.GDSI not in s[k]:
            problems.append('no GDS-Images line in ' + k)
    # A picture of Anna must say so in the alt, in the book's own terms. This does
    # not prove the render is right - only looking at it does - but it catches the
    # run that generated her without ever thinking about how she looks, which is
    # exactly what happened on 4 Oct 2026.
    blob = (s['alt'] + ' ' + ' '.join(s.get('alts') or []) + ' '
            + s['fb'] + ' ' + s['ig'] + ' ' + s['pin']).lower()
    if 'anna' in blob:
        a = (s['alt'] + ' ' + ' '.join(s.get('alts') or [])).lower()
        if 'anna' not in a:
            problems.append("captions name Anna but no alt describes her")
        if 'chocolate-brown' not in a:
            problems.append("Anna's alt must say chocolate-brown skin (see sched/characters.py)")
        if 'black hair' not in a:
            problems.append("Anna's alt must say long black hair (see sched/characters.py)")
    print('%s %-42s %s' % (s['day'], shown, 'OK' if not problems else 'PROBLEMS: ' + '; '.join(problems)))
    bad += len(problems)

n_collage = sum(1 for s in m.S if s.get('panels'))
days = sorted({s['day'] for s in m.S})
collage_days = sorted({s['day'] for s in m.S if s.get('panels')})
print('\nslots: %d over %d days | collage slots: %d on %d days (%s)'
      % (len(m.S), len(days), n_collage, len(collage_days), ', '.join(collage_days) or 'none'))
print('problems: %d' % bad)
sys.exit(1 if bad else 0)
