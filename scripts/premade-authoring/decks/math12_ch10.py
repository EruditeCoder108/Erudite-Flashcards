import sys, os, math
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_math as sm

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Mathematics', 'class12-mathematics-ch10-vector-algebra')
d = Deck('Chapter 10: Vector Algebra', 'Class 12', ['class-12', 'mathematics', 'ch-10'])
d.description = 'Vectors and scalars, types of vectors, addition, components, direction cosines, section formula, dot and cross products with projections and areas, and exam-style problems.'
b = d.basic


# ---------------------------------------------------------------- small vector helpers (answers are computed, not typed)
def fr(x):
    return x if isinstance(x, Fr) else Fr(x)


def dot(a, c): return sum(fr(x) * fr(y) for x, y in zip(a, c))
def cross(a, c): return (fr(a[1]) * fr(c[2]) - fr(a[2]) * fr(c[1]), fr(a[2]) * fr(c[0]) - fr(a[0]) * fr(c[2]), fr(a[0]) * fr(c[1]) - fr(a[1]) * fr(c[0]))
def sub(a, c): return tuple(fr(x) - fr(y) for x, y in zip(a, c))
def add(a, c): return tuple(fr(x) + fr(y) for x, y in zip(a, c))
def scale(k, a): return tuple(fr(k) * fr(x) for x in a)
def n2(a): return dot(a, a)


