# -*- coding: utf-8 -*-
"""Shared posting runner for a week's schedule.

A slot is either SINGLE or a COLLAGE DAY:

  single   pid='gds/<slug>/<name>'              one picture on all three channels
  collage  panels=['gds/<slug>/a', ...]         Facebook and Instagram get a native
                                                CAROUSEL of the panels at full size;
                                                Pinterest gets ONE composited collage,
                                                because a pin cannot carousel.

Bridge, 11 Oct 2026: a collage on at least four days a week, mixing existing and
newly generated pictures, every panel from the same book. Four panels, two new and
two catalogued, is the agreed default.

Verified 11 Oct: Buffer accepts a list of assets on both Facebook and Instagram -
four panels created and read back on each. `assets` is a LIST in CreatePostInput.

The Pinterest collage is built by collage.py and uploaded under
`gds/<slug>/collage-<theme>-<YYYYMMDD>`. It is NOT added to images.json: every
panel is already a card in the picture library, so the collage would duplicate them.
"""
import json, os, urllib.request

K = os.environ['BUFFER_API_KEY']; CN = os.environ['CLOUDINARY_CLOUD_NAME']
FB, IG, PIN = '6a87c738ccaf649a67e82609', '6a8bbcd7ccaf649a6704f154', '6a8bbd26ccaf649a6704f202'

STD = lambda p: "https://res.cloudinary.com/%s/image/upload/%s.png" % (CN, p)
IGC = lambda p: "https://res.cloudinary.com/%s/image/upload/c_fill,ar_4:5,g_auto,w_1080,f_jpg,q_auto:good/%s.jpg" % (CN, p)
IGP = lambda p: "https://res.cloudinary.com/%s/image/upload/c_pad,b_rgb:fffef8,w_1080,h_1350,f_jpg,q_85/%s.jpg" % (CN, p)

M = """mutation($input: CreatePostInput!){ createPost(input:$input){
  ... on PostActionSuccess { post { id status dueAt channelService } }
  ... on InvalidInputError { message } ... on RestProxyError { message code }
  ... on LimitReachedError { message } ... on NotFoundError { message }
  ... on UnauthorizedError { message } ... on UnexpectedError { message } } }"""


def call(q, v):
    r = urllib.request.Request('https://api.buffer.com/graphql',
        data=json.dumps({'query': q, 'variables': v}).encode(),
        headers={'Authorization': 'Bearer ' + K, 'Content-Type': 'application/json'})
    return json.loads(urllib.request.urlopen(r, timeout=90).read())


def asset(url, alt):
    return {'image': {'url': url, 'thumbnailUrl': url, 'metadata': {'altText': alt[:480]}}}


def send(ch, text, due, assets, meta):
    v = {'input': {'channelId': ch, 'text': text, 'mode': 'customScheduled',
         'schedulingType': 'automatic', 'dueAt': due, 'assets': assets, 'metadata': meta}}
    d = call(M, v)
    node = d.get('data', {}).get('createPost', {})
    if 'post' in node:
        p = node['post']
        print('  ok  %s %-10s %d asset(s)' % (p['dueAt'][:16], p['channelService'], len(assets)))
        return True
    print('  FAIL', json.dumps(d)[:260])
    return False


def run(slots):
    """slots: the S list from a wk*.py. Returns (ok, failed)."""
    ok = fail = 0
    for s in slots:
        d, b = s['day'], s['base']
        panels = s.get('panels')
        alts = s.get('alts') or []
        if panels:
            if len(panels) != len(alts):
                print('  FAIL %s: %d panels but %d alts' % (d, len(panels), len(alts)))
                fail += 3; continue
            if len({p.split('/')[1] for p in panels}) != 1:
                print('  FAIL %s: panels span more than one book' % d)
                fail += 3; continue
            pad = s.get('pad_panels') or [False] * len(panels)
            fb_assets = [asset(STD(p), a) for p, a in zip(panels, alts)]
            ig_assets = [asset((IGP if q else IGC)(p), a) for p, q, a in zip(panels, pad, alts)]
            pin_assets = [asset(STD(s['collage']), s['alt'])]
        else:
            ig_url = (IGP if s['pad'] else IGC)(s['pid'])
            fb_assets = [asset(STD(s['pid']), s['alt'])]
            ig_assets = [asset(ig_url, s['alt'])]
            pin_assets = [asset(STD(s['pid']), s['alt'])]
        for ch, due, text, assets, meta in (
            (FB,  '%sT%02d:00:00Z' % (d, b), s['fb'],  fb_assets,  {'facebook': {'type': 'post'}}),
            (IG,  '%sT%02d:20:00Z' % (d, b), s['ig'],  ig_assets,
                  {'instagram': {'type': 'post', 'shouldShareToFeed': True}}),
            (PIN, '%sT%02d:40:00Z' % (d, b), s['pin'], pin_assets,
                  {'pinterest': {'boardServiceId': s['board'], 'title': s['pin_t'], 'url': s['pin_url']}}),
        ):
            if send(ch, text, due, assets, meta): ok += 1
            else: fail += 1
    print('\ncreated %d, failed %d' % (ok, fail))
    return ok, fail
