"""Crops the figures for Physics 11 Ch 7 (Gravitation). Rects are (page, (x0, y0, x1, y1)) in PDF points.
The g-vs-r graph is self-drawn below with draw.py."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export
from draw import Fig

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph107.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch07-gravitation', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_7_1a_ellipse': (1, (146, 378, 300, 499)),
    'fig_7_1b_drawing_ellipse': (1, (130, 555, 318, 682)),
    'fig_7_2_law_of_areas': (1, (370, 492, 580, 632)),
    'tab_7_1_kepler_data': (2, (72, 294, 304, 423)),
    'fig_7_4_superposition': (3, (380, 289, 565, 466)),
    'fig_7_5_triangle': (4, (114, 106, 268, 250)),
    'fig_7_6_cavendish': (4, (355, 518, 542, 638)),
    'fig_7_7_mine': (5, (366, 236, 570, 384)),
    'fig_7_8a_height': (6, (108, 520, 276, 668)),
    'fig_7_8b_depth': (7, (150, 108, 325, 229)),
    'fig_7_9_square': (8, (352, 106, 503, 272)),
    'fig_7_10_two_spheres': (9, (378, 243, 548, 302)),
    'fig_7_11_hemisphere': (15, (265, 490, 430, 575)),
}, MEDIA, long_side=1000)

# ---------------------------------------------------------------- self-drawn: g versus r
f = Fig(620, 380)
ox, oy, R = 60, 320, 170
f.axes(ox, oy, 530, 280, 'r', 'g')
f.line(ox, oy, ox + R, oy - 220, 'blue', 3.4)
f.curve(lambda r: 220 * (R / r) ** 2, R, 530, lambda r: ox + r, lambda y: oy - y, 'red', 3.4)
f.line(ox + R, oy, ox + R, oy - 220, 'grey', 1.4, '6 5'); f.line(ox, oy - 220, ox + R, oy - 220, 'grey', 1.4, '6 5')
f.text(ox + R, oy + 26, 'R (surface)', 'ink', 18, 'middle'); f.text(ox - 8, oy - 214, 'g', 'ink', 20, 'end', italic=True)
f.text(ox + 40, oy - 120, 'inside: g ∝ r', 'blue', 20)
f.text(ox + 300, oy - 120, 'outside: g ∝ 1/r²', 'red', 20)
f.text(310, 34, 'g is maximum at the surface; zero at the centre', 'ink', 20, 'middle', bold=True)
f.save(MEDIA, 'drawn_g_vs_r')
