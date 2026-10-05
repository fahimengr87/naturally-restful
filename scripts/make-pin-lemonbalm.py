# Lemon balm pin — Dawn style (light sensation; last pin was Sticker)
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins/pin-38-lemonbalm-dawn.png"
F = "C:/Windows/Fonts/"
GEO_B, GEO_I = F+"georgiab.ttf", F+"georgiai.ttf"
SEGOE_B, SEGOE_L = F+"segoeuib.ttf", F+"segoeuil.ttf"
def font(p, s): return ImageFont.truetype(p, s)

def vgrad(stops):
    img = Image.new("RGB", (W, H)); px = img.load()
    for y in range(H):
        t = y/(H-1); c = stops[-1][1]
        for i in range(len(stops)-1):
            p0,c0 = stops[i]; p1,c1 = stops[i+1]
            if p0 <= t <= p1:
                k=(t-p0)/max(p1-p0,1e-6); c=tuple(round(c0[j]+(c1[j]-c0[j])*k) for j in range(3)); break
        for x in range(W): px[x,y]=c
    return img

img = vgrad([(0,(253,246,236)),(0.4,(249,230,214)),(1,(240,238,236))]).convert("RGBA")  # cream → soft lemon → pale sage
glow = Image.new("RGBA",(W,H),(0,0,0,0)); gd = ImageDraw.Draw(glow)
gd.ellipse([640,60,960,360], fill=(255,236,200,190))
img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(80)))
d = ImageDraw.Draw(img)
d.ellipse([720,110,880,270], fill=(255,244,222))
for x,y,s in [(130,150,4),(220,260,3),(580,120,3),(170,420,3),(640,340,3),(150,700,3)]:
    d.line([x-s,y,x+s,y],fill=(205,180,140),width=2); d.line([x,y-s,x,y+s],fill=(205,180,140),width=2)

d.text((66,96), "THE HONEST VERDICT · SLEEP HERBALS", font=font(SEGOE_B,28), fill=(150,130,90))

d.text((64,340), "What lemon balm", font=font(GEO_B,88), fill=(35,42,77))
d.text((64,442), "can — and can't — do", font=font(GEO_I,88), fill=(35,42,77))

d.text((70,590), "CAN: take the edge off stress and mild anxiety —", font=font(GEO_I,36), fill=(60,66,100))
d.text((70,638), "noticeable, modest, same-day.", font=font(GEO_I,36), fill=(60,66,100))
d.text((70,700), "CAN'T: treat insomnia. The sleep data is thin;", font=font(GEO_I,36), fill=(60,66,100))
d.text((70,748), "the calm is real, the sedation isn't.", font=font(GEO_I,36), fill=(60,66,100))

facts = [
    ("300–600 mg extract", "the dose the trials tested"),
    ("Skip with thyroid conditions", "lab evidence, ask your doctor"),
    ("Pairs with glycine & magnesium", "a fair supporting actor"),
]
y = 860
for main, sub in facts:
    d.rounded_rectangle([70,y,930,y+96], 18, fill=(255,252,246))
    d.text((100,y+16), main, font=font(SEGOE_B,32), fill=(35,42,77))
    d.text((100,y+56), sub, font=font(SEGOE_L,26), fill=(140,125,100))
    y += 118

d.text((70,H-116), "naturallyrestful.xyz", font=font(SEGOE_B,30), fill=(35,42,77))
d.text((70,H-76), "Honest, research-cited guides", font=font(SEGOE_L,22), fill=(140,125,100))

ov = Image.new("RGBA",(W,H),(0,0,0,0)); od = ImageDraw.Draw(ov); rnd = random.Random(15)
for _ in range(1400):
    x,y = rnd.randrange(W), rnd.randrange(H); v = rnd.randrange(180,255)
    od.point((x,y), fill=(v,v,v,12))
img = Image.alpha_composite(img, ov)

img.convert("RGB").save(OUT)
print("wrote", OUT)
