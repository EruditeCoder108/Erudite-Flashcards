import sys, io, json
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pymupdf
from PIL import Image, ImageDraw, ImageFont
from clean_pdf import clean
def grid(pdf, page, panels, out, cell=(450, 430), strip=56, cols=2):
    """panels: [(letter, (x0,y0,x1,y1) pts)] -> 2-col grid webp; returns size and label-strip boxes."""
    d,_ = clean(pdf)
    rows = (len(panels) + cols - 1) // cols
    W, H = cell[0]*cols, (cell[1]+strip)*rows
    canvas = Image.new('RGB', (W, H), 'white'); dr = ImageDraw.Draw(canvas)
    try: font = ImageFont.truetype('C:/Windows/Fonts/georgia.ttf', 30)
    except OSError: font = ImageFont.load_default()
    boxes = []
    for i, (letter, r) in enumerate(panels):
        R = pymupdf.Rect(*r)
        z = min((cell[0]-30)/R.width, (cell[1]-20)/R.height)
        pix = d[page].get_pixmap(clip=R, matrix=pymupdf.Matrix(z, z), alpha=False)
        im = Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGB')
        row, col = divmod(i, cols)
        if len(panels) % cols and row == rows-1:   # centre a lone last panel
            ox = (W - cell[0]) // 2
        else:
            ox = col*cell[0]
        oy = row*(cell[1]+strip)
        canvas.paste(im, (ox + (cell[0]-im.width)//2, oy + (cell[1]-im.height)//2))
        tw = dr.textlength(f'({letter})', font=font)
        dr.text((ox + (cell[0]-tw)/2, oy + cell[1] + 8), f'({letter})', fill='#222', font=font)
        boxes.append([ox + 60, oy + cell[1] + 2, cell[0]-120, strip-6])
    canvas.save(out, 'WEBP', quality=82, method=6)
    return canvas.size, boxes
