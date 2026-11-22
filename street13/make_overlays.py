#!/usr/bin/env python3
"""Build overlay PNGs: transparent Street 13 wordmark (sign) and caption cards."""
import pathlib
from collections import deque
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "overlays"; OUT.mkdir(exist_ok=True)

# --- wordmark: crop from circular logo, flood-fill the yellow/red background away
src = Image.open(HERE / "refs" / "logo.jpg").convert("RGB")
crop = src.crop((120, 360, 860, 620)).convert("RGBA")
W, H = crop.size; px = crop.load()
BG = [(236, 170, 60), (132, 28, 25)]
def is_bg(c, tol=55):
    return any(sum(abs(c[i] - b[i]) for i in range(3)) < tol * 1.6 for b in BG)
seen = set(); q = deque()
for x in range(W):
    q.extend([(x, 0), (x, H - 1)])
for y in range(H):
    q.extend([(0, y), (W - 1, y)])
while q:
    x, y = q.popleft()
    if (x, y) in seen or not (0 <= x < W and 0 <= y < H):
        continue
    seen.add((x, y))
    if is_bg(px[x, y]):
        px[x, y] = (0, 0, 0, 0)
        q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
a = crop.split()[3].filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
crop.putalpha(a)
crop = crop.crop(crop.getbbox())
crop.save(OUT / "wordmark.png")

# sign overlay: full 1080x1920 frame, wordmark fitted inside the blank red panel with a glow
PANEL = (405, 590, 780, 838)
pw, ph = PANEL[2] - PANEL[0], PANEL[3] - PANEL[1]
scale = min(pw * 0.92 / crop.width, ph * 0.80 / crop.height)
wm = crop.resize((int(crop.width * scale), int(crop.height * scale)), Image.LANCZOS)
frame = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
ox = PANEL[0] + (pw - wm.width) // 2; oy = PANEL[1] + (ph - wm.height) // 2
glow = Image.new("RGBA", frame.size, (0, 0, 0, 0))
g = Image.new("RGBA", wm.size, (255, 230, 220, 0)); g.putalpha(wm.split()[3].point(lambda v: v * 0.7))
glow.paste(g, (ox, oy), g); glow = glow.filter(ImageFilter.GaussianBlur(14))
frame = Image.alpha_composite(frame, glow)
frame.alpha_composite(wm, (ox, oy))
frame.save(OUT / "sign.png")

# --- captions (TikTok-style lower third)
FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 76)
CAPS = [
    ("cap01", "3 A.M. IN ABUJA."),
    ("cap02", "EVERYWHERE'S CLOSED…"),
    ("cap03", "…EXCEPT STREET 13."),
    ("cap04", "LOADED FRIES."),
    ("cap05", "JUICY BURGERS."),
    ("cap06", "SAUCY WINGS."),
    ("cap07", "DINE IN OR DELIVERY."),
    ("cap08", "STREET 13.|ALWAYS OPEN."),
]
for name, text in CAPS:
    img = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    words, lines, cur = text.split(), [], ""
    if "|" in text:
        words = []; lines = text.split("|")[:-1]; cur = text.split("|")[-1]
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=FONT) > 940 and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    lines.append(cur)
    y = 1430 if name != "cap08" else 1690
    for ln in lines:
        w = d.textlength(ln, font=FONT)
        hl = "13" in ln or ln.startswith(("LOADED", "JUICY", "SAUCY"))
        d.text(((1080 - w) / 2, y), ln, font=FONT, fill=(255, 211, 77) if hl else (255, 255, 255),
               stroke_width=8, stroke_fill=(0, 0, 0))
        y += 96
    img.save(OUT / f"{name}.png")
print("ok")
