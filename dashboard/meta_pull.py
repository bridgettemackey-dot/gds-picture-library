#!/usr/bin/env python3
"""Read Facebook Page and Instagram insights straight from Meta, as a second
source alongside Buffer.

    python3 dashboard/meta_pull.py --probe   # check the token, print what it can see
    python3 dashboard/meta_pull.py           # pull insights -> dashboard/meta.json

Needs META_PAGE_TOKEN in the environment: a long-lived Facebook PAGE access
token. Page tokens derived from a long-lived user token do not expire, so this
is set once. The script never prints the token and never writes it to disk.
"""
import json, os, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = 'https://graph.facebook.com/v21.0'
TOKEN = os.environ.get('META_PAGE_TOKEN')

# What each object can report. Meta renamed several of these in v22; if a metric
# is rejected the call retries without it rather than losing the whole pull.
# Verified against the live API on 24 Sep 2026. Meta has REMOVED impressions and
# reach from the Pages API entirely - post_impressions, post_reach, post_views and
# every page-level equivalent are rejected as invalid metrics on v19 through v23.
# What survives is engagement only. Do not re-add them without testing first.
FB_POST_METRICS = ['post_clicks', 'post_reactions_by_type_total',
                   'post_activity_by_action_type', 'post_reactions_like_total']
IG_MEDIA_METRICS = ['reach', 'likes', 'comments', 'saved', 'shares', 'views']


def get(path, **params):
    params['access_token'] = TOKEN
    url = '%s/%s?%s' % (GRAPH, path.lstrip('/'), urllib.parse.urlencode(params))
    try:
        return json.loads(urllib.request.urlopen(url, timeout=60).read())
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', 'replace')
        try:
            err = json.loads(body)['error']
        except Exception:
            err = {'message': body[:200]}
        return {'__error': err, '__status': e.code}


def insights(obj_id, metrics):
    """Ask for everything, then fall back to one at a time.

    Meta retires metric names without warning and rejects the WHOLE call if any
    one name is stale, which would silently cost every other figure on the post.
    """
    d = get('%s/insights' % obj_id, metric=','.join(metrics))
    if '__error' not in d:
        return {x['name']: x['values'][0].get('value') for x in d.get('data', [])}, []
    out, dead = {}, []
    for m in metrics:
        one = get('%s/insights' % obj_id, metric=m)
        if '__error' in one:
            dead.append(m)
        else:
            for x in one.get('data', []):
                out[x['name']] = x['values'][0].get('value')
    return out, dead


def die(msg, detail=None):
    print('FAILED: ' + msg)
    if detail:
        print('  Meta said: %s' % detail)
    sys.exit(1)


def resolve():
    """Find the Page and the Instagram business account behind this token."""
    me = get('me', fields='id,name')
    if '__error' in me:
        die('the token was rejected', me['__error'].get('message'))
    page_id, page_name = me['id'], me.get('name', '?')

    ig = get(page_id, fields='instagram_business_account{id,username}')
    iga = (ig or {}).get('instagram_business_account') or {}
    return page_id, page_name, iga.get('id'), iga.get('username')


