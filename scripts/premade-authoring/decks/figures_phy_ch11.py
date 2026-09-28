"""Crops the figures for Physics 11 Ch 11 (Thermodynamics). Rects are (page, (x0, y0, x1, y1)) in PDF points.
A P-V comparison of processes and an engine/refrigerator schematic are self-drawn below."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from figcrop import export
from draw import Fig

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PDF = os.path.join(ROOT, 'NCERT-pdfs', 'phy11', 'keph204.pdf')
MEDIA = os.path.join(ROOT, 'premade-cards', '11th', 'Physics', 'class11-physics-ch11-thermodynamics', 'media')
os.makedirs(MEDIA, exist_ok=True)

export(PDF, {
    'fig_11_1_walls': (1, (312, 193, 490, 422)),
    'fig_11_2_zeroth_law': (2, (362, 318, 525, 576)),
    'fig_11_3_internal_energy': (3, (304, 165, 512, 236)),
    'fig_11_4_heat_work': (3, (350, 366, 498, 590)),
    'tab_11_1_solids_heat': (5, (290, 537, 523, 680)),
    'fig_11_5_water_specific_heat': (6, (106, 246, 290, 355)),
    'fig_11_6_non_equilibrium': (7, (90, 208, 232, 358)),
    'fig_11_7_quasi_static': (8, (84, 366, 306, 531)),
    'tab_11_2_processes': (8, (328, 275, 553, 415)),
    'fig_11_8_isotherm_adiabat': (9, (92, 530, 244, 683)),
    'fig_11_9_carnot': (11, (311, 454, 504, 613)),
    'fig_11_10_engine_refrigerator': (13, (50, 240, 270, 380)),
    'fig_11_11_ex_pv': (17, (214, 112, 374, 276)),
}, MEDIA, long_side=1000)

# ---------------------------------------------------------------- self-drawn: four processes from one state
f = Fig(620, 440)
ox, oy = 70, 380
f.axes(ox, oy, 520, 340, 'V', 'P')
P0, V0 = 200, 150                      # start point (pixels relative to origin)
X = lambda v: ox + v; Y = lambda p: oy - p
f.circle(X(V0), Y(P0), 6, 'ink', 'ink'); f.text(X(V0) - 10, Y(P0) - 10, 'A', 'ink', 20, 'end', bold=True)
f.arrow(X(V0), Y(P0), X(V0 + 260), Y(P0), 'blue', 3, 13); f.text(X(V0 + 250), Y(P0) - 10, 'isobaric', 'blue', 19, 'end')
f.arrow(X(V0), Y(P0), X(V0), Y(P0 - 150), 'red', 3, 13); f.text(X(V0) + 8, Y(P0 - 150) + 4, 'isochoric', 'red', 19)
f.curve(lambda v: P0 * V0 / v, V0, V0 + 260, X, Y, 'green', 3)
f.text(X(V0 + 250), Y(P0 * V0 / (V0 + 260)) - 34, 'isothermal: PV = const', 'green', 18, 'end')
f.curve(lambda v: P0 * (V0 / v) ** 1.6, V0, V0 + 260, X, Y, 'purple', 3)
f.text(X(V0 + 250), Y(P0 * (V0 / (V0 + 260)) ** 1.6) + 26, 'adiabatic: PVᵞ = const', 'purple', 18, 'end')
f.text(310, 34, 'Expansion from A: adiabat is steeper than isotherm', 'ink', 20, 'middle', bold=True)
f.text(310, 62, 'work done = area under the curve', 'ink', 18, 'middle')
f.save(MEDIA, 'drawn_pv_processes')

# ---------------------------------------------------------------- self-drawn: heat engine and refrigerator
f = Fig(640, 380)
for k, (title, up) in enumerate([('Heat engine', False), ('Refrigerator', True)]):
    ox = 30 + k * 320
    f.rect(ox + 40, 50, 200, 50, 'red', '#f6d4d4', 2, 8); f.text(ox + 140, 82, 'hot reservoir T₁', 'red', 18, 'middle')
    f.rect(ox + 40, 280, 200, 50, 'blue', '#dbe7f7', 2, 8); f.text(ox + 140, 312, 'cold reservoir T₂', 'blue', 18, 'middle')
    f.circle(ox + 140, 190, 42, 'ink', '#f1ecdf', 2); f.text(ox + 140, 196, 'engine' if not up else 'fridge', 'ink', 17, 'middle')
    if not up:
        f.arrow(ox + 140, 100, ox + 140, 146, 'red', 3.2, 13); f.text(ox + 150, 128, 'Q₁', 'red', 19)
        f.arrow(ox + 140, 232, ox + 140, 278, 'blue', 3.2, 13); f.text(ox + 150, 262, 'Q₂', 'blue', 19)
        f.arrow(ox + 182, 190, ox + 250, 190, 'green', 3.2, 13); f.text(ox + 254, 196, 'W', 'green', 20, italic=True)
        f.text(ox + 140, 362, 'η = W/Q₁ = 1 − Q₂/Q₁', 'ink', 18, 'middle')
    else:
        f.arrow(ox + 140, 146, ox + 140, 100, 'red', 3.2, 13); f.text(ox + 150, 128, 'Q₁', 'red', 19)
        f.arrow(ox + 140, 278, ox + 140, 232, 'blue', 3.2, 13); f.text(ox + 150, 262, 'Q₂', 'blue', 19)
        f.arrow(ox + 250, 190, ox + 182, 190, 'green', 3.2, 13); f.text(ox + 254, 196, 'W', 'green', 20, italic=True)
        f.text(ox + 140, 362, 'β = Q₂/W = Q₂/(Q₁ − Q₂)', 'ink', 18, 'middle')
    f.text(ox + 140, 32, title, 'ink', 20, 'middle', bold=True)
f.save(MEDIA, 'drawn_engine_fridge')
