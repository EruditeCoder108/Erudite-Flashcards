"""Drawn figures for Physics 11 Ch 4 (Laws of Motion).
The NCERT crops (fig_4_*.webp) were made for the pilot deck and are kept as they are; this script only
adds clean self-drawn diagrams for friction, lifts, pulleys, banking, impulse and connected bodies."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from draw import Fig

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch04-laws-of-motion', 'media')
os.makedirs(MEDIA, exist_ok=True)

# ---------------------------------------------------------------- friction vs applied force
f = Fig(620, 380)
ox, oy = 70, 320
f.axes(ox, oy, 520, 280, 'applied force F', 'f')
f.line(ox, oy, 300, oy - 200, 'blue', 3.4)
f.line(300, oy - 200, 312, oy - 150, 'red', 3.4)
f.line(312, oy - 150, 580, oy - 150, 'red', 3.4)
f.line(300, oy - 200, 300, oy, 'grey', 1.4, '6 5')
f.line(ox, oy - 200, 300, oy - 200, 'grey', 1.2, '4 5')
f.line(ox, oy - 150, 312, oy - 150, 'grey', 1.2, '4 5')
f.text(ox + 10, oy - 208, '(fₛ)ₘₐₓ = μₛN', 'blue', 19)
f.text(ox + 10, oy - 158, 'fₖ = μₖN', 'red', 19)
f.text(180, oy - 60, 'fₛ = F', 'blue', 21, 'middle', bold=True)
f.text(180, oy - 36, '(self-adjusting)', 'blue', 18, 'middle')
f.text(185, oy + 50, 'static: no motion', 'blue', 18, 'middle')
f.text(450, oy - 170, 'kinetic: sliding', 'red', 19, 'middle', bold=True)
f.text(450, oy - 120, 'nearly constant', 'red', 18, 'middle')
f.text(300, oy + 50, 'slips here', 'ink', 18, 'middle', italic=True)
f.text(310, 34, 'Friction as the push F grows', 'ink', 22, 'middle', bold=True)
f.save(MEDIA, 'drawn_friction_graph')

# ---------------------------------------------------------------- lift: apparent weight
f = Fig(640, 380)
f.rect(40, 40, 220, 300, 'ink', '#efe8d8', 2.4, 6)
f.line(150, 40, 150, 8, 'ink', 2)
f.rect(110, 170, 80, 110, 'ink', '#9cc3f0', 2, 6)
f.text(150, 232, 'm', 'ink', 26, 'middle', italic=True, bold=True)
f.arrow(150, 280, 150, 336, 'red', 3.4, 14)
f.arrow(150, 170, 150, 92, 'blue', 3.4, 14)
f.text(166, 112, 'N', 'blue', 24, italic=True, bold=True)
f.text(166, 326, 'mg', 'red', 24, italic=True, bold=True)
f.arrow(232, 250, 232, 170, 'green', 3, 13)
f.text(226, 162, 'a', 'green', 22, 'end', italic=True, bold=True)
f.text(300, 64, 'Scale reading = N (what the floor pushes)', 'ink', 19)
f.text(300, 120, 'a upward:', 'green', 20, bold=True); f.text(300, 148, 'N = m(g + a)  → feel heavier', 'ink', 20)
f.text(300, 196, 'a downward:', 'orange', 20, bold=True); f.text(300, 224, 'N = m(g − a)  → feel lighter', 'ink', 20)
f.text(300, 272, 'uniform velocity:', 'ink', 20, bold=True); f.text(300, 300, 'N = mg (either direction)', 'ink', 20)
f.text(300, 342, 'free fall (a = g):  N = 0', 'red', 20, bold=True)
f.save(MEDIA, 'drawn_lift')

# ---------------------------------------------------------------- Atwood machine
f = Fig(640, 430)
f.line(180, 20, 420, 20, 'ink', 3)
for x in range(190, 420, 22):
    f.line(x, 20, x - 12, 8, 'grey', 1.2)
f.line(300, 20, 300, 70, 'ink', 2)
f.circle(300, 90, 40, 'ink', '#efe8d8', 2.4); f.circle(300, 90, 4, 'ink', '#1f2430', 1)
f.line(260, 90, 260, 200, 'ink', 2); f.line(340, 90, 340, 280, 'ink', 2)
f.rect(225, 200, 70, 60, 'ink', '#9cc3f0', 2, 4); f.text(260, 238, 'm₁', 'ink', 22, 'middle', italic=True)
f.rect(300, 280, 80, 70, 'ink', '#f6dcb5', 2, 4); f.text(340, 322, 'm₂', 'ink', 22, 'middle', italic=True)
f.arrow(260, 200, 260, 140, 'blue', 3, 13); f.text(250, 158, 'T', 'blue', 22, 'end', italic=True, bold=True)
f.arrow(340, 280, 340, 220, 'blue', 3, 13); f.text(352, 238, 'T', 'blue', 22, italic=True, bold=True)
f.arrow(260, 260, 260, 330, 'red', 3, 13); f.text(250, 324, 'm₁g', 'red', 21, 'end', italic=True)
f.arrow(340, 350, 340, 415, 'red', 3, 13); f.text(352, 410, 'm₂g', 'red', 21, italic=True)
f.arrow(205, 260, 205, 205, 'green', 2.6, 12); f.text(198, 236, 'a', 'green', 21, 'end', italic=True, bold=True)
f.arrow(400, 290, 400, 345, 'green', 2.6, 12); f.text(408, 322, 'a', 'green', 21, italic=True, bold=True)
f.text(450, 150, '(m₂ > m₁)', 'ink', 19)
f.text(450, 210, 'a = (m₂ − m₁)g', 'ink', 21, bold=True); f.line(470, 218, 600, 218, 'ink', 1.4); f.text(535, 244, 'm₁ + m₂', 'ink', 21, 'middle')
f.text(450, 300, 'T = 2m₁m₂g', 'ink', 21, bold=True); f.line(470, 308, 580, 308, 'ink', 1.4); f.text(525, 334, 'm₁ + m₂', 'ink', 21, 'middle')
f.save(MEDIA, 'drawn_atwood')

# ---------------------------------------------------------------- banked road (cross-section)
f = Fig(640, 400)
x0, y0, x1, y1 = 40, 340, 580, 150
th = math.degrees(math.atan2(y0 - y1, x1 - x0))
f.poly([(x0, y0), (x1, y1), (x1, y0)], 'ink', 2.2, fill='#e6dcc8', closed=True)
ux, uy = (x1 - x0), (y1 - y0); L = math.hypot(ux, uy); ux, uy = ux / L, uy / L
nx, ny = uy, -ux                                   # outward normal (up-left)
px = 330; py = y0 + (px - x0) * uy / ux
cx, cy = px + nx * 26, py + ny * 26
f.raw(f'<rect x="{cx - 50:.1f}" y="{cy - 24:.1f}" width="100" height="48" rx="8" fill="#9cc3f0" stroke="#1f2430" stroke-width="2" transform="rotate({-th:.1f} {cx:.1f} {cy:.1f})"/>')
f.arrow(cx, cy, cx + nx * 150, cy + ny * 150, 'blue', 3.4, 15); f.text(cx + nx * 150 - 8, cy + ny * 150 - 6, 'N', 'blue', 24, 'end', italic=True, bold=True)
f.arrow(cx, cy, cx, cy + 120, 'red', 3.4, 15); f.text(cx + 12, cy + 118, 'mg', 'red', 23, italic=True, bold=True)
f.arrow(cx, cy, cx - ux * 105, cy - uy * 105, 'orange', 3.2, 14); f.text(cx - ux * 105 - 6, cy - uy * 105 + 24, 'f', 'orange', 23, 'end', italic=True, bold=True)
f.line(cx, cy, cx, cy - 150, 'grey', 1.3, '6 5')
f.arc(cx, cy, 70, 90, 90 + th, 'ink', 1.6); f.text(cx - 18, cy - 76, 'θ', 'ink', 21, 'middle', italic=True)
f.arc(x0, y0, 80, 0, th, 'ink', 1.6); f.text(x0 + 98, y0 - 12, 'θ', 'ink', 21, italic=True)
f.arrow(200, 42, 50, 42, 'green', 3, 13); f.text(125, 32, 'to the centre', 'green', 19, 'middle')
f.text(610, 40, 'N sin θ + f cos θ = mv²/R', 'ink', 19, 'end')
f.text(610, 68, 'N cos θ = mg + f sin θ', 'ink', 19, 'end')
f.text(610, 104, 'f = 0 at v₀ = √(Rg tan θ)', 'green', 19, 'end', bold=True)
f.text(330, 388, 'f drawn down the slope: the car tends to skid out (v > v₀)', 'orange', 17, 'middle')
f.save(MEDIA, 'drawn_banked_road')

# ---------------------------------------------------------------- impulse = area under F–t
f = Fig(620, 360)
ox, oy = 70, 300
f.axes(ox, oy, 520, 250, 't', 'F')
bell = lambda t: 210 * math.exp(-((t - 300) / 55) ** 2)
pts = [(t, oy - bell(t)) for t in range(170, 431, 3)]
f.poly([(170, oy)] + pts + [(430, oy)], 'none', 0, fill='#dbe7f7', closed=True)
f.poly(pts, 'blue', 3.2)
avg = 210 * 55 * math.sqrt(math.pi) / 200
f.rect(200, oy - avg, 200, avg, 'orange', 'none', 2.2)
f.text(410, oy - avg - 8, 'F_avg × Δt (same area)'.replace('F_avg', 'Fₐᵥ'), 'orange', 18)
f.text(300, oy - 40, 'area', 'blue', 20, 'middle', bold=True)
f.text(200, oy + 26, 't₁', 'ink', 19, 'middle', italic=True); f.text(400, oy + 26, 't₂', 'ink', 19, 'middle', italic=True)
f.text(330, 36, 'Impulse = ∫F dt = area = Δp', 'ink', 23, 'middle', bold=True)
f.save(MEDIA, 'drawn_impulse')

# ---------------------------------------------------------------- lawn mower: push vs pull
f = Fig(660, 320)
def mower(x, label, push):
    f.line(x - 20, 250, x + 240, 250, 'ink', 2)
    f.rect(x + 60, 200, 110, 40, 'ink', '#9cc3f0', 2, 6)
    f.circle(x + 78, 244, 9, 'ink', '#1f2430', 1); f.circle(x + 152, 244, 9, 'ink', '#1f2430', 1)
    a = math.radians(40)
    if push:                     # handle behind (left), force pushes down along it
        hx, hy = x + 60 - 95 * math.cos(a), 205 - 95 * math.sin(a)
        f.line(x + 60, 205, hx, hy, 'ink', 3)
        f.arrow(hx - 30 * math.cos(a), hy - 30 * math.sin(a), x + 55 - 10, 205 - 8, 'red', 3.4, 14)
        f.arrow(x + 115, 150, x + 115, 190, 'red', 2.4, 11); f.text(x + 125, 172, 'F sin θ', 'red', 18)
        f.text(x + 115, 292, 'N = mg + F sin θ', 'ink', 20, 'middle', bold=True)
    else:                        # handle in front (right), force pulls up along it
        hx, hy = x + 170 + 100 * math.cos(a), 205 - 100 * math.sin(a)
        f.line(x + 170, 205, hx, hy, 'ink', 3)
        f.arrow(hx, hy, hx + 50 * math.cos(a), hy - 50 * math.sin(a), 'red', 3.4, 14)
        f.arrow(x + 115, 190, x + 115, 150, 'red', 2.4, 11); f.text(x + 125, 160, 'F sin θ', 'red', 18)
        f.text(x + 115, 292, 'N = mg − F sin θ', 'ink', 20, 'middle', bold=True)
    f.text(x + 115, 40, label, 'ink', 22, 'middle', bold=True)
mower(40, 'Push: pressed down', True)
mower(350, 'Pull: lifted up', False)
f.line(330, 30, 330, 300, 'light', 1.6)
f.save(MEDIA, 'drawn_mower')

# ---------------------------------------------------------------- two blocks joined by a string
f = Fig(640, 250)
f.line(20, 180, 620, 180, 'ink', 2)
f.rect(80, 110, 110, 70, 'ink', '#9cc3f0', 2, 4); f.text(135, 152, '10 kg', 'ink', 21, 'middle', bold=True)
f.rect(330, 90, 150, 90, 'ink', '#f6dcb5', 2, 4); f.text(405, 142, '20 kg', 'ink', 21, 'middle', bold=True)
f.line(190, 145, 330, 145, 'ink', 2)
f.arrow(190, 145, 240, 145, 'blue', 3, 12); f.text(215, 132, 'T', 'blue', 21, 'middle', italic=True, bold=True)
f.arrow(330, 145, 280, 145, 'blue', 3, 12); f.text(305, 132, 'T', 'blue', 21, 'middle', italic=True, bold=True)
f.arrow(480, 135, 590, 135, 'red', 3.4, 14); f.text(535, 122, 'F = 600 N', 'red', 20, 'middle', bold=True)
f.text(320, 36, 'Pull the 20 kg: a = F/(total) = 20 m/s²', 'ink', 20, 'middle')
f.text(320, 64, 'T moves only the 10 kg behind it: T = 10 × 20 = 200 N', 'ink', 20, 'middle', bold=True)
f.text(320, 224, 'Pull the 10 kg instead: T = 20 × 20 = 400 N', 'grey', 19, 'middle')
f.save(MEDIA, 'drawn_connected_blocks')

print('drawn figures saved')
