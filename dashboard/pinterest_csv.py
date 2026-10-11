#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Turn Pinterest's analytics exports into dashboard/pinterest.json.

    python3 dashboard/pinterest_csv.py

Pinterest's API needs app review even for Trial access, so Bridge exports CSVs by
hand. Each export is a SNAPSHOT: the same pins, counted up to a different end date.
Keeping several lets us see which pins are GROWING, which one snapshot cannot.

An export is FOUR STACKED SECTIONS, each with its own title row, then its header,
then rows, then a footnote. Sections are identified by the COLUMNS they carry, not
by the title above them - assuming a single table cost a rewrite on 24 Sep 2026.

THE FINDING THIS FILE EXISTS TO PROTECT (11 Oct 2026): PINS RAMP SLOWLY. A pin sits
at one to five impressions for one to three weeks and then climbs, sometimes
steeply. Pin ...838670136 read 2 on 23 Sep, 13 on 30 Sep, and 680 by 11 Oct. Judging
a pin in its first fortnight says nothing. Never conclude a pin is dead from a
single snapshot - that error produced a "distribution stall" in this dashboard that
was wrong for three weeks.
"""
import csv, glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'pinterest-exports')


def sections(path):
    rows = list(csv.reader(open(path, newline='', encoding='utf-8-sig')))
    out, cur = [], []
    for r in rows:
        if not any(c.strip() for c in r):
            if cur: out.append(cur); cur = []
        else: cur.append(r)
    if cur: out.append(cur)
    return out


def parse(path):
    daily, pins, boards = {}, {}, {}
    for sec in sections(path):
        hi = None
        for i, r in enumerate(sec[:3]):           # title row, then header
            h = [c.strip().lower() for c in r]
            if 'impressions' in h and h and h[0] in ('date', 'pinterest link'):
                hi, hdr = i, h
                break
        if hi is None:
            continue
        body = sec[hi + 1:]
        if hdr[0] == 'date':
            for r in body:
                if re.match(r'^\d{4}-\d{2}-\d{2}$', r[0].strip()):
                    daily[r[0].strip()] = int(r[1])
        elif 'content type' in hdr:               # Top Pins
            iu, ii = hdr.index('pinterest link'), hdr.index('impressions')
            for r in body:
                m = re.search(r'/pin/(\d+)/', r[iu])
                if m: pins[m.group(1)] = int(r[ii])
        else:                                     # Top Boards
            iu, ii = hdr.index('pinterest link'), hdr.index('impressions')
            for r in body:
                m = re.search(r'/gdsgroupofcompanies/([^/]+)/', r[iu])
                if m: boards[m.group(1)] = int(r[ii])
    return daily, pins, boards


def main():
    files = sorted(glob.glob(os.path.join(SRC, '*.csv')))
    if not files:
        raise SystemExit('no exports in %s' % SRC)
    snaps, daily = {}, {}
    for p in files:
        end = re.search(r'(\d{8})\.csv$', p).group(1)
        end = '%s-%s-%s' % (end[:4], end[4:6], end[6:])
        d, pins, boards = parse(p)
        snaps[end] = {'pins': pins, 'boards': boards}
        daily.update(d)        # a later export corrects an earlier one's estimates
    ends = sorted(snaps)
    last = ends[-1]

    # per-pin trajectory across snapshots, newest pin id last
    traj = {}
    for pid in sorted(set().union(*(s['pins'] for s in snaps.values())), key=int):
        traj[pid] = {e: snaps[e]['pins'].get(pid) for e in ends}

    out = {
        'source': 'Pinterest analytics export (manual), %d snapshots' % len(ends),
        'snapshots': ends,
        'asof': last,
        'daily': daily,
        'boards': snaps[last]['boards'],
        'pins': snaps[last]['pins'],
        'trajectory': traj,
        'totals': {e: sum(snaps[e]['pins'].values()) for e in ends},
    }
    with open(os.path.join(HERE, 'pinterest.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print('%d snapshots (%s .. %s)' % (len(ends), ends[0], last))
    print('%d pins, %d impressions as of %s' % (len(out['pins']), sum(out['pins'].values()), last))
    print('daily series: %d days, %s .. %s' % (len(daily), min(daily), max(daily)))


if __name__ == '__main__':
    main()
