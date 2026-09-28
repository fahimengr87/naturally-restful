# Quiz tool pin — Chrome style (rotation: Dawn was last). Per docs/design-system.md
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins/pin-33-quiz-chrome.png"
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
gd.ellipse([-120,1000,320,1400], fill=(255,90,200,75))
img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(95)))
d = ImageDraw.Draw(img)

# chrome gradient text for "60s"
mask = Image.new("L",(W,H),0); md = ImageDraw.Draw(mask)
md.text((62,300), "60s", font=font(IMPACT, 280), fill=255)
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
d.text((98,134),"FREE TOOL · NO EMAIL",font=font(SEGOE_B,27),fill=(140,220,255))

d.text((66,630), "Find the sleep", font=font(SEGOE_L,58), fill=(235,240,250))
d.text((62,695), "supplement that", font=font(SEGOE_L,58), fill=(235,240,250))
d.text((62,760), "fits YOU.", font=font(SEGOE_B,62), fill=(255,255,255))

d.text((66,890), "4 questions. Backed by human trials + what", font=font(SEGOE,31), fill=(185,195,215))
d.text((66,932), "1,673 Reddit posts report actually happening.", font=font(SEGOE,31), fill=(185,195,215))

x = 66
for label, hot in [("racing mind",0),("3 a.m. wakeups",0),("stress",1),("jet lag",0)]:
    f = font(SEGOE_B,29); tw = d.textlength(label, font=f)
    d.rounded_rectangle([x,1000,x+tw+42,1058],29, fill=(255,90,200,60) if hot else (140,220,255,45),
                        outline=(255,90,200) if hot else (140,220,255), width=3)
    d.text((x+21,1010), label, font=f, fill=(255,255,255))
    x += tw + 74

d.line([66,1130,934,1130], fill=(60,70,100), width=2)
d.text((66,1160), "Sometimes the honest answer is \u201cno supplement yet\u201d — it says that too.", font=font(SEGOE_L,26), fill=(160,170,195))

d.text((70,H-116), "naturallyrestful.xyz", font=font(SEGOE_B,30), fill=(255,255,255))
d.text((70,H-76), "Sleep Supplement Finder", font=font(SEGOE_L,22), fill=(150,160,185))

ov = Image.new("RGBA",(W,H),(0,0,0,0)); od = ImageDraw.Draw(ov); rnd = random.Random(9)
for _ in range(1800):
    x,y = rnd.randrange(W), rnd.randrange(H); v = rnd.randrange(180,255)
    od.point((x,y), fill=(v,v,v,15))
img = Image.alpha_composite(img, ov)

img.convert("RGB").save(OUT)
print("wrote", OUT)
