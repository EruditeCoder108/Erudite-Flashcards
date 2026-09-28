"""Crops the figures for Physics 12 Ch 2 (Electrostatic Potential and Capacitance). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph102.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch02-electrostatic-potential-and-capacitance', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_2_2_path': (3, (75, 98, 295, 198)),
    'fig_2_3_point': (3, (75, 364, 297, 466)),
    'fig_2_4_V_E_graph': (4, (258, 98, 538, 282)),
    'fig_2_5_dipole': (5, (78, 100, 345, 292)),
    'fig_2_6_system': (6, (312, 546, 537, 650)),
    'fig_2_8_example': (8, (128, 222, 370, 368)),
    'fig_2_9_point_equi': (9, (90, 98, 190, 340)),
    'fig_2_10_uniform_equi': (9, (250, 428, 485, 522)),
    'fig_2_11_dipole_equi': (9, (205, 594, 522, 708)),
    'fig_2_12_E_from_V': (10, (338, 150, 537, 332)),
    'fig_2_14_three': (11, (75, 572, 290, 650)),
    'fig_2_15_square': (12, (100, 198, 345, 361)),
    'fig_2_16_dipole_pe': (15, (75, 424, 270, 553)),
    'fig_2_17_pillbox': (18, (378, 340, 545, 468)),
    'fig_2_18_cavity': (19, (75, 98, 290, 232)),
    'fig_2_19_properties': (19, (235, 300, 495, 465)),
    'fig_2_20_conductor_dielectric': (20, (370, 255, 500, 405)),
    'fig_2_21_molecules': (20, (275, 462, 548, 670)),
    'fig_2_22_polarisation': (21, (75, 98, 348, 385)),
    'fig_2_23_slab': (22, (352, 98, 538, 320)),
    'fig_2_24_two_conductors': (22, (310, 519, 550, 640)),
    'fig_2_25_parallel_plate': (23, (75, 530, 280, 697)),
    'fig_2_26_series_two': (26, (318, 400, 548, 540)),
    'fig_2_27_series_n': (26, (300, 578, 495, 700)),
    'fig_2_28_parallel': (27, (80, 350, 265, 655)),
    'fig_2_29_network': (28, (145, 170, 338, 324)),
    'fig_2_30_charging': (29, (60, 98, 285, 225)),
    'fig_2_31_sharing': (30, (145, 322, 372, 532)),
}, MEDIA, long_side=1000)

# ---------------------------------------------------------------- self-drawn figures
from draw import Fig

# V and E versus r for a charged conducting sphere (or thin shell)
f = Fig(620, 400)
ox, oy, R = 70, 330, 170
f.axes(ox, oy, 520, 290, 'r', 'V, E')
f.line(ox, oy - 200, ox + R, oy - 200, 'red', 3.4)
f.curve(lambda r: 200 * R / r, R, 515, lambda r: ox + r, lambda v: oy - v, 'red', 3.4)
f.line(ox, oy, ox + R, oy, 'blue', 4)
f.curve(lambda r: 150 * (R / r) ** 2, R, 515, lambda r: ox + r, lambda e: oy - e, 'blue', 3.4)
f.line(ox + R, oy, ox + R, 60, 'grey', 1.4, '6 5')
f.text(ox + R, oy + 28, 'R', 'ink', 22, 'middle', italic=True)
f.text(ox + 8, oy - 212, 'V constant inside', 'red', 19)
f.text(ox + R + 150, oy - 118, 'V ∝ 1/r', 'red', 20)
f.text(ox + 8, oy - 14, 'E = 0 inside', 'blue', 19)
f.text(ox + R + 200, oy - 50, 'E ∝ 1/r²', 'blue', 20)
f.text(330, 36, 'V is continuous at R; E jumps from 0 to σ/ε₀', 'ink', 20, 'middle', bold=True)
f.save(MEDIA, 'drawn_sphere_V_E')
