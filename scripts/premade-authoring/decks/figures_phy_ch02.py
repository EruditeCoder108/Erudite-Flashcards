"""Crops the figures for Physics 11 Ch 2 (Motion in a Straight Line). Rects are (page, (x0, y0, x1, y1)) in PDF points.
Most graphs in this deck are self-drawn in phy_ch02.py (draw.py); only clear NCERT figures are cropped here."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph102.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch02-motion-in-a-straight-line', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'tab_2_1_limit': (1, (133, 572, 500, 692)),
    'fig_2_6_building': (6, (70, 80, 256, 318)),
    'tab_2_2_odd_numbers': (7, (105, 568, 520, 704)),
    'fig_2_8_ruler': (8, (342, 76, 470, 275)),
    'fig_2_9_children': (11, (245, 275, 392, 390)),
    'fig_2_10_impossible': (12, (305, 198, 508, 423)),
    'fig_2_11_xt': (12, (330, 470, 500, 590)),
    'fig_2_12_situations': (13, (110, 105, 522, 232)),
    'fig_2_13_shm': (13, (210, 295, 430, 405)),
    'fig_2_14_xt': (13, (388, 408, 505, 527)),
    'fig_2_15_speed': (13, (372, 550, 540, 660)),
}, MEDIA, long_side=1000)

# ---------------------------------------------------------------- self-drawn graphs (clean, standard notation)
from draw import Fig

def panel_axes(f, ox, oy, w, h, xl='t', yl='x', neg=0):
    f.axes(ox, oy, w, h, xl, yl, neg_y=neg)

# x-t graphs for a > 0, a < 0, a = 0
f = Fig(630, 270)
for i, (title, fn, col) in enumerate([('a > 0', lambda t: 0.9 * t * t, 'blue'),
                                      ('a < 0', lambda t: 3.6 * t - 0.9 * t * t, 'red'),
                                      ('a = 0', lambda t: 1.8 * t, 'green')]):
    ox, oy = 38 + i * 205, 215
    f.axes(ox, oy, 175, 185, 't', 'x')
    f.curve(fn, 0, 2, lambda t: ox + t * 72, lambda x: oy - x * 42, c=col, w=3.4)
    f.text(ox + 85, 258, title, col, 22, 'middle', bold=True)
f.save(MEDIA, 'drawn_xt_acceleration')

# v-t graphs, four cases of constant acceleration
f = Fig(620, 540)
cases = [('(a) v > 0, a > 0', (0.6, 1.6), None), ('(b) v > 0, a < 0', (1.6, 0.4), None),
         ('(c) v < 0, a < 0', (-0.4, -1.6), None), ('(d) a < 0, turns at t₁', (1.4, -1.2), 1.4 / 2.6)]
for i, (title, (v0, v1), tz) in enumerate(cases):
    ox, oy = 40 + (i % 2) * 310, 130 + (i // 2) * 270
    f.arrow(ox, oy, ox + 250, oy, 'ink', 1.8, 10); f.arrow(ox, oy + 90, ox, oy - 108, 'ink', 1.8, 10)
    f.text(ox + 248, oy + 26, 't', 'ink', 20, 'end', italic=True); f.text(ox - 8, oy - 94, 'v', 'ink', 20, 'end', italic=True)
    f.line(ox, oy - v0 * 58, ox + 215, oy - v1 * 58, 'blue', 3.4)
    if tz:
        f.circle(ox + 215 * tz, oy, 5, 'red', 'red'); f.text(ox + 215 * tz, oy + 28, 't₁', 'red', 20, 'middle', italic=True)
    f.text(ox + 120, oy + 122, title, 'ink', 20, 'middle')
f.save(MEDIA, 'drawn_vt_cases')

# area under v-t = displacement (uniform acceleration)
f = Fig(620, 420)
ox, oy = 70, 350
f.axes(ox, oy, 500, 310, 't', 'v')
x1, yv0, yv = ox + 400, oy - 110, oy - 270
f.poly([(ox, oy), (ox, yv0), (x1, yv0), (x1, oy)], 'grey', 1, fill='#dbe7f7', closed=True)
f.poly([(ox, yv0), (x1, yv), (x1, yv0)], 'grey', 1, fill='#f6dcb5', closed=True)
f.line(ox, yv0, x1, yv, 'blue', 3.4)
f.line(x1, oy, x1, yv, 'ink', 1.4, '5 4'); f.line(ox, yv, x1, yv, 'ink', 1.4, '5 4')
f.text(ox - 10, yv0 + 6, 'v₀', 'ink', 20, 'end', italic=True); f.text(ox - 10, yv + 6, 'v', 'ink', 20, 'end', italic=True)
f.text(x1, oy + 28, 't', 'ink', 20, 'middle', italic=True); f.text(ox - 6, oy + 26, 'O', 'ink', 18, 'end')
f.text(ox + 200, yv0 + 70, 'rectangle = v₀t', 'blue', 21, 'middle')
f.text(x1 - 90, yv0 - 25, '½(v − v₀)t = ½at²', '#a05a00', 20, 'middle')
f.text(ox + 250, 30, 'area = displacement:  x = v₀t + ½at²', 'ink', 21, 'middle', bold=True)
f.save(MEDIA, 'drawn_vt_area')

# free fall (upward positive): a-t, v-t, y-t
f = Fig(630, 300)
for i, (yl, title) in enumerate([('a', 'a = −g'), ('v', 'v = −gt'), ('y', 'y = −½gt²')]):
    ox, oy = 45 + i * 205, 70
    f.arrow(ox, oy, ox + 170, oy, 'ink', 1.8, 10); f.arrow(ox, oy + 175, ox, oy - 52, 'ink', 1.8, 10)
    f.text(ox + 168, oy - 10, 't', 'ink', 20, 'end', italic=True); f.text(ox - 8, oy - 36, yl, 'ink', 20, 'end', italic=True)
    if i == 0:
        f.line(ox, oy + 80, ox + 150, oy + 80, 'red', 3.4); f.text(ox - 6, oy + 87, '−g', 'red', 20, 'end', italic=True)
    elif i == 1:
        f.line(ox, oy, ox + 150, oy + 165, 'red', 3.4)
    else:
        f.curve(lambda t: t * t, 0, 1, lambda t: ox + t * 150, lambda y: oy + y * 165, 'red', 3.4)
    f.text(ox + 80, 285, title, 'ink', 21, 'middle', bold=True)
f.save(MEDIA, 'drawn_freefall_graphs')

# velocity = slope of the tangent: x = 0.08 t^3, chords shrinking to the tangent at t = 4 s
f = Fig(640, 480)
ox, oy = 70, 420
X = lambda t: ox + (t - 2) * 120; Y = lambda x: oy - x * 18
f.axes(ox, oy, 530, 380, 't (s)', 'x (m)')
for t in (2, 3, 4, 5, 6):
    f.line(X(t), oy, X(t), oy + 6, 'ink', 1.4); f.text(X(t), oy + 26, str(t), 'ink', 19, 'middle')
f.curve(lambda t: 0.08 * t ** 3, 2, 6.2, X, Y, 'blue', 3.2)
for (a, b), col in [((3, 5), 'orange'), ((3.5, 4.5), 'purple')]:
    xa, xb = 0.08 * a ** 3, 0.08 * b ** 3
    f.line(X(a), Y(xa), X(b), Y(xb), col, 2.2)
    f.circle(X(a), Y(xa), 4.5, col, col); f.circle(X(b), Y(xb), 4.5, col, col)
f.line(X(2.6), Y(5.12 + 3.84 * -1.4), X(5.6), Y(5.12 + 3.84 * 1.6), 'red', 2.6)
f.circle(X(4), Y(5.12), 6, 'red', 'red'); f.text(X(4) - 10, Y(5.12) - 12, 'P', 'red', 20, 'end', bold=True)
f.text(X(3) - 8, Y(0.08 * 27) - 12, 'P₁', 'orange', 17, 'end'); f.text(X(5) + 10, Y(10) + 4, 'P₂', 'orange', 17)
f.text(ox + 20, 40, 'chords P₁P₂ → tangent at P as Δt → 0', 'ink', 21)
f.text(ox + 20, 68, 'slope of tangent = v(4 s) = 3.84 m/s', 'red', 21)
f.save(MEDIA, 'drawn_tangent_velocity')
