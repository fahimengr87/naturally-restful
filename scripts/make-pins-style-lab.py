# Naturally Restful — Style Lab: 4 design languages for 2026-current pins.
# Same content (glycine Reality Index finding) in each, for head-to-head comparison.
# Output: C:/Users/Fahim/ZCodeProject/pinterest-pins/style-lab/style-{a,b,c,d}-*.png

import os
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins/style-lab"
os.makedirs(OUT, exist_ok=True)

F = "C:/Windows/Fonts/"
IMPACT = F + "impact.ttf"
GEO = F + "georgia.ttf"
GEO_B = F + "georgiab.ttf"
GEO_I = F + "georgiai.ttf"
SEGOE = F + "segoeui.ttf"
SEGOE_B = F + "segoeuib.ttf"
SEGOE_L = F + "segoeuil.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def vgrad(stops):
    """stops: list of (pos 0-1, (r,g,b))"""
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        for i in range(len(stops) - 1):
            p0, c0 = stops[i]; p1, c1 = stops[i + 1]
            if p0 <= t <= p1:
                k = (t - p0) / max(p1 - p0, 1e-6)
                c = tuple(round(c0[j] + (c1[j] - c0[j]) * k) for j in range(3))
                break
        else:
            c = stops[-1][1]
        for x in range(W):
            px[x, y] = c
    return img

def grain(img, n=2600, alpha=22):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    rnd = random.Random(42)
    for _ in range(n):
        x, y = rnd.randrange(W), rnd.randrange(H)
        v = rnd.randrange(190, 255)
        d.point((x, y), fill=(v, v, v, alpha))
    return Image.alpha_composite(img.convert("RGBA"), overlay)

def stars(d, pts, color, r=2):
    for x, y, s in pts:
        d.line([x - s, y, x + s, y], fill=color, width=2)
        d.line([x, y - s, x, y + s], fill=color, width=2)

def footer(draw, text_color, sub_color, base=Image.new("RGB", (1, 1))):
    draw.text((70, H - 116), "naturallyrestful.xyz", font=font(SEGOE_B, 30), fill=text_color)
    draw.text((70, H - 76), "Sleep Supplement Reality Index · Sept 2026", font=font(SEGOE_L, 22), fill=sub_color)

def text_on(img, xy, s, f, fill, stroke=0, stroke_fill=None):
    d = ImageDraw.Draw(img)
    d.text(xy, s, font=f, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
    return d

# ---------------------------------------------------------------- STYLE A — AURA
# Gen-Z "aura gradient": indigo→violet→teal, glowing moon, grain, serif display.
def style_a():
    img = vgrad([(0, (26, 20, 64)), (0.45, (74, 47, 122)), (1.0, (26, 78, 92))]).convert("RGBA")

    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([640, 60, 900, 320], fill=(255, 236, 200, 200))
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    img = Image.alpha_composite(img, glow)

    d = ImageDraw.Draw(img)
    d.ellipse([700, 90, 850, 240], fill=(250, 238, 214))  # moon
    stars(d, [(120, 140, 5), (210, 260, 4), (600, 120, 4), (170, 420, 3), (620, 330, 3), (880, 400, 4)], (250, 238, 214))

    text_on(img, (66, 420), "1,673 REDDIT THREADS.", font(IMPACT, 44), (255, 255, 255))
    text_on(img, (66, 480), "ONE QUIET WINNER.", font(IMPACT, 44), (255, 255, 255))

    # giant serif stat
    text_on(img, (58, 560), "97%", font(GEO_B, 340), (250, 238, 214))
    text_on(img, (70, 940), "of outcome posts about glycine were positive —", font(GEO_I, 36), (235, 228, 240))
    text_on(img, (70, 990), "the best score of all 12 supplements we tracked.", font(GEO_I, 36), (235, 228, 240))

    # minimal comparison ticks
    rows = [("glycine", 0.97), ("melatonin", 0.83), ("magnesium", 0.81), ("ashwagandha", 0.71)]
    d = ImageDraw.Draw(img)
    y = 1090
    for name, v in rows:
        d.text((70, y), name, font=font(SEGOE_B, 28), fill=(255, 255, 255))
        d.rounded_rectangle([300, y + 8, 300 + int(560 * v), y + 26], 9, fill=(250, 238, 214) if name == "glycine" else (120, 110, 160))
        y += 74
    footer(d, (255, 255, 255), (200, 195, 220))
    grain(img).convert("RGB").save(f"{OUT}/style-a-aura.png")
    print("style-a-aura.png")

# ---------------------------------------------------------------- STYLE B — EDITORIAL
# Cream paper, huge black type, one hot accent. The "editorial infographic" look.
def style_b():
    img = Image.new("RGB", (W, H), (245, 239, 228))
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, W, 14], fill=(18, 18, 18))
    d.text((70, 60), "REALITY INDEX — FIELD REPORT", font=font(SEGOE_B, 26), fill=(18, 18, 18))
    d.text((70, 96), "N°001 · SEPT 2026", font=font(SEGOE_L, 22), fill=(120, 116, 108))
    d.rectangle([70, 140, 930, 143], fill=(18, 18, 18))

    text_on(img, (62, 180), "THE QUIET", font(IMPACT, 128), (18, 18, 18))
    text_on(img, (62, 300), "WINNER", font(IMPACT, 128), (18, 18, 18))
    text_on(img, (62, 420), "OF REDDIT'S", font(IMPACT, 128), (18, 18, 18))
    text_on(img, (62, 540), "SLEEP TALK", font(IMPACT, 128), (228, 87, 46))

    d.rectangle([70, 690, 930, 1050], outline=(18, 18, 18), width=4)
    text_on(img, (100, 720), "97%", font(GEO_B, 200), (228, 87, 46))
    text_on(img, (100, 930), "of glycine outcome-posts were positive.", font(GEO, 33), (18, 18, 18))
    text_on(img, (100, 975), "56 posts. Exactly 1 negative. Best of 12.", font(GEO_I, 27), (110, 106, 98))

    rows = [("Glycine", "97%"), ("Reishi", "86%"), ("Melatonin", "83%"), ("Ashwagandha", "71%")]
    y = 1105
    for name, v in rows:
        d.text((100, y), name, font=font(SEGOE_B, 30), fill=(18, 18, 18))
        vw = d.textlength(v, font=font(SEGOE_B, 30))
        d.text((900 - vw, y), v, font=font(SEGOE_B, 30), fill=(228, 87, 46) if y == 1105 else (18, 18, 18))
        d.line([100, y + 44, 900, y + 44], fill=(210, 203, 190), width=2)
        y += 66
    footer(d, (18, 18, 18), (120, 116, 108))
    img.save(f"{OUT}/style-b-editorial.png")
    print("style-b-editorial.png")

