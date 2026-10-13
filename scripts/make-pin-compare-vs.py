# Pin 42 — GLYCINE vs MELATONIN VS battle, STICKER style (rotation: Aura was last)
# Promotes the new /compare pages. Real data: Glycine 97% approval (56 threads),
# Melatonin 83% approval (202 threads) — October Reality Index, 1,645 posts.
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins/pin-42-compare-vs-sticker.png"
F = "C:/Windows/Fonts/"
IMPACT, SEGOE, SEGOE_B, SEGOE_L = F+"impact.ttf", F+"segoeui.ttf", F+"segoeuib.ttf", F+"segoeuil.ttf"
NAVY = (22, 28, 50)
YELLOW = (255, 214, 10)
TEAL = (120, 200, 190)
WHITE = (255, 255, 255)
GREY = (190, 198, 220)

def font(p, s): return ImageFont.truetype(p, s)

img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)
rnd = random.Random(42)
for _ in range(900):
    x, y = rnd.randrange(W), rnd.randrange(H)
    d.point((x, y), fill=(38, 46, 78))

def sticker(xy, s, f, fill, text_fill, pad=10, rot=0):
    tmp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    td = ImageDraw.Draw(tmp)
    tw = td.textlength(s, font=f)
    bbox = f.getbbox(s)
    th = bbox[3] - bbox[1]
    x, y = xy
    td.rounded_rectangle([x - pad, y - pad, x + tw + pad, y + th + pad * 2], 16, fill=fill)
    td.text((x, y - bbox[1]), s, font=f, fill=text_fill)
    if rot:
        tmp = tmp.rotate(rot, resample=Image.BICUBIC, center=(x + tw / 2, y + th / 2))
    return tmp

# kicker
img = Image.alpha_composite(img.convert("RGBA"), sticker((70, 85), "  WE SCORED 1,645 REDDIT THREADS  ", font(SEGOE_B, 30), YELLOW, NAVY, 14, rot=-2))

# glycine side
d = ImageDraw.Draw(img)
d.text((66, 215), "GLYCINE", font=font(IMPACT, 118), fill=WHITE, stroke_width=3, stroke_fill=YELLOW)
img = Image.alpha_composite(img.convert("RGBA"), sticker((90, 355), "  97% approval · 56 threads  ", font(SEGOE_B, 34), TEAL, NAVY, 12, rot=1.5))
img = Image.alpha_composite(img.convert("RGBA"), sticker((95, 30), "  still #1  ", font(SEGOE_B, 26), YELLOW, NAVY, 10, rot=-6))

# VS badge
img = Image.alpha_composite(img.convert("RGBA"), sticker((455, 470), "  VS  ", font(IMPACT, 88), YELLOW, NAVY, 18, rot=-8))

# melatonin side
d = ImageDraw.Draw(img)
d.text((66, 600), "MELATONIN", font=font(IMPACT, 92), fill=YELLOW, stroke_width=3, stroke_fill=NAVY)
img = Image.alpha_composite(img.convert("RGBA"), sticker((90, 705), "  83% approval · 202 threads  ", font(SEGOE_B, 34), WHITE, NAVY, 12, rot=-2))

# divider doodles
d = ImageDraw.Draw(img)
for x, y, s in [(880, 250, 9), (140, 560, 7), (900, 640, 6), (90, 840, 5), (790, 800, 4)]:
    d.line([x - s, y, x + s, y], fill=YELLOW, width=3)
    d.line([x, y - s, x, y + s], fill=YELLOW, width=3)
d.arc([520, 760, 1000, 1120], 200, 320, fill=TEAL, width=5)

# the plot twist
d.text((70, 880), "the plot twist:", font=font(SEGOE_B, 34), fill=WHITE)
d.text((70, 928), "melatonin got 8\u00d7 the threads.", font=font(SEGOE_L, 32), fill=GREY)
d.text((70, 972), "GLYCINE GOT THE LOVE.", font=font(IMPACT, 64), fill=WHITE, stroke_width=2, stroke_fill=YELLOW)

# zinger sticker
img = Image.alpha_composite(img.convert("RGBA"), sticker((90, 1090), "  loudest \u2260 best-loved  ", font(SEGOE_B, 40), YELLOW, NAVY, 14, rot=1.5))

# fill the lower-right dead space: moon doodle + sparkles
d = ImageDraw.Draw(img)
d.ellipse([740, 1075, 900, 1235], outline=TEAL, width=5)
d.ellipse([782, 1117, 858, 1193], fill=(30, 38, 66))
for x, y, s in [(700, 1050, 7), (920, 1250, 6), (660, 1260, 5), (930, 1090, 4)]:
    d.line([x - s, y, x + s, y], fill=YELLOW, width=3)
    d.line([x, y - s, x, y + s], fill=YELLOW, width=3)

# bottom small print
d = ImageDraw.Draw(img)
d.text((70, 1200), "every head-to-head scored —", font=font(SEGOE_L, 30), fill=GREY)
d.text((70, 1240), "all 66 matchups, free to browse.", font=font(SEGOE_L, 30), fill=GREY)

# footer (brand DNA)
d.text((70, H - 116), "naturallyrestful.xyz", font=font(SEGOE_B, 30), fill=WHITE)
d.text((70, H - 76), "Reality Index · October data · /compare", font=font(SEGOE_L, 22), fill=(170, 178, 205))

img.convert("RGB").save(OUT)
print("wrote", OUT)
