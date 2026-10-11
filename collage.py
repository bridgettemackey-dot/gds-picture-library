#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a Pinterest collage from several catalogued pictures of ONE book.

Bridge, 11 Oct 2026: a collage on at least four days a week, mixing existing and
newly generated pictures, every panel from the same book.

Facebook and Instagram take a native carousel instead (Buffer accepts a list of
assets - verified 11 Oct, four panels created and read back on both). Pinterest
cannot carousel: a pin is one image. So the same four panels are composited here
into a single 2:3 pin.

    python3 collage.py --out collage.png \
        --panel gds/girl-whale/golden-shore-20260907 \
        --panel gds/girl-whale/reef-at-sunset-20260907 \
        --panel gds/girl-whale/beach-at-sunset-20260907 \
        --panel gds/girl-whale/on-the-outrigger-20260907

Three or four panels is the sweet spot; six still reads on Pinterest but is
cramped on a phone. The result is NOT added to images.json - every panel is
already a card in the picture library, so the collage would duplicate them.
"""
import argparse, io, os, sys, urllib.request
from PIL import Image

W, H = 1080, 1620          # Pinterest 2:3
MARGIN, GUTTER = 24, 16
CREAM = (244, 242, 236)    # matches the caption band in brand.py
GOLD = (167, 111, 22)

def fetch(pid):
    cn = os.environ['CLOUDINARY_CLOUD_NAME']
    url = "https://res.cloudinary.com/%s/image/upload/%s.png" % (cn, pid)
    with urllib.request.urlopen(url, timeout=90) as r:
        if r.status != 200:
            raise SystemExit("panel %s -> HTTP %s" % (pid, r.status))
        return Image.open(io.BytesIO(r.read())).convert("RGB")

def cover(im, w, h):
    """Crop to fill the cell, centred, without distorting."""
    s = max(w / im.width, h / im.height)
    im = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    l, t = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((l, t, l + w, t + h))

def grid(n):
    """Rows and columns for a panel count. 3 is a wide hero over two."""
    return {2: (2, 1), 3: (3, 1), 4: (2, 2), 6: (3, 2)}.get(n)

def build(pids, out):
    n = len(pids)
    rc = grid(n)
    if not rc:
        raise SystemExit("panel count %d not supported - use 2, 3, 4 or 6" % n)
    rows, cols = rc
    canvas = Image.new("RGB", (W, H), CREAM)
    inner_w = W - 2 * MARGIN - GUTTER * (cols - 1)
    inner_h = H - 2 * MARGIN - GUTTER * (rows - 1)
    cw, ch = inner_w // cols, inner_h // rows

    ims = [fetch(p) for p in pids]
    if n == 3:
        # hero across the full width, then two beneath it
        hero_h = ch + (ch // 2)
        rest_h = H - 2 * MARGIN - GUTTER * 2 - hero_h
        canvas.paste(cover(ims[0], W - 2 * MARGIN, hero_h), (MARGIN, MARGIN))
        y = MARGIN + hero_h + GUTTER
        half = (W - 2 * MARGIN - GUTTER) // 2
        canvas.paste(cover(ims[1], half, rest_h), (MARGIN, y))
        canvas.paste(cover(ims[2], half, rest_h), (MARGIN + half + GUTTER, y))
    else:
        for i, im in enumerate(ims):
            r, c = divmod(i, cols)
            canvas.paste(cover(im, cw, ch),
                         (MARGIN + c * (cw + GUTTER), MARGIN + r * (ch + GUTTER)))
    # a thin gold rule along the foot, the one piece of GDS furniture
    canvas.paste(Image.new("RGB", (W - 2 * MARGIN, 4), GOLD), (MARGIN, H - MARGIN - 4))
    canvas.save(out, "PNG")
    print("collage -> %s  %dx%d  %d panels (%dx%d grid)" % (out, W, H, n, cols, rows))
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Composite catalogued pictures into a Pinterest collage.")
    ap.add_argument("--panel", action="append", required=True,
                    help="Cloudinary public_id, repeated. All panels must be the same book.")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    slugs = {p.split('/')[1] for p in a.panel if '/' in p}
    if len(slugs) > 1:
        raise SystemExit("panels span more than one book (%s) - a collage is one book" % ', '.join(sorted(slugs)))
    build(a.panel, a.out)
