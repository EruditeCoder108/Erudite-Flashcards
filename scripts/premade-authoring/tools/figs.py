"""List figure-sized image/drawing blocks per page: python figs.py <pdf> [min_side_pt]
Prints merged bboxes (PDF points) of raster images and vector drawing clusters, plus figure captions."""
import sys, re
from _work import WORK, ROOT
import pymupdf
from clean_pdf import clean
pdf = sys.argv[1]; minside = float(sys.argv[2]) if len(sys.argv) > 2 else 40
d, _ = clean(pdf)

def merge(rects, gap=6):
    rects = [pymupdf.Rect(r) for r in rects]
    changed = True
    while changed:
        changed = False
        out = []
        while rects:
            r = rects.pop()
            for o in rects[:]:
                if (r + (-gap, -gap, gap, gap)).intersects(o):
                    r |= o; rects.remove(o); changed = True
            out.append(r)
        rects = out
    return rects

for i, page in enumerate(d):
    rects = [b['bbox'] for b in page.get_image_info()]
    rects += [dr['rect'] for dr in page.get_drawings() if dr['rect'].width < page.rect.width * 0.9]
    blocks = [r for r in merge(rects) if r.width >= minside and r.height >= minside and r.width < page.rect.width * 0.95]
    caps = [ln.strip() for ln in page.get_text().split('\n') if re.match(r'(Figure|Fig\.|TABLE|Table)\s*\d', ln.strip())]
    if blocks or caps:
        print(f'p{i}:', ' '.join(f'({r.x0:.0f},{r.y0:.0f},{r.x1:.0f},{r.y1:.0f})' for r in sorted(blocks, key=lambda r: (r.y0, r.x0))), '|', '; '.join(caps))
