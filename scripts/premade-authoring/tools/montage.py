"""Montage every image in a folder: python montage.py <folder> <out name>"""
import sys, os
from _work import WORK, ROOT
from PIL import Image, ImageDraw
HERE = WORK
folder, name = sys.argv[1], sys.argv[2]
files = sorted(f for f in os.listdir(folder) if f.lower().endswith(('.webp', '.png', '.jpg')))
tiles = []
for f in files:
    im = Image.open(os.path.join(folder, f)).convert('RGB'); im.thumbnail((300, 280))
    t = Image.new('RGB', (300, 300), '#ddd'); t.paste(im, (0, 0)); ImageDraw.Draw(t).text((3, 286), f[:48], fill='black')
    tiles.append(t)
cols = 6
sheet = Image.new('RGB', (300 * cols, 300 * ((len(tiles) + cols - 1) // cols)), '#ccc')
for i, t in enumerate(tiles):
    sheet.paste(t, ((i % cols) * 300, (i // cols) * 300))
out = os.path.join(HERE, name + '.png'); sheet.save(out); print(out, len(files))
