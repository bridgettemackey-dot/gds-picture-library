#!/usr/bin/env python3
"""Fold a Pinterest analytics CSV export into the dashboard as a second source.

    python3 dashboard/pinterest_csv.py --inspect <file.csv>   # show what it found, write nothing
    python3 dashboard/pinterest_csv.py <file.csv>             # -> dashboard/pinterest.json

Pinterest does not document its export headers and changes them between views, so
nothing here is hard-coded to one spelling. Columns are matched by a normalised
name against the aliases below, and anything unmatched is reported rather than
quietly dropped. Run --inspect first on any new export.
"""
import csv, io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# normalised header -> our field. Normalising strips case, spaces and punctuation,
# so "Outbound clicks", "outbound_clicks" and "Outbound Clicks " all collapse together.
ALIASES = {
    'impressions': 'impressions', 'totalimpressions': 'impressions',
    'saves': 'saves', 'totalsaves': 'saves', 'repins': 'saves',
    'pinclicks': 'pin_clicks', 'totalpinclicks': 'pin_clicks', 'closeups': 'pin_clicks',
    'outboundclicks': 'outbound_clicks', 'totaloutboundclicks': 'outbound_clicks',
    'linkclicks': 'outbound_clicks',
    'engagements': 'engagements', 'totalengagements': 'engagements',
    'pinid': 'pin_id', 'id': 'pin_id',
    'pinurl': 'url', 'url': 'url', 'link': 'url', 'pinlink': 'url',
    'date': 'date', 'createdat': 'date', 'publishdate': 'date', 'created': 'date',
    'title': 'title', 'pintitle': 'title', 'description': 'title',
}
NUMERIC = {'impressions', 'saves', 'pin_clicks', 'outbound_clicks', 'engagements'}


def norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


def read(path):
    """Find the header row, which Pinterest sometimes buries under a title line."""
    raw = open(path, encoding='utf-8-sig', errors='replace').read()
    try:
        dialect = csv.Sniffer().sniff(raw[:4096], delimiters=',;\t')
    except Exception:
        dialect = csv.excel
    rows = list(csv.reader(io.StringIO(raw), dialect))
    rows = [r for r in rows if any((c or '').strip() for c in r)]
    if not rows:
        sys.exit('that file has no rows in it')
    best, best_hits = 0, -1
    for i, r in enumerate(rows[:10]):
        hits = sum(1 for c in r if norm(c) in ALIASES)
        if hits > best_hits:
            best, best_hits = i, hits
    header = rows[best]
    return header, rows[best + 1:], best_hits


def parse(path, verbose=True):
    header, body, hits = read(path)
    mapping, unmatched = {}, []
    for i, h in enumerate(header):
        f = ALIASES.get(norm(h))
        if f:
            mapping[i] = f
        elif (h or '').strip():
            unmatched.append(h.strip())
    if verbose:
        print('header row found with %d recognised columns' % hits)
        for i, f in sorted(mapping.items()):
            print('   %-34s -> %s' % (header[i].strip(), f))
        if unmatched:
            print('   not recognised (ignored): %s' % ', '.join(unmatched[:12]))
    if not any(f in NUMERIC for f in mapping.values()):
        sys.exit('no impressions/saves/clicks column found - is this a pin-level export?')

    pins = []
    for r in body:
        rec = {}
        for i, f in mapping.items():
            if i >= len(r):
                continue
            v = (r[i] or '').strip()
            if f in NUMERIC:
                v = v.replace(',', '').replace('%', '')
                try:
                    rec[f] = int(float(v)) if v else 0
                except ValueError:
                    rec[f] = 0
            elif v:
                rec[f] = v
        # a pin id hidden inside a pinterest.com/pin/<id> url is the best join key
        if 'pin_id' not in rec and rec.get('url'):
            m = re.search(r'/pin/(\d+)', rec['url'])
            if m:
                rec['pin_id'] = m.group(1)
        if any(rec.get(f) for f in NUMERIC) or rec.get('pin_id'):
            pins.append(rec)
    return pins


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        sys.exit(__doc__)
    path = args[0]
    if not os.path.exists(path):
        sys.exit('no such file: %s' % path)
    pins = parse(path)
    withid = sum(1 for p in pins if p.get('pin_id'))
    print('\nrows with figures : %d' % len(pins))
    print('rows with a pin id: %d  (needed to line up against Buffer)' % withid)
    for f in sorted(NUMERIC):
        tot = sum(p.get(f, 0) for p in pins)
        if tot:
            print('   %-16s %d' % (f, tot))
    if withid == 0:
        print('\nNOTE: no pin ids or pin URLs in this export, so these figures cannot be')
        print('      matched to individual Buffer posts. They still work as a total.')
    if '--inspect' in sys.argv:
        print('\n--inspect: nothing written')
        return
    out = os.path.join(HERE, 'pinterest.json')
    json.dump({'source': os.path.basename(path), 'pins': pins}, open(out, 'w'), indent=1)
    print('\nwrote %s' % out)


if __name__ == '__main__':
    main()
