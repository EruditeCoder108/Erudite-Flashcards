"""Draw every occlusion mask of a deck onto its image, as one contact sheet: python maskcheck.py <deck folder> [out name]"""
import sys, os, json, math
from _work import WORK, ROOT
from PIL import Image, ImageDraw
HERE = WORK
folder = sys.argv[1]
out = os.path.join(HERE, (sys.argv[2] if len(sys.argv) > 2 else 'maskcheck') + '.png')
deck = json.load(open(os.path.join(folder, 'deck.json'), encoding='utf8'))
tiles = []
for c in deck['cards']:
    if c['noteType'] != 'image-occlusion':
        continue
    im = Image.open(os.path.join(folder, c['image'])).convert('RGB')
    dr = ImageDraw.Draw(im, 'RGBA')
    for m in c['occlusion']['masks']:
        x, y, w, h = m['bboxPx']
        if m.get('rotate'):
            a = math.radians(m['rotate']); cx, cy = x + w / 2, y + h / 2
            pts = [(cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a))
                   for dx, dy in [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]]
        elif m.get('points'):
            pts = [(x + px * w, y + py * h) for px, py in m['points']]
        else:
            pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        dr.polygon(pts, fill=(255, 0, 0, 110), outline=(255, 0, 0))
    im.thumbnail((420, 420))
    tiles.append(im)
cols = 4
sheet = Image.new('RGB', (420 * cols, 420 * ((len(tiles) + cols - 1) // cols)), 'white')
for i, t in enumerate(tiles):
    sheet.paste(t, ((i % cols) * 420, (i // cols) * 420))
sheet.save(out)
print(len(tiles), 'images ->', out)
