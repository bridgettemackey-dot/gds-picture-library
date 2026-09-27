#!/usr/bin/env python3
"""Check a week's schedule BEFORE it is queued. Passing does not guarantee that
Instagram will publish, but failing guarantees a loss.

    python3 sched/verify.py sched/wk43.py
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
    for k in ('fb', 'ig', 'pin'):
        if m.GDSI not in s[k]:
            problems.append('no GDS-Images line in ' + k)
    print('%s %-42s %s ratio %.2f alt %-4d %s'
          % (s['day'], s['pid'].rsplit('/', 1)[-1], im.mode if im else '??', ratio, len(s['alt']),
             'OK' if not problems else 'PROBLEMS: ' + '; '.join(problems)))
    bad += len(problems)
print('\nslots: %d | problems: %d' % (len(m.S), bad))
sys.exit(1 if bad else 0)
