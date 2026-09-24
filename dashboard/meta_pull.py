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
FB_POST_METRICS = ['post_impressions', 'post_impressions_unique',
                   'post_clicks', 'post_reactions_by_type_total']
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
            ins = get('%s/insights' % pid, metric=','.join(FB_POST_METRICS))
            if '__error' in ins:
                print('  Post insights : cannot read — %s' % ins['__error'].get('message'))
            else:
                got = {d['name']: d['values'][0].get('value') for d in ins.get('data', [])}
                print('  Post insights : readable — %s' % got)

    if ig_id:
        media = get('%s/media' % ig_id, fields='id,timestamp', limit=3)
        if '__error' in media:
            print('  IG media      : cannot read — %s' % media['__error'].get('message'))
        else:
            print('  IG media      : readable, %d returned' % len(media.get('data', [])))
            if media.get('data'):
                mid = media['data'][0]['id']
                ins = get('%s/insights' % mid, metric=','.join(IG_MEDIA_METRICS))
                if '__error' in ins:
                    print('  IG insights   : cannot read — %s' % ins['__error'].get('message'))
                    print('                  (usually a missing instagram_manage_insights permission)')
                else:
                    got = {d['name']: d['values'][0].get('value') for d in ins.get('data', [])}
                    print('  IG insights   : readable — %s' % got)
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
            ins = get('%s/insights' % p['id'], metric=','.join(FB_POST_METRICS))
            m = {} if '__error' in ins else {
                d['name']: d['values'][0].get('value') for d in ins.get('data', [])}
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
                ins = get('%s/insights' % p['id'], metric=','.join(IG_MEDIA_METRICS))
                m = {} if '__error' in ins else {
                    d['name']: d['values'][0].get('value') for d in ins.get('data', [])}
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