def probe():
    if not TOKEN:
        die('META_PAGE_TOKEN is not set in this environment. '
            'Add it in the environment settings, then start a new session.')
    page_id, page_name, ig_id, ig_user = resolve()
    print('token works.')

    # Which permissions the token actually carries. Meta offers two Instagram
    # families - instagram_* (Facebook Login) and instagram_business_* (Instagram
    # Login) - and only the granted set tells you which path this token is on.
    dbg = get('debug_token', input_token=TOKEN)
    info = (dbg or {}).get('data') or {}
    if info:
        print('  token type    : %s, expires %s'
              % (info.get('type'), 'never' if info.get('expires_at') == 0 else info.get('expires_at')))
        granted = sorted(info.get('scopes') or [])
        declined = []
        print('  granted       : %s' % (', '.join(granted) or 'none'))
        if declined:
            print('  NOT granted   : %s' % ', '.join(declined))
        fb_family = [p for p in granted if p.startswith('instagram_')
                     and not p.startswith('instagram_business_')]
        ig_family = [p for p in granted if p.startswith('instagram_business_')]
        if ig_family and not fb_family:
            print('  NOTE: this token carries the instagram_business_* family, which belongs')
            print('        to Instagram Login, not Facebook Login. The media calls below use')
            print('        the Facebook Login endpoints; if they fail, that is why, and the')
            print('        fix is to read via graph.instagram.com instead.')
        if not any(p.endswith('manage_insights') for p in granted):
            print('  NOTE: no *_manage_insights permission was granted - per-post reach and')
            print('        saves will come back empty however well everything else works.')

    print('  Facebook Page : %s  (id %s)' % (page_name, page_id))
    if ig_id:
        print('  Instagram     : @%s  (id %s)' % (ig_user, ig_id))
    else:
        print('  Instagram     : NOT LINKED to this Page — insights will be Facebook only.')
        print('                  Link the IG professional account to the Page in Meta')
        print('                  Business Suite, then re-run this probe.')

    posts = get('%s/posts' % page_id, fields='id,created_time', limit=3)
    if '__error' in posts:
        print('  Page posts    : cannot read — %s' % posts['__error'].get('message'))
        print('                  (usually a missing pages_read_engagement permission)')
    else:
        print('  Page posts    : readable, %d returned' % len(posts.get('data', [])))
        if posts.get('data'):
            pid = posts['data'][0]['id']
            got, dead = insights(pid, FB_POST_METRICS)
            if not got and dead:
                print('  Post insights : cannot read any of %s' % dead)
            else:
                print('  Post insights : readable — %s' % got)
                if dead:
                    print('                  retired metrics, skipped: %s' % dead)

    if ig_id:
        media = get('%s/media' % ig_id, fields='id,timestamp', limit=3)
        if '__error' in media:
            print('  IG media      : cannot read — %s' % media['__error'].get('message'))
        else:
            print('  IG media      : readable, %d returned' % len(media.get('data', [])))
            if media.get('data'):
                mid = media['data'][0]['id']
                got, dead = insights(mid, IG_MEDIA_METRICS)
                if not got and dead:
                    print('  IG insights   : cannot read any of %s' % dead)
                    print('                  (usually a missing instagram_manage_insights permission)')
                else:
                    print('  IG insights   : readable — %s' % got)
                    if dead:
                        print('                  retired metrics, skipped: %s' % dead)
    print('\nIf every line above reads "readable", run without --probe to pull the figures.')


def pull():
    page_id, page_name, ig_id, ig_user = resolve()
    out = {'page': {'id': page_id, 'name': page_name}, 'posts': [], 'media': []}

    nxt = '%s/posts' % page_id
    params = {'fields': 'id,created_time,permalink_url,message', 'limit': 50}
    while nxt:
        page = get(nxt, **params) if not nxt.startswith('http') else json.loads(
            urllib.request.urlopen(nxt, timeout=60).read())
        if '__error' in page:
            print('  page posts stopped: %s' % page['__error'].get('message')); break
        for p in page.get('data', []):
            m, _ = insights(p['id'], FB_POST_METRICS)
            out['posts'].append({'id': p['id'], 'at': p.get('created_time'),
                                 'url': p.get('permalink_url'), 'm': m})
        nxt = (page.get('paging') or {}).get('next'); params = {}
    print('facebook posts: %d' % len(out['posts']))

    if ig_id:
        out['ig'] = {'id': ig_id, 'username': ig_user}
        nxt = '%s/media' % ig_id
        params = {'fields': 'id,timestamp,permalink,caption', 'limit': 50}
        while nxt:
            page = get(nxt, **params) if not nxt.startswith('http') else json.loads(
                urllib.request.urlopen(nxt, timeout=60).read())
            if '__error' in page:
                print('  ig media stopped: %s' % page['__error'].get('message')); break
            for p in page.get('data', []):
                m, _ = insights(p['id'], IG_MEDIA_METRICS)
                out['media'].append({'id': p['id'], 'at': p.get('timestamp'),
                                     'url': p.get('permalink'), 'm': m})
            nxt = (page.get('paging') or {}).get('next'); params = {}
        print('instagram media: %d' % len(out['media']))

    path = os.path.join(HERE, 'meta.json')
    json.dump(out, open(path, 'w'), indent=1)
    print('wrote %s' % path)


if __name__ == '__main__':
    if not TOKEN:
        die('META_PAGE_TOKEN is not set in this environment. '
            'Add it in the environment settings, then start a new session.')
    probe() if '--probe' in sys.argv else pull()
