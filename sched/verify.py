#!/usr/bin/env python3
"""Check a week's schedule BEFORE it is queued. Passing does not guarantee that
Instagram will publish, but failing guarantees a loss.

    python3 sched/verify.py sched/wk45.py
"""
import importlib.util, io, sys, urllib.request
from PIL import Image

spec = importlib.util.spec_from_file_location('wk', sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
bad = 0
for s in m.S:
    ig = (m.IGP if s['pad'] else m.IGC)(s['pid']); std = m.STD(s['pid'])
    problems = []
    try:
        r = urllib.request.urlopen(std, timeout=90)
        if r.status != 200 or not r.headers['content-type'].startswith('image/'):
            problems.append('std %s %s' % (r.status, r.headers['content-type']))
    except Exception as e:
        problems.append('std fetch failed: %s' % e)
    try:
        im = Image.open(io.BytesIO(urllib.request.urlopen(ig, timeout=90).read()))
        ratio = im.size[0] / im.size[1]
        if im.mode != 'RGB':
            problems.append('IG mode ' + im.mode)
        if not 0.8 <= ratio <= 1.91:
            problems.append('IG ratio %.3f' % ratio)
    except Exception as e:
        problems.append('IG fetch failed: %s' % e); im = None; ratio = 0
    if len(s['alt']) > 500:
        problems.append('alt %d' % len(s['alt']))
    # A picture of Anna must say so in the alt, in the book's own terms. This does
    # not prove the render is right - only looking at it does - but it catches the
    # run that generated her without ever thinking about how she looks, which is
    # exactly what happened on 4 Oct 2026.
    blob = (s['alt'] + ' ' + s['fb'] + ' ' + s['ig'] + ' ' + s['pin']).lower()
    if 'anna' in blob:
        a = s['alt'].lower()
        if 'anna' not in a:
            problems.append("captions name Anna but the alt does not describe her")
        if 'chocolate-brown' not in a:
            problems.append("Anna's alt must say chocolate-brown skin (see sched/characters.py)")
        if 'black hair' not in a:
            problems.append("Anna's alt must say long black hair (see sched/characters.py)")
    for k in ('fb', 'ig', 'pin'):
        if m.GDSI not in s[k]:
            problems.append('no GDS-Images line in ' + k)
    print('%s %-42s %s ratio %.2f alt %-4d %s'
          % (s['day'], s['pid'].rsplit('/', 1)[-1], im.mode if im else '??', ratio, len(s['alt']),
             'OK' if not problems else 'PROBLEMS: ' + '; '.join(problems)))
    bad += len(problems)
print('\nslots: %d | problems: %d' % (len(m.S), bad))
sys.exit(1 if bad else 0)
