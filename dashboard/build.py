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
    'title': 'Pinterest pins ramp slowly \u2014 a young pin tells you nothing',
    'body': "This panel said for three weeks that Pinterest had stalled on 11 September and "
            "that no pin since had cleared ten impressions. THAT WAS WRONG, and eight "
            "exports covering 23 September to 11 October show why. A pin sits at one to five "
            "impressions for one to three weeks and then climbs, sometimes steeply. One pin "
            "read 2 impressions on 23 September, 13 on 30 September, and 680 by 11 October. "
            "Another went 1 \u2192 12 \u2192 348. Of the twelve newest pins, ten have now "
            "cleared ten impressions. The account is carrying 300\u2013450 impressions a day "
            "through October against about 70 a day in early September. Nothing stalled: the "
            "old reading measured pins while they were days old and called them dead. Judge a "
            "pin at a month, not at a week.",
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


SHOWN = {'facebook': 'impressions', 'pinterest': 'impressions', 'instagram': 'views'}
FLOOR = 10          # below this a post was published but never really carried


def _shown(p):
    return p['m'].get(SHOWN[p['ch']], 0)


def _acted(p):
    return sum(v for k, v in p['m'].items() if k not in ('engagementRate', SHOWN[p['ch']]))


def quiet_since(posts, channel):
    """Two runs, because they answer different questions.

    `silent`  - consecutive posts reporting literally nothing. Catches a channel
                that has stopped reporting.
    `weak`    - consecutive posts that never cleared FLOOR. Catches a channel that
                is still reporting but no longer carrying anything, which a
                single impression would otherwise hide.
    """
    seen = sorted([p for p in posts if p['ch'] == channel and p['d'] >= CAMPAIGN_START],
                  key=lambda p: p['d'], reverse=True)
    silent = weak = 0
    for p in seen:
        if _shown(p) or _acted(p):
            break
        silent += 1
    for p in seen:
        if _shown(p) >= FLOOR:
            break
        weak += 1
    last = next((p['d'] for p in seen if _shown(p) or _acted(p)), None)
    last_real = next((p['d'] for p in seen if _shown(p) >= FLOOR), None)
    return {'silent': silent, 'weak': weak, 'last': last, 'last_real': last_real,
            'floor': FLOOR, 'total': len(seen)}


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

    # Pinterest's own figures, from the manual exports. Buffer's Pinterest numbers
    # are a floor: they lag Pinterest's and the gap looks like reporting lag rather
    # than under-reporting, so prefer these wherever both exist.
    try:
        pj = json.load(open(os.path.join(HERE, 'pinterest.json')))
        traj = pj.get('trajectory') or {}
        ends = pj.get('snapshots') or []
        risers = []
        if len(ends) >= 2:
            a, b = ends[0], ends[-1]
            for pid, t in traj.items():
                first, last = t.get(a), t.get(b)
                if last is None:
                    continue
                risers.append({'id': pid[-9:], 'first': first, 'last': last,
                               'gain': last - (first or 0)})
            risers.sort(key=lambda r: -r['gain'])
        # Only pins still in the final snapshot: one that has dropped out of
        # Pinterest's top-50 table has no end value and would render as bars
        # trailing into nothing, which reads as a collapse rather than a gap.
        present = [q for q in traj if traj[q].get(ends[-1]) is not None] if ends else []
        newest = sorted(present, key=int)[-12:]
        data['pinterest'] = {
            'asof': pj.get('asof'), 'snapshots': ends,
            'daily': pj.get('daily') or {},
            'boards': pj.get('boards') or {},
            'totals': pj.get('totals') or {},
            'pins': len(pj.get('pins') or {}),
            'impressions': sum((pj.get('pins') or {}).values()),
            'risers': risers[:8],
            'newest': [{'id': q[-9:], 'v': (traj[q].get(ends[-1]) if ends else None)}
                       for q in newest],
            'ramp': {q[-9:]: [traj[q].get(e) for e in ends] for q in newest},
        }
    except FileNotFoundError:
        data['pinterest'] = None

    # Alert on a CHANGE of state, not on a channel that is simply small. Without
    # this, Facebook and Instagram alert every night forever and the one night
    # Pinterest recovers is lost in the noise.
    state_path = os.path.join(HERE, 'state.json')
    try:
        prev = json.load(open(state_path))
    except Exception:
        prev = {}
    state, news = {}, []
    for ch, q in data['meta']['quiet'].items():
        stalled = q['weak'] >= 8
        state[ch] = {'stalled': stalled, 'weak': q['weak']}
        was = (prev.get(ch) or {}).get('stalled')
        if was is None:
            print('note  %-9s %s (no previous run to compare)'
                  % (ch, 'stalled' if stalled else 'carrying'))
        elif stalled and not was:
            news.append('ALERT %-9s has STOPPED carrying - last %d posts never cleared %d'
                        % (ch, q['weak'], q['floor']))
        elif was and not stalled:
            news.append('ALERT %-9s is CARRYING AGAIN - a post cleared %d on %s'
                        % (ch, q['floor'], q['last_real']))
    for line in news:
        print(line)
    if not news:
        print('no change of state on any channel since the last run')
    for ch, q in data['meta']['quiet'].items():
        print('      %-9s weak run %-3d silent run %-3d last real figure %s'
              % (ch, q['weak'], q['silent'], q['last_real']))

    if '--check' not in sys.argv:
        json.dump(state, open(state_path, 'w'), indent=1)

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
