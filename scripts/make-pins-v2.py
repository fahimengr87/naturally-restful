# Naturally Restful — Pin v2 generator per docs/design-system.md
# Builds: Dawn style sample + pins 29/30/31, each a DIFFERENT style (rotation rule).
import os, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins"
F = "C:/Windows/Fonts/"
IMPACT, GEO, GEO_B, GEO_I = F+"impact.ttf", F+"georgia.ttf", F+"georgiab.ttf", F+"georgiai.ttf"
SEGOE, SEGOE_B, SEGOE_L = F+"segoeui.ttf", F+"segoeuib.ttf", F+"segoeuil.ttf"

def font(p, s): return ImageFont.truetype(p, s)

def vgrad(stops, w=W, h=H):
    img = Image.new("RGB", (w, h)); px = img.load()
    for y in range(h):
        t = y/(h-1); c = stops[-1][1]
        for i in range(len(stops)-1):
            p0,c0 = stops[i]; p1,c1 = stops[i+1]
            if p0 <= t <= p1:
                k = (t-p0)/max(p1-p0,1e-6)
                c = tuple(round(c0[j]+(c1[j]-c0[j])*k) for j in range(3)); break
        for x in range(w): px[x,y] = c
    return img

def grain(img, n=2200, alpha=18):
    ov = Image.new("RGBA",(W,H),(0,0,0,0)); d = ImageDraw.Draw(ov); rnd = random.Random(11)
    for _ in range(n):
        x,y = rnd.randrange(W), rnd.randrange(H); v = rnd.randrange(180,255)
        d.point((x,y), fill=(v,v,v,alpha))
    return Image.alpha_composite(img.convert("RGBA"), ov)

def stars(d, pts, color):
    for x,y,s in pts:
        d.line([x-s,y,x+s,y],fill=color,width=2); d.line([x,y-s,x,y+s],fill=color,width=2)

def footer(d, main, sub):
    d.text((70,H-116),"naturallyrestful.xyz",font=font(SEGOE_B,30),fill=main)
    d.text((70,H-76),"Sleep Supplement Reality Index · Sept 2026",font=font(SEGOE_L,22),fill=sub)

# ---------------------------------------------------------------- DAWN (light sensation)
def dawn(kicker, headline, big, big_caption, rows, note, path, hero="stat"):
    img = vgrad([(0,(253,246,236)),(0.4,(249,227,224)),(1,(239,230,247))]).convert("RGBA")
    glow = Image.new("RGBA",(W,H),(0,0,0,0)); gd = ImageDraw.Draw(glow)
    gd.ellipse([660,40,960,340], fill=(255,236,200,190))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    img = Image.alpha_composite(img, glow)
    d = ImageDraw.Draw(img)
    d.ellipse([720,100,880,260], fill=(255,244,222))  # soft sun-moon disc
    stars(d, [(130,150,4),(220,260,3),(580,120,3),(170,400,3),(640,330,3)], (200,170,190))
    d.text((66,96), kicker.upper(), font=font(SEGOE_B,28), fill=(120,105,150))
    y = 380
    for line, ital in headline:
        d.text((64,y), line, font=font(GEO_I if ital else GEO_B, 74), fill=(35,42,77))
        y += 96
    if hero=="stat":
        d.text((58,y+16), big, font=font(GEO_B,290), fill=(214,98,112))
        d.text((70,y+380), big_caption[0], font=font(GEO_I,34), fill=(60,66,100))
        d.text((70,y+426), big_caption[1], font=font(GEO_I,34), fill=(60,66,100))
        y += 470
    if rows:
        for name,v,hl in rows:
            d.text((70,y), name, font=font(SEGOE_B,28), fill=(35,42,77))
            bar_w = int(400*v/max(r[1] for r in rows))
            d.rounded_rectangle([330,y+6,330+bar_w,y+28],11,
                fill=(222,140,150) if hl else (203,196,220))
            d.text((330+bar_w+14,y-1), name if False else f"{int(v*100)}%", font=font(SEGOE_B,26), fill=(35,42,77))
            y += 68
    if note:
        d.text((70,y+12), note, font=font(SEGOE_L,26), fill=(130,120,150))
    footer(d,(35,42,77),(130,120,150))
    grain(img,1400,12).convert("RGB").save(path); print(os.path.basename(path))

