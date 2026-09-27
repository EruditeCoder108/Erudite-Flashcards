"""Crops the figures for Biology 12 Ch 3 (Reproductive Health). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'bio12', 'lebo103.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch03-reproductive-health', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_3_1a_male_condom': (3, (60, 155, 205, 200)),
    'fig_3_1b_female_condom': (3, (55, 236, 226, 327)),
    'fig_3_2_copper_t': (3, (55, 378, 227, 580)),
    'fig_3_3_implants': (4, (342, 83, 512, 207)),
    'fig_3_4_vasectomy_tubectomy': (4, (37, 476, 522, 690)),
}, MEDIA, long_side=1000)

# White out the page-number tab caught at the right edge of Figure 3.4.
from PIL import Image, ImageDraw
p = os.path.join(MEDIA, 'fig_3_4_vasectomy_tubectomy.webp')
im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).rectangle((895, 270, 1001, 370), fill='white'); im.save(p, quality=85)
