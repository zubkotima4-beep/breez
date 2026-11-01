from PIL import Image, ImageDraw, ImageFont, ImageOps
import os, hashlib

src = 'assets/photos/source'
files = sorted([f for f in os.listdir(src) if f.lower().endswith('.jpg')])

seen = {}
for f in files:
    h = hashlib.md5(open(os.path.join(src, f), 'rb').read()).hexdigest()
    seen.setdefault(h, []).append(f)

print('unique', len(seen), 'total', len(files))
for h, fs in seen.items():
    if len(fs) > 1:
        print('DUP', fs)

cols, rows = 5, 6
w, h = 360, 270
labelh = 28
sheet = Image.new('RGB', (cols * w, rows * (h + labelh)), (20, 24, 40))
d = ImageDraw.Draw(sheet)
font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 18)

for i, f in enumerate(files):
    im = Image.open(os.path.join(src, f)).convert('RGB')
    im = ImageOps.fit(im, (w, h))
    x = (i % cols) * w
    y = (i // cols) * (h + labelh)
    sheet.paste(im, (x, y))
    d.text((x + 8, y + h + 4), f'{i+1:02d}  {f[:8]}', fill=(240, 231, 213), font=font)

sheet.save('assets/photos/contact-sheet.jpg', quality=88)
print('saved', sheet.size)
