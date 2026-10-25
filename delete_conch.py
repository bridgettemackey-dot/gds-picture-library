#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Delete the superseded queen conch assets from Cloudinary.

Bridge, 25 Oct 2026: "I want to remove the queen conch image versions 2, 3 & 4
from pictures.gdsbahamas.com as they are incorrect and I don't want people
downloading them."

NEEDS CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET in the environment. The
unsigned upload preset cannot delete. Add them in the cloud environment settings
- never paste them into chat.

Run:  python3 delete_conch.py --dry-run     (lists, deletes nothing)
      python3 delete_conch.py --confirm     (actually deletes)
"""
import argparse, hashlib, json, os, sys, time, urllib.parse, urllib.request

# Everything carrying an incorrect conch. v5 and the v5 collage are NOT here.
DOOMED = [
    'gds/atb-upper/queen-conch-20261018',                 # v1, the garden-snail body
    'gds-share/atb-upper/queen-conch-20261018-bhm',       # v1 branded
    'gds/atb-upper/queen-conch-20261018-v2',
    'gds-share/atb-upper/queen-conch-20261018-v2',
    'gds/atb-upper/queen-conch-20261018-v3',
    'gds-share/atb-upper/queen-conch-20261018-v3',
    'gds/atb-upper/queen-conch-20261018-v4',
    'gds-share/atb-upper/queen-conch-20261018-v4',
    'gds/atb-upper/collage-island-culture-20261018',      # collage built on v1
    'gds/atb-upper/collage-island-culture-20261018-v2',
    'gds/atb-upper/collage-island-culture-20261018-v3',
    'gds/atb-upper/collage-island-culture-20261018-v4',
]
KEEP = [
    'gds/atb-upper/queen-conch-20261018-v5',
    'gds-share/atb-upper/queen-conch-20261018-v5',
    'gds/atb-upper/collage-island-culture-20261018-v5',
]

CN = os.environ['CLOUDINARY_CLOUD_NAME']

def guard():
    """Refuse to run if anything doomed is still referenced by the live library."""
    here = os.path.dirname(os.path.abspath(__file__))
    man = os.path.join(here, 'images.json')
    if not os.path.exists(man):
        man = '/home/user/gds-picture-library/images.json'
    d = json.load(open(man))
    live = set()
    for i in d['images']:
        live.add(i['clean']); live.add(i['branded'])
    clash = sorted(live & set(DOOMED))
    if clash:
        sys.exit('REFUSING: images.json still points at %s' % clash)
    missing = [k for k in KEEP if k not in live and 'collage' not in k]
    if missing:
        sys.exit('REFUSING: the keeper %s is not in images.json' % missing)
    print('guard ok - nothing doomed is referenced by images.json')

def destroy(pid):
    key, sec = os.environ['CLOUDINARY_API_KEY'], os.environ['CLOUDINARY_API_SECRET']
    ts = str(int(time.time()))
    sig = hashlib.sha1(('public_id=%s&timestamp=%s%s' % (pid, ts, sec)).encode()).hexdigest()
    body = urllib.parse.urlencode({'public_id': pid, 'timestamp': ts,
                                   'api_key': key, 'signature': sig}).encode()
    r = urllib.request.Request('https://api.cloudinary.com/v1_1/%s/image/destroy' % CN, data=body)
    return json.loads(urllib.request.urlopen(r, timeout=60).read())

def served(pid):
    u = 'https://res.cloudinary.com/%s/image/upload/%s.png' % (CN, pid)
    try:
        return urllib.request.urlopen(urllib.request.Request(u, method='HEAD'), timeout=30).status
    except Exception as e:
        return getattr(e, 'code', 'ERR')

a = argparse.ArgumentParser()
a.add_argument('--dry-run', action='store_true')
a.add_argument('--confirm', action='store_true')
a = a.parse_args()
if not (a.dry_run or a.confirm):
    sys.exit('pass --dry-run or --confirm')

guard()
print('\n%d assets to delete:' % len(DOOMED))
for p in DOOMED:
    print('   %-58s currently %s' % (p, served(p)))
print('\n%d assets to KEEP:' % len(KEEP))
for p in KEEP:
    print('   %-58s currently %s' % (p, served(p)))

if a.dry_run:
    print('\ndry run - nothing deleted'); sys.exit(0)

for v in ('CLOUDINARY_API_KEY', 'CLOUDINARY_API_SECRET'):
    if not os.environ.get(v):
        sys.exit('\n%s is not set. Add it in the cloud environment settings, '
                 'then re-run. Do not paste it into chat.' % v)

print()
for p in DOOMED:
    try:
        print('  %-58s %s' % (p, destroy(p).get('result')))
    except Exception as e:
        print('  %-58s FAILED %s' % (p, str(e)[:120]))

print('\nverifying:')
bad = 0
for p in DOOMED:
    c = served(p)
    if c == 200: bad += 1; print('  STILL SERVING', p)
for p in KEEP:
    c = served(p)
    if c != 200: bad += 1; print('  KEEPER BROKEN', p, c)
print('deleted and gone: %d/%d | problems: %d' % (len(DOOMED) - bad, len(DOOMED), bad))
