# Naturally Restful — Reality Index chart pins (1000x1500, house style)
# Navy gradient, cream crescent moon, stars, kicker, bold white title,
# cream underline, bar charts, cream footer. Font: Arial family (Windows).
# Output: C:/Users/Fahim/ZCodeProject/pinterest-pins/pin-2[7-9]-*.png, pin-3[0-1]-*.png

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins"

NAVY_TOP = (58, 70, 97)      # #3A4661
NAVY_BOT = (43, 53, 80)      # #2B3550
CREAM = (232, 220, 195)      # #E8DCC3
WHITE = (255, 255, 255)
GREY = (196, 200, 210)
BAR = (232, 220, 195)
BAR_DIM = (120, 130, 155)
ACCENT = (240, 180, 120)

F_BOLD = "C:/Windows/Fonts/arialbd.ttf"
F_BLACK = "C:/Windows/Fonts/ariblk.ttf"
F_REG = "C:/Windows/Fonts/arial.ttf"
F_IT = "C:/Windows/Fonts/ariali.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def vertical_gradient():
    img = Image.new("RGB", (W, H))
    for y in range(H):
        t = y / (H - 1)
        c = tuple(round(NAVY_TOP[i] + (NAVY_BOT[i] - NAVY_TOP[i]) * t) for i in range(3))
        for x in range(W):
            img.putpixel((x, y), c)
    return img


def draw_moon_stars(draw):
    # crescent moon (cream circle minus offset gradient-colored circle), top-right
    cx, cy, r = 830, 118, 50
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CREAM)
    t = cy / (H - 1)
    band = tuple(round(NAVY_TOP[i] + (NAVY_BOT[i] - NAVY_TOP[i]) * t) for i in range(3))
    dx, dy = -26, -12
    draw.ellipse([cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r], fill=band)
    # stars
    for sx, sy, s in [(140, 120, 5), (230, 220, 4), (700, 90, 4), (600, 210, 5),
                      (180, 300, 3), (870, 260, 4), (90, 210, 3), (760, 330, 3)]:
        draw.line([sx - s, sy, sx + s, sy], fill=CREAM, width=2)
        draw.line([sx, sy - s, sx, sy + s], fill=CREAM, width=2)


def base_canvas(kicker, title_lines, title_size=64):
    img = vertical_gradient()
    draw = ImageDraw.Draw(img)
    draw_moon_stars(draw)

    # kicker
    kf = font(F_BOLD, 30)
    draw.text((70, 92), kicker.upper(), font=kf, fill=CREAM)

    # title
    tf = font(F_BLACK, title_size)
    y = 400
    line_h = title_size + 14
    for i, line in enumerate(title_lines):
        draw.text((68, y), line, font=tf, fill=WHITE)
        y += line_h
    # underline under last line
    y += 12
    draw.rectangle([70, y, 70 + 110, y + 6], fill=CREAM)
    return img, draw, y + 60


def footer(draw):
    ff = font(F_BOLD, 30)
    sf = font(F_IT, 24)
    draw.text((70, H - 118), "naturallyrestful.xyz", font=ff, fill=WHITE)
    draw.text((70, H - 78), "Honest, research-cited guides", font=sf, fill=(200, 205, 218))


def bars(draw, y, rows, hi_index=None, max_val=None, unit="", val_fmt=str):
    """rows: list of (label, value). hi_index: row to highlight."""
    bf = font(F_BOLD, 30)
    vf = font(F_BOLD, 30)
    lf = font(F_REG, 25)
    max_val = max_val or max(v for _, v in rows)
    lh = 78
    for i, (label, val) in enumerate(rows):
        ry = y + i * lh
        highlight = (hi_index is None or i == hi_index)
        draw.text((70, ry), label, font=bf, fill=WHITE if highlight else GREY)
        bw = int(430 * (val / max_val)) if max_val else 0
        # value right-aligned after bar zone
        val_s = val_fmt(val) + unit
        vw = draw.textlength(val_s, font=vf)
        draw.text((W - 70 - vw, ry - 3), val_s, font=vf, fill=CREAM if highlight else GREY)
        bar_x0 = W - 70 - vw - 30 - 430
        draw.rectangle([bar_x0, ry + 2, bar_x0 + 430, ry + 22], fill=(38, 46, 68))
        draw.rectangle([bar_x0, ry + 2, bar_x0 + max(bw, 6), ry + 22],
                       fill=BAR if highlight else BAR_DIM)
    return y + len(rows) * lh


def note(draw, y, text, size=27):
    nf = font(F_IT, size)
    draw.text((70, y + 14), text, font=nf, fill=(206, 211, 224))


def make_pin(filename, kicker, title_lines, chart, title_size=64):
    img, draw, y = base_canvas(kicker, title_lines, title_size)
    kind = chart["kind"]
    if kind == "bars":
        y = bars(draw, y, chart["rows"], chart.get("hi"), chart.get("max"),
                 chart.get("unit", ""), chart.get("fmt", str))
    if chart.get("note"):
        note(draw, y, chart["note"])
    footer(draw)
    img.save(os.path.join(OUT, filename))
    print("wrote", filename)


# 27 — flagship: full ranking
make_pin(
    "pin-27-reality-index.png",
    "Reality Index — Sept 2026",
    ["12 Supplements.", "1,673 Reddit", "Threads, Ranked."],
    {
        "kind": "bars",
        "rows": [("Glycine", 97), ("Reishi", 86), ("Melatonin", 83), ("Magnesium", 81),
                 ("L-Theanine", 81), ("Ashwagandha", 71)],
        "hi": 0,
        "unit": "%",
        "max": 100,
        "note": "% of positive outcome language, 5 sleep communities",
    },
)

# 28 — glycine
make_pin(
    "pin-28-glycine.png",
    "The Reality Index · Sept 2026",
    ["Reddit's Secret", "Favorite Sleep", "Supplement"],
    {
        "kind": "bars",
        "rows": [("Glycine", 97), ("Magnesium", 81), ("L-Theanine", 81), ("Ashwagandha", 71)],
        "hi": 0,
        "unit": "%",
        "max": 100,
        "note": "97% positive — and exactly 1 negative post in 56",
    },
    title_size=68,
)

# 29 — ashwagandha
make_pin(
    "pin-29-ashwagandha.png",
    "The Reality Index · Sept 2026",
    ["The Most", "Controversial", "Sleep Supplement", "on Reddit"],
    {
        "kind": "bars",
        "rows": [("Glycine", 97), ("Melatonin", 83), ("Magnesium", 81), ("Ashwagandha", 71)],
        "hi": 3,
        "unit": "%",
        "max": 100,
        "note": "36 of 214 threads report side effects — read them first",
    },
    title_size=64,
)

# 30 — magnesium forms
make_pin(
    "pin-30-magnesium.png",
    "The Reality Index · Sept 2026",
    ["8 in 10 Back", "Magnesium —", "But Only One", "Form"],
    {
        "kind": "bars",
        "rows": [("Glycinate", 81), ("Threonate", 14), ("Oxide", 10)],
        "hi": 0,
        "unit": "",
        "note": "form mentions across 217 magnesium threads",
    },
)

# 31 — melatonin
make_pin(
    "pin-31-melatonin.png",
    "The Reality Index · Sept 2026",
    ["47,000 Upvotes", "Agree: You're", "Overdosing", "Melatonin"],
    {
        "kind": "bars",
        "rows": [("Typical bottle", 10), ("Study dose", 1)],
        "hi": 1,
        "unit": " mg",
        "max": 10,
        "note": "highest-engagement supplement in the index (47.6k upvotes)",
    },
)

print("done")
