#!/usr/bin/env python3
"""Fold a Pinterest analytics CSV export into the dashboard as a second source.

    python3 dashboard/pinterest_csv.py --inspect <file.csv>   # show what it found, write nothing
    python3 dashboard/pinterest_csv.py <file.csv>             # -> dashboard/pinterest.json

A Pinterest export is NOT one table. It is several stacked sections - a filter
preamble, a daily series, Top Boards, Top Pins - each with its own header row and
its own footnote, separated by blank lines. Anything that assumes a single header
reads the preamble and finds nothing. Sections are split on blank lines, each one
gets its own header hunt, and sections are identified by the columns they carry
rather than by the title above them, which is not always present.
"""
import csv, io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

ALIASES = {
    'impressions': 'impressions', 'totalimpressions': 'impressions',
    'saves': 'saves', 'totalsaves': 'saves', 'repins': 'saves',
    'pinclicks': 'pin_clicks', 'totalpinclicks': 'pin_clicks', 'closeups': 'pin_clicks',
    'outboundclicks': 'outbound_clicks', 'totaloutboundclicks': 'outbound_clicks',
    'linkclicks': 'outbound_clicks',
    'engagement': 'engagements', 'engagements': 'engagements', 'totalengagements': 'engagements',
    'pinid': 'pin_id', 'id': 'pin_id',
    'pinterestlink': 'url', 'pinurl': 'url', 'url': 'url', 'link': 'url', 'pinlink': 'url',
    'date': 'date', 'createdat': 'date', 'publishdate': 'date', 'created': 'date',
    'title': 'title', 'pintitle': 'title', 'description': 'title',
    'contenttype': 'content_type', 'source': 'source', 'canonical': 'canonical',
}
NUMERIC = {'impressions', 'saves', 'pin_clicks', 'outbound_clicks', 'engagements'}


def norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


def sections(path):
    """Split the file into blocks on blank lines, keeping each block's rows."""
    raw = open(path, encoding='utf-8-sig', errors='replace').read()
    try:
        dialect = csv.Sniffer().sniff(raw[:2048], delimiters=',;\t')
    except Exception:
        dialect = csv.excel
    blocks, cur = [], []
    for row in csv.reader(io.StringIO(raw), dialect):
        if any((c or '').strip() for c in row):
            cur.append(row)
        elif cur:
            blocks.append(cur); cur = []
    if cur:
        blocks.append(cur)
    return blocks


def parse_block(rows):
    """Find this block's header and return (mapping, body). A footnote line is one
    long cell with no recognised columns, so it scores zero and is skipped."""
    best, best_hits = None, 0
    for i, r in enumerate(rows):
        hits = sum(1 for c in r if norm(c) in ALIASES)
        if hits > best_hits:
            best, best_hits = i, hits
    if best is None or best_hits < 2:
        return None, [], 0
    header = rows[best]
    mapping = {i: ALIASES[norm(h)] for i, h in enumerate(header) if norm(h) in ALIASES}
    return mapping, rows[best + 1:], best_hits


def rows_from(mapping, body):
    out = []
    for r in body:
        if len(r) < 2:                       # footnote lines
            continue
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
                    continue
            elif v:
                rec[f] = v
        if rec.get('url'):
            m = re.search(r'/pin/(\d+)', rec['url'])
            if m:
                rec['pin_id'] = m.group(1)
        if rec:
            out.append(rec)
    return out


def parse(path, verbose=True):
    found = {'daily': [], 'boards': [], 'pins': []}
    for n, block in enumerate(sections(path), 1):
        mapping, body, hits = parse_block(block)
        if not mapping:
            if verbose:
                print('  section %d: no table here (filters or a footnote) - skipped' % n)
            continue
        rows = rows_from(mapping, body)
        fields = set(mapping.values())
        if 'pin_id' in {k for r in rows for k in r}:
            kind = 'pins'
        elif 'url' in fields:
            kind = 'boards'
        elif 'date' in fields:
            kind = 'daily'
        else:
            kind = 'pins' if 'impressions' in fields else None
        if verbose:
            print('  section %d: %-6s %3d rows  columns: %s'
                  % (n, kind or '?', len(rows), ', '.join(sorted(fields))))
        if kind:
            found[kind] += rows
    return found


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        sys.exit(__doc__)
    path = args[0]
    if not os.path.exists(path):
        sys.exit('no such file: %s' % path)
    print('reading %s' % os.path.basename(path))
    found = parse(path)
    print('\ndaily rows : %d' % len(found['daily']))
    print('board rows : %d' % len(found['boards']))
    print('pin rows   : %d  (%d with a pin id)'
          % (len(found['pins']), sum(1 for p in found['pins'] if p.get('pin_id'))))
    for kind in ('daily', 'pins', 'boards'):
        tot = {}
        for r in found[kind]:
            for f in NUMERIC:
                if f in r:
                    tot[f] = tot.get(f, 0) + r[f]
        if tot:
            print('  %-7s %s' % (kind, '  '.join('%s %d' % kv for kv in sorted(tot.items()))))
    if not found['pins']:
        print('\nNo per-pin rows found. Export the Top Pins view to compare pin by pin.')
    if '--inspect' in sys.argv:
        print('\n--inspect: nothing written')
        return
    out = os.path.join(HERE, 'pinterest.json')
    json.dump({'source': os.path.basename(path), **found}, open(out, 'w'), indent=1)
    print('\nwrote %s' % out)


if __name__ == '__main__':
    main()
