"""Contact sheet of PDF pages with a 50-pt grid: python sheet.py <pdf> <pages e.g. 1-8> <out name>
Each page is labelled with its index; grid labels are PDF points, for picking crop rects."""
import sys, os, io
from _work import WORK, ROOT
import pymupdf
from PIL import Image, ImageDraw
from clean_pdf import clean
HERE = WORK
pdf, rng, name = sys.argv[1], sys.argv[2], sys.argv[3]
a, b = (int(x) for x in rng.split('-'))
d, _ = clean(pdf)
z = 0.9
tiles = []
for i in range(a, b + 1):
    p = d[i]
    im = Image.open(io.BytesIO(p.get_pixmap(matrix=pymupdf.Matrix(z, z), alpha=False).tobytes('png'))).convert('RGB')
    dr = ImageDraw.Draw(im, 'RGBA')
    for x in range(0, int(p.rect.width), 50):
        dr.line([(x * z, 0), (x * z, im.height)], fill=(255, 0, 0, 70)); dr.text((x * z + 1, 1), str(x), fill=(220, 0, 0))
    for y in range(0, int(p.rect.height), 50):
        dr.line([(0, y * z), (im.width, y * z)], fill=(0, 0, 255, 70)); dr.text((1, y * z + 1), str(y), fill=(0, 0, 220))
    dr.text((im.width - 40, 4), f'p{i}', fill=(0, 140, 0))
    tiles.append(im)
cols = 4
w, h = tiles[0].size
sheet = Image.new('RGB', (w * cols, h * ((len(tiles) + cols - 1) // cols)), 'white')
for k, t in enumerate(tiles):
    sheet.paste(t, ((k % cols) * w, (k // cols) * h))
out = os.path.join(HERE, name + '.png')
sheet.save(out)
print(out, sheet.size)
