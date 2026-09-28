"""Crops the figures for Physics 12 Ch 1 (Electric Charges and Fields). Rects are (page, (x0, y0, x1, y1)) in PDF points."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy12', 'leph101.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch01-electric-charges-and-fields', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_1_1_rods': (1, (205, 100, 535, 192)),
    'fig_1_2_electroscope': (3, (60, 95, 262, 330)),
    'fig_1_3_coulomb_vectors': (7, (70, 100, 285, 310)),
    'fig_1_5_superposition': (10, (375, 440, 540, 690)),
    'fig_1_6_triangle': (11, (274, 513, 472, 655)),
    'fig_1_7_triangle_qqq': (12, (75, 388, 425, 557)),
    'fig_1_8_point_field': (13, (70, 380, 186, 645)),
    'fig_1_9_system_field': (15, (75, 110, 262, 258)),
    'fig_1_10_fall': (16, (132, 378, 355, 466)),
    'fig_1_11_example': (17, (262, 418, 490, 560)),
    'fig_1_12_point_arrows': (18, (352, 485, 535, 668)),
    'fig_1_13_density': (19, (75, 98, 242, 252)),
    'fig_1_14a_pos': (20, (392, 98, 524, 212)),
    'fig_1_14b_neg': (20, (392, 247, 525, 362)),
    'fig_1_14c_like': (20, (373, 395, 530, 513)),
    'fig_1_14d_dipole': (20, (351, 544, 547, 660)),
    'fig_1_15_flux_tilt': (21, (60, 95, 322, 312)),
    'fig_1_16_normal': (21, (72, 380, 193, 648)),
    'fig_1_17_dipole': (23, (74, 98, 260, 352)),
    'fig_1_19_dipole_uniform': (26, (400, 258, 540, 350)),
    'fig_1_20_dipole_nonuniform': (26, (350, 428, 535, 686)),
    'fig_1_21_densities': (27, (70, 205, 185, 470)),
    'fig_1_22_sphere_flux': (28, (424, 524, 540, 648)),
    'fig_1_23_cylinder': (29, (75, 100, 250, 158)),
    'fig_1_24_cube': (30, (148, 360, 352, 490)),
    'fig_1_25_cylinder_ex': (31, (268, 548, 458, 639)),
    'fig_1_27_sheet': (33, (72, 550, 292, 685)),
    'fig_1_28_shell': (34, (384, 344, 537, 575)),
    'fig_1_29_atom': (35, (312, 305, 424, 417)),
    'fig_1_30_tracks': (42, (114, 102, 335, 178)),
    'fig_1_31_square': (42, (121, 398, 345, 565)),
}, MEDIA, long_side=1000)

# ---------------------------------------------------------------- self-drawn figures
import math
from draw import Fig

# Infinite line charge with a cylindrical Gaussian surface (replaces cluttered Fig. 1.26)
f = Fig(620, 420)
cx, top, bot, rx, ry = 300, 110, 330, 110, 26
f.line(cx, 20, cx, 360, 'red', 5)
for y in range(40, 360, 40):
    f.text(cx - 20, y + 6, '+', 'red', 19, 'middle')
f.poly([(cx - rx, top), (cx - rx, bot)], 'blue', 2.4); f.poly([(cx + rx, top), (cx + rx, bot)], 'blue', 2.4)
f.raw(f'<ellipse cx="{cx}" cy="{top}" rx="{rx}" ry="{ry}" fill="#dbe7f7" fill-opacity="0.6" stroke="#1d5fd6" stroke-width="2.4"/>')
f.raw(f'<path d="M {cx - rx} {bot} A {rx} {ry} 0 0 0 {cx + rx} {bot}" fill="none" stroke="#1d5fd6" stroke-width="2.4"/>')
f.raw(f'<path d="M {cx - rx} {bot} A {rx} {ry} 0 0 1 {cx + rx} {bot}" fill="none" stroke="#1d5fd6" stroke-width="1.6" stroke-dasharray="6 5"/>')
for y in (170, 270):
    f.arrow(cx + rx, y, cx + rx + 90, y, 'green', 3, 13); f.arrow(cx - rx, y, cx - rx - 90, y, 'green', 3, 13)
f.text(cx + rx + 96, 176, 'E', 'green', 24, italic=True, bold=True)
f.line(cx, 220, cx + rx, 220, 'ink', 1.6, '5 4'); f.text(cx + rx / 2, 212, 'r', 'ink', 22, 'middle', italic=True)
f.arrow(cx + rx + 26, 225, cx + rx + 26, top, 'ink', 1.6, 9); f.arrow(cx + rx + 26, 225, cx + rx + 26, bot, 'ink', 1.6, 9)
f.text(cx + rx + 34, 300, 'l', 'ink', 22, italic=True)
f.text(cx + 12, 36, 'λ', 'red', 24, italic=True)
f.text(20, 60, 'flux only through', 'ink', 19); f.text(20, 84, 'the curved surface', 'ink', 19)
f.text(310, 395, 'E · 2πrl = λl / ε₀  ⇒  E = λ / 2πε₀r', 'ink', 21, 'middle', bold=True)
f.save(MEDIA, 'drawn_line_charge_gauss')

# E versus r for a uniformly charged thin spherical shell
f = Fig(620, 380)
ox, oy, R = 70, 310, 180
f.axes(ox, oy, 520, 270, 'r', 'E')
f.line(ox, oy, ox + R, oy, 'blue', 4)
f.line(ox + R, oy, ox + R, 70, 'grey', 1.4, '6 5')
f.curve(lambda r: 240 * (R / r) ** 2, R, 515, lambda r: ox + r, lambda e: oy - e, 'blue', 3.4)
f.text(ox + R, oy + 28, 'R', 'ink', 22, 'middle', italic=True)
f.text(ox + R / 2, oy - 14, 'E = 0 inside', 'blue', 19, 'middle')
f.text(ox + R + 30, 90, 'E = q / 4πε₀R² at the surface', 'ink', 19)
f.text(ox + R + 130, 170, 'E ∝ 1/r² outside', 'blue', 19)
f.save(MEDIA, 'drawn_shell_E_vs_r')
