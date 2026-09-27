"""List figure-sized image/drawing blocks per page: python figs.py <pdf> [min_side_pt]
Prints bboxes (PDF points, clipped to the page) of raster images and vector drawing clusters,
plus figure captions with their positions. Boxes are a starting point: refine with ptgrid.py."""
import sys, re
from _work import WORK
import pymupdf
from clean_pdf import clean
pdf = sys.argv[1]; minside = float(sys.argv[2]) if len(sys.argv) > 2 else 40
d, _ = clean(pdf)

for i, page in enumerate(d):
    pr = page.rect
    rects = [pymupdf.Rect(b['bbox']) & pr for b in page.get_image_info()]
    try:
        rects += [r & pr for r in page.cluster_drawings(x_tolerance=6, y_tolerance=6)]
    except Exception:
        pass
    blocks = [r for r in rects if r.width >= minside and r.height >= minside and r.width < pr.width * 0.95]
    caps = []
    for b in page.get_text('blocks'):
        t = b[4].strip().replace('\n', ' ')
        if re.match(r'(Figure|Fig\.|TABLE|Table)\s*\d', t):
            caps.append(f'"{t[:40]}" @y{b[1]:.0f} x{b[0]:.0f}-{b[2]:.0f}')
    if blocks or caps:
        print(f'p{i}:', ' '.join(f'({r.x0:.0f},{r.y0:.0f},{r.x1:.0f},{r.y1:.0f})' for r in sorted(blocks, key=lambda r: (r.y0, r.x0))), '|', '; '.join(caps))
