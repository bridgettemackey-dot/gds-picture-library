# -*- coding: utf-8 -*-
"""Add a caption band with a QR code to each picture, so a downloaded file
still routes a reader to the right book."""
import os, qrcode
from PIL import Image, ImageDraw, ImageFont

W        = 1080          # every branded file is this wide
BAND     = 252           # caption band height
PAD      = 30
CREAM    = (244, 242, 236)
INK      = (20, 32, 31)
SOFT     = (77, 93, 91)
GOLD     = (167, 111, 22)
SEA      = (13, 109, 107)
LSB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
LSR = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
F = lambda p, f=LSR: ImageFont.truetype(f, p)

def qr_png(url, px):
    """border=4 is the spec quiet zone; integer module scaling keeps it crisp."""
    q = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M,
                      box_size=1, border=4)
    q.add_data(url); q.make(fit=True)
    img = q.make_image(fill_color="black", back_color="white").convert("RGB")
    modules = img.size[0]
    k = max(1, px // modules)
    return img.resize((modules * k, modules * k), Image.NEAREST), modules * k

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

    q, qpx = qr_png(url, BAND - PAD * 2)
    qx = W - PAD - qpx
    canvas.paste(q, (qx, h + PAD))

    textw = qx - PAD - 26
    ft = F(44, LSB)
    lines = wrap(d, title, ft, textw)
    if len(lines) > 2:
        ft = F(37, LSB); lines = wrap(d, title, ft, textw)[:2]
    y = h + PAD + 2
    for ln in lines:
        d.text((PAD, y), ln, font=ft, fill=INK); y += ft.size + 7
    y += 6
    d.text((PAD, y), "GDS Publications  ·  Nassau, The Bahamas", font=F(27), fill=SOFT)
    y += 34
    d.text((PAD, y), "Scan the code to find this book on Amazon", font=F(27), fill=SEA)

    canvas.save(out, "PNG")
    return canvas.size


# ---------------------------------------------------------------- CLI
if __name__ == "__main__":
    import argparse, json, subprocess, sys
    p = argparse.ArgumentParser(description="Add a caption band and QR code, then publish to the picture library.")
    p.add_argument("--image",  required=True, help="local source image")
    p.add_argument("--title",  required=True, help="book title printed on the band")
    p.add_argument("--url",    required=True, help="Amazon link the QR points at")
    p.add_argument("--slug",   required=True, choices=list(
        ["girl-whale","girl-whale-activity","regatta","regatta-activity","atb-upper","atb-lower"]))
    p.add_argument("--name",   required=True, help="asset name, e.g. souse-and-johnnycake-20260906")
    p.add_argument("--out",    default=None, help="where to write the branded png")
    p.add_argument("--upload", action="store_true", help="upload to Cloudinary and tag for the site")
    a = p.parse_args()

    out = a.out or ("branded-%s.png" % a.name)
    brand(a.image, out, a.title, a.url)
    print("branded ->", out)

    if a.upload:
        cn = os.environ["CLOUDINARY_CLOUD_NAME"]; pr = os.environ["CLOUDINARY_UPLOAD_PRESET"]
        code = {"girl-whale":"gw","girl-whale-activity":"gwa","regatta":"reg",
                "regatta-activity":"rega","atb-upper":"atbu","atb-lower":"atbl"}[a.slug]
        pid = "gds-share/%s/%s" % (a.slug, a.name)
        r = subprocess.run(["curl","-sS","-X","POST",
            "https://api.cloudinary.com/v1_1/%s/image/upload" % cn,
            "-F","file=@"+out,"-F","upload_preset="+pr,"-F","public_id="+pid,
            "-F","tags=gdsshelf,book-%s" % code], capture_output=True, text=True)
        d = json.loads(r.stdout)
        if "error" in d:
            print("UPLOAD FAILED:", d["error"], file=sys.stderr); sys.exit(1)
        print("uploaded ->", d["public_id"])
        print("the picture library will show it on the next page load")
