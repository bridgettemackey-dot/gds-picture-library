#!/usr/bin/env python3
"""Rebuild the GDS post-activity dashboard from live Buffer data.

    python3 dashboard/build.py            # writes dashboard/index.html
    python3 dashboard/build.py --check    # pull and report, write nothing

Needs BUFFER_API_KEY in the environment. Thumbnails are cached in
dashboard/thumbs.json so a daily run only fetches pictures it has not seen.
The page is then published to the artifact with `url`, never without it —
publishing without the url creates a second, orphaned dashboard.
"""
import base64, collections, io, json, os, re, sys, urllib.request
import concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
ORG  = '6a87c5fd3160101448e2db31'
API  = 'https://api.buffer.com/graphql'
CAMPAIGN_START = '2026-08-01'
BOOK = {'girl-whale':'The Girl and The Whale','girl-whale-activity':'Girl & Whale Activity Book',
        'regatta':'Going To The Regatta','regatta-activity':'Regatta Activity Book',
        'atb-upper':'All Things Bahamian: Upper','atb-lower':'All Things Bahamian: Lower'}

# Dated caveats the page shows against a channel. Remove one when it stops being true.
CAVEATS = [{
    'channel': 'pinterest',
    'from': '2026-09-11',
    'title': 'Pinterest stopped distributing new pins on 11 September',
    'body': "Every pin published since 11 September has earned nothing \u2014 seventeen in a row. "
            "This is REAL, not a reporting gap: Pinterest's own per-pin analytics show zero for those "
            "pins too, checked on 22 September. Buffer is reporting accurately. The pins publish fine "
            "and are publicly live, and pins from August and early September are still circulating and "
            "still gaining \u2014 they added 203 impressions in a single day, which is the whole of the "
            "rising curve on Pinterest's account chart. So the account keeps the reach it already built "
            "while anything new goes nowhere. That is an account-level distribution problem, not a "
            "problem with any individual pin.",
}]

KEY = os.environ.get('BUFFER_API_KEY')
if not KEY:
    sys.exit('BUFFER_API_KEY is not set — cannot reach Buffer. Nothing was written.')


def call(query, variables):
    req = urllib.request.Request(API, data=json.dumps(
        {'query': query, 'variables': variables}).encode(),
        headers={'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    out = json.loads(urllib.request.urlopen(req, timeout=120).read())
    if 'errors' in out:
        raise RuntimeError(json.dumps(out['errors'])[:400])
    return out['data']


POSTS_Q = """query($input: PostsInput!, $first: Int, $after: String){
  posts(input:$input, first:$first, after:$after){
    pageInfo{ hasNextPage endCursor }
    edges{ node{ id status sentAt channelService externalLink metricsUpdatedAt
      metrics{ type name description unit value }
      assets{ ... on ImageAsset { source } } } } } }"""


def fetch_sent():
    rows, after = [], None
    while True:
        v = {'input': {'organizationId': ORG, 'filter': {'status': ['sent']}}, 'first': 50}
        if after:
            v['after'] = after
        page = call(POSTS_Q, v)['posts']
        rows += [e['node'] for e in page['edges']]
        if not page['pageInfo']['hasNextPage']:
            break
        after = page['pageInfo']['endCursor']
    return rows


def thumbnails(sources):
    """Fetch and shrink any picture not already cached. Cache survives in git."""
    path = os.path.join(HERE, 'thumbs.json')
    try:
        cache = json.load(open(path))
    except Exception:
        cache = {}
    missing = [s for s in sources if s and s not in cache]
    if missing:
        from PIL import Image

        def grab(src):
            try:
                raw = urllib.request.urlopen(urllib.request.Request(
                    src, headers={'User-Agent': 'Mozilla/5.0'}), timeout=45).read()
                im = Image.open(io.BytesIO(raw)); im.load()
                if im.mode != 'RGB':
                    im = im.convert('RGB')
                im.thumbnail((120, 120), Image.LANCZOS)
                buf = io.BytesIO(); im.save(buf, 'JPEG', quality=72, optimize=True)
                return src, 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
            except Exception:
                return src, ''          # a picture that will not load is not worth failing over

        with cf.ThreadPoolExecutor(8) as pool:
            for src, data in pool.map(grab, missing):
                cache[src] = data
        json.dump(cache, open(path, 'w'))
        print('thumbnails: %d new, %d cached' % (len(missing), len(cache)))
    return cache


def quiet_since(posts, channel):
    """Days of consecutive silence: how long since this channel last reported anything."""
    seen = [p for p in posts if p['ch'] == channel and p['d'] >= CAMPAIGN_START]
    seen.sort(key=lambda p: p['d'], reverse=True)
    run = 0
    for p in seen:
        if any(v for k, v in p['m'].items() if k != 'engagementRate'):
            break
        run += 1
    last = next((p['d'] for p in seen if any(v for k, v in p['m'].items() if k != 'engagementRate')), None)
    return {'silent': run, 'last': last, 'total': len(seen)}


def main():
    raw = fetch_sent()
    print('sent posts: %d' % len(raw))
    thumbs = thumbnails({(p.get('assets') or [{}])[0].get('source') for p in raw})

    posts = []
    for p in raw:
        src = (p.get('assets') or [{}])[0].get('source') or ''
        slug = re.search(r'/gds/([a-z-]+)/', src)
        mets = {m['type']: m['value'] for m in (p.get('metrics') or [])}
        posts.append({
            'id': p['id'], 'd': p['sentAt'][:10], 'ch': p['channelService'],
            'txt': ' '.join((p.get('text') or '').split())[:200],
            'url': p.get('externalLink') or '', 'th': thumbs.get(src) or '',
            'book': BOOK.get(slug.group(1)) if slug else '',
            'm': {k: (round(v, 2) if k == 'engagementRate' else int(v))
                  for k, v in mets.items() if v},
        })
    posts.sort(key=lambda r: r['d'], reverse=True)

    glossary = {}
    for p in raw:
        for m in (p.get('metrics') or []):
            glossary.setdefault(m['type'], {'name': m['name'], 'unit': m['unit'],
                                            'description': m['description'],
                                            'channels': []})
            ch = p['channelService']
            if ch not in glossary[m['type']]['channels']:
                glossary[m['type']]['channels'].append(ch)

    data = {'meta': {
                'fresh': max(p['metricsUpdatedAt'] for p in raw if p.get('metricsUpdatedAt')),
                'built': __import__('datetime').datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ'),
                'n': len(posts),
                'quiet': {ch: quiet_since(posts, ch) for ch in ('facebook', 'instagram', 'pinterest')},
                'caveats': CAVEATS},
            'glossary': glossary, 'posts': posts}

    for ch, q in data['meta']['quiet'].items():
        if q['silent']:
            print('ALERT %-9s silent on the last %d posts (last figure %s)' % (ch, q['silent'], q['last']))

    if '--check' in sys.argv:
        return
    tmpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
    blob = json.dumps(data, separators=(',', ':'))
    if '</script' in blob:
        raise RuntimeError('post text contains a script tag — refusing to inline it')
    out = os.path.join(HERE, 'index.html')
    open(out, 'w', encoding='utf-8').write(tmpl.replace('__DATA__', blob))
    print('wrote %s (%.1f MB)' % (out, os.path.getsize(out) / 1e6))


if __name__ == '__main__':
    main()
