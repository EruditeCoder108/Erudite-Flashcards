import sys, os, math
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_math as sm

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Mathematics', 'class12-mathematics-ch11-three-dimensional-geometry')
d = Deck('Chapter 11: Three Dimensional Geometry', 'Class 12', ['class-12', 'mathematics', 'ch-11'])
d.description = 'Direction cosines and ratios, equations of a line in vector and Cartesian form, angle between lines, shortest distance between skew and parallel lines, with exam-style problems.'
b = d.basic


def fr(x): return x if isinstance(x, Fr) else Fr(x)
def dot(a, c): return sum(fr(x) * fr(y) for x, y in zip(a, c))
def cross(a, c): return (fr(a[1]) * fr(c[2]) - fr(a[2]) * fr(c[1]), fr(a[2]) * fr(c[0]) - fr(a[0]) * fr(c[2]), fr(a[0]) * fr(c[1]) - fr(a[1]) * fr(c[0]))
def sub(a, c): return tuple(fr(x) - fr(y) for x, y in zip(a, c))
def n2(a): return dot(a, a)
def V(*a): return tuple(fr(x) for x in a)


def num(x):
    x = fr(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'


def sq(n):
    n = fr(n).numerator
    r = math.isqrt(n)
    if r * r == n:
        return str(r)
    k, m, f = 1, n, 2
    while f * f <= m:
        while m % (f * f) == 0:
            m //= f * f
            k *= f
        f += 1
    return (str(k) if k > 1 else '') + '√' + str(m)


def dcs(v):
    m = sq(n2(v))
    return ', '.join((num(x) if m == '1' else f'{num(x)}/{m}') for x in v)


# ---------------------------------------------------------------- 11.2 Direction cosines
d.sec('11.2-direction-cosines-and-ratios')
b('Direction cosines of a line?', 'The cosines of the angles α, β, γ the line makes with the positive x, y, z axes: ' + T('l = cos α, m = cos β, n = cos γ') + ', with ' + T('l² + m² + n² = 1'))
b('Direction cosines of the three coordinate axes?', T('x-axis (1, 0, 0), y-axis (0, 1, 0), z-axis (0, 0, 1)') + ' (Example 4: angles 0°, 90°, 90°)')
b('Reversed direction: what happens to the direction cosines?', 'All three change sign: ' + T('(−l, −m, −n)') + ' (angles become π − α, π − β, π − γ). So a line has two sets of direction cosines')
b('Direction ratios: definition and link to direction cosines.', 'Any numbers a, b, c proportional to (l, m, n). Then ' + T('l = a/√(a² + b² + c²), m = b/√(...), n = c/√(...)') + ' (with ± for the two directions)')
sm.direction_cosines_axes(d)
b('Direction ratios of the line through P(x₁, y₁, z₁) and Q(x₂, y₂, z₂)?', T('x₂ − x₁, y₂ − y₁, z₂ − z₁') + ' (and dividing by PQ gives the direction cosines)')
b('Example 1: a line makes 90°, 60°, 30° with the x, y, z axes. Its direction cosines?', 'cos 90° = 0, cos 60° = ½, cos 30° = √3/2: ' + N('(0, 1/2, √3/2)') + '. Check: 0 + 1/4 + 3/4 = 1 ✓')
b('Example 2: direction ratios 2, −1, −2. Direction cosines?', 'Magnitude √(4 + 1 + 4) = 3: ' + N('(2/3, −1/3, −2/3)'))
b('Example 5: A(2, 3, −4), B(1, −2, 3), C(3, 8, −11): show they are collinear.', 'AB has ratios (−1, −5, 7) and BC has (2, 10, −14) = −2 × (−1, −5, 7). Proportional and B is common: ' + E('collinear'))
b('Trap: are the direction cosines of a line unique?', X('No') + ': (l, m, n) and (−l, −m, −n) both describe the line (opposite directions), and direction ratios can be scaled by any non-zero factor')
b('If a line makes equal angles with the axes, its direction cosines are?', 'l = m = n with 3l² = 1: ' + N('±(1/√3, 1/√3, 1/√3)') + ' (angle cos⁻¹(1/√3) ≈ 54.7°)')
b('Can a line make angles 30°, 45°, 60° with the three axes?', 'cos²30° + cos²45° + cos²60° = 3/4 + 1/2 + 1/4 = 3/2 ≠ 1: ' + X('No'))
d.sec('11.2-exercise-11-1')
b('Ex 11.1 Q1: a line makes 90°, 135°, 45° with the x, y, z axes. Find its direction cosines.', 'cos 90° = 0, cos 135° = −1/√2, cos 45° = 1/√2: ' + N('(0, −1/√2, 1/√2)'))
b('Ex 11.1 Q2: direction cosines of a line making equal angles with the axes.', N('±(1/√3, 1/√3, 1/√3)'))
v3 = V(-18, 12, -4)
b('Ex 11.1 Q3: direction ratios −18, 12, −4. Direction cosines?', '√(324 + 144 + 16) = ' + sq(n2(v3)) + ': ' + N('(−9/11, 6/11, −2/11)'))
b('Ex 11.1 Q4: show (2, 3, 4), (−1, −2, 1), (5, 8, 7) are collinear.', 'Ratios of the first two: (−3, −5, −3). Of the last two: (6, 10, 6) = −2(−3, −5, −3). ' + E('Collinear'))
A, B, C = V(3, 5, -4), V(-1, 1, 2), V(-5, -5, -2)
ab, bc, ca = sub(B, A), sub(C, B), sub(A, C)
b('Ex 11.1 Q5: direction cosines of the sides of the triangle with vertices (3, 5, −4), (−1, 1, 2), (−5, −5, −2).', 'AB = ' + str(tuple(int(x) for x in ab)) + ': ' + N('(−2/√17, −2/√17, 3/√17)') + '. BC = ' + str(tuple(int(x) for x in bc)) + ': ' + N('(−2/√17, −3/√17, −2/√17)') + '. CA = ' + str(tuple(int(x) for x in ca)) + ': ' + N('(4/√42, 5/√42, −1/√42)') + ' (each up to an overall sign)')
assert sq(n2(ab)) == '2√17' and sq(n2(ca)) == '2√42'

# ---------------------------------------------------------------- 11.3 Equation of a line
d.sec('11.3-equation-of-a-line')
sm.line_param_3d(d)
b('Vector equation of the line through the point a parallel to b?', T('r = a + λ b') + ' (λ ∈ R). Here r is the position vector of a general point of the line')
b('Cartesian equation of the line through (x₁, y₁, z₁) with direction ratios a, b, c?', T('(x − x₁)/a = (y − y₁)/b = (z − z₁)/c') + '. If a denominator is 0, that numerator is 0 (e.g. x/1 = y/0 = z/0 is the x-axis)')
b('Line through two points a and a′?', 'Direction is a′ − a: ' + T('r = a + λ(a′ − a)') + '; Cartesian ' + T('(x − x₁)/(x₂ − x₁) = (y − y₁)/(y₂ − y₁) = (z − z₁)/(z₂ − z₁)'))
b('Conversion between vector and Cartesian forms.', 'r = (x₁î + y₁ĵ + z₁k̂) + λ(aî + bĵ + ck̂) ⇔ (x − x₁)/a = (y − y₁)/b = (z − z₁)/c. Read a point and the direction ratios off either form')
b('Example 6: line through (5, 2, −4) parallel to 3î + 2ĵ − 8k̂. Vector and Cartesian equations.', N('r = 5î + 2ĵ − 4k̂ + λ(3î + 2ĵ − 8k̂)') + ' and ' + N('(x − 5)/3 = (y − 2)/2 = (z + 4)/(−8)'))
b('Parametric equations of a line: what are they?', T('x = x₁ + λa, y = y₁ + λb, z = z₁ + λc') + ': every value of λ gives a point of the line. They are handy for finding intersections and distances')
b('Trap: is the direction of the line (x − 1)/2 = (y + 3)/(−1) = (z − 4)/5 the vector (1, −3, 4)?', X('No') + ': (1, −3, 4) is a point on the line. The direction ratios are the denominators: ' + T('(2, −1, 5)'))
d.sec('11.3-exercise-11-2-lines')
b('Ex 11.2 Q4: the line through (1, 2, 3) parallel to 3î + 2ĵ − 2k̂.', N('r = î + 2ĵ + 3k̂ + λ(3î + 2ĵ − 2k̂)') + ' or ' + N('(x − 1)/3 = (y − 2)/2 = (z − 3)/(−2)'))
b('Ex 11.2 Q5: the line (vector and Cartesian) through the point 2î − ĵ + 4k̂ in the direction î + 2ĵ − k̂.', N('r = 2î − ĵ + 4k̂ + λ(î + 2ĵ − k̂)') + ' and ' + N('(x − 2)/1 = (y + 1)/2 = (z − 4)/(−1)'))
b('Ex 11.2 Q6: the Cartesian equation of the line through (−2, 4, −5) parallel to (x + 3)/3 = (y − 4)/5 = (z + 8)/6.', 'Parallel lines share direction ratios (3, 5, 6): ' + N('(x + 2)/3 = (y − 4)/5 = (z + 5)/6'))
b('Ex 11.2 Q7: the Cartesian equation (x − 5)/3 = (y + 4)/7 = (z − 6)/2. Write its vector form.', 'Point (5, −4, 6), direction (3, 7, 2): ' + N('r = 5î − 4ĵ + 6k̂ + λ(3î + 7ĵ + 2k̂)'))
b('Ex 11.2 Q1: show the three lines with direction cosines (12/13, −3/13, −4/13), (4/13, 12/13, 3/13), (3/13, −4/13, 12/13) are mutually perpendicular.', 'Dot products: 12·4 − 3·12 − 4·3 = 0, 4·3 + 12(−4) + 3·12 = 0, 12·3 + (−3)(−4) + (−4)(12) = 0 (each over 169). ' + E('Mutually perpendicular'))
b('Ex 11.2 Q2: show the line through (1, −1, 2), (3, 4, −2) is perpendicular to the line through (0, 3, 2), (3, 5, 6).', 'Directions (2, 5, −4) and (3, 2, 4): 6 + 10 − 16 = ' + N('0') + '. ' + E('Perpendicular'))
b('Ex 11.2 Q3: show the line through (4, 7, 8), (2, 3, 4) is parallel to the line through (−1, −2, 1), (1, 2, 5).', 'Directions (−2, −4, −4) and (2, 4, 4): proportional (ratio −1). ' + E('Parallel'))

# ---------------------------------------------------------------- 11.4 Angle between lines
d.sec('11.4-angle-between-lines')
sm.angle_between_lines(d)
b('Angle between two lines with direction cosines (l₁, m₁, n₁) and (l₂, m₂, n₂)?', T('cos θ = |l₁l₂ + m₁m₂ + n₁n₂|') + ' (θ acute). With direction ratios divide by both magnitudes')
b('Conditions for two lines to be perpendicular / parallel?', T('Perpendicular') + ': a₁a₂ + b₁b₂ + c₁c₂ = 0. ' + T('Parallel') + ': a₁/a₂ = b₁/b₂ = c₁/c₂')
b('Angle between lines r = a₁ + λb₁ and r = a₂ + μb₂ in vector form?', T('cos θ = |b₁ · b₂|/(|b₁||b₂|)'))
b('Angle between lines with direction ratios (1, 1, 2) and (1, 1, 0)?', 'dot = 2, magnitudes √6 and √2: cos θ = 2/√12 = 1/√3, so ' + N('θ = cos⁻¹(1/√3)'))
d.sec('11.4-exercise-11-2-angles')
l1, l2 = V(3, 2, 6), V(1, 2, 2)
b('Ex 11.2 Q8(i): angle between r = 2î − 5ĵ + k̂ + λ(3î + 2ĵ + 6k̂) and r = 7î − 6k̂ + μ(î + 2ĵ + 2k̂).', 'b₁ · b₂ = ' + num(dot(l1, l2)) + ', |b₁| = ' + sq(n2(l1)) + ', |b₂| = ' + sq(n2(l2)) + ': cos θ = 19/21. ' + N('θ = cos⁻¹(19/21)'))
l3, l4 = V(1, -1, -2), V(3, -5, -4)
b('Ex 11.2 Q8(ii): angle between r = 3î + ĵ − 2k̂ + λ(î − ĵ − 2k̂) and r = 2î − ĵ − 56k̂ + μ(3î − 5ĵ − 4k̂).', 'b₁ · b₂ = ' + num(dot(l3, l4)) + ', |b₁| = ' + sq(n2(l3)) + ', |b₂| = ' + sq(n2(l4)) + ': cos θ = 16/(√6 · 5√2) = 8/(5√3). ' + N('θ = cos⁻¹(8/(5√3))'))
l5, l6 = V(2, 5, -3), V(-1, 8, 4)
b('Ex 11.2 Q9(i): angle between (x − 2)/2 = (y − 1)/5 = (z + 3)/(−3) and (x + 2)/(−1) = (y − 4)/8 = (z − 5)/4.', 'Directions (2, 5, −3), (−1, 8, 4): dot = ' + num(dot(l5, l6)) + ', magnitudes ' + sq(n2(l5)) + ' and ' + sq(n2(l6)) + ': ' + N('θ = cos⁻¹(26/(9√38))'))
l7, l8 = V(2, 2, 1), V(4, 1, 8)
b('Ex 11.2 Q9(ii): angle between x/2 = y/2 = z/1 and (x − 5)/4 = (y − 2)/1 = (z − 3)/8.', 'Directions (2, 2, 1), (4, 1, 8): dot = ' + num(dot(l7, l8)) + ', magnitudes 3 and 9: ' + N('θ = cos⁻¹(2/3)'))
b('Ex 11.2 Q10: find p so the lines (1 − x)/3 = (7y − 14)/(2p) = (z − 3)/2 and (7 − 7x)/(3p) = (y − 5)/1 = (6 − z)/5 are perpendicular.', 'Rewrite to standard form: direction ratios (−3, 2p/7, 2) and (−3p/7, 1, −5). Dot = 9p/7 + 2p/7 − 10 = 0: ' + N('p = 70/11'))
b('Ex 11.2 Q11: show (x − 5)/7 = (y + 2)/(−5) = z/1 and x/1 = y/2 = z/3 are perpendicular.', 'Directions (7, −5, 1) and (1, 2, 3): 7 − 10 + 3 = ' + N('0') + ' ✓')

# ---------------------------------------------------------------- 11.5 Shortest distance
d.sec('11.5-shortest-distance')
b('What are skew lines?', 'Two lines in space that are ' + T('neither parallel nor intersecting') + ' (they do not lie in one plane)')
b('Angle between skew lines?', 'The angle between two intersecting lines drawn through any point (often the origin) parallel to each. It equals the angle between the direction vectors')
sm.skew_lines_distance(d)
b('Distance between skew lines r = a₁ + λb₁ and r = a₂ + μb₂?', T('d = |(a₂ − a₁) · (b₁ × b₂)| / |b₁ × b₂|'))
b('Distance between parallel lines r = a₁ + λb and r = a₂ + μb?', T('d = |b × (a₂ − a₁)| / |b|'))
b('Cartesian form of the skew-lines distance.', 'For (x − x₁)/a₁ = (y − y₁)/b₁ = (z − z₁)/c₁ and (x − x₂)/a₂ = ...: d = |det[x₂ − x₁, y₂ − y₁, z₂ − z₁; a₁ b₁ c₁; a₂ b₂ c₂]| / √((b₁c₂ − b₂c₁)² + (c₁a₂ − c₂a₁)² + (a₁b₂ − a₂b₁)²)')
b('How can you tell whether two lines are coplanar (intersect or are parallel)?', 'The shortest distance is ' + T('0') + ' (scalar triple product (a₂ − a₁) · (b₁ × b₂) = 0)')
b('Example 10: distance between the parallel lines through a₁ = î + 2ĵ − 4k̂ and a₂ = 3î + 3ĵ − 5k̂, both with b = 2î + 3ĵ + 6k̂.', 'a₂ − a₁ = (2, 1, −1); b × (a₂ − a₁) = (−9, 14, −4), magnitude √293; |b| = 7: ' + N('d = √293/7'))
cx = cross(V(2, 3, 6), V(2, 1, -1))
assert n2(cx) == 293 and cx == V(-9, 14, -4)
d.sec('11.5-exercise-11-2-distance')
def sd(a1, b1, a2, b2):
    c = cross(b1, b2)
    return abs(dot(sub(a2, a1), c)), n2(c)
n, m = sd(V(1, 2, 1), V(1, -1, 1), V(2, -1, -1), V(2, 1, 2))
assert (n, m) == (9, 18)
b('Ex 11.2 Q12: shortest distance between r = (î + 2ĵ + k̂) + λ(î − ĵ + k̂) and r = 2î − ĵ − k̂ + μ(2î + ĵ + 2k̂).', 'b₁ × b₂ = ' + str(tuple(int(x) for x in cross(V(1, -1, 1), V(2, 1, 2)))) + ', |b₁ × b₂| = ' + sq(m) + '; (a₂ − a₁) · (b₁ × b₂) = ' + str(int(dot(sub(V(2, -1, -1), V(1, 2, 1)), cross(V(1, -1, 1), V(2, 1, 2)))))  + ': ' + N('d = 9/(3√2) = 3√2/2'))
n, m = sd(V(-1, -1, -1), V(7, -6, 1), V(3, 5, 7), V(1, -2, 1))
b('Ex 11.2 Q13: shortest distance between (x + 1)/7 = (y + 1)/(−6) = (z + 1)/1 and (x − 3)/1 = (y − 5)/(−2) = (z − 7)/1.', 'b₁ × b₂ = (−4, −6, −8), |b₁ × b₂| = 2√29. a₂ − a₁ = (4, 6, 8), so |(a₂ − a₁) · (b₁ × b₂)| = 116. ' + N('d = 116/(2√29) = 2√29'))
n14, m14 = sd(V(1, 2, 3), V(1, -3, 2), V(4, 5, 6), V(2, 3, 1))
b('Ex 11.2 Q14: shortest distance between r = (î + 2ĵ + 3k̂) + λ(î − 3ĵ + 2k̂) and r = 4î + 5ĵ + 6k̂ + μ(2î + 3ĵ + k̂).', 'b₁ × b₂ = ' + str(tuple(int(x) for x in cross(V(1, -3, 2), V(2, 3, 1)))) + ', |b₁ × b₂| = ' + sq(m14) + ', numerator ' + str(int(n14)) + ': ' + N('d = 3/√19'))
b('Ex 11.2 Q15: shortest distance between r = (1 − t)î + (t − 2)ĵ + (3 − 2t)k̂ and r = (s + 1)î + (2s − 1)ĵ − (2s + 1)k̂.', 'Line 1: a₁ = î − 2ĵ + 3k̂, b₁ = −î + ĵ − 2k̂. Line 2: a₂ = î − ĵ − k̂, b₂ = î + 2ĵ − 2k̂. b₁ × b₂ = (2, −4, −3), |b₁ × b₂| = √29, and (a₂ − a₁) = (0, 1, −4) gives (a₂ − a₁) · (b₁ × b₂) = 8. ' + N('d = 8/√29'))
n15, m15 = sd(V(1, -2, 3), V(-1, 1, -2), V(1, -1, -1), V(1, 2, -2))
assert (n15, m15) == (8, 29), (n15, m15)

# ---------------------------------------------------------------- Miscellaneous
d.sec('11.6-miscellaneous')
b('Misc Q1: the angle between lines with direction ratios a, b, c and b − c, c − a, a − b.', 'Dot product: a(b − c) + b(c − a) + c(a − b) = ab − ac + bc − ab + ac − bc = ' + N('0') + ': ' + E('90°'))
b('Misc Q2: the equation of the line through the origin parallel to the x-axis.', 'Direction ratios of the x-axis: (1, 0, 0). ' + N('x/1 = y/0 = z/0'))
b('Misc Q3: if (x − 1)/(−3) = (y − 2)/(2k) = (z − 3)/2 and (x − 1)/(3k) = (y − 1)/1 = (z − 6)/(−5) are perpendicular, find k.', 'Directions (−3, 2k, 2) and (3k, 1, −5): −9k + 2k − 10 = 0: ' + N('k = −10/7'))
b('Misc Q4: shortest distance between r = 6î + 2ĵ + 2k̂ + λ(î − 2ĵ + 2k̂) and r = −4î − k̂ + μ(3î − 2ĵ − 2k̂).', 'a₂ − a₁ = (−10, −2, −3); b₁ × b₂ = (8, 8, 4) after computing (−2·(−2) − 2·(−2), 2·3 − 1·(−2), 1·(−2) − (−2)·3) = (8, 8, 4); |b₁ × b₂| = 12; numerator |−80 − 16 − 12| = 108: ' + N('d = 9'))
assert cross(V(1, -2, 2), V(3, -2, -2)) == V(8, 8, 4) and abs(dot(V(-10, -2, -3), V(8, 8, 4))) == 108
q5 = cross(V(3, -16, 7), V(3, 8, -5))
b('Misc Q5: the vector equation of the line through (1, 2, −4) perpendicular to (x − 8)/3 = (y + 19)/(−16) = (z − 10)/7 and (x − 15)/3 = (y − 29)/8 = (z − 5)/(−5).', 'Direction = cross product of (3, −16, 7) and (3, 8, −5) = (' + ', '.join(str(int(x)) for x in q5) + ') = 12(2, 3, 6). ' + N('r = î + 2ĵ − 4k̂ + λ(2î + 3ĵ + 6k̂)'))
assert q5 == V(24, 36, 72)

# ---------------------------------------------------------------- Exam patterns
d.sec('11.z-exam-patterns')
b('Do the lines (x − 1)/2 = (y − 2)/3 = (z − 3)/4 and (x − 4)/5 = (y − 1)/2 = z intersect?', 'Points: (1 + 2λ, 2 + 3λ, 3 + 4λ) and (4 + 5μ, 1 + 2μ, μ). From z: μ = 3 + 4λ. From y: 2 + 3λ = 1 + 2μ = 7 + 8λ, so λ = −1 and μ = −1. Check x: 1 − 2 = −1 and 4 − 5 = −1 ✓. ' + E('They intersect at (−1, −1, −1)'))
b('Foot of the perpendicular from a point to a line: method.', 'Take a general point on the line (from the parametric form), form the vector to the given point, and set its dot product with the direction to 0 to find λ. The distance is the length of that vector')
b('Distance of the point (x₀, y₀, z₀) from the line r = a + λb?', T('|b × (p − a)| / |b|') + ' where p is the position vector of the point')
b('Distance of the point (1, 2, 3) from the line through the origin with direction (1, 1, 1)?', 'p × b = (2 − 3, 3 − 1, 1 − 2) = (−1, 2, −1), magnitude √6; |b| = √3: ' + N('√2'))
b('Reflection of a point in a line: idea.', 'Find the foot F of the perpendicular; the image P′ satisfies F = midpoint of P and P′, so ' + T('P′ = 2F − P'))
b('The line joining (2, 3, 4) and (5, 6, 7): direction cosines?', 'Ratios (3, 3, 3): ' + N('(1/√3, 1/√3, 1/√3)') + ' (the line is equally inclined to the axes)')
b('Equation of the z-axis in Cartesian form?', N('x/0 = y/0 = z/1') + ' (direction ratios 0, 0, 1 through the origin)')
b('Equation of the line through (1, 2, 3) and (4, 6, 3)?', 'Direction (3, 4, 0): ' + N('(x − 1)/3 = (y − 2)/4 = (z − 3)/0') + ' (the line lies in the plane z = 3)')
b('When are two lines with equations in parametric form the same line?', 'When they share a point and their direction ratios are proportional')

# ---------------------------------------------------------------- How it is asked
d.sec('11.z-how-its-asked')
b('MCQ: direction cosines of the line joining (1, 2, 3) and (3, 4, 4)?<br>(a) (2/3, 2/3, 1/3) (b) (1/3, 1/3, 1/3) (c) (2, 2, 1) (d) (1/√3, 1/√3, 1/√3)', 'Ratios (2, 2, 1), magnitude 3: ' + E('(a)'))
b('MCQ: the direction ratios of the line (x − 1)/2 = (y + 2)/3 = (z − 5)/(−1) are<br>(a) 2, 3, −1 (b) 1, −2, 5 (c) 2, 3, 1 (d) −1, 2, −5', E('(a) 2, 3, −1'))
b('MCQ: if a line has direction cosines (l, m, n) with l = m = n, then l =<br>(a) ±1/√3 (b) ±1/3 (c) ±1/2 (d) 1', E('(a)'))
b('MCQ: the angle between the lines with directions (1, 1, 0) and (0, 1, 1) is<br>(a) 60° (b) 30° (c) 90° (d) 45°', 'cos θ = 1/2: ' + E('(a) 60°'))
b('MCQ: the lines with direction ratios (1, 2, 3) and (2, 4, 6) are<br>(a) parallel (b) perpendicular (c) skew (d) intersecting at 60°', E('(a) parallel'))
b('MCQ: the shortest distance between r = t(î + ĵ + k̂) and r = î + s(ĵ + k̂) is<br>(a) 1/√2 (b) 1 (c) 1/√3 (d) 0', 'Both lines pass through (1, 1, 1) (t = 1, s = 1), so they intersect: ' + E('(d) 0'))
b('MCQ: the line r = î + λ(î + ĵ + k̂) passes through the point<br>(a) (2, 1, 1) (b) (2, 1, 0) (c) (1, 1, 1) (d) (0, 0, 0)', 'λ = 1 gives (2, 1, 1): ' + E('(a)'))
b('MCQ: the distance between the parallel lines r = a + λb with a = (0, 0, 0) and a′ = (1, 0, 0), b = (0, 0, 1) is<br>(a) 1 (b) 0 (c) 2 (d) √2', '|b × (a′ − a)|/|b| = |(0, 1, 0)|/1 = ' + E('(a) 1'))
b('Integer answer (JEE Main): the square of the shortest distance between the lines r = (1, 2, 3) + λ(1, 0, 0) and r = (0, 0, 0) + μ(0, 1, 0) is?', 'b₁ × b₂ = (0, 0, 1); (a₂ − a₁) · (0, 0, 1) = −3: d = 3, so d² = ' + N('9'))
b('Integer answer: the direction ratios of a line are 2, −1, −2. What is 3l, where l is the first direction cosine (positive direction)?', 'Magnitude 3: l = 2/3, so 3l = ' + N('2'))
b('Assertion–Reason.<br><b>A:</b> the direction cosines of a line satisfy l² + m² + n² = 1.<br><b>R:</b> they are the components of a unit vector along the line.<br>(a) Both true, R explains A (b) Both true, R does not (c) A true, R false (d) A false, R true', E('(a)'))
b('Assertion–Reason.<br><b>A:</b> two skew lines have a unique common perpendicular.<br><b>R:</b> a line perpendicular to b₁ and b₂ is parallel to b₁ × b₂.<br>(a) Both true, R explains A (b) Both true, R does not (c) A true, R false (d) A false, R true', E('(a)') + ': the direction of the common perpendicular is fixed by b₁ × b₂')
b('True/False: two distinct lines with the same direction cosines must be parallel.', E('True'))
b('True/False: direction ratios of a line are unique.', X('False') + ': any non-zero multiple works')
b('2-mark: find the direction cosines of the line joining (0, 0, 0) and (1, 2, 2).', 'Magnitude 3: ' + N('(1/3, 2/3, 2/3)'))
b('2-mark: find the vector equation of the line through (1, 2, 3) with direction 2î − ĵ + k̂.', N('r = î + 2ĵ + 3k̂ + λ(2î − ĵ + k̂)'))
b('3-mark: find the angle between the lines (x − 1)/1 = (y − 2)/2 = (z − 3)/2 and x/2 = y/1 = z/2.', 'Directions (1, 2, 2), (2, 1, 2): dot = 8, magnitudes 3 and 3: cos θ = 8/9. ' + N('θ = cos⁻¹(8/9)'))
b('3-mark: find the shortest distance between r = (î + ĵ) + λ(2î − ĵ + k̂) and r = (2î + ĵ − k̂) + μ(3î − 5ĵ + 2k̂).', 'b₁ × b₂ = (−2 + 5, 3 − 4, −10 + 3) = (3, −1, −7), magnitude √59. (a₂ − a₁) = (1, 0, −1): dot = 3 + 7 = 10: ' + N('d = 10/√59'))
b('4-mark: show that the lines (x − 1)/2 = (y − 2)/3 = (z − 3)/4 and (x − 4)/5 = (y − 1)/2 = z intersect and find the point.', 'Equate parametric values: λ = μ = −1 satisfies all three equations. ' + N('Point (−1, −1, −1)'))
b('4-mark: find the foot of the perpendicular from (1, 2, 3) to the line through the origin with direction (1, 1, 1).', 'Foot F = t(1, 1, 1) with (1 − t, 2 − t, 3 − t) · (1, 1, 1) = 6 − 3t = 0 → t = 2: ' + N('F = (2, 2, 2)') + ' and the distance = |(−1, 0, 1)| = √2')
b('Case-based: two aircraft fly along the lines r = (0, 0, 10) + t(1, 0, 0) and r = (0, 0, 0) + s(0, 1, 0) (positions in km). What is their minimum separation?', 'The common perpendicular direction is (0, 0, 1); the offset is (0, 0, 10): ' + N('10 km'))
b('Case-based: a laser beam travels from A(0, 0, 0) along direction (1, 2, 2). How far from the beam is the point P(3, 0, 0)?', 'AP × b = (3, 0, 0) × (1, 2, 2) = (0, −6, 6), magnitude 6√2; |b| = 3: distance ' + N('2√2 units'))

print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
