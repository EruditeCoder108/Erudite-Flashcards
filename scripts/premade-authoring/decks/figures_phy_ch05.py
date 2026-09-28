"""Crops the figures for Physics 11 Ch 5 (Work, Energy and Power). Rects are (page, (x0, y0, x1, y1)) in PDF points.
Cluttered NCERT figures (5.3, 5.4, 5.6, 5.7, 5.8) are redrawn cleanly below with draw.py."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export
from draw import Fig

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph105.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch05-work-energy-and-power', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'tab_5_1_energy_units': (3, (340, 95, 550, 165)),
    'tab_5_2_kinetic_energies': (4, (125, 95, 440, 208)),
    'fig_5_9_car_spring': (11, (330, 80, 552, 184)),
    'fig_5_10_collision_2d': (12, (295, 539, 522, 640)),
    'fig_5_11_pe_functions': (17, (320, 180, 528, 688)),
    'fig_5_13_man_load': (18, (268, 205, 485, 302)),
    'fig_5_14_ball_bearings': (19, (150, 520, 432, 668)),
    'fig_5_15_pendulum_bobs': (20, (340, 85, 490, 212)),
}, MEDIA, long_side=1000)

# ---------------------------------------------------------------- self-drawn figures
# Work by a force at angle θ to the displacement
f = Fig(600, 320)
f.line(20, 250, 580, 250, 'ink', 2.4)
for x in range(30, 580, 24):
    f.line(x, 250, x - 12, 264, 'grey', 1.2)
f.rect(120, 180, 90, 70, 'ink', '#9cc3f0', 2, 4)
f.rect(430, 180, 90, 70, 'grey', 'none', 1.6, 4)
f.arrow(165, 215, 165 + 150 * math.cos(math.radians(35)), 215 - 150 * math.sin(math.radians(35)), 'red', 3.6, 16)
f.line(165, 215, 330, 215, 'grey', 1.4, '6 5')
f.arc(165, 215, 60, 0, 35, 'ink', 1.6); f.text(232, 206, 'θ', 'ink', 21, italic=True)
f.text(300, 110, 'F', 'red', 26, italic=True, bold=True)
f.arrow(165, 295, 475, 295, 'blue', 2.8, 13); f.text(320, 288, 'd', 'blue', 24, 'middle', italic=True, bold=True)
f.text(300, 44, 'W = F d cos θ = F · d', 'ink', 24, 'middle', bold=True)
f.text(300, 74, 'only the component F cos θ along d does work', 'ink', 19, 'middle')
f.save(MEDIA, 'drawn_work_angle')

# Work by a variable force = area under F–x
f = Fig(600, 400)
ox, oy = 60, 330
f.axes(ox, oy, 510, 290, 'x', 'F(x)')
Fx = lambda x: 150 + 90 * math.sin((x - 60) / 95) + 0.12 * (x - 60)
xi, xf = 120, 480
pts = [(xi, oy)] + [(x, oy - Fx(x)) for x in range(xi, xf + 1, 4)] + [(xf, oy)]
f.poly(pts, 'none', 0, fill='#dbe7f7', closed=True)
for x in range(xi, xf, 30):
    f.rect(x, oy - Fx(x), 30, Fx(x), 'grey', 'none', 1)
f.rect(300, oy - Fx(300), 30, Fx(300), 'orange', '#f6dcb5', 2)
f.curve(Fx, 70, 520, lambda x: x, lambda y: oy - y, 'blue', 3.2)
f.text(xi, oy + 26, 'xᵢ', 'ink', 20, 'middle', italic=True); f.text(xf, oy + 26, 'x_f'.replace('x_f', 'x𝒻'), 'ink', 20, 'middle', italic=True)
f.text(315, oy + 26, 'Δx', 'orange', 18, 'middle')
f.text(330, 36, 'W = ∫ F(x) dx = area under the F–x curve', 'ink', 21, 'middle', bold=True)
f.text(330, 64, 'strip: ΔW ≈ F(x) Δx', 'orange', 19, 'middle')
f.save(MEDIA, 'drawn_variable_force')

# Example 5.5: woman pushing a trunk; friction −50 N
f = Fig(600, 400)
ox, oy, sx, sy = 70, 250, 24, 1.8
f.arrow(ox, oy, ox + 530, oy, 'ink', 1.8, 10); f.arrow(ox, oy + 140, ox, 30, 'ink', 1.8, 10)
f.text(ox + 526, oy - 12, 'x (m)', 'ink', 18, 'end', italic=True); f.text(ox - 8, 44, 'F (N)', 'ink', 18, 'end', italic=True)
f.poly([(ox, oy), (ox, oy - 100 * sy), (ox + 10 * sx, oy - 100 * sy), (ox + 20 * sx, oy - 50 * sy), (ox + 20 * sx, oy)], 'none', 0, fill='#dbe7f7', closed=True)
f.poly([(ox, oy - 100 * sy), (ox + 10 * sx, oy - 100 * sy), (ox + 20 * sx, oy - 50 * sy)], 'blue', 3.2)
f.poly([(ox, oy), (ox, oy + 50 * sy), (ox + 20 * sx, oy + 50 * sy), (ox + 20 * sx, oy)], 'none', 0, fill='#f6d4d4', closed=True)
f.line(ox, oy + 50 * sy, ox + 20 * sx, oy + 50 * sy, 'red', 3.2)
for v in (100, 50, -50):
    f.text(ox - 8, oy - v * sy + 6, str(v), 'ink', 17, 'end')
for x in (10, 20):
    f.text(ox + x * sx, oy + 22, str(x), 'ink', 17, 'middle')
f.text(ox + 120, oy - 60, 'W_F = 1000 + 750 = 1750 J'.replace('W_F', 'W'), 'blue', 20, 'middle')
f.text(ox + 240, oy + 60, 'friction: W = −50 × 20 = −1000 J', 'red', 20, 'middle')
f.text(ox + 360, oy - 170, 'applied F', 'blue', 19)
f.save(MEDIA, 'drawn_ex_5_5')

# Spring: Fs vs x (area = work) and V, K parabolas
f = Fig(640, 340)
ox, oy = 150, 170
f.arrow(ox - 130, oy, ox + 140, oy, 'ink', 1.8, 10); f.arrow(ox, oy + 140, ox, oy - 150, 'ink', 1.8, 10)
f.text(ox + 136, oy + 24, 'x', 'ink', 19, 'end', italic=True); f.text(ox - 8, oy - 132, 'F', 'ink', 19, 'end', italic=True, sub='s')
xm = 100
f.poly([(ox, oy), (ox + xm, oy), (ox + xm, oy + xm)], 'none', 0, fill='#f6d4d4', closed=True)
f.line(ox - 110, oy - 110, ox + 120, oy + 120, 'red', 3.2)
f.text(ox + xm, oy - 10, 'xₘ', 'ink', 18, 'middle', italic=True)
f.text(ox + 50, oy + 130, 'area = −½kxₘ²', 'red', 18, 'middle')
f.text(ox - 60, oy - 120, 'Fₛ = −kx', 'red', 20, 'middle')
ox2, oy2 = 470, 280
f.arrow(ox2 - 150, oy2, ox2 + 150, oy2, 'ink', 1.8, 10); f.arrow(ox2, oy2 + 8, ox2, 40, 'ink', 1.8, 10)
f.text(ox2 + 146, oy2 + 24, 'x', 'ink', 19, 'end', italic=True)
E = 200; X = lambda x: ox2 + x * 120
f.line(X(-1.1), oy2 - E, X(1.1), oy2 - E, 'ink', 2, '7 5'); f.text(X(1.1), oy2 - E - 10, 'E = K + V', 'ink', 18, 'end')
f.curve(lambda x: x * x, -1, 1, X, lambda v: oy2 - E * v, 'blue', 3)
f.curve(lambda x: 1 - x * x, -1, 1, X, lambda v: oy2 - E * v, 'green', 3)
f.text(X(-1), oy2 + 24, '−xₘ', 'ink', 17, 'middle'); f.text(X(1), oy2 + 24, 'xₘ', 'ink', 17, 'middle')
f.text(X(0.7), oy2 - 150, 'V = ½kx²', 'blue', 18); f.text(X(-0.2), oy2 - 214, 'K', 'green', 20, 'end', italic=True)
f.save(MEDIA, 'drawn_spring')

# Example 5.7: bob in a vertical circle, just completing it
f = Fig(480, 480)
cx, cy, r = 240, 250, 170
f.circle(cx, cy, r, 'grey', 'none', 1.8)
f.circle(cx, cy, 5, 'ink', 'ink')
for (px, py, lab, v) in [(cx, cy + r, 'A', 'v₀ = √(5gL)'), (cx + r, cy, 'B', 'v = √(3gL)'), (cx, cy - r, 'C', 'v = √(gL)')]:
    f.line(cx, cy, px, py, 'ink', 1.6)
    f.circle(px, py, 11, 'ink', '#ffd166', 1.8)
f.arrow(cx, cy + r, cx + 110, cy + r, 'blue', 3, 13); f.text(cx + 118, cy + r + 6, 'v₀ = √(5gL)', 'blue', 20)
f.arrow(cx + r, cy, cx + r, cy - 90, 'blue', 3, 13); f.text(cx + r - 12, cy - 60, '√(3gL)', 'blue', 20, 'end')
f.arrow(cx, cy - r, cx - 90, cy - r, 'blue', 3, 13); f.text(cx - 96, cy - r - 16, '√(gL)', 'blue', 20, 'end')
f.text(cx + 12, cy + r + 36, 'A', 'ink', 22, bold=True); f.text(cx + r + 14, cy + 26, 'B', 'ink', 22, bold=True)
f.text(cx + 16, cy - r - 12, 'C  (T = 0 here)', 'ink', 20, bold=True)
f.text(cx + 60, cy - 10, 'L', 'ink', 20, italic=True)
f.save(MEDIA, 'drawn_vertical_circle')
