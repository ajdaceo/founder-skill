"""Compose Etsy listing images (2000x1600) from rendered sheet screenshots.

Usage: python3 make_images.py SHOTS_DIR OUT_DIR
Expects SHOTS_DIR/vehicle-{1..4}.png and reseller-{1..4}.png (pages in sheet order).
"""
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

W, H = 2000, 1600
NAVY, ACCENT, BG = (31, 42, 68), (46, 125, 91), (246, 248, 251)
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def trim(img):
    bg = Image.new(img.mode, img.size, (255, 255, 255))
    box = ImageChops.difference(img.convert("RGB"), bg.convert("RGB")).getbbox()
    return img.crop((max(box[0] - 20, 0), max(box[1] - 20, 0), box[2] + 20, box[3] + 20)) if box else img


def card(shot, headline, sub, out, tag="Excel + Google Sheets"):
    canvas = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, 0, W, 260], fill=NAVY)
    d.text((80, 55), headline, font=ImageFont.truetype(FONT_B, 72), fill="white")
    d.text((80, 160), sub, font=ImageFont.truetype(FONT_R, 40), fill=(205, 215, 230))
    tf = ImageFont.truetype(FONT_B, 34)
    tw = d.textlength(tag, font=tf)
    d.rounded_rectangle([W - tw - 140, 1490, W - 60, 1560], radius=30, fill=ACCENT)
    d.text((W - tw - 100, 1502), tag, font=tf, fill="white")
    img = trim(Image.open(shot).convert("RGB"))
    maxw, maxh = W - 160, H - 260 - 220
    scale = min(maxw / img.width, maxh / img.height)
    img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
    x, y = (W - img.width) // 2, 300 + (maxh - img.height) // 2
    d.rectangle([x - 6, y - 6, x + img.width + 6, y + img.height + 6], fill=(208, 215, 226))
    canvas.paste(img, (x, y))
    canvas.save(out, quality=92)


if __name__ == "__main__":
    shots, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    v = [
        ("Car Flipping Profit Tracker", "See what every vehicle really made you", 1),
        ("Every vehicle, every cost", "Purchase, fees, logged costs, sale, profit, ROI, days in stock", 2),
        ("Cost Log", "Parts, labour, MOT, valeting and transport flow in automatically", 3),
        ("UK tax year summary", "6 April to 5 April, with a £1,000 takings flag", 4),
    ]
    for i, (h, s, p) in enumerate(v, start=1):
        card(shots / f"vehicle-{p}.png", h, s, out / f"vehicle-{i}.jpg")
    r = [
        ("UK Reseller Profit Tracker", "eBay, Vinted, Depop: your real profit per item", 1),
        ("Every item, every fee", "Cost, postage, platform fees, profit, margin, days to sell", 2),
        ("HMRC platform reporting check", "How close you are to 30 sales or about £1,700 per platform", 3),
        ("UK tax year summary", "Takings and profit, with personal items kept separate", 4),
    ]
    for i, (h, s, p) in enumerate(r, start=1):
        card(shots / f"reseller-{p}.png", h, s, out / f"reseller-{i}.jpg")
    print("done", out)
