"""Stitch screenshots into one annotated flow image.

Usage: python3 -I compose.py spec.json out.png

Spec (all coordinates are pixels of the panel's own source image):
{
  "panels": [{"image": "/abs/a.png", "steps": "1", "caption": "Click New Order"}],
  "boxes": [{"panel": 0, "rect": [x0, y0, x1, y1], "n": "1", "badge": "left|right|below"}],
  "arrows": [[[0, 1916, 161], [0, "lane", 161], [1, "lane", "gap"], [1, 810, "gap"], [1, 810, 270]]],
  "redact": [{"panel": 2, "rect": [x0, y0, x1, y1]}]
}
An arrow point is [panel, x, y]. x "lane" is the empty column right of every panel; y "gap" is the strip
between that panel's caption and its image. Route arrows along those so they cross no text.
"""

import json
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

spec = json.load(open(sys.argv[1]))
ORANGE, BG, TEXT = (234, 88, 12), (243, 244, 246), (17, 24, 39)
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"
caption_font = ImageFont.truetype(FONT, 46)
badge_font = ImageFont.truetype(FONT, 38)
LEFT, RIGHT_LANE, CAPTION_H, GAP, TOP = 80, 140, 130, 50, 60

images = [Image.open(panel["image"]).convert("RGB") for panel in spec["panels"]]
for redaction in spec.get("redact", []):
    image = images[redaction["panel"]]
    region = tuple(redaction["rect"])
    image.paste(image.crop(region).filter(ImageFilter.GaussianBlur(14)), region[:2])

panel_width = max(image.width for image in images)
offsets, y = [], TOP
for image in images:
    offsets.append(y + CAPTION_H)
    y += CAPTION_H + image.height + GAP
canvas = Image.new("RGB", (LEFT + panel_width + RIGHT_LANE, y - GAP + TOP), BG)

for image, top in zip(images, offsets):
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle(
        (LEFT, top + 8, LEFT + image.width, top + image.height + 8), 18, fill=(0, 0, 0, 40)
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))
    canvas.paste(shadow, (0, 0), shadow)
    mask = Image.new("L", image.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, image.width, image.height), 18, fill=255)
    canvas.paste(image, (LEFT, top), mask)

draw = ImageDraw.Draw(canvas)
for panel, top in zip(spec["panels"], offsets):
    pill_w = draw.textlength(panel["steps"], font=caption_font) + 44
    draw.rounded_rectangle((LEFT, top - 118, LEFT + pill_w, top - 54), 32, fill=ORANGE)
    draw.text((LEFT + 22, top - 86), panel["steps"], font=caption_font, fill="white", anchor="lm")
    draw.text((LEFT + pill_w + 22, top - 86), panel["caption"], font=caption_font, fill=TEXT, anchor="lm")

lane = LEFT + panel_width + 60


def point(panel, x, y):
    return (
        lane if x == "lane" else LEFT + x,
        offsets[panel] - 24 if y == "gap" else offsets[panel] + y,
    )


for path in spec.get("arrows", []):
    points = [point(*p) for p in path]
    draw.line(points, fill=ORANGE, width=9, joint="curve")
    (x0, y0), (x1, y1) = points[-2], points[-1]
    size = 28
    if x0 == x1:
        d = 1 if y1 > y0 else -1
        head = [(x1, y1), (x1 - size * 0.7, y1 - d * size), (x1 + size * 0.7, y1 - d * size)]
    else:
        d = 1 if x1 > x0 else -1
        head = [(x1, y1), (x1 - d * size, y1 - size * 0.7), (x1 - d * size, y1 + size * 0.7)]
    draw.polygon(head, fill=ORANGE)

for box in spec.get("boxes", []):
    x0, y0, x1, y1 = box["rect"]
    pad = 10
    a, b = point(box["panel"], x0 - pad, y0 - pad), point(box["panel"], x1 + pad, y1 + pad)
    draw.rounded_rectangle((*a, *b), 14, outline=ORANGE, width=7)
    cx, cy = {
        "left": (a[0] - 6, a[1] - 6),
        "right": (b[0] + 6, a[1] - 6),
        "below": (a[0] + 24, b[1] + 40),
    }[box.get("badge", "left")]
    draw.ellipse((cx - 30, cy - 30, cx + 30, cy + 30), fill=ORANGE, outline="white", width=4)
    draw.text((cx, cy + 1), box["n"], font=badge_font, fill="white", anchor="mm")

canvas.save(sys.argv[2])
print(canvas.size)
