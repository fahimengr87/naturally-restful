# Sleep-trackers pin — EDITORIAL style (last was Chrome; rotation rule)
from PIL import Image, ImageDraw, ImageFont

W, H = 1000, 1500
OUT = r"C:/Users/Fahim/ZCodeProject/pinterest-pins/pin-40-trackers-editorial.png"
F = "C:/Windows/Fonts/"
IMPACT, GEO, GEO_I, SEGOE, SEGOE_B, SEGOE_L = F+"impact.ttf", F+"georgia.ttf", F+"georgiai.ttf", F+"segoeui.ttf", F+"segoeuib.ttf", F+"segoeuil.ttf"
def font(p, s): return ImageFont.truetype(p, s)

img = Image.new("RGB", (W, H), (245, 239, 228))
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 14], fill=(18, 18, 18))
d.text((70, 60), "SLEEP TECH · THE HONEST VERDICT", font=font(SEGOE_B, 26), fill=(18, 18, 18))
d.text((70, 96), "N°006 · OCT 2026", font=font(SEGOE_L, 22), fill=(120, 116, 108))
d.rectangle([70, 140, 930, 143], fill=(18, 18, 18))

d.text((62, 180), "YOUR WATCH", font=font(IMPACT, 122), fill=(18, 18, 18))
d.text((62, 292), "CANNOT", font=font(IMPACT, 122), fill=(18, 18, 18))
d.text((62, 404), "MEASURE", font=font(IMPACT, 122), fill=(228, 87, 46))
d.text((62, 516), "SLEEP.", font=font(IMPACT, 122), fill=(18, 18, 18))

d.rectangle([70, 680, 930, 1010], outline=(18, 18, 18), width=4)
d.text((100, 706), "It measures stillness", font=font(GEO_I, 52), fill=(228, 87, 46))
d.text((100, 772), "+ heart rhythm.", font=font(GEO_I, 52), fill=(228, 87, 46))
d.text((100, 852), "Sleep is a brain event.", font=font(GEO, 44), fill=(18, 18, 18))
d.text((100, 910), "That gap is where the errors live.", font=font(GEO_I, 30), fill=(110, 106, 98))

rows = [("Total sleep time", "roughly trustworthy"), ("Deep / REM minutes", "a coin flip"), ("Your 2-week trend", "the useful number"), ("If you have insomnia", "consider taking it off")]
y = 1055
for main, v in rows:
    d.text((100, y), main, font=font(SEGOE_B, 30), fill=(18, 18, 18))
    vw = d.textlength(v, font=font(SEGOE_B, 30))
    d.text((900 - vw, y), v, font=font(SEGOE_B, 30), fill=(228, 87, 46))
    d.line([100, y + 44, 900, y + 44], fill=(210, 203, 190), width=2)
    y += 64

d.text((70, H - 116), "naturallyrestful.xyz", font=font(SEGOE_B, 30), fill=(18, 18, 18))
d.text((70, H - 76), "Honest, research-cited guides", font=font(SEGOE_L, 22), fill=(120, 116, 108))

img.save(OUT)
print("wrote", OUT)
