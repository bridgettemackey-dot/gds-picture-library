#!/usr/bin/env python3
"""Publish Instagram posts that Buffer failed to publish, directly through Meta.

    python3 ig_rescue.py --dry-run    # show what it would do, publish nothing
    python3 ig_rescue.py              # rescue them for real

Buffer's Instagram error - "Failed to create media container for instagram: the
media could not be fetched from this URI" - IS Meta's own POST /<ig>/media step.
Buffer is relaying Meta, not failing itself, and it tries exactly once. Every post
re-queued by hand has eventually published, so the fault is transient and a retry
is the whole fix. This does the retry automatically instead of a day later.

Needs BUFFER_API_KEY and META_PAGE_TOKEN, and the token must carry
instagram_content_publish (added to the app already; it has to be ticked when the
token is generated).

SAFETY. This posts publicly, so it is deliberately narrow:
  - only posts Buffer has marked `error`, never anything scheduled or sent
  - only the instagram channel
  - at most MAX_PER_RUN in one run, so a bad state cannot empty the queue
  - nothing older than MAX_AGE_DAYS, so it cannot resurrect stale posts
  - the Buffer post is deleted only after Meta confirms publication
"""
import json, os, sys, time, urllib.parse, urllib.request, urllib.error

MAX_PER_RUN = 3
MAX_AGE_DAYS = 7
GRAPH = 'https://graph.facebook.com/v21.0'
ORG = '6a87c5fd3160101448e2db31'
IG_CHANNEL = '6a8bbcd7ccaf649a6704f154'
CONTAINER_ATTEMPTS = 4          # the fetch failure is transient; this is the point
BACKOFF = [0, 20, 60, 120]

BUF = os.environ.get('BUFFER_API_KEY')
TOK = os.environ.get('META_PAGE_TOKEN')
DRY = '--dry-run' in sys.argv


def buffer(query, variables):
    r = urllib.request.Request('https://api.buffer.com/graphql',
        data=json.dumps({'query': query, 'variables': variables}).encode(),
        headers={'Authorization': 'Bearer ' + BUF, 'Content-Type': 'application/json'})
    return json.loads(urllib.request.urlopen(r, timeout=60).read())


def graph(path, params=None, post=False):
    params = dict(params or {}); params['access_token'] = TOK
    url = '%s/%s' % (GRAPH, path.lstrip('/'))
    try:
        if post:
            req = urllib.request.Request(url, data=urllib.parse.urlencode(params).encode())
        else:
            req = urllib.request.Request(url + '?' + urllib.parse.urlencode(params))
        return json.loads(urllib.request.urlopen(req, timeout=120).read())
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', 'replace')
        try:
            return {'__error': json.loads(body)['error']}
        except Exception:
            return {'__error': {'message': body[:300]}}


ERRORED = """query($input: PostsInput!, $first: Int){ posts(input:$input, first:$first){
  edges{ node{ id dueAt channelService text
    error{ message }
    assets{ ... on ImageAsset { source image{ altText } } } } } } }"""
DELETE = """mutation($input: DeletePostInput!){ deletePost(input:$input){
  ... on DeletePostSuccess { id } ... on VoidMutationError { message } } }"""


def ig_user_id():
    me = graph('me', {'fields': 'instagram_business_account{id,username}'})
    if '__error' in me:
        sys.exit('cannot read the Page: %s' % me['__error'].get('message'))
    iga = me.get('instagram_business_account') or {}
    if not iga.get('id'):
        sys.exit('no Instagram business account is linked to this Page')
    return iga['id'], iga.get('username')


def publish(ig, url, caption, alt):
    """Create the container, retrying the step Meta keeps refusing, then publish."""
    cid = None
    for attempt, wait in enumerate(BACKOFF[:CONTAINER_ATTEMPTS], 1):
        if wait:
            print('      waiting %ds before retry %d' % (wait, attempt)); time.sleep(wait)
        params = {'image_url': url, 'caption': caption}
        if alt:
            params['alt_text'] = alt[:1000]
        res = graph('%s/media' % ig, params, post=True)
        if 'id' in res:
            cid = res['id']
            print('      container created on attempt %d (%s)' % (attempt, cid))
            break
        print('      attempt %d refused: %s' % (attempt, res.get('__error', {}).get('message', '?')[:110]))
    if not cid:
        return None, 'Meta refused the container on all %d attempts' % CONTAINER_ATTEMPTS

    for _ in range(10):
        st = graph(cid, {'fields': 'status_code,status'})
        code = st.get('status_code')
        if code == 'FINISHED':
            break
        if code == 'ERROR':
            return None, 'container went to ERROR: %s' % st.get('status', '')[:120]
        time.sleep(6)
    else:
        return None, 'container never reached FINISHED'

    if DRY:
        return 'DRY-RUN', None
    out = graph('%s/media_publish' % ig, {'creation_id': cid}, post=True)
    if 'id' in out:
        return out['id'], None
    return None, 'publish refused: %s' % out.get('__error', {}).get('message', '?')[:150]


def main():
    if not BUF or not TOK:
        sys.exit('BUFFER_API_KEY and META_PAGE_TOKEN must both be set')
    d = buffer(ERRORED, {'input': {'organizationId': ORG, 'filter': {'status': ['error']}},
                         'first': 50})
    nodes = [e['node'] for e in d['data']['posts']['edges']
             if e['node']['channelService'] == 'instagram']
    if not nodes:
        print('nothing to rescue: no errored Instagram posts')
        return

    cutoff = time.time() - MAX_AGE_DAYS * 86400
    fresh = []
    for n in nodes:
        try:
            when = time.mktime(time.strptime(n['dueAt'][:19], '%Y-%m-%dT%H:%M:%S'))
        except Exception:
            when = time.time()          # unparseable date: treat as current, let it through
        if when >= cutoff:
            fresh.append(n)
        else:
            print('skipping %s - older than %d days' % (n['dueAt'][:16], MAX_AGE_DAYS))

    ig, user = ig_user_id()
    print('rescuing to @%s%s' % (user, '   [DRY RUN - nothing will be published]' if DRY else ''))
    done = failed = 0
    for n in fresh[:MAX_PER_RUN]:
        a = (n.get('assets') or [{}])[0]
        url = a.get('source'); alt = ((a.get('image') or {}).get('altText')) or ''
        print('\n  %s  %s' % (n['dueAt'][:16], (url or '').rsplit('/', 1)[-1][:46]))
        if not url:
            print('      no image on this post - skipped'); failed += 1; continue
        mid, err = publish(ig, url, n.get('text') or '', alt)
        if err:
            print('      FAILED: %s' % err); failed += 1; continue
        print('      published%s' % ('' if DRY else ' as ' + mid))
        if not DRY:
            r = buffer(DELETE, {'input': {'id': n['id']}})
            print('      cleared from Buffer: %s' % json.dumps(r.get('data', {}).get('deletePost', {})))
        done += 1
    if len(fresh) > MAX_PER_RUN:
        print('\n%d more left for the next run (cap is %d per run)'
              % (len(fresh) - MAX_PER_RUN, MAX_PER_RUN))
    print('\nrescued %d, failed %d' % (done, failed))


if __name__ == '__main__':
    main()
