#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Every path images.json RECORDS must resolve - not just the path an upload printed.

25 Oct 2026. Fifteen cards on pictures.gdsbahamas.com were serving a 404 image:
every picture added from 18 Oct onward. brand.py uploads to
`gds-share/<slug>/<name>`, and the runbook says --name MUST end in -bhm. I passed
names WITHOUT the suffix and then wrote `...-bhm` into images.json by hand. The
sha256 check after each upload passed, because it checked the path brand.py had
just printed - never the different path the manifest was recording.

Verifying what you uploaded is not the same as verifying what you wrote down.
Run this after every images.json change, and before pushing.
"""
import json, os, sys, urllib.request

CN = os.environ['CLOUDINARY_CLOUD_NAME']
URL = 'https://res.cloudinary.com/%s/image/upload/%s.png'

def code(pid):
    try:
        return urllib.request.urlopen(
            urllib.request.Request(URL % (CN, pid), method='HEAD'), timeout=30).status
    except Exception as e:
        return getattr(e, 'code', 'ERR')

def main():
    d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images.json')))
    problems = []
    for i in d['images']:
        for field in ('clean', 'branded'):
            c = code(i[field])
            if c != 200:
                problems.append('%s: %s -> %s (%s)' % (i['id'], field, c, i[field]))
    for i in d['images']:
        if i['branded'] in d['retired'] or i['clean'] in d['retired']:
            problems.append('%s: points at a RETIRED path' % i['id'])
    print('library: %d images, %d paths checked' % (len(d['images']), len(d['images']) * 2))
    for p in problems:
        print('  PROBLEM', p)
    print('problems: %d' % len(problems))
    return 1 if problems else 0

if __name__ == '__main__':
    sys.exit(main())
