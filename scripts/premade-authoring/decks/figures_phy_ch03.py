"""Crops the figures for Physics 11 Ch 3 (Motion in a Plane). Rects are (page, (x0, y0, x1, y1)) in PDF points.
Key diagrams (vector addition, components, projectile, circular motion, river) are also self-drawn below with draw.py."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export
from draw import Fig

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph103.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch03-motion-in-a-plane', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_3_1_position_paths': (1, (334, 185, 552, 290)),
    'fig_3_2_equal_vectors': (2, (55, 80, 265, 195)),
    'fig_3_3_scalar_multiple': (2, (55, 545, 280, 648)),
    'fig_3_4_addition_laws': (2, (290, 383, 520, 648)),
    'fig_3_5_subtraction': (3, (120, 498, 522, 682)),
    'fig_3_6_parallelogram': (4, (50, 100, 510, 222)),
    'fig_3_10_resultant': (7, (110, 80, 280, 186)),
    'fig_3_11_boat': (7, (338, 250, 548, 458)),
    'fig_3_12_position_velocity': (8, (70, 198, 250, 512)),
    'fig_3_17_projectile': (12, (306, 145, 496, 318)),
    'fig_3_19_skaters': (20, (360, 136, 492, 292)),
    'fig_3_20_cyclist': (20, (212, 390, 355, 532)),
}, MEDIA, long_side=1000)

# ---------------------------------------------------------------- self-drawn figures
# Components of a vector
f = Fig(560, 420)
ox, oy, A, th = 80, 360, 380, math.radians(35)
ex, ey = ox + A * math.cos(th), oy - A * math.sin(th)
f.axes(ox, oy, 440, 330, 'x', 'y')
f.line(ex, ey, ex, oy, 'grey', 1.6, '6 5'); f.line(ex, ey, ox, ey, 'grey', 1.6, '6 5')
f.arrow(ox, oy, ex, oy, 'red', 3.4, 14); f.arrow(ox, oy, ox, ey, 'green', 3.4, 14)
f.arrow(ox, oy, ex, ey, 'blue', 3.8, 16)
f.arc(ox, oy, 70, 0, 35, 'ink', 1.8); f.text(ox + 78, oy - 16, 'θ', 'ink', 22, italic=True)
f.text(ex - 150, ey + 60, 'A', 'blue', 26, bold=True, italic=True)
f.text((ox + ex) / 2, oy + 34, 'Aₓ = A cos θ', 'red', 22, 'middle')
f.text(ox + 12, (oy + ey) / 2, 'Aᵧ = A sin θ', 'green', 20)
f.text(300, 36, 'A = √(Aₓ² + Aᵧ²),  tan θ = Aᵧ / Aₓ', 'ink', 21, 'middle')
f.save(MEDIA, 'drawn_components')

# Resultant of two vectors at angle θ (parallelogram law)
f = Fig(620, 380)
ox, oy, A, B, th = 60, 320, 300, 200, math.radians(50)
P = (ox + A, oy); Q = (ox + B * math.cos(th), oy - B * math.sin(th)); S = (P[0] + Q[0] - ox, Q[1])
f.line(Q[0], Q[1], S[0], S[1], 'grey', 1.6, '6 5'); f.line(P[0], P[1], S[0], S[1], 'grey', 1.6, '6 5')
f.arrow(ox, oy, P[0], P[1], 'red', 3.4, 14); f.arrow(ox, oy, Q[0], Q[1], 'green', 3.4, 14); f.arrow(ox, oy, S[0], S[1], 'blue', 3.8, 16)
f.arc(ox, oy, 62, 0, 50, 'ink', 1.6); f.text(ox + 40, oy - 58, 'θ', 'ink', 21, italic=True)
al = math.degrees(math.atan2(oy - S[1], S[0] - ox))
f.arc(ox, oy, 110, 0, al, 'blue', 1.6); f.text(ox + 118, oy - 12, 'α', 'blue', 21, italic=True)
f.text(ox + A / 2, oy + 32, 'A', 'red', 24, 'middle', italic=True, bold=True)
f.text((ox + Q[0]) / 2 - 18, (oy + Q[1]) / 2, 'B', 'green', 24, 'end', italic=True, bold=True)
f.text((ox + S[0]) / 2 + 20, (oy + S[1]) / 2 - 10, 'R', 'blue', 26, italic=True, bold=True)
f.text(310, 40, 'R² = A² + B² + 2AB cos θ', 'ink', 22, 'middle')
f.text(310, 70, 'tan α = B sin θ / (A + B cos θ)', 'ink', 22, 'middle')
f.save(MEDIA, 'drawn_resultant')

# Projectile: path, components at launch, top and landing
f = Fig(640, 420)
ox, oy, th, R = 50, 330, math.radians(55), 480
H = R * math.tan(th) / 4
Y = lambda x: oy - (x * math.tan(th) - x * x * math.tan(th) / R)
f.line(ox - 10, oy, ox + R + 90, oy, 'ink', 1.8)
f.poly([(ox + R * i / 120, Y(R * i / 120)) for i in range(121)], 'blue', 3.2)
vx, vy = 90, 90 * math.tan(th)
f.arrow(ox, oy, ox + vx, oy - vy, 'ink', 3, 14); f.arrow(ox, oy, ox + vx, oy, 'red', 2.6, 12); f.arrow(ox, oy, ox, oy - vy, 'green', 2.6, 12)
f.text(ox + vx + 6, oy - vy - 6, 'u', 'ink', 22, italic=True, bold=True)
f.arc(ox, oy, 36, 0, 55, 'ink', 1.4); f.text(ox + 40, oy - 10, 'θ', 'ink', 19, italic=True)
tx, ty = ox + R / 2, oy - H
f.arrow(tx, ty, tx + vx, ty, 'red', 2.6, 12); f.text(tx + vx + 6, ty + 6, 'u cos θ', 'red', 19)
f.text(tx, ty - 14, 'top: vᵧ = 0', 'green', 19, 'middle')
f.line(tx, ty, tx, oy, 'grey', 1.4, '5 5'); f.text(tx + 8, oy - H / 2, 'H', 'ink', 22, italic=True)
lx, k = ox + R, 0.62
f.arrow(lx, oy, lx + vx * k, oy, 'red', 2.4, 11); f.arrow(lx, oy, lx, oy + vy * k, 'green', 2.4, 11)
f.arrow(lx, oy, lx + vx * k, oy + vy * k, 'ink', 2.6, 12)
f.text(lx - 10, oy + vy * k - 4, 'lands at θ below', 'ink', 17, 'end')
f.text(ox + R * 0.3, oy + 28, '← range R →', 'ink', 20, 'middle')
f.text(320, 34, 'vₓ = u cos θ stays constant;  vᵧ = u sin θ − gt', 'ink', 20, 'middle')
f.save(MEDIA, 'drawn_projectile')

# Rain and umbrella (Example 3.1): wind towards west, rain down
f = Fig(560, 430)
cx, cy = 320, 80
f.arrow(cx, cy, cx, cy + 280, 'blue', 3.4, 14); f.text(cx + 12, cy + 150, 'vᵣ = 35 m/s', 'blue', 20)
f.arrow(cx, cy + 280, cx - 96, cy + 280, 'green', 3.4, 14); f.text(cx - 48, cy + 312, 'wind 12 m/s (to west)', 'green', 18, 'middle')
f.arrow(cx, cy, cx - 96, cy + 280, 'red', 3.6, 15); f.text(cx - 64, cy + 150, 'R = 37 m/s', 'red', 20, 'end')
f.arc(cx, cy, 70, 270, 251, 'ink', 1.6); f.text(cx - 20, cy + 96, 'θ', 'ink', 20, italic=True)
f.text(30, 40, 'W', 'ink', 20); f.text(515, 40, 'E', 'ink', 20)
f.arrow(110, 34, 56, 34, 'ink', 1.6, 9); f.arrow(450, 34, 505, 34, 'ink', 1.6, 9)
f.text(280, 414, 'tan θ = 12/35 → θ ≈ 19°: tilt the umbrella towards the east', 'ink', 17, 'middle')
f.save(MEDIA, 'drawn_rain_umbrella')

# River crossing: least time vs shortest path
f = Fig(640, 400)
for k, title in enumerate(['least time: head straight across', 'shortest path: head upstream']):
    ox = 20 + k * 320
    f.rect(ox, 70, 290, 230, 'grey', '#e3eef8', 1)
    f.line(ox, 70, ox + 290, 70, 'ink', 2); f.line(ox, 300, ox + 290, 300, 'ink', 2)
    for yy in (130, 190, 250):
        f.arrow(ox + 200, yy, ox + 270, yy, 'grey', 1.6, 9)
    f.text(ox + 235, 280, 'vᵣ', 'grey', 18, 'middle')
    bx = ox + 70
    if k == 0:
        f.arrow(bx, 300, bx, 180, 'blue', 3, 13); f.text(bx - 8, 230, 'vʙ', 'blue', 19, 'end')
        f.arrow(bx, 300, bx + 110, 70, 'red', 3.2, 14); f.text(bx + 64, 150, 'actual path', 'red', 17)
        f.text(ox + 145, 330, 't = d / vʙ,  drift = vᵣd / vʙ', 'ink', 17, 'middle')
    else:
        f.arrow(bx + 60, 300, bx, 186, 'blue', 3, 13); f.text(bx - 6, 250, 'vʙ', 'blue', 19, 'end')
        f.arrow(bx + 60, 300, bx + 60, 70, 'red', 3.2, 14); f.text(bx + 70, 150, 'straight across', 'red', 17)
        f.text(ox + 145, 330, 'sin θ = vᵣ / vʙ (needs vʙ > vᵣ)', 'ink', 17, 'middle')
    f.text(ox + 145, 40, title, 'ink', 18, 'middle', bold=True)
f.text(320, 380, 'd = river width, vᵣ = river speed, vʙ = boat speed in still water', 'ink', 16, 'middle')
f.save(MEDIA, 'drawn_river')

# Uniform circular motion: v tangent, a towards centre
f = Fig(480, 440)
cx, cy, r = 240, 240, 150
f.circle(cx, cy, r, 'grey', 'none', 2); f.circle(cx, cy, 4, 'ink', 'ink'); f.text(cx + 8, cy + 22, 'O', 'ink', 18)
for ang in (20, 140, 250):
    a = math.radians(ang); px, py = cx + r * math.cos(a), cy - r * math.sin(a)
    tx, ty = -math.sin(a), -math.cos(a)
    f.arrow(px, py, px + 80 * tx, py + 80 * ty, 'blue', 3, 13)
    f.arrow(px, py, px + 70 * (cx - px) / r, py + 70 * (cy - py) / r, 'red', 3, 13)
    f.circle(px, py, 7, 'ink', '#ffd166', 1.5)
f.text(20, 32, 'v: along the tangent', 'blue', 20); f.text(20, 58, 'a = v²/R: towards the centre', 'red', 20)
f.save(MEDIA, 'drawn_circular')