# ---------------------------------------------------------------- STYLE C — STICKER
# Playful Gen-Z collage: rotated blocks, outline type, doodles, pill badge.
def style_c():
    img = Image.new("RGB", (W, H), (22, 28, 50))
    d = ImageDraw.Draw(img)

    # dotted texture
    rnd = random.Random(7)
    for _ in range(900):
        x, y = rnd.randrange(W), rnd.randrange(H)
        d.point((x, y), fill=(38, 46, 78))

    def sticker(xy, s, f, fill, outline, pad=10, rot=0):
        tmp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        td = ImageDraw.Draw(tmp)
        tw = td.textlength(s, font=f)
        bbox = f.getbbox(s)
        th = bbox[3] - bbox[1]
        x, y = xy
        td.rounded_rectangle([x - pad, y - pad, x + tw + pad, y + th + pad * 2], 16, fill=fill)
        td.text((x, y - bbox[1]), s, font=f, fill=outline)
        if rot:
            tmp = tmp.rotate(rot, resample=Image.BICUBIC, center=(x + tw / 2, y + th / 2))
        return tmp

    badge = sticker((70, 90), "  97% POSITIVE  ", font(SEGOE_B, 40), (255, 214, 10), (22, 28, 50), 14, rot=-3)
    img = Image.alpha_composite(img.convert("RGBA"), badge)

    d = ImageDraw.Draw(img)
    text_on(img, (66, 250), "GLYCINE IS", font(IMPACT, 120), (255, 255, 255), stroke=3, stroke_fill=(255, 214, 10))
    text_on(img, (66, 380), "REDDIT'S", font(IMPACT, 120), (255, 255, 255), stroke=3, stroke_fill=(255, 214, 10))
    text_on(img, (66, 510), "SECRET", font(IMPACT, 120), (255, 214, 10))
    text_on(img, (66, 640), "FAVORITE", font(IMPACT, 120), (255, 214, 10))

    tilt = sticker((90, 830), "  1 negative post. out of 56.  ", font(SEGOE_B, 34), (255, 255, 255), (22, 28, 50), 12, rot=2)
    img = Image.alpha_composite(img, tilt)

    d = ImageDraw.Draw(img)
    # doodles: stars + orbit
    stars(d, [(850, 260, 8), (140, 800, 7), (880, 560, 6), (250, 190, 5), (760, 720, 5)], (255, 214, 10))
    d.arc([560, 760, 1060, 1120], 200, 320, fill=(120, 200, 190), width=5)
    d.line([70, 1010, 930, 1010], fill=(255, 214, 10), width=4)
    for x in range(70, 931, 40):
        d.line([x, 1010, x + 18, 1010], fill=(22, 28, 50), width=4)

    text_on(img, (70, 1050), "How the rest scored:", font(SEGOE_L, 30), (190, 198, 220))
    rows = [("melatonin", 0.83), ("magnesium", 0.81), ("ashwagandha", 0.71)]
    y = 1100
    for name, v in rows:
        d.text((70, y), name, font=font(SEGOE_B, 30), fill=(255, 255, 255))
        d.rounded_rectangle([340, y + 6, 340 + int(520 * v), y + 30], 12, fill=(120, 200, 190) if v < 0.8 else (255, 214, 10))
        y += 78
    footer(d, (255, 255, 255), (170, 178, 205))
    img.convert("RGB").save(f"{OUT}/style-c-sticker.png")
    print("style-c-sticker.png")

