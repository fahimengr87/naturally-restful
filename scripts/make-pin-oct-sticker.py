# October-edition pin — STICKER style (first live use; rotation: Dawn was last)
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins/pin-34-oct-sticker.png"
F = "C:/Windows/Fonts/"
IMPACT, SEGOE, SEGOE_B, SEGOE_L = F+"impact.ttf", F+"segoeui.ttf", F+"segoeuib.ttf", F+"segoeuil.ttf"
def font(p, s): return ImageFont.truetype(p, s)

img = Image.new("RGB", (W, H), (22, 28, 50))
d = ImageDraw.Draw(img)
rnd = random.Random(21)
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

img = Image.alpha_composite(img.convert("RGBA"), sticker((70, 90), "  OCTOBER EDITION · 1,645 POSTS RE-SCORED  ", font(SEGOE_B, 30), (255, 214, 10), (22, 28, 50), 14, rot=-2))

d = ImageDraw.Draw(img)
d.text((66, 240), "WE RE-SCORED", font=font(IMPACT, 110), fill=(255, 255, 255), stroke_width=3, stroke_fill=(255, 214, 10))
d.text((66, 355), "EVERYTHING.", font=font(IMPACT, 110), fill=(255, 214, 10), stroke_width=3, stroke_fill=(255, 214, 10))
d.text((66, 475), "THE RANKING", font=font(IMPACT, 110), fill=(255, 255, 255))
d.text((66, 585), "BARELY MOVED.", font=font(IMPACT, 110), fill=(255, 255, 255))

img = Image.alpha_composite(img, sticker((90, 760), "  glycine: 97% both months.  ", font(SEGOE_B, 36), (120, 200, 190), (22, 28, 50), 12, rot=1.5))
img = Image.alpha_composite(img, sticker((150, 880), "  ashwagandha: last. both months.  ", font(SEGOE_B, 34), (255, 255, 255), (22, 28, 50), 12, rot=-2))
img = Image.alpha_composite(img, sticker((90, 1000), "  11 of 12 unchanged. that's a signal.  ", font(SEGOE_B, 32), (255, 214, 10), (22, 28, 50), 12, rot=1))

d = ImageDraw.Draw(img)
# doodles
for x, y, s in [(860, 240, 9), (150, 730, 7), (880, 620, 6), (250, 210, 5), (770, 1130, 5), (120, 1150, 4)]:
    d.line([x - s, y, x + s, y], fill=(255, 214, 10), width=3)
    d.line([x, y - s, x, y + s], fill=(255, 214, 10), width=3)
d.arc([540, 1090, 1020, 1420], 200, 320, fill=(120, 200, 190), width=5)

d.text((70, 1200), "The one mover:", font=font(SEGOE_B, 32), fill=(255, 255, 255))
d.text((70, 1245), "tart cherry talked about less, liked more.", font=font(SEGOE_L, 30), fill=(190, 198, 220))

d.text((70, H - 116), "naturallyrestful.xyz", font=font(SEGOE_B, 30), fill=(255, 255, 255))
d.text((70, H - 76), "Reality Index · Report #002 · Free to cite", font=font(SEGOE_L, 22), fill=(170, 178, 205))

img.convert("RGB").save(OUT)
print("wrote", OUT)
