#!/usr/bin/env python3
"""Buffer queue tools. Lives in the repo because the scratchpad does NOT survive a
container being reclaimed - which happened on 27 Sep 2026, taking the only copies
of the scheduling scripts with it. Anything a future run needs belongs in git.

    python3 buffer_queue.py            # errored + scheduled posts
    python3 buffer_queue.py --errors   # errored posts with the raw network message
"""
import json, os, sys, urllib.request

K = os.environ['BUFFER_API_KEY']
ORG = '6a87c5fd3160101448e2db31'


def call(query, variables):
    r = urllib.request.Request('https://api.buffer.com/graphql',
        data=json.dumps({'query': query, 'variables': variables}).encode(),
        headers={'Authorization': 'Bearer ' + K, 'Content-Type': 'application/json'})
    return json.loads(urllib.request.urlopen(r, timeout=90).read())


Q = """query($input: PostsInput!, $first: Int, $after: String){
  posts(input:$input, first:$first, after:$after){
    pageInfo{ hasNextPage endCursor }
    edges{ node{ id status dueAt sentAt channelService text
      error{ message rawError }
      assets{ ... on ImageAsset { source image{ width height altText } } } } } } }"""


def pull(status):
    out, after = [], None
    while True:
        v = {'input': {'organizationId': ORG, 'filter': {'status': [status]}}, 'first': 50}
        if after:
            v['after'] = after
        d = call(Q, v)['data']['posts']
        out += [e['node'] for e in d['edges']]
        if not d['pageInfo']['hasNextPage']:
            break
        after = d['pageInfo']['endCursor']
    return out


def main():
    errs = pull('error')
    print('== errored: %d ==' % len(errs))
    for n in errs:
        a = (n['assets'] or [{}])[0]
        print('  %s %-10s %s  id=%s' % (n['dueAt'][:16], n['channelService'],
              (a.get('source') or '').rsplit('/', 1)[-1][:40], n['id']))
        if '--errors' in sys.argv:
            print('     %s' % (((n.get('error') or {}).get('rawError') or '')[:240]))
    sched = sorted(pull('scheduled'), key=lambda p: p['dueAt'])
    print('\n== scheduled: %d ==' % len(sched))
    per = {}
    for n in sched:
        per[n['channelService']] = per.get(n['channelService'], 0) + 1
        a = (n['assets'] or [{}])[0]
        print('  %s %-10s %s' % (n['dueAt'][:16], n['channelService'],
              (a.get('source') or '').rsplit('/', 1)[-1][:44]))
    print('\n  per channel: %s   (Buffer allows 10 each)' % per)


if __name__ == '__main__':
    main()