# ---------------------------------------------------------------- STYLE D — CHROME
# Y2K-lite: near-black, chrome-gradient display type, glass pills, cyan-magenta glow.
def style_d():
    img = vgrad([(0, (10, 12, 24)), (0.5, (16, 20, 38)), (1, (10, 14, 30))]).convert("RGBA")

    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([600, 80, 980, 380], fill=(90, 200, 255, 90))
    gd.ellipse([-100, 900, 300, 1300], fill=(255, 90, 200, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(90))
    img = Image.alpha_composite(img, glow)
    d = ImageDraw.Draw(img)

    def chrome_text(xy, s, f, grad_stops):
        tmp = Image.new("L", (W, H), 0)
        td = ImageDraw.Draw(tmp)
        td.text(xy, s, font=f, fill=255)
        w, h = tmp.size
        grad = Image.new("RGB", (w, h))
        gp = grad.load()
        for yy in range(h):
            t = yy / (h - 1)
            for i in range(len(grad_stops) - 1):
                p0, c0 = grad_stops[i]; p1, c1 = grad_stops[i + 1]
                if p0 <= t <= p1:
                    k = (t - p0) / max(p1 - p0, 1e-6)
                    c = tuple(round(c0[j] + (c1[j] - c0[j]) * k) for j in range(3))
                    break
            else:
                c = grad_stops[-1][1]
            for xx in range(w):
                gp[xx, yy] = c
        out = img.convert("RGB").copy()
        out.paste(grad, (0, 0), tmp)
        return out.convert("RGBA")

    stops = [(0, (245, 250, 255)), (0.42, (150, 175, 210)), (0.5, (60, 70, 100)), (0.58, (200, 215, 240)), (1, (110, 125, 160))]
    img = chrome_text((62, 300), "97%", font(IMPACT, 300), stops)
    d = ImageDraw.Draw(img)

    d.rounded_rectangle([66, 120, 470, 180], 30, outline=(140, 220, 255), width=3)
    d.text((100, 132), "DATA DROPPED: SEPT 2026", font=font(SEGOE_B, 26), fill=(140, 220, 255))

    text_on(img, (66, 640), "glycine:", font(SEGOE_L, 54), (235, 240, 250))
    text_on(img, (62, 700), "THE QUIET WINNER", font(SEGOE_B, 64), (255, 255, 255))

    text_on(img, (66, 830), "1,673 Reddit threads mined · 5 communities ·", font(SEGOE, 32), (185, 195, 215))
    text_on(img, (66, 872), "12 supplements scored by real outcomes", font(SEGOE, 32), (185, 195, 215))

    pills = [("56 posts", 0), ("1 negative", 0), ("best of 12", 1)]
    x = 66
    for label, hot in pills:
        f = font(SEGOE_B, 30)
        tw = d.textlength(label, font=f)
        d.rounded_rectangle([x, 960, x + tw + 44, 1020], 30, fill=(255, 90, 200, 60) if hot else (140, 220, 255, 45),
                            outline=(255, 90, 200) if hot else (140, 220, 255), width=3)
        d.text((x + 22, 971), label, font=f, fill=(255, 255, 255))
        x += tw + 76

    d.line([66, 1090, 934, 1090], fill=(60, 70, 100), width=2)
    text_on(img, (66, 1120), "runner-ups:  melatonin 83 · magnesium 81 · ashwagandha 71", font(SEGOE_L, 28), (185, 195, 215))
    footer(d, (255, 255, 255), (150, 160, 185))
    grain(img, n=1800, alpha=16).convert("RGB").save(f"{OUT}/style-d-chrome.png")
    print("style-d-chrome.png")

style_a(); style_b(); style_c(); style_d()
print("style lab complete")
