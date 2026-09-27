"""Render PDF pages for a look: python pg.py <pdf> <page[,page...]> [dpi]  -> scratchpad/pg_<name>_<page>.png"""
import sys, os
from _work import WORK, ROOT
from clean_pdf import clean
HERE = WORK
pdf = sys.argv[1]
dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 80
d, _ = clean(pdf)
name = os.path.splitext(os.path.basename(pdf))[0]
for page in sys.argv[2].split(','):
    out = os.path.join(HERE, f'pg_{name}_{page}.png')
    d[int(page)].get_pixmap(dpi=dpi).save(out)
    print(out)