# ---------------------------------------------------------------- AURA (chart-hero variant)
def aura(kicker, line1, line2, big, cap, bars, note, path):
    img = vgrad([(0,(26,20,64)),(0.45,(74,47,122)),(1.0,(26,78,92))]).convert("RGBA")
    glow = Image.new("RGBA",(W,H),(0,0,0,0)); gd = ImageDraw.Draw(glow)
    gd.ellipse([640,60,900,320], fill=(255,236,200,200))
    img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(70)))
    d = ImageDraw.Draw(img)
    d.ellipse([700,90,850,240], fill=(250,238,214))
    stars(d, [(120,140,5),(210,260,4),(600,120,4),(170,430,3),(880,400,4)], (250,238,214))
    d.text((66,380), kicker, font=font(IMPACT,46), fill=(255,255,255))
    d.text((66,446), line1, font=font(IMPACT,46), fill=(255,255,255))
    d.text((66,512), line2, font=font(IMPACT,46), fill=(250,238,214))
    d.text((58,600), big, font=font(GEO_B,250), fill=(250,238,214))
    d.text((70,880), cap[0], font=font(GEO_I,34), fill=(235,228,240))
    d.text((70,926), cap[1], font=font(GEO_I,34), fill=(235,228,240))
    y = 1030
    for name,v,hl in bars:
        d.text((70,y), name, font=font(SEGOE_B,28), fill=(255,255,255))
        bar_w = int(430*(v/bars[0][1]))
        d.rounded_rectangle([340,y+6,340+bar_w,y+28],11,
            fill=(250,238,214) if hl else (120,110,160))
        d.text((340+bar_w+14,y-1), str(v), font=font(SEGOE_B,26), fill=(250,238,214) if hl else (190,185,215))
        y += 72
    d.text((70,y+10), note, font=font(SEGOE_L,25), fill=(190,185,215))
    footer(d,(255,255,255),(200,195,220))
    grain(img).convert("RGB").save(path); print(os.path.basename(path))

# ---------------------------------------------------------------- EDITORIAL (headline-hero)
def editorial(kicker, stack, box_big, box_lines, rows, path):
    img = Image.new("RGB",(W,H),(245,239,228)); d = ImageDraw.Draw(img)
    d.rectangle([0,0,W,14], fill=(18,18,18))
    d.text((70,60), kicker, font=font(SEGOE_B,26), fill=(18,18,18))
    d.text((70,96), "N°001 · SEPT 2026", font=font(SEGOE_L,22), fill=(120,116,108))
    d.rectangle([70,140,930,143], fill=(18,18,18))
    y = 180
    for line, hot in stack:
        d.text((62,y), line, font=font(IMPACT,112), fill=(228,87,46) if hot else (18,18,18))
        y += 124
    d.rectangle([70,y+10,930,y+400], outline=(18,18,18), width=4)
    d.text((100,y+40), box_big, font=font(GEO_B,170), fill=(228,87,46))
    d.text((100,y+250), box_lines[0], font=font(GEO,32), fill=(18,18,18))
    d.text((100,y+296), box_lines[1], font=font(GEO_I,27), fill=(110,106,98))
    yy = y+440
    for name,v,hot in rows:
        d.text((100,yy), name, font=font(SEGOE_B,30), fill=(18,18,18))
        vw = d.textlength(v, font=font(SEGOE_B,30))
        d.text((900-vw,yy), v, font=font(SEGOE_B,30), fill=(228,87,46) if hot else (18,18,18))
        d.line([100,yy+44,900,yy+44], fill=(210,203,190), width=2)
        yy += 64
    footer(d,(18,18,18),(120,116,108))
    img.save(path); print(os.path.basename(path))

# ---- Dawn sample (glycine, light sensation) ----
dawn("Reality Index · 1,673 Reddit threads",
     [("The supplement", False), ("nobody hypes", True)],
     "97%",
     ("positive outcome-posts for glycine —", "the best score of all 12 we tracked."),
     [("glycine",0.97,True),("melatonin",0.83,False),("ashwagandha",0.71,False)],
     "56 posts. exactly 1 negative.",
     f"{OUT}/style-lab/style-e-dawn.png")

# ---- pin 29: ashwagandha — Editorial ----
editorial("REALITY INDEX — FIELD REPORT",
     [("MOST", False), ("CONTROVERSIAL", True), ("SUPPLEMENT", False), ("ON REDDIT", False)],
     "71%",
     ("of ashwagandha outcome-posts were positive — the lowest", "of any major supplement. 36 negative threads: side-effect stories."),
     [("Glycine","97%",False),("Melatonin","83%",False),("Magnesium","81%",False),("Ashwagandha","71%",True)],
     f"{OUT}/pin-29-ashwagandha-v2.png")

# ---- pin 30: magnesium — Aura chart-hero ----
aura("MAGNESIUM WON.", "THE CROWD PICKED", "THE FORM.", "81",
     ("threads name glycinate specifically.", "Threonate: 14. Oxide: 10 — “runs through you.”"),
     [("glycinate",81,True),("threonate",14,False),("oxide",10,False)],
     "217 magnesium threads · 63k upvotes · forms as % of mentions",
     f"{OUT}/pin-30-magnesium-v2.png")

# ---- pin 31: melatonin — Dawn (dose story) ----
dawn("Reality Index · 47,600 upvotes on melatonin threads",
     [("Your bottle says", False), ("ten milligrams.", True)],
     "10×",
     ("the dose used in sleep research (0.5–1 mg).", "Same conclusion the threads keep reaching."),
     [("typical bottle",1.0,False),("study dose",0.1,True)],
     "highest-engagement supplement in the index",
     f"{OUT}/pin-31-melatonin-v2.png")
