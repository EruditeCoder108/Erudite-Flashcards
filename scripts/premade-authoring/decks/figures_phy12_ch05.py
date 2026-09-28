"""Crops the figures for Physics 12 Ch 5 (Magnetism and Matter). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph105.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch05-magnetism-and-matter', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_5_2_field_lines': (2, (72, 95, 540, 302)),
    'fig_5_4_needles': (5, (165, 417, 322, 566)),
    # Fig 5.6, one panel per card (Example 5.3: right or wrong?)
    'fig_5_6a': (7, (100, 295, 212, 392)),
    'fig_5_6b': (7, (100, 402, 212, 480)),
    'fig_5_6c': (7, (95, 500, 232, 628)),
    'fig_5_6d': (7, (95, 640, 240, 692)),
    'fig_5_6e': (7, (240, 292, 350, 390)),
    'fig_5_6f': (7, (250, 440, 368, 559)),
    'fig_5_6g': (7, (250, 615, 362, 689)),
    'fig_5_7_dia_para': (11, (431, 474, 539, 612)),
    'fig_5_8_domains': (13, (422, 100, 539, 290)),
}, MEDIA, long_side=1000)

# ---------------------------------------------------------------- self-drawn figures
from draw import Fig

# Far field of a short bar magnet: axial B along m, equatorial B opposite to m
f = Fig(760, 410)
f.rect(250, 180, 220, 50, 'ink', '#f4efe2', 2.4)
f.rect(360, 180, 110, 50, 'ink', '#e7d9d2', 2.4)
f.text(305, 214, 'S', 'ink', 24, 'middle', bold=True)
f.text(415, 214, 'N', 'red', 24, 'middle', bold=True)
f.arrow(300, 158, 420, 158, 'ink', 2.4, 12); f.text(360, 146, 'm', 'ink', 22, 'middle', bold=True)
f.line(470, 205, 590, 205, 'ink', 1.2)
f.circle(595, 205, 5, 'ink', '#1f2430', 1)
f.arrow(605, 205, 700, 205, 'blue', 3, 14)
f.text(745, 250, 'axial: B = μ₀·2m / 4πr³', 'blue', 19, 'end')
f.text(745, 276, '(along m)', 'blue', 19, 'end')
f.line(360, 230, 360, 330, 'ink', 1.2)
f.circle(360, 340, 5, 'ink', '#1f2430', 1)
f.arrow(350, 340, 260, 340, 'red', 3, 14)
f.text(560, 350, 'equatorial:', 'red', 19, 'middle')
f.text(560, 376, 'B = μ₀m / 4πr³, opposite to m', 'red', 19, 'middle')
f.text(360, 60, 'Short bar magnet, far field (r ≫ l)', 'ink', 22, 'middle', bold=True)
f.text(360, 92, 'axial field = 2 × equatorial field', 'ink', 19, 'middle')
f.save(MEDIA, 'drawn_axial_equatorial')
