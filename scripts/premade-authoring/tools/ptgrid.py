"""Render a PDF region with a PDF-point grid: python ptgrid.py pdf page x0 y0 x1 y1 [step] -> ptgrid.png"""
import sys, os, io
from _work import WORK, ROOT
import pymupdf
from PIL import Image, ImageDraw
from clean_pdf import clean
pdf, page = sys.argv[1], int(sys.argv[2]); x0, y0, x1, y1 = map(float, sys.argv[3:7])
step = int(sys.argv[7]) if len(sys.argv) > 7 else 20
d, _ = clean(pdf); R = pymupdf.Rect(x0, y0, x1, y1); z = 1100 / max(R.width, R.height)
im = Image.open(io.BytesIO(d[page].get_pixmap(clip=R, matrix=pymupdf.Matrix(z, z), alpha=False).tobytes('png'))).convert('RGB')
dr = ImageDraw.Draw(im, 'RGBA')
for x in range(int(x0 // step * step), int(x1) + 1, step):
    X = (x - x0) * z; dr.line([(X, 0), (X, im.height)], fill=(255, 0, 0, 90)); dr.text((X + 2, 2), str(x), fill=(200, 0, 0))
for y in range(int(y0 // step * step), int(y1) + 1, step):
    Y = (y - y0) * z; dr.line([(0, Y), (im.width, Y)], fill=(0, 0, 255, 90)); dr.text((2, Y + 2), str(y), fill=(0, 0, 200))
im.save(os.path.join(WORK, 'ptgrid.png'))
