"""Crops the figures for Physics 12 Ch 4 (Moving Charges and Magnetism). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph104.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch04-moving-charges-and-magnetism', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_4_2_force_direction': (3, (72, 125, 305, 218)),
    'fig_4_3_suspended_wire': (4, (150, 160, 360, 238)),
    'fig_4_4_example': (4, (170, 488, 305, 622)),
    'fig_4_5_circular': (5, (75, 300, 229, 442)),
    'fig_4_6_helical': (5, (70, 481, 297, 699)),
    'fig_4_7_biot_savart': (6, (393, 422, 538, 572)),
    'fig_4_8_element': (7, (298, 624, 432, 716)),
    'fig_4_9_loop_axis': (8, (344, 398, 538, 561)),
    'fig_4_10_loop_lines': (9, (311, 531, 437, 679)),
    'fig_4_11_semicircle': (10, (110, 210, 370, 298)),
    'fig_4_12_amperian': (10, (355, 618, 492, 712)),
    'fig_4_13_thick_wire': (12, (150, 560, 330, 664)),
    'fig_4_14_B_vs_r': (13, (280, 388, 480, 516)),
    'fig_4_15_solenoid': (14, (75, 238, 522, 404)),
    'fig_4_16_long_solenoid': (14, (97, 586, 377, 704)),
    'fig_4_17_parallel_wires': (15, (80, 509, 247, 649)),
    'fig_4_18_coil_torque': (18, (348, 99, 537, 391)),
    'fig_4_19_coil_angle': (19, (75, 98, 297, 367)),
    'fig_4_20_mcg': (23, (75, 98, 277, 339)),
    'fig_4_21_ammeter': (23, (75, 504, 185, 603)),
    'fig_4_22_voltmeter': (24, (425, 100, 535, 207)),
    'fig_4_23_example': (24, (145, 585, 325, 712)),
}, MEDIA, long_side=1000)

# ---------------------------------------------------------------- self-drawn figures
import math
from draw import Fig

# Field of a long straight wire: current out of the page (dot) and into the page (cross)
f = Fig(640, 360)
for cx, out in ((165, True), (475, False)):
    cy = 185
    for r in (40, 80, 120):
        f.circle(cx, cy, r, 'blue', 'none', 2.4)
        for a in (0, 180):  # arrowheads at the top and bottom of each circle
            ang = math.radians(90 + a)
            x, y = cx + r * math.cos(ang), cy - r * math.sin(ang)
            s = 1 if (out != (a == 180)) else -1  # anticlockwise for out, clockwise for in
            f.arrow(x + 6 * s, y, x - 6 * s, y, 'blue', 2.4, 12)
    f.circle(cx, cy, 16, 'ink', '#f4efe2', 2.4)
    if out:
        f.circle(cx, cy, 4, 'ink', '#1f2430', 2)
    else:
        f.line(cx - 9, cy - 9, cx + 9, cy + 9, 'ink', 2.6); f.line(cx - 9, cy + 9, cx + 9, cy - 9, 'ink', 2.6)
    f.text(cx, 340, 'I out of page: B anticlockwise' if out else 'I into page: B clockwise', 'ink', 19, 'middle')
f.text(320, 36, 'B = μ₀I / 2πr, circles around the wire', 'ink', 21, 'middle', bold=True)
f.save(MEDIA, 'drawn_wire_field')
