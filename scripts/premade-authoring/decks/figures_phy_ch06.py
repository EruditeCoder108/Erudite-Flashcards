"""Crops the figures for Physics 11 Ch 6 (Systems of Particles and Rotational Motion). Rects are (page, (x0, y0, x1, y1)) in PDF points.
Torque lever arm, rolling velocities and the axis theorems are self-drawn below with draw.py."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export
from draw import Fig

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph106.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch06-systems-of-particles-and-rotational-motion', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_6_1_sliding': (1, (90, 80, 242, 182)),
    'fig_6_2_rolling': (1, (88, 478, 240, 584)),
    'fig_6_4_fixed_axis': (2, (45, 82, 318, 345)),
    'fig_6_5a_top': (2, (330, 66, 562, 200)),
    'fig_6_9_triangle': (5, (322, 553, 508, 691)),
    'fig_6_10_lamina': (6, (86, 478, 308, 592)),
    'fig_6_11_l_lamina': (6, (328, 360, 550, 527)),
    'fig_6_12_explosion': (8, (86, 228, 310, 356)),
    'fig_6_13_decay': (9, (44, 224, 222, 332)),
    'fig_6_14_binary': (9, (294, 80, 522, 173)),
    'fig_6_15_screw_rule': (10, (94, 430, 292, 608)),
    'fig_6_17a_omega': (12, (325, 148, 556, 256)),
    'fig_6_17b_v_omega_r': (12, (355, 340, 542, 514)),
    'fig_6_18_torque': (14, (88, 80, 306, 311)),
    'fig_6_19_const_velocity': (17, (64, 140, 257, 258)),
    'fig_6_20a_parallel_forces': (18, (88, 500, 309, 573)),
    'fig_6_20b_couple': (18, (338, 85, 553, 170)),
    'fig_6_21a_lid': (18, (336, 560, 537, 682)),
    'fig_6_21b_compass': (19, (70, 84, 248, 233)),
    'fig_6_23_lever': (19, (298, 168, 523, 250)),
    'fig_6_24_balance': (20, (108, 465, 277, 652)),
    'fig_6_25_suspension': (20, (334, 398, 546, 656)),
    'fig_6_26_bar': (21, (44, 500, 277, 582)),
    'fig_6_27_ladder': (21, (364, 512, 446, 692)),
    'fig_6_28_dumbbell': (23, (64, 218, 267, 350)),
    'tab_6_1_moment_of_inertia': (24, (83, 80, 557, 615)),
    'tab_6_2_linear_vs_rotational': (27, (100, 80, 478, 271)),
    'fig_6_31_flywheel': (28, (397, 104, 519, 285)),
    'fig_6_32a_swivel': (30, (108, 484, 286, 652)),
    'fig_6_32b_acrobat': (30, (370, 455, 516, 662)),
    'fig_6_33_bar_strings': (33, (178, 480, 398, 642)),
}, MEDIA, long_side=1000)

# ---------------------------------------------------------------- self-drawn figures
# Torque: lever arm r⊥ = r sin θ
f = Fig(620, 430)
O = (80, 190); P = (400, 190); th = math.radians(50); u = (math.cos(th), -math.sin(th))
f.circle(*O, 7, 'ink', 'ink'); f.text(O[0] - 10, O[1] - 18, 'O (axis)', 'ink', 18)
f.line(*O, *P, 'blue', 3.4); f.text(240, 180, 'r', 'blue', 24, 'middle', italic=True, bold=True)
f.circle(*P, 6, 'ink', 'ink'); f.text(P[0] + 4, P[1] + 26, 'P', 'ink', 18)
f.arrow(*P, P[0] + 110 * u[0], P[1] + 110 * u[1], 'red', 3.6, 16); f.text(P[0] + 110 * u[0] + 10, P[1] + 110 * u[1] + 6, 'F', 'red', 26, italic=True, bold=True)
f.line(P[0], P[1], P[0] + 90, P[1], 'grey', 1.4, '5 5'); f.arc(*P, 46, 0, 50, 'ink', 1.6); f.text(P[0] + 52, P[1] - 14, 'θ', 'ink', 21, italic=True)
t = (O[0] - P[0]) * u[0] + (O[1] - P[1]) * u[1]; Q = (P[0] + t * u[0], P[1] + t * u[1])
f.line(*P, Q[0] - 20 * u[0], Q[1] - 20 * u[1], 'red', 1.6, '7 6'); f.text(Q[0] + 60, Q[1] + 6, 'line of action', 'red', 16)
f.line(*O, *Q, 'green', 3.2); f.text((O[0] + Q[0]) / 2 - 12, (O[1] + Q[1]) / 2 + 8, 'r⊥ = r sin θ', 'green', 21, 'end')
f.text(310, 40, 'τ = r × F,   |τ| = rF sin θ = r⊥ F', 'ink', 23, 'middle', bold=True)
f.text(310, 70, 'lever arm r⊥: perpendicular distance from O to the line of action', 'ink', 16, 'middle')
f.save(MEDIA, 'drawn_torque_lever_arm')

# Rolling without slipping: velocities of points
f = Fig(600, 400)
cx, cy, R = 230, 220, 120
f.line(40, cy + R, 560, cy + R, 'ink', 2.4)
f.circle(cx, cy, R, 'ink', '#e3eef8', 2.4); f.circle(cx, cy, 5, 'ink', 'ink')
f.arrow(cx, cy - R, cx + 200, cy - R, 'red', 3.6, 15); f.text(cx + 208, cy - R + 7, '2v', 'red', 24, bold=True)
f.arrow(cx, cy, cx + 100, cy, 'blue', 3.4, 14); f.text(cx + 108, cy + 7, 'v', 'blue', 24, italic=True, bold=True)
f.circle(cx, cy + R, 7, 'green', 'green'); f.text(cx + 16, cy + R + 28, '0 (contact point at rest)', 'green', 18)
a = math.radians(45); px, py = cx + R * math.cos(a), cy - R * math.sin(a)
# velocity at P = v x̂ + ω × r : perpendicular to line from contact point, magnitude ∝ distance from contact
dx, dy = px - cx, py - (cy + R); dist = math.hypot(dx, dy)
vx, vy = -dy * 100 / R, dx * 100 / R          # v = ω × (P − contact): (dx, dy) → (−dy, dx)
f.line(cx, cy + R, px, py, 'purple', 1.4, '5 5')
f.arrow(px, py, px + vx, py + vy, 'purple', 3, 13); f.circle(px, py, 6, 'purple', 'purple')
f.text(px + vx + 8, py + vy + 4, '√2 v', 'purple', 20)
f.text(40, 40, 'rolling without slipping: v = Rω', 'ink', 22, bold=True)
f.text(40, 68, 'each point moves ⟂ to its line from the contact point', 'purple', 17)
f.save(MEDIA, 'drawn_rolling_velocities')

# Parallel and perpendicular axis theorems
f = Fig(640, 360)
# parallel axis: rod with CM axis and parallel axis at distance d
ox = 60
f.rect(ox, 160, 240, 22, 'ink', '#dbe7f7', 2, 4)
f.line(ox + 120, 60, ox + 120, 280, 'blue', 2.2, '8 6'); f.text(ox + 120, 50, 'axis through CM', 'blue', 17, 'middle')
f.line(ox + 20, 90, ox + 20, 280, 'red', 2.2, '8 6'); f.text(ox + 20, 80, 'parallel axis', 'red', 17, 'middle')
f.arrow(ox + 24, 240, ox + 116, 240, 'ink', 1.6, 9); f.arrow(ox + 116, 240, ox + 24, 240, 'ink', 1.6, 9); f.text(ox + 70, 262, 'd', 'ink', 20, 'middle', italic=True)
f.text(ox + 120, 320, 'I = I_cm + Md²'.replace('I_cm', 'I꜀ₘ'), 'ink', 22, 'middle', bold=True)
# perpendicular axis: lamina in xy plane
cx, cy = 470, 200
f.poly([(cx - 110, cy + 30), (cx + 50, cy + 60), (cx + 110, cy - 20), (cx - 50, cy - 50)], 'ink', 2, fill='#f6dcb5', closed=True)
f.arrow(cx, cy, cx + 140, cy + 30, 'ink', 1.8, 10); f.text(cx + 146, cy + 38, 'x', 'ink', 18, italic=True)
f.arrow(cx, cy, cx - 120, cy + 40, 'ink', 1.8, 10); f.text(cx - 132, cy + 52, 'y', 'ink', 18, italic=True)
f.arrow(cx, cy, cx, cy - 150, 'ink', 1.8, 10); f.text(cx + 10, cy - 146, 'z', 'ink', 18, italic=True)
f.text(cx, 320, 'I_z = I_x + I_y'.replace('I_z', 'I𝓏').replace('I_x', 'Iₓ').replace('I_y', 'Iᵧ'), 'ink', 22, 'middle', bold=True)
f.text(cx, 345, '(plane lamina only)', 'ink', 16, 'middle')
f.save(MEDIA, 'drawn_axis_theorems')
