from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance
import os

SRC = 'assets/photos/source'
OUT = 'assets/photos/optimized'
os.makedirs(OUT, exist_ok=True)

# slug, source file, target ratio (w/h), full width, focal point (0-1 x, 0-1 y)
IMAGES = [
    ('hero-facade', '82a38b79-e122-4861-bc71-f25cc20c2811.jpg', 16/10, 1920, (0.58, 0.48)),
    ('hero-mobile', '82a38b79-e122-4861-bc71-f25cc20c2811.jpg', 4/5, 960, (0.58, 0.5)),
    ('facility-tall', '58f4506d-f585-4e46-b341-a47ba5b63d5d.jpg', 4/5, 1200, (0.55, 0.45)),
    ('facility-gate', 'c7bad504-4175-48de-9932-044a82a29b46.jpg', 4/5, 1200, (0.6, 0.45)),
    ('warehouse-wide', '442a7f7b-5169-4aa0-b25b-6d0575111962.jpg', 16/10, 1600, (0.55, 0.5)),
    ('factory-floor', '50560e2c-f25d-4590-a0a6-d6312ac08bbf.jpg', 16/10, 1600, (0.5, 0.5)),
    ('paper-rolls', '53434844-9d01-4d28-8e1d-98017226c5ef.jpg', 16/10, 1600, (0.55, 0.5)),
    ('paper-rolls-tall', '255c633b-d044-42a7-8492-0a45fb32344d.jpg', 4/5, 1200, (0.5, 0.5)),
    ('paper-stack', '3fc48a33-5d38-4995-a68d-d391a3d2ad61.jpg', 16/10, 1600, (0.55, 0.5)),
    ('rolls-close', 'df6fc0b6-3b4b-4684-ae5a-b764edfc5f86.jpg', 16/10, 1600, (0.5, 0.5)),
    ('finished-goods', '2e95e55c-9ae8-482e-be47-ad3d26921310.jpg', 16/10, 1600, (0.5, 0.5)),
    ('boxes', 'cfbcda0c-edb4-4dd4-863f-a7b0872a901e.jpg', 16/10, 1600, (0.5, 0.5)),
    ('print-sheets', '4cf3a144-12f9-4446-ab37-76eee790decd.jpg', 4/5, 1200, (0.5, 0.5)),
    ('print-detail', 'e8f81e29-7ef9-4d19-a154-581d75e80b4e.jpg', 16/10, 1600, (0.45, 0.5)),
    ('press', '7915a3cb-e00f-4d1c-a352-03e251b586d5.jpg', 16/10, 1600, (0.5, 0.5)),
    ('diecut', 'd078190e-3c0a-455b-bc56-6f41393363aa.jpg', 16/10, 1600, (0.5, 0.5)),
    ('bobst', '24a8a3e1-1452-4f32-b2c4-7a4985f09d9d.jpg', 16/10, 1600, (0.5, 0.5)),
    ('gluer', '5765493d-b665-4b86-876d-1a6ab4ff1c9d.jpg', 16/10, 1600, (0.5, 0.5)),
    ('labels', 'e3d9fa2f-319e-466a-b2a6-d92cf06c2d53.jpg', 16/10, 1600, (0.5, 0.5)),
    ('shrink', 'df98300a-372c-410f-a046-ee86942386f4.jpg', 16/10, 1600, (0.5, 0.5)),
]


def crop_to_ratio(im, ratio, focal):
    w, h = im.size
    current = w / h
    if current > ratio:
        new_w = int(h * ratio)
        left = int((w - new_w) * focal[0])
        box = (left, 0, left + new_w, h)
    else:
        new_h = int(w / ratio)
        top = int((h - new_h) * focal[1])
        box = (0, top, w, top + new_h)
    return im.crop(box)


for slug, src, ratio, full_width, focal in IMAGES:
    im = Image.open(os.path.join(SRC, src)).convert('RGB')
    im = crop_to_ratio(im, ratio, focal)
    im = ImageEnhance.Color(im).enhance(0.92)
    im = ImageEnhance.Contrast(im).enhance(1.03)
    for width in [full_width, min(960, full_width), 480]:
        if width >= full_width and width != full_width:
            continue
        h = int(width / ratio)
        out = im.resize((width, h), Image.LANCZOS)
        path = os.path.join(OUT, f'{slug}-{width}.webp')
        out.save(path, 'WEBP', quality=83, method=6)
    # always save a 960 and 480 variant if full width bigger
    for width in [960, 480]:
        if width < full_width:
            h = int(width / ratio)
            out = im.resize((width, h), Image.LANCZOS)
            path = os.path.join(OUT, f'{slug}-{width}.webp')
            out.save(path, 'WEBP', quality=83, method=6)

# Open Graph image
og = Image.open(os.path.join(SRC, '82a38b79-e122-4861-bc71-f25cc20c2811.jpg')).convert('RGB')
og = crop_to_ratio(og, 1200/630, (0.55, 0.45)).resize((1200, 630), Image.LANCZOS)
overlay = Image.new('RGBA', og.size, (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
for y in range(630):
    alpha = int(210 * (1 - y / 630) + 35)
    od.line([(0, y), (1200, y)], fill=(33, 40, 66, min(alpha, 225)))
og = Image.alpha_composite(og.convert('RGBA'), overlay).convert('RGB')
d = ImageDraw.Draw(og)
try:
    font_big = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 88)
    font_small = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 30)
except Exception:
    font_big = ImageFont.load_default()
    font_small = ImageFont.load_default()
d.text((72, 190), 'БРИЗ', fill=(240, 231, 213), font=font_big)
d.text((76, 300), 'Материя упаковки', fill=(240, 231, 213), font=font_small)
d.text((76, 356), 'Размотка · печать · высечка · отделка', fill=(200, 195, 185), font=font_small)
d.line([(76, 500), (1124, 500)], fill=(240, 231, 213, 90), width=1)
d.text((76, 528), 'Климовск · Московская область · с 2010 года', fill=(240, 231, 213), font=font_small)
og.save('assets/og-image.jpg', quality=88, optimize=True)

print('done')
