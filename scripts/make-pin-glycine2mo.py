# Glycine two-month pin — Aura style (last was Editorial; rotation rule)
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins/pin-41-glycine-aura.png"
F = "C:/Windows/Fonts/"
IMPACT, GEO_B, GEO_I, SEGOE_B, SEGOE_L = F+"impact.ttf", F+"georgiab.ttf", F+"georgiai.ttf", F+"segoeuib.ttf", F+"segoeuil.ttf"
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

img = vgrad([(0,(26,20,64)),(0.45,(74,47,122)),(1.0,(26,78,92))]).convert("RGBA")
glow = Image.new("RGBA",(W,H),(0,0,0,0)); gd = ImageDraw.Draw(glow)
gd.ellipse([640,60,900,320], fill=(255,236,200,200))
img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(70)))
d = ImageDraw.Draw(img)
d.ellipse([700,90,850,240], fill=(250,238,214))
for x,y,s in [(120,140,5),(210,260,4),(600,120,4),(170,430,3),(880,400,4)]:
    d.line([x-s,y,x+s,y],fill=(250,238,214),width=2); d.line([x,y-s,x,y+s],fill=(250,238,214),width=2)

d.text((66,380), "97% BOTH MONTHS.", font=font(IMPACT,46), fill=(255,255,255))
d.text((66,446), "ONE NEGATIVE POST.", font=font(IMPACT,46), fill=(250,238,214))
d.text((66,512), "BOTH MONTHS.", font=font(IMPACT,46), fill=(255,255,255))

d.text((58,600), "97%", font=font(GEO_B,240), fill=(250,238,214))
d.text((70,870), "user approval for glycine, unchanged across", font=font(GEO_I,34), fill=(235,228,240))
d.text((70,916), "two full re-scores, a month apart.", font=font(GEO_I,34), fill=(235,228,240))

rows = [("September index",0.97,True),("October index",0.97,True),("ashwagandha, for scale",0.71,False)]
y = 1010
for name,v,hl in rows:
    d.text((70,y), name, font=font(SEGOE_B,27), fill=(255,255,255))
    d.rounded_rectangle([420,y+6,420+int(450*v),y+26],10, fill=(250,238,214) if hl else (120,110,160))
    y += 66

d.text((70,y+8), "3 g before bed. That's the whole trick.", font=font(GEO_I,30), fill=(190,185,215))

d.text((70,H-116), "naturallyrestful.xyz", font=font(SEGOE_B,30), fill=(255,255,255))
d.text((70,H-76), "Sleep Supplement Reality Index · Oct 2026", font=font(SEGOE_L,22), fill=(200,195,220))

ov = Image.new("RGBA",(W,H),(0,0,0,0)); od = ImageDraw.Draw(ov); rnd = random.Random(77)
for _ in range(2200):
    x,y = rnd.randrange(W), rnd.randrange(H); v = rnd.randrange(190,255)
    od.point((x,y), fill=(v,v,v,20))
img = Image.alpha_composite(img, ov)

img.convert("RGB").save(OUT)
print("wrote", OUT)
