# Reddit-verdict page pin — Chrome style (last pin was Dawn; rotation rule)
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins/pin-39-redditpage-chrome.png"
F = "C:/Windows/Fonts/"
IMPACT, SEGOE, SEGOE_B, SEGOE_L = F+"impact.ttf", F+"segoeui.ttf", F+"segoeuib.ttf", F+"segoeuil.ttf"
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

img = vgrad([(0,(10,12,24)),(0.5,(16,20,38)),(1,(10,14,30))]).convert("RGBA")
glow = Image.new("RGBA",(W,H),(0,0,0,0)); gd = ImageDraw.Draw(glow)
gd.ellipse([560,60,980,380], fill=(90,200,255,95))
gd.ellipse([-120,1020,320,1420], fill=(255,90,200,70))
img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(95)))

# chrome gradient text
mask = Image.new("L",(W,H),0); md = ImageDraw.Draw(mask)
md.text((62,290), "TOP 5", font=font(IMPACT, 240), fill=255)
grad = Image.new("RGB",(W,H)); gp = grad.load()
stops = [(0,(245,250,255)),(0.42,(150,175,210)),(0.5,(60,70,100)),(0.58,(200,215,240)),(1,(110,125,160))]
for y in range(H):
    t = y/(H-1); c = stops[-1][1]
    for i in range(len(stops)-1):
        p0,c0 = stops[i]; p1,c1 = stops[i+1]
        if p0 <= t <= p1:
            k=(t-p0)/max(p1-p0,1e-6); c=tuple(round(c0[j]+(c1[j]-c0[j])*k) for j in range(3)); break
    for x in range(W): gp[x,y]=c
base = img.convert("RGB").copy(); base.paste(grad,(0,0),mask); img = base.convert("RGBA")
d = ImageDraw.Draw(img)

d.rounded_rectangle([66,120,560,182],31, outline=(140,220,255), width=3)
d.text((98,134),"WHAT REDDIT RANKS #1",font=font(SEGOE_B,27),fill=(140,220,255))

d.text((66,610), "sleep supplements,", font=font(SEGOE_L,56), fill=(235,240,250))
d.text((62,672), "by real outcomes", font=font(SEGOE_B,60), fill=(255,255,255))

d.text((66,790), "1,673 threads · 5 communities · 12 supplements,", font=font(SEGOE,30), fill=(185,195,215))
d.text((66,832), "scored by what users actually report.", font=font(SEGOE,30), fill=(185,195,215))

rows = [("1. Glycine",0.97,True),("2. Reishi",0.86,False),("3. Melatonin",0.83,False),("4. Tart cherry",0.82,False),("5. Magnesium",0.81,False)]
y = 920
for name,v,hl in rows:
    d.text((70,y), name, font=font(SEGOE_B,30), fill=(255,255,255))
    bw = int(500*v)
    d.rounded_rectangle([380,y+4,380+bw,y+30],13, fill=(250,238,214) if hl else (120,110,160))
    d.text((380+bw+14,y+1), f"{int(v*100)}%", font=font(SEGOE_B,26), fill=(250,238,214) if hl else (190,185,215))
    y += 72

d.text((70,H-116), "naturallyrestful.xyz", font=font(SEGOE_B,30), fill=(255,255,255))
d.text((70,H-76), "Best Supplements, per Reddit — full ranking", font=font(SEGOE_L,22), fill=(150,160,185))

ov = Image.new("RGBA",(W,H),(0,0,0,0)); od = ImageDraw.Draw(ov); rnd = random.Random(33)
for _ in range(1800):
    x,y = rnd.randrange(W), rnd.randrange(H); v = rnd.randrange(180,255)
    od.point((x,y), fill=(v,v,v,15))
img = Image.alpha_composite(img, ov)

img.convert("RGB").save(OUT)
print("wrote", OUT)