def num(x):
    x = fr(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'


def sqrt_str(n):
    n = fr(n)
    if n.denominator != 1:
        top, bot = sqrt_str(n.numerator), sqrt_str(n.denominator)
        return f'{top}/{bot}' if '√' not in bot and bot != '1' else f'√({num(n)})'
    n = n.numerator
    r = int(math.isqrt(n))
    if r * r == n:
        return str(r)
    k, m = 1, n
    f = 2
    while f * f <= m:
        while m % (f * f) == 0:
            m //= f * f
            k *= f
        f += 1
    return (str(k) if k > 1 else '') + '√' + str(m)


def fv(v):
    s = ''
    for x, u in zip(v, ('î', 'ĵ', 'k̂')):
        x = fr(x)
        if x == 0:
            continue
        sign = '−' if x < 0 else '+'
        ax = abs(x)
        coef = '' if ax == 1 else num(ax)
        if ax.denominator != 1:
            coef = '(' + num(ax) + ')'
        s += (' ' + sign + ' ' if s else ('−' if x < 0 else '')) + coef + u
    return s or '0'


def V(*a): return tuple(fr(x) for x in a)


# ---------------------------------------------------------------- 10.2 Basic concepts
d.sec('10.2-basic-concepts')
b('What is a vector? A scalar?', T('Vector') + ': a quantity with both magnitude and direction (displacement, velocity, force)<br>' + T('Scalar') + ': magnitude only (time, mass, speed, work, temperature)')
b('How are vectors represented and written?', 'A directed line segment (arrow) from A to B: AB, or a single letter a. Magnitude |a|. Its tail is the ' + T('initial point') + ', its tip the ' + T('terminal point'))
b('Position vector of a point P(x, y, z)?', T('OP = xî + yĵ + zk̂') + ' from the origin O; magnitude ' + T('√(x² + y² + z²)'))
b('Types of vectors: zero, unit, coinitial, collinear, equal, negative.', T('Zero') + ' 0 (magnitude 0)<br>' + T('Unit') + ' (magnitude 1)<br>' + T('Coinitial') + ' (same initial point)<br>' + T('Collinear') + ' (parallel to the same line)<br>' + T('Equal') + ' (same magnitude AND direction)<br>' + T('Negative') + ' −a (same magnitude, opposite direction)')
b('Ex 10.1 Q1: represent graphically a displacement of 40 km, 30° east of north.', 'Draw an arrow of length 4 units (scale 1 unit = 10 km) that makes 30° with the north direction, tilted towards the east')
b('Ex 10.1 Q2: classify (i) 10 kg (ii) 2 m north-west (iii) 40° (iv) 40 watt (v) 10⁻¹⁹ coulomb (vi) 20 m/s²', 'Scalars: ' + N('10 kg, 40°, 40 watt, 10⁻¹⁹ C') + '. Vectors: ' + N('2 m north-west, 20 m/s² (acceleration has direction)'))
b('Ex 10.1 Q3: classify (i) time period (ii) distance (iii) force (iv) velocity (v) work done', 'Scalars: ' + N('time period, distance, work done') + '. Vectors: ' + N('force, velocity'))
b('Ex 10.1 Q4: in the square of Fig 10.6 (sides a, b, c, d), identify (i) coinitial (ii) equal (iii) collinear but not equal vectors.', '(i) Coinitial: ' + N('a and b') + '. (ii) Equal: ' + N('b and d') + '. (iii) Collinear but not equal: ' + N('a and c') + ' (parallel sides that point opposite ways)')
b('Ex 10.1 Q5: true or false: (i) a and −a are collinear (ii) two collinear vectors are always equal in magnitude (iii) two vectors of the same magnitude are collinear (iv) two collinear vectors of the same magnitude are equal', '(i) ' + E('True') + ' (ii) ' + X('False') + ' (iii) ' + X('False') + ' (iv) ' + X('False') + ' (they could point in opposite directions)')

d.sec('10.4-addition-and-scalar-multiplication')
sm.vector_addition_laws(d)
b('Properties of vector addition.', T('a + b = b + a') + ', ' + T('(a + b) + c = a + (b + c)') + ', a + 0 = a, a + (−a) = 0. Triangle inequality: ' + T('|a + b| ≤ |a| + |b|') + ', with equality when a and b have the same direction')
b('Multiplication of a vector by a scalar λ.', T('λa') + ' has magnitude |λ||a| and the direction of a if λ > 0, opposite if λ < 0. Components: λ(a₁î + a₂ĵ + a₃k̂) = λa₁î + λa₂ĵ + λa₃k̂')
b('Unit vector in the direction of a; vector of magnitude m in the direction of a?', T('â = a/|a|') + ' and ' + T('m â = m a/|a|'))
b('Components and magnitude: a = a₁î + a₂ĵ + a₃k̂.', 'Magnitude ' + T('|a| = √(a₁² + a₂² + a₃²)') + '. a₁, a₂, a₃ are the scalar components (direction ratios)')
b('Direction ratios and direction cosines of a = a₁î + a₂ĵ + a₃k̂.', 'Direction ratios a₁, a₂, a₃. Direction cosines ' + T('l = a₁/|a|, m = a₂/|a|, n = a₃/|a|') + ' with ' + T('l² + m² + n² = 1') + '. So â = lî + mĵ + nk̂')
b('Vector joining P(x₁, y₁, z₁) to Q(x₂, y₂, z₂)?', T('PQ = (x₂ − x₁)î + (y₂ − y₁)ĵ + (z₂ − z₁)k̂') + ' (head minus tail); |PQ| = √(Σ(differences)²)')
sm.section_formula_line(d)
b('When are two vectors collinear? Test with components.', 'a = λb for some scalar λ, i.e. ' + T('a₁/b₁ = a₂/b₂ = a₃/b₃') + '<br>Three points A, B, C are collinear iff AB ∥ BC<br>(or |AC| = |AB| + |BC| in the right order)')
b('Example 21: show A(−2î + 3ĵ + 5k̂), B(î + 2ĵ + 3k̂), C(7î − k̂) are collinear.', 'AB = 3î − ĵ − 2k̂, BC = 6î − 2ĵ − 4k̂, AC = 9î − 3ĵ − 6k̂<br>|AB| = √14, |BC| = 2√14, |AC| = 3√14, so |AC| = |AB| + |BC|. ' + E('Collinear'))
b('Example (right-angled triangle test).', 'If |AB|² = |BC|² + |CA|² then the angle at C is a right angle (Pythagoras). Compare squared lengths, or check that a dot product of two side vectors is 0')

d.sec('10.5-exercise-10-2')
a = V(1, 1, 1); bb = V(2, -7, -3); c = V(1, 1, -1)
b('Ex 10.2 Q1: magnitudes of a = î + ĵ + k̂, b = 2î − 7ĵ − 3k̂, c = (1/√3)î + (1/√3)ĵ − (1/√3)k̂.', '|a| = ' + N(sqrt_str(n2(a))) + ', |b| = ' + N(sqrt_str(n2(bb))) + ', |c| = ' + N('1') + ' (a unit vector: 3 × 1/3 = 1)')
b('Ex 10.2 Q2: write two different vectors having the same magnitude.', 'For example î + 2ĵ and 2î + ĵ (both magnitude √5), or î + ĵ + k̂ and î − ĵ + k̂ (both √3)')
b('Ex 10.2 Q3: write two different vectors having the same direction.', 'Any positive multiples: î + ĵ and 2î + 2ĵ')
b('Ex 10.2 Q4: find x and y so that 2î + 3ĵ and xî + yĵ are equal.', 'Equal vectors have equal components: ' + N('x = 2, y = 3'))
v = sub(V(-5, 7), V(2, 1))
b('Ex 10.2 Q5: scalar and vector components of the vector with initial point (2, 1) and terminal point (−5, 7).', 'Vector = (−5 − 2, 7 − 1) = ' + N(fv(V(v[0], v[1], 0))) + '. Scalar components ' + N(f'{num(v[0])}, {num(v[1])}') + '; vector components ' + N(f'{num(v[0])}î and {num(v[1])}ĵ'))
s = add(add(V(1, -2, 1), V(-2, 4, 5)), V(1, -6, -7))
b('Ex 10.2 Q6: sum of a = î − 2ĵ + k̂, b = −2î + 4ĵ + 5k̂, c = î − 6ĵ − 7k̂.', 'Add components: ' + N(fv(s)))
u = V(1, 1, 2)
b('Ex 10.2 Q7: unit vector in the direction of a = î + ĵ + 2k̂.', '|a| = ' + sqrt_str(n2(u)) + ': ' + N('(î + ĵ + 2k̂)/' + sqrt_str(n2(u))))
pq = sub(V(4, 5, 6), V(1, 2, 3))
b('Ex 10.2 Q8: unit vector in the direction of PQ, P(1, 2, 3), Q(4, 5, 6).', 'PQ = ' + fv(pq) + ', |PQ| = ' + sqrt_str(n2(pq)) + ': ' + N('(î + ĵ + k̂)/√3'))
s = add(V(2, -1, 2), V(-1, 1, -1))
b('Ex 10.2 Q9: unit vector in the direction of a + b for a = 2î − ĵ + 2k̂, b = −î + ĵ − k̂.', 'a + b = ' + fv(s) + ', magnitude ' + sqrt_str(n2(s)) + ': ' + N('(î + k̂)/√2'))
b('Ex 10.2 Q10: a vector in the direction of 5î − ĵ + 2k̂ with magnitude 8.', '|v| = √30: ' + N('(8/√30)(5î − ĵ + 2k̂)'))
b('Ex 10.2 Q11: show 2î − 3ĵ + 4k̂ and −4î + 6ĵ − 8k̂ are collinear.', 'The second equals −2 times the first: ' + E('collinear (opposite directions)'))
b('Ex 10.2 Q12: direction cosines of î + 2ĵ + 3k̂.', 'Magnitude √14: ' + N('1/√14, 2/√14, 3/√14'))
ab = sub(V(-1, -2, 1), V(1, 2, -3))
b('Ex 10.2 Q13: direction cosines of the vector joining A(1, 2, −3) to B(−1, −2, 1).', 'AB = ' + fv(ab) + ', |AB| = ' + sqrt_str(n2(ab)) + ': ' + N('−1/3, −2/3, 2/3'))
b('Ex 10.2 Q14: show î + ĵ + k̂ is equally inclined to the axes.', 'Direction cosines are all 1/√3 = cos α = cos β = cos γ, so α = β = γ = cos⁻¹(1/√3). ' + E('✓'))
P_, Q_ = V(1, 2, -1), V(-1, 1, 1)
R1 = scale(Fr(1, 3), add(scale(2, Q_), P_)); R2 = sub(scale(2, Q_), P_)
b('Ex 10.2 Q15: position vector of the point R dividing PQ in the ratio 2 : 1, P = î + 2ĵ − k̂, Q = −î + ĵ + k̂: (i) internally (ii) externally.', '(i) (2Q + P)/3 = ' + N(fv(R1)) + '. (ii) (2Q − P)/(2 − 1) = ' + N(fv(R2)))
mid = scale(Fr(1, 2), add(V(2, 3, 4), V(4, 1, -2)))
b('Ex 10.2 Q16: position vector of the midpoint of P(2, 3, 4) and Q(4, 1, −2).', N(fv(mid)) + ', that is the point (3, 2, 1)')
A_, B_, C_ = V(3, -4, -4), V(2, -1, 1), V(1, -3, -5)
b('Ex 10.2 Q17: a = 3î − 4ĵ − 4k̂, b = 2î − ĵ + k̂, c = î − 3ĵ − 5k̂ are the vertices of a right-angled triangle. Show it.', 'AB = ' + fv(sub(B_, A_)) + ' (|AB|² = ' + num(n2(sub(B_, A_))) + '), BC = ' + fv(sub(C_, B_)) + ' (' + num(n2(sub(C_, B_))) + '), CA = ' + fv(sub(A_, C_)) + ' (' + num(n2(sub(A_, C_))) + '). Since ' + num(n2(sub(B_, A_))) + ' + ' + num(n2(sub(A_, C_))) + ' = ' + num(n2(sub(C_, B_))) + ', the right angle is at A. ' + E('✓'))
b('Ex 10.2 Q18: in triangle ABC which is not true? (A) AB + BC + CA = 0 (B) AB + BC − AC = 0 (C) AB + BC − CA = 0 (D) AB − CB + CA = 0', 'AB + BC = AC, so AB + BC − CA = 2AC ≠ 0: ' + E('(C)'))
b('Ex 10.2 Q19: if a and b are collinear, which of these are incorrect? (A) b = λa for some λ (B) a = ±b (C) the components of a and b are not proportional (D) a and b have the same direction but different magnitudes', 'Collinear ⇒ b = λa and proportional components, so (A) is correct. (B) fails when magnitudes differ; (C) is the opposite of the true statement; (D) ignores that the direction may be reversed. ' + E('Incorrect: (B), (C), (D)'))

# ---------------------------------------------------------------- 10.6 Products
d.sec('10.6-scalar-product')
b('Scalar (dot) product: definition.', T('a · b = |a||b| cos θ') + ' (0 ≤ θ ≤ π). The result is a scalar. In components: ' + T('a₁b₁ + a₂b₂ + a₃b₃'))
sm.dot_projection(d)
b('Properties of the dot product.', 'Commutative a · b = b · a; distributive a · (b + c) = a · b + a · c; ' + T('a · a = |a|²') + '; (λa) · b = λ(a · b); î · î = ĵ · ĵ = k̂ · k̂ = 1 and î · ĵ = ĵ · k̂ = k̂ · î = 0')
b('Angle between a and b?', T('cos θ = a · b/(|a||b|)') + '. Perpendicular ⇔ a · b = 0; acute ⇔ a · b > 0; obtuse ⇔ a · b < 0')
b('Projection of a on b, and the vector projection?', 'Scalar projection ' + T('a · b/|b|') + ', vector projection ' + T('(a · b/|b|²) b'))
b('Expand |a + b|² and |a − b|².', T('|a ± b|² = |a|² ± 2 a · b + |b|²') + '. So |a + b| = |a − b| ⇔ a ⟂ b, and (a + b) · (a − b) = |a|² − |b|²')
b('Cauchy–Schwarz and triangle inequality for vectors.', T('|a · b| ≤ |a||b|') + ' and ' + T('|a + b| ≤ |a| + |b|') + ' (Example 19, 20)')
b('Trap: a · b = 0 implies a = 0 or b = 0?', X('No') + ': î · ĵ = 0 with both non-zero. They can also be perpendicular (Ex 10.3 Q14)')
d.sec('10.6-exercise-10-3')
b('Ex 10.3 Q1: find the angle between a and b with |a| = √3, |b| = 2 and a · b = √6.', 'cos θ = √6/(2√3) = √2/2: ' + N('θ = π/4'))
a1, a2 = V(1, -2, 3), V(3, -2, 1)
b('Ex 10.3 Q2: angle between î − 2ĵ + 3k̂ and 3î − 2ĵ + k̂.', 'a · b = ' + num(dot(a1, a2)) + ', |a|² = |b|² = ' + num(n2(a1)) + ': cos θ = ' + num(dot(a1, a2) / n2(a1)) + '. ' + N('θ = cos⁻¹(5/7)'))
b('Ex 10.3 Q3: projection of î − ĵ on î + ĵ.', '(1 − 1)/√2 = ' + N('0'))
b('Ex 10.3 Q4: projection of î + 3ĵ + 7k̂ on 7î − ĵ + 8k̂.', 'a · b = ' + num(dot(V(1, 3, 7), V(7, -1, 8))) + ', |b| = ' + sqrt_str(n2(V(7, -1, 8))) + ': ' + N('60/√114'))
vs = [V(2, 3, 6), V(3, -6, 2), V(6, 2, -3)]
b('Ex 10.3 Q5: show (1/7)(2î + 3ĵ + 6k̂), (1/7)(3î − 6ĵ + 2k̂), (1/7)(6î + 2ĵ − 3k̂) are unit vectors and mutually perpendicular.', 'Squares: ' + ', '.join(num(n2(x)) for x in vs) + ' (all 49, so unit after dividing by 7). Dot products: ' + ', '.join(num(dot(vs[i], vs[j])) for i, j in [(0, 1), (1, 2), (0, 2)]) + ' (all 0). ' + E('✓'))
b('Ex 10.3 Q6: find |a| and |b| if (a + b) · (a − b) = 8 and |a| = 8|b|.', '(a + b) · (a − b) = |a|² − |b|² = 63|b|² = 8 → |b|² = 8/63. ' + N('|b| = 2√14/21') + ', ' + N('|a| = 16√14/21'))
b('Ex 10.3 Q7: evaluate (3a − 5b) · (2a + 7b).', '6|a|² + 21 a·b − 10 a·b − 35|b|² = ' + N('6|a|² + 11 a·b − 35|b|²'))
b('Ex 10.3 Q8: two vectors of equal magnitude, angle 60° and scalar product ½. Find their magnitudes.', '|a|² cos 60° = ½ → |a|² = 1: ' + N('|a| = |b| = 1'))
b('Ex 10.3 Q9: find |x| if for a unit vector a, (x − a) · (x + a) = 12.', '|x|² − |a|² = 12 → |x|² = 13: ' + N('|x| = √13'))
lam = Fr(8)
b('Ex 10.3 Q10: a = 2î + 2ĵ + 3k̂, b = −î + 2ĵ + k̂, c = 3î + ĵ. If a + λb ⟂ c, find λ.', 'a + λb = (2 − λ, 2 + 2λ, 3 + λ). Dot with c = (3, 1, 0): 6 − 3λ + 2 + 2λ = 8 − λ = 0: ' + N('λ = 8'))
b('Ex 10.3 Q11: show |a|b + |b|a is perpendicular to |a|b − |b|a.', 'Dot product = |a|²|b|² − |b|²|a|² + (|a||b| − |a||b|)(a · b) = ' + N('0') + '. ' + E('✓'))
b('Ex 10.3 Q12: if a · a = 0 and a · b = 0, what can you say about b?', 'a · a = |a|² = 0 forces a = 0, and then a · b = 0 holds for any b: ' + N('b can be any vector'))
b('Ex 10.3 Q13: a, b, c are unit vectors with a + b + c = 0. Find a·b + b·c + c·a.', '0 = |a + b + c|² = 3 + 2(a·b + b·c + c·a): ' + N('−3/2'))
b('Ex 10.3 Q14: if a = 0 or b = 0 then a · b = 0. Is the converse true? Example.', 'No: î · ĵ = 0 although î ≠ 0 and ĵ ≠ 0 (perpendicular vectors)')
BA, BC = sub(V(1, 2, 3), V(-1, 0, 0)), sub(V(0, 1, 2), V(-1, 0, 0))
b('Ex 10.3 Q15: vertices A(1, 2, 3), B(−1, 0, 0), C(0, 1, 2). Find ∠ABC.', 'BA = ' + fv(BA) + ', BC = ' + fv(BC) + ', BA · BC = ' + num(dot(BA, BC)) + ', |BA| = ' + sqrt_str(n2(BA)) + ', |BC| = ' + sqrt_str(n2(BC)) + ': ' + N('∠ABC = cos⁻¹(10/√102)'))
AB1, BC1 = sub(V(2, 6, 3), V(1, 2, 7)), sub(V(3, 10, -1), V(2, 6, 3))
b('Ex 10.3 Q16: show A(1, 2, 7), B(2, 6, 3), C(3, 10, −1) are collinear.', 'AB = ' + fv(AB1) + ' and BC = ' + fv(BC1) + ' are equal: ' + E('collinear'))
b('Ex 10.3 Q17: show 2î − ĵ + k̂, î − 3ĵ − 5k̂, 3î − 4ĵ − 4k̂ form a right-angled triangle.', 'Same set as Ex 10.2 Q17 in a different order: squared sides 6, 35, 41 with 6 + 35 = 41. ' + E('✓'))
b('Ex 10.3 Q18: λa is a unit vector if (A) λ = 1 (B) λ = −1 (C) a = |λ| (D) a = 1/|λ|', '|λa| = |λ||a| = 1 → |a| = 1/|λ|: ' + E('(D)'))

d.sec('10.7-vector-product')
b('Vector (cross) product: definition.', T('a × b = |a||b| sin θ n̂') + ', where n̂ is the unit vector perpendicular to both, chosen by the right-hand rule. In components a × b = |î ĵ k̂; a₁ a₂ a₃; b₁ b₂ b₃|')
sm.cross_parallelogram(d)
b('Properties of the cross product.', T('a × b = −(b × a)') + ' (anticommutative); a × a = 0; a × b = 0 ⇔ a ∥ b (for non-zero); a × (b + c) = a × b + a × c; î × ĵ = k̂, ĵ × k̂ = î, k̂ × î = ĵ (cyclic), and reversed order gives a minus sign')
b('Area formulas using the cross product.', T('Parallelogram: |a × b|') + '; ' + T('triangle with sides a, b: ½|a × b|') + '; triangle ABC: ½|AB × AC|')
b('Lagrange’s identity: |a × b|² + (a · b)² = ?', T('|a|²|b|²') + '. It follows from sin²θ + cos²θ = 1')
b('How to find a unit vector perpendicular to two vectors a and b?', 'Compute ' + T('n = a × b') + ' and divide by |a × b|. The other perpendicular unit vector is −n̂')
b('Example 22–25 type: Example 25, area of the parallelogram with a = 3î + ĵ + 4k̂, b = î − ĵ + k̂.', 'a × b = ' + N(fv(cross(V(3, 1, 4), V(1, -1, 1)))) + ', area = |a × b| = ' + N('√42'))
d.sec('10.7-exercise-10-4')
q1 = cross(V(1, -7, 7), V(3, -2, 2))
b('Ex 10.4 Q1: |a × b| for a = î − 7ĵ + 7k̂, b = 3î − 2ĵ + 2k̂.', 'a × b = ' + fv(q1) + ': ' + N('|a × b| = ' + sqrt_str(n2(q1))))
q2 = cross(add(V(3, 2, 2), V(1, 2, -2)), sub(V(3, 2, 2), V(1, 2, -2)))
b('Ex 10.4 Q2: a unit vector perpendicular to a + b and a − b, where a = 3î + 2ĵ + 2k̂, b = î + 2ĵ − 2k̂.', 'a + b = (4, 4, 0), a − b = (2, 0, 4). Cross = ' + fv(q2) + ' = 8(2, −2, −1), magnitude 24: ' + N('(2î − 2ĵ − k̂)/3'))
b('Ex 10.4 Q3: a unit vector makes π/3 with î, π/4 with ĵ, and an acute angle θ with k̂. Find θ and the components.', 'cos²(π/3) + cos²(π/4) + cos²θ = 1: 1/4 + 1/2 + cos²θ = 1, so cos θ = 1/2<br>' + N('θ = π/3') + '<br>Components ' + N('½î + (1/√2)ĵ + ½k̂'))
b('Ex 10.4 Q4: show (a − b) × (a + b) = 2(a × b).', 'Expand: a × a + a × b − b × a − b × b = 0 + a × b + a × b − 0 = ' + N('2(a × b)') + '. ' + E('✓'))
b('Ex 10.4 Q5: find λ and μ if (2î + 6ĵ + 27k̂) × (î + λĵ + μk̂) = 0.', 'Parallel vectors have proportional components: 1/2 = λ/6 = μ/27: ' + N('λ = 3, μ = 27/2'))
b('Ex 10.4 Q6: a · b = 0 and a × b = 0. What can you say about a and b?', 'a · b = 0 means a = 0, b = 0 or a ⟂ b; a × b = 0 means a = 0, b = 0 or a ∥ b. Both hold only if ' + N('a = 0 or b = 0'))
b('Ex 10.4 Q7: prove a × (b + c) = a × b + a × c using components.', 'Each component of a × (b + c) is aᵢ(bⱼ + cⱼ) − aⱼ(bᵢ + cᵢ) = (aᵢbⱼ − aⱼbᵢ) + (aᵢcⱼ − aⱼcᵢ). ' + E('✓') + ' (distributive)')
b('Ex 10.4 Q8: if a = 0 or b = 0 then a × b = 0. Is the converse true? Example.', 'No: î × 2î = 0 with both non-zero (parallel vectors)')
AB9, AC9 = sub(V(2, 3, 5), V(1, 1, 2)), sub(V(1, 5, 5), V(1, 1, 2))
cr9 = cross(AB9, AC9)
b('Ex 10.4 Q9: area of the triangle with vertices A(1, 1, 2), B(2, 3, 5), C(1, 5, 5).', 'AB = ' + fv(AB9) + ', AC = ' + fv(AC9) + ', AB × AC = ' + fv(cr9) + ', magnitude ' + sqrt_str(n2(cr9)) + ': ' + N('area = √61/2'))
cr10 = cross(V(1, -1, 3), V(2, -7, 1))
b('Ex 10.4 Q10: area of the parallelogram with adjacent sides a = î − ĵ + 3k̂ and b = 2î − 7ĵ + k̂.', 'a × b = ' + fv(cr10) + ', |a × b| = ' + sqrt_str(n2(cr10)) + ': ' + N('15√2'))
b('Ex 10.4 Q11: |a| = 3, |b| = √2/3. a × b is a unit vector if the angle between them is (A) π/6 (B) π/4 (C) π/3 (D) π/2', '|a||b| sin θ = 1 → sin θ = 1/√2: ' + E('(B) π/4'))
b('Ex 10.4 Q12: area of the rectangle with vertices A(−î + ½ĵ + 4k̂), B(î + ½ĵ + 4k̂), C(î − ½ĵ + 4k̂), D(−î − ½ĵ + 4k̂) is (A) ½ (B) 1 (C) 2 (D) 4', 'Sides |AB| = 2 and |BC| = 1: ' + E('(C) 2'))

# ---------------------------------------------------------------- Miscellaneous
d.sec('10.8-miscellaneous')
sm.unit_vector_plane(d)
b('Misc Q1: a unit vector in the XY-plane making 30° with the positive x-axis.', N('(√3/2)î + ½ĵ'))
b('Misc Q2: scalar components and magnitude of the vector joining P(x₁, y₁, z₁) to Q(x₂, y₂, z₂).', 'Components ' + N('x₂ − x₁, y₂ − y₁, z₂ − z₁') + '; magnitude ' + N('√((x₂ − x₁)² + (y₂ − y₁)² + (z₂ − z₁)²)'))
b('Misc Q3: a girl walks 4 km west, then 3 km in a direction 30° east of north. Find her displacement from the start.', 'Take î east, ĵ north. Total = −4î + 3(sin 30° î + cos 30° ĵ) = ' + N('(−5/2)î + (3√3/2)ĵ') + ', magnitude √(25/4 + 27/4) = ' + N('√13 km'))
b('Misc Q4: if a = b + c, is |a| = |b| + |c|?', X('No in general') + '.<br>By the triangle inequality |a| ≤ |b| + |c|,<br>with equality only when b and c have the same direction')
b('Misc Q5: find x for which x(î + ĵ + k̂) is a unit vector.', '|x|√3 = 1: ' + N('x = ±1/√3'))
s5 = add(V(2, 3, -1), V(1, -2, 1))
b('Misc Q6: a vector of magnitude 5 parallel to the resultant of a = 2î + 3ĵ − k̂ and b = î − 2ĵ + k̂.', 'a + b = ' + fv(s5) + ', magnitude ' + sqrt_str(n2(s5)) + ': ' + N('(5/√10)(3î + ĵ) = (3√10/2)î + (√10/2)ĵ'))
r7 = add(sub(scale(2, V(1, 1, 1)), V(2, -1, 3)), scale(3, V(1, -2, 1)))
b('Misc Q7: unit vector parallel to 2a − b + 3c for a = î + ĵ + k̂, b = 2î − ĵ + 3k̂, c = î − 2ĵ + k̂.', '2a − b + 3c = ' + fv(r7) + ', magnitude ' + sqrt_str(n2(r7)) + ': ' + N('(3î − 3ĵ + 2k̂)/√22'))
AB8, BC8 = sub(V(5, 0, -2), V(1, -2, -8)), sub(V(11, 3, 7), V(5, 0, -2))
b('Misc Q8: show A(1, −2, −8), B(5, 0, −2), C(11, 3, 7) are collinear and find the ratio in which B divides AC.', 'AB = ' + fv(AB8) + ', BC = ' + fv(BC8) + ' = 3/2 · AB: collinear. ' + N('AB : BC = 2 : 3'))
b('Misc Q9: R divides P = 2a + b and Q = a − 3b externally in the ratio 1 : 2. Show P is the midpoint of RQ.', 'R = (1·Q − 2·P)/(1 − 2) = 2P − Q = 4a + 2b − a + 3b = ' + N('3a + 5b') + '<br>Midpoint of RQ = (3a + 5b + a − 3b)/2 = 2a + b = P ✓')
d10 = add(V(2, -4, 5), V(1, -2, -3))
c10 = cross(V(2, -4, 5), V(1, -2, -3))
b('Misc Q10: adjacent sides 2î − 4ĵ + 5k̂ and î − 2ĵ − 3k̂. Find the unit vector parallel to its diagonal, and the area.', 'Diagonal = sum = ' + fv(d10) + ', magnitude ' + sqrt_str(n2(d10)) + ': ' + N('(3î − 6ĵ + 2k̂)/7') + '. Area = |a × b| = |' + fv(c10) + '| = ' + N(sqrt_str(n2(c10)) + ' = 11√5'))
b('Misc Q11: show that the direction cosines of a vector equally inclined to OX, OY, OZ are ±(1/√3, 1/√3, 1/√3).', 'Equal angles give l = m = n and l² + m² + n² = 1: 3l² = 1. ' + N('l = m = n = ±1/√3'))
a12, b12, c12 = V(1, 4, 2), V(3, -2, 7), V(2, -1, 4)
d12 = cross(a12, b12)
t12 = Fr(15) / dot(c12, d12)
b('Misc Q12: find a vector d perpendicular to a = î + 4ĵ + 2k̂ and b = 3î − 2ĵ + 7k̂ with c · d = 15, c = 2î − ĵ + 4k̂.', 'd = t(a × b) = t' + fv(d12) + '. c · d = t · ' + num(dot(c12, d12)) + ' = 15 → t = ' + num(t12) + ': ' + N('d = (160/3)î − (5/3)ĵ − (70/3)k̂'))
b('Misc Q13: the scalar product of î + ĵ + k̂ with the unit vector along the sum of 2î + 4ĵ − 5k̂ and λî + 2ĵ + 3k̂ equals 1. Find λ.', 'Sum = (2 + λ, 6, −2). Dot with (1, 1, 1): λ + 6. So (λ + 6)² = (λ + 2)² + 40 → 8λ + 32 = 40: ' + N('λ = 1'))
b('Misc Q14: a, b, c mutually perpendicular with equal magnitudes. Show a + b + c is equally inclined to a, b and c.', '(a + b + c) · a = |a|² and similarly for b, c; |a + b + c| = √3|a|. So cos θ = 1/√3 for each. ' + E('✓'))
b('Misc Q15: prove (a + b) · (a + b) = |a|² + |b|² iff a ⟂ b (a, b ≠ 0).', 'Expand: |a|² + 2a·b + |b|² = |a|² + |b|² ⇔ a · b = 0 ⇔ ' + E('perpendicular ✓'))
b('Misc Q16: if θ is the angle between a and b, then a · b ≥ 0 only when (A) 0 < θ < π/2 (B) 0 ≤ θ ≤ π/2 (C) 0 < θ < π (D) 0 ≤ θ ≤ π', 'cos θ ≥ 0 exactly for 0 ≤ θ ≤ π/2: ' + E('(B)'))
b('Misc Q17: a, b are unit vectors at angle θ. a + b is a unit vector if (A) θ = π/4 (B) π/3 (C) π/2 (D) 2π/3', '|a + b|² = 2 + 2cos θ = 1 → cos θ = −½: ' + E('(D) θ = 2π/3'))
b('Misc Q18: î · (ĵ × k̂) + ĵ · (î × k̂) + k̂ · (î × ĵ) is (A) 0 (B) −1 (C) 1 (D) 3', '1 + ĵ · (−ĵ) + 1 = 1 − 1 + 1 = ' + E('(C) 1'))
b('Misc Q19: |a · b| = |a × b| when θ equals (A) 0 (B) π/4 (C) π/2 (D) π', '|cos θ| = |sin θ| → tan θ = ±1: ' + E('(B) π/4'))

# ---------------------------------------------------------------- Exam patterns
d.sec('10.z-exam-patterns')
b('Scalar triple product (JEE): a · (b × c) and its meaning.', T('[a b c] = a · (b × c)') + ' = the determinant of the components. Its absolute value is the ' + T('volume of the parallelepiped') + ' on a, b, c; it is 0 iff the three vectors are coplanar')
b('Are vectors a = î + 2ĵ + 3k̂, b = 2î + 3ĵ + 4k̂, c = 3î + 4ĵ + 5k̂ coplanar?', 'The determinant |1 2 3; 2 3 4; 3 4 5| = 0 (rows in AP): ' + E('coplanar'))
b('Vector triple product identity.', T('a × (b × c) = (a · c)b − (a · b)c') + ' (BAC − CAB rule)')
b('Component of a vector perpendicular to b?', 'a − (a · b/|b|²) b: the vector minus its projection along b')
b('When is |a + b| = |a − b|?', 'When ' + T('a ⟂ b') + ' (a · b = 0)')
b('If |a| = 3, |b| = 4 and a · b = 6, find |a × b|.', 'cos θ = 6/12 = ½, sin θ = √3/2: |a × b| = 12 · √3/2 = ' + N('6√3'))
b('If |a| = 2, |b| = 3, angle 60°, find |a + b| and |a − b|.', '|a ± b|² = 4 + 9 ± 2 · 6 · ½ = 13 ± 6: ' + N('|a + b| = √19') + ', ' + N('|a − b| = √7'))
b('Find the angle between a = î + ĵ and b = ĵ + k̂.', 'cos θ = 1/(√2 · √2) = ½: ' + N('60° = π/3'))
b('Area of the triangle with vertices O, A(1, 2, 3), B(3, 2, 1)?', 'OA × OB = (2 − 6, 9 − 1, 2 − 6) = (−4, 8, −4), magnitude 4√6: area = ' + N('2√6'))
b('Work done by a force F along a displacement d.', T('W = F · d') + ' (a scalar). Example: F = 3î + 2ĵ − k̂, d = 2î + ĵ + 3k̂ gives 6 + 2 − 3 = 5 units')
b('Moment (torque) of a force F about a point: r × F.', T('τ = r × F') + ': a vector whose magnitude is force × perpendicular distance from the pivot')
b('If a, b, c are vectors with a + b + c = 0, what do a × b, b × c, c × a satisfy?', N('a × b = b × c = c × a') + '. From a × (a + b + c) = 0 we get a × b = c × a, and similarly for the others')

# ---------------------------------------------------------------- How it is asked
d.sec('10.z-how-its-asked')
b('MCQ: the magnitude of the vector 3î − 4ĵ + 12k̂ is<br>(a) 5 (b) 13 (c) 19 (d) 7', '√(9 + 16 + 144) = ' + E('(b) 13'))
b('MCQ: the unit vector in the direction of 3î + 4ĵ is<br>(a) (3î + 4ĵ)/5 (b) 3î + 4ĵ (c) (3î + 4ĵ)/7 (d) (3î + 4ĵ)/25', E('(a)'))
b('MCQ: if a = î + ĵ and b = î − ĵ then a · b =<br>(a) 0 (b) 2 (c) −2 (d) 1', '1 − 1 = ' + E('(a) 0'))
b('MCQ: î × ĵ · k̂ =<br>(a) 1 (b) 0 (c) −1 (d) 3', '(î × ĵ) · k̂ = k̂ · k̂ = ' + E('(a) 1'))
b('MCQ: the area of the parallelogram whose adjacent sides are î and ĵ + k̂ is<br>(a) √2 (b) 1 (c) 2 (d) 0', '|î × (ĵ + k̂)| = |k̂ − ĵ| = ' + E('(a) √2'))
b('MCQ: the projection of î + ĵ on î is<br>(a) 1 (b) 2 (c) 0 (d) √2', E('(a) 1'))
b('MCQ: the vectors 2î + 3ĵ and λî + 6ĵ are parallel if λ =<br>(a) 4 (b) 3 (c) 6 (d) 9', '2/λ = 3/6: ' + E('(a) 4'))
b('MCQ: the angle between î + ĵ and ĵ + k̂ is<br>(a) π/3 (b) π/4 (c) π/2 (d) π/6', E('(a) π/3'))
b('MCQ: if |a × b| = |a · b| then the angle between a and b is<br>(a) 0 (b) π/4 (c) π/2 (d) π', E('(b) π/4'))
b('MCQ: for a unit vector a, |a × î|² + |a × ĵ|² + |a × k̂|² =<br>(a) 1 (b) 2 (c) 3 (d) 0', 'Each |a × î|² = 1 − a₁², so the sum is 3 − 1 = ' + E('(b) 2'))
b('Integer answer (JEE Main): if a = î + ĵ + k̂ and b = 2î − ĵ + 3k̂, find a · b.', '2 − 1 + 3 = ' + N('4'))
b('Integer answer: |a × b|² + (a · b)² when |a| = 2 and |b| = 3?', N('36') + ' (= |a|²|b|²)')
b('Integer answer: 2î + λĵ + k̂ is perpendicular to î − 2ĵ − 3k̂. Find 2λ.', 'Dot product: 2 − 2λ − 3 = 0, so λ = −½ and ' + N('2λ = −1'))
b('Assertion–Reason.<br><b>A:</b> a × b = b × a.<br><b>R:</b> the cross product is anticommutative.<br>(a) Both true, R explains A (b) A false, R true (c) A true, R false (d) Both false', E('(b)') + ': a × b = −(b × a)')
b('Assertion–Reason.<br><b>A:</b> if a · b = 0 then a ⟂ b.<br><b>R:</b> a · b = |a||b| cos θ.<br>(a) Both true, R explains A (b) Both true, R does not (c) A false, R true (d) A true, R false', E('(c)') + ': A fails when a or b is the zero vector (the zero vector has no defined direction)')
b('True/False: the cross product of two parallel vectors is the zero vector.', E('True'))
b('True/False: the dot product of two vectors is a vector.', X('False') + ': it is a scalar')
b('2-mark: find a unit vector along a = 2î − ĵ + 2k̂.', '|a| = 3: ' + N('(2î − ĵ + 2k̂)/3'))
b('2-mark: find the projection of a = 2î + 3ĵ on b = î + ĵ.', '5/√2 = ' + N('5/√2'))
b('3-mark: find the angle between a = î + 2ĵ + 3k̂ and b = 3î + 2ĵ + k̂.', 'a · b = 3 + 4 + 3 = 10; |a| = |b| = √14: cos θ = 5/7. ' + N('θ = cos⁻¹(5/7)'))
b('3-mark: find the area of the triangle with vertices (0, 0, 0), (1, 2, 3), (2, 1, 0).', 'a × b = (2·0 − 3·1, 3·2 − 1·0, 1·1 − 2·2) = (−3, 6, −3): magnitude 3√6. Area = ' + N('3√6/2'))
b('4-mark: show that î − 2ĵ + 3k̂, −2î + 3ĵ − 4k̂, −ĵ + 2k̂ are coplanar.', 'Determinant |1 −2 3; −2 3 −4; 0 −1 2| = 1(6 − 4) + 2(−4 − 0) + 3(2 − 0) = 2 − 8 + 6 = ' + N('0') + ': ' + E('coplanar'))
b('4-mark: if a + b + c = 0, |a| = 3, |b| = 5, |c| = 7, find the angle between a and b.', '|c|² = |a|² + |b|² + 2a·b: 49 = 9 + 25 + 30 cos θ → cos θ = ½: ' + N('θ = 60°'))
b('Case-based: a force F = 4î + 3ĵ newtons moves an object from (1, 1) to (5, 4) metres. Find the work done.', 'd = (4, 3): W = F · d = 16 + 9 = ' + N('25 J'))
b('Case-based: the position vectors of the ends of a rod are 2î + ĵ and 6î + 4ĵ. Find its length and midpoint.', 'Vector = (4, 3): length ' + N('5') + '; midpoint (a + b)/2 = ' + N('4î + (5/2)ĵ'))

print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
