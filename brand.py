# -*- coding: utf-8 -*-
"""Add a caption band with a QR code to each picture, so a downloaded file still
leads a reader back to the book — and to more pictures they can share."""
import os, qrcode
from PIL import Image, ImageDraw, ImageFont

W      = 1080          # every branded file is this wide
BAND   = 344           # caption band height
PAD    = 30
QRFRAC = 0.26          # QR width as a fraction of image width. Measured, not guessed:
                       # the library URL is 63 characters, which needs 45 modules, and
                       # below ~0.26 it stops decoding once a platform recompresses it.
SITE   = "https://pictures.gdsbahamas.com/"
CODE   = {"girl-whale":"gw","girl-whale-activity":"gwa","regatta":"reg",
          "regatta-activity":"rega","atb-upper":"atbu","atb-lower":"atbl"}
CREAM, INK, SOFT, GOLD, SEA = (244,242,236), (20,32,31), (77,93,91), (167,111,22), (13,109,107)
LSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
LSR = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
F = lambda p, f=LSR: ImageFont.truetype(f, p)

def book_url(slug):
    """Where a scanned code lands: that book's page in the picture library."""
    return SITE + "b/" + CODE[slug] + "/"

def qr_png(url, px):
    """border=4 is the spec quiet zone; integer module scaling keeps edges crisp."""
    q = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M,
                      box_size=1, border=4)
    q.add_data(url); q.make(fit=True)
    img = q.make_image(fill_color="black", back_color="white").convert("RGB")
    m = img.size[0]; k = max(1, px // m)
    return img.resize((m*k, m*k), Image.NEAREST), m*k

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def brand(src, out, title, url):
    art = Image.open(src).convert("RGB")
    h = round(art.height * W / art.width)
    art = art.resize((W, h), Image.LANCZOS)

    canvas = Image.new("RGB", (W, h + BAND), CREAM)
    canvas.paste(art, (0, 0))
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, h, W, h + 5], fill=GOLD)

    q, qpx = qr_png(url, int(W * QRFRAC))
    qx, qy = W - PAD - qpx, h + (BAND - qpx)//2
    canvas.paste(q, (qx, qy))

    textw = qx - PAD - 30
    ft = F(46, LSB)
    lines = wrap(d, title, ft, textw)
    if len(lines) > 2:
        ft = F(38, LSB); lines = wrap(d, title, ft, textw)[:2]
    block = len(lines)*(ft.size+8) + 12 + 34 + 36
    y = h + (BAND - block)//2
    for ln in lines:
        d.text((PAD, y), ln, font=ft, fill=INK); y += ft.size + 8
    y += 12
    d.text((PAD, y), "GDS Publications  ·  Nassau, The Bahamas", font=F(28), fill=SOFT); y += 36
    d.text((PAD, y), "Scan for more free pictures, and where to buy the book", font=F(28), fill=SEA)

    canvas.save(out, "PNG")
    return canvas.size


if __name__ == "__main__":
    import argparse, json, subprocess, sys
    p = argparse.ArgumentParser(description="Add a caption band and QR code, then publish to the picture library.")
    p.add_argument("--image",  required=True, help="local source image")
    p.add_argument("--title",  required=True, help="book title printed on the band")
    p.add_argument("--slug",   required=True, choices=list(CODE))
    p.add_argument("--name",   required=True, help="asset name, e.g. souse-and-johnnycake-20260906")
    p.add_argument("--url",    default=None, help="QR destination; defaults to this book's library page")
    p.add_argument("--out",    default=None)
    p.add_argument("--upload", action="store_true", help="upload to Cloudinary and tag for the site")
    a = p.parse_args()

    url = a.url or book_url(a.slug)
    out = a.out or ("branded-%s.png" % a.name)
    brand(a.image, out, a.title, url)
    print("branded ->", out, "| QR ->", url)

    if a.upload:
        cn = os.environ["CLOUDINARY_CLOUD_NAME"]; pr = os.environ["CLOUDINARY_UPLOAD_PRESET"]
        pid = "gds-share/%s/%s" % (a.slug, a.name)
        r = subprocess.run(["curl","-sS","-X","POST",
            "https://api.cloudinary.com/v1_1/%s/image/upload" % cn,
            "-F","file=@"+out,"-F","upload_preset="+pr,"-F","public_id="+pid,
            "-F","tags=gdsshelf,book-%s" % CODE[a.slug]], capture_output=True, text=True)
        d = json.loads(r.stdout)
        if "error" in d:
            print("UPLOAD FAILED:", d["error"], file=sys.stderr); sys.exit(1)
        print("uploaded ->", d["public_id"])
        print("NOTE: the unsigned preset cannot overwrite. If this public_id already existed,")
        print("      Cloudinary kept the old file and this changed nothing. Use a fresh name.")
