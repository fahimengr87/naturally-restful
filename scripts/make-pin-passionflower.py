# Passionflower pin — Dawn style, headline-hero (per docs/design-system.md rotation)
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins/pin-32-passionflower-dawn.png"
F = "C:/Windows/Fonts/"
GEO_B, GEO_I = F+"georgiab.ttf", F+"georgiai.ttf"
SEGOE_B, SEGOE_L = F+"segoeuib.ttf", F+"segoeuil.ttf"

def font(p, s): return ImageFont.truetype(p, s)

img = Image.new("RGB", (W, H))
px = img.load()
# cream -> blush -> pale lavender sky
stops = [(0,(253,246,236)),(0.4,(249,227,224)),(1,(239,230,247))]
for y in range(H):
    t = y/(H-1); c = stops[-1][1]
    for i in range(len(stops)-1):
        p0,c0 = stops[i]; p1,c1 = stops[i+1]
        if p0 <= t <= p1:
            k=(t-p0)/max(p1-p0,1e-6); c=tuple(round(c0[j]+(c1[j]-c0[j])*k) for j in range(3)); break
    for x in range(W): px[x,y]=c
img = img.convert("RGBA")

# soft glowing disc (light-mood moon)
glow = Image.new("RGBA",(W,H),(0,0,0,0)); gd = ImageDraw.Draw(glow)
gd.ellipse([640,60,960,360], fill=(255,236,200,190))
img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(80)))
d = ImageDraw.Draw(img)
d.ellipse([720,110,890,280], fill=(255,244,222))
for x,y,s in [(130,150,4),(220,260,3),(580,120,3),(170,420,3),(640,340,3),(860,430,4)]:
    d.line([x-s,y,x+s,y],fill=(200,170,190),width=2); d.line([x,y-s,x,y+s],fill=(200,170,190),width=2)

d.text((66,96), "THE HONEST VERDICT · SLEEP HERBALS", font=font(SEGOE_B,28), fill=(120,105,150))

d.text((64,340), "The gentlest", font=font(GEO_B,96), fill=(35,42,77))
d.text((64,452), "evidence in sleep", font=font(GEO_B,96), fill=(35,42,77))
d.text((64,564), "is a tea.", font=font(GEO_I,96), fill=(214,98,112))

d.text((70,720), "Passionflower matched a prescription", font=font(GEO_I,36), fill=(60,66,100))
d.text((70,768), "sedative for anxiety in a small trial —", font=font(GEO_I,36), fill=(60,66,100))
d.text((70,816), "with less daytime drowsiness.", font=font(GEO_I,36), fill=(60,66,100))

# three soft fact rows
facts = [
    ("matched oxazepam", "2001 anxiety trial"),
    ("better sleep quality", "7-day tea study, 2011"),
    ("skip if pregnant", "or on sedatives"),
]
y = 880
for main, sub in facts:
    d.rounded_rectangle([70,y,930,y+96], 18, fill=(255,252,246))
    d.text((100,y+16), main, font=font(SEGOE_B,32), fill=(35,42,77))
    d.text((100,y+56), sub, font=font(SEGOE_L,26), fill=(130,120,150))
    y += 118

d.text((70,y+16), "One cup, ten minutes, judge it after two weeks.", font=font(GEO_I,32), fill=(120,105,140))

d.text((70,H-116), "naturallyrestful.xyz", font=font(SEGOE_B,30), fill=(35,42,77))
d.text((70,H-76), "Honest, research-cited guides", font=font(SEGOE_L,22), fill=(130,120,150))

# light grain
ov = Image.new("RGBA",(W,H),(0,0,0,0)); od = ImageDraw.Draw(ov); rnd = random.Random(5)
for _ in range(1400):
    x,y = rnd.randrange(W), rnd.randrange(H); v = rnd.randrange(180,255)
    od.point((x,y), fill=(v,v,v,12))
img = Image.alpha_composite(img, ov)

img.convert("RGB").save(OUT)
print("wrote", OUT)
