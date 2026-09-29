import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_math as sm
import math12_ch09_data as data

bad = data.verify()
assert not bad, bad

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Mathematics', 'class12-mathematics-ch09-differential-equations')
d = Deck('Chapter 9: Differential Equations', 'Class 12', ['class-12', 'mathematics', 'ch-9'])
d.description = 'Order and degree, general and particular solutions, variables separable, homogeneous and linear equations, growth and decay models, with every solved exercise checked numerically.'
b = d.basic


def ode_cards(prefix, verb='Solve'):
    for tag, ode, sol, hint, kind, g, S, pts, init in data.ODE:
        if tag == prefix.rstrip(':'):
            b(tag + ': ' + ode, N(sol) + '<br><small>' + hint + '</small>')


# ---------------------------------------------------------------- 9.2 Basic concepts
d.sec('9.2-basic-concepts')
b('What is a differential equation?', 'An equation involving ' + T('derivatives of the dependent variable with respect to the independent variable(s)') + '. Example: dy/dx + y = eˣ. If only one independent variable it is an ordinary differential equation')
b('Order of a differential equation?', 'The order of the ' + T('highest order derivative') + ' present. d²y/dx² + y = 0 has order 2')
b('Degree of a differential equation?', 'The power of the highest-order derivative, ' + T('when the equation is a polynomial in its derivatives') + '. If it is not a polynomial in the derivatives (e.g. contains sin(y′) or e^(y′)), the degree is ' + T('not defined'))
b('Trap: is the degree the power of y or of the first derivative?', X('No') + '. Only the ' + T('highest-order derivative') + ' power counts, and only after the equation is a polynomial in derivatives (remove radicals and fractions of derivatives first)')
b('Example: (y″)² + (y′)³ + y = 0. Order and degree?', 'Highest derivative y″, its power 2: order ' + N('2') + ', degree ' + N('2'))
b('Order and degree of (dy/dx) + 1/(dy/dx) = 3?', 'Multiply: (dy/dx)² + 1 = 3 dy/dx, a polynomial: order ' + N('1') + ', degree ' + N('2'))
b('Order and degree of y = x (dy/dx) + √(1 + (dy/dx)²)?', 'Isolate the radical and square: (y − xy′)² = 1 + y′²: order ' + N('1') + ', degree ' + N('2'))
b('Number of arbitrary constants in the general solution of an nth-order equation?', T('n') + ' (one for each integration). A particular solution has none')
b('How do you form a differential equation from a family of curves?', 'Differentiate as many times as there are arbitrary constants, then ' + T('eliminate the constants') + '. Example: y = Ax + B → y′ = A, y″ = 0. And y = Ae^(2x): y′ = 2y')
b('Form the differential equation of y = a sin(x + b) (2 constants).', 'y′ = a cos(x + b), y″ = −a sin(x + b) = −y: ' + N('y″ + y = 0'))
b('Form the differential equation of the family of circles x² + y² = r².', 'Differentiate: 2x + 2y y′ = 0 → ' + N('x + y dy/dx = 0'))
b('Form the differential equation of y² = 4ax (parabolas, a arbitrary).', '2y y′ = 4a = y²/x: ' + N('2xy y′ = y²  i.e. y = 2x dy/dx'))
sm.slope_field_family(d)

d.sec('9.2-exercise-9-1')
table_card(d, 'Ex 9.1 Q1–Q5', 'Order and degree (if defined).', [
    ('Q1: d⁴y/dx⁴ + sin(y‴) = 0', 'order 4; degree not defined (sine of a derivative)', False),
    ('Q2: y′ + 5y = 0', 'order 1, degree 1', False),
    ('Q3: (ds/dt)⁴ + 3s d²s/dt² = 0', 'order 2, degree 1', False),
    ('Q4: (d²y/dx²)² + cos(dy/dx) = 0', 'order 2; degree not defined (cos of a derivative)', False),
    ('Q5: d²y/dx² = cos 3x + sin 3x', 'order 2, degree 1', False)], term='Ex 9.1 Q1 to Q5: order and degree')
table_card(d, 'Ex 9.1 Q6–Q10', 'Order and degree (if defined).', [
    ('Q6: (y‴)² + (y″)³ + (y′)⁴ + y⁵ = 0', 'order 3, degree 2', False),
    ('Q7: y‴ + 2y″ + y′ = 0', 'order 3, degree 1', False),
    ('Q8: y′ + y = eˣ', 'order 1, degree 1', False),
    ('Q9: y″ + (y′)² + 2y = 0', 'order 2, degree 1', False),
    ('Q10: y″ + 2y′ + sin y = 0', 'order 2, degree 1 (sin y is not a derivative)', False)], term='Ex 9.1 Q6 to Q10: order and degree')
b('Ex 9.1 Q11: the degree of (d²y/dx²)³ + (dy/dx)² + sin(dy/dx) + 1 = 0 is (A) 3 (B) 2 (C) 1 (D) not defined', 'It contains sin(dy/dx), so it is not a polynomial in the derivatives: ' + E('(D) not defined'))
b('Ex 9.1 Q12: the order of 2x² d²y/dx² − 3 dy/dx + y = 0 is (A) 2 (B) 1 (C) 0 (D) not defined', E('(A) 2') + ' (highest derivative is d²y/dx²)')
b('Example 1(iii): order and degree of y‴ + y² + e^(y′) = 0.', 'Order 3. Because of e^(y′) it is not a polynomial in the derivatives: ' + N('degree not defined'))

# ---------------------------------------------------------------- 9.3 Verify solutions
d.sec('9.3-solutions-exercise-9-2')
b('How do you verify that a function is a solution?', 'Differentiate it as many times as needed, substitute the derivatives and the function into the equation, and check that ' + T('LHS = RHS') + ' (for an implicit relation, differentiate implicitly)')
b('Ex 9.2 Q1: verify y = eˣ + 1 solves y″ − y′ = 0.', 'y′ = eˣ, y″ = eˣ: y″ − y′ = ' + N('0') + ' ✓')
b('Ex 9.2 Q2: verify y = x² + 2x + C solves y′ − 2x − 2 = 0.', 'y′ = 2x + 2: ' + N('0') + ' ✓')
b('Ex 9.2 Q3: verify y = cos x + C solves y′ + sin x = 0.', 'y′ = −sin x: ' + N('0') + ' ✓')
b('Ex 9.2 Q4: verify y = √(1 + x²) solves y′ = xy/(1 + x²).', 'y′ = x/√(1 + x²) = x y/(1 + x²) since y = √(1 + x²) ✓')
b('Ex 9.2 Q5: verify y = Ax solves xy′ = y (x ≠ 0).', 'y′ = A: x y′ = Ax = y ✓')
b('Ex 9.2 Q6: verify y = x sin x solves xy′ = y + x√(x² − y²).', 'y′ = sin x + x cos x. xy′ = x sin x + x² cos x = y + x²cos x. And x²cos x = x√(x² − x² sin² x) = x√(x² − y²) (for cos x ≥ 0). ✓')
b('Ex 9.2 Q7: verify xy = log y + C solves y′ = y²/(1 − xy) (xy ≠ 1).', 'Differentiate: y + xy′ = y′/y → y′(1/y − x) = y → y′ = y²/(1 − xy) ✓')
b('Ex 9.2 Q8: verify y − cos y = x solves (y sin y + cos y + x) y′ = y.', 'y′(1 + sin y) = 1. With x = y − cos y: y sin y + cos y + x = y(1 + sin y). So LHS = y(1 + sin y)y′ = y ✓')
b('Ex 9.2 Q9: verify x + y = tan⁻¹y solves y²y′ + y² + 1 = 0.', 'Differentiate: 1 + y′ = y′/(1 + y²) → y′(1/(1 + y²) − 1) = 1 → y′ = −(1 + y²)/y² ✓')
b('Ex 9.2 Q10: verify y = √(a² − x²), x ∈ (−a, a), solves x + y dy/dx = 0 (y ≠ 0).', 'y′ = −x/√(a² − x²) = −x/y, so x + y y′ = 0 ✓')
b('Ex 9.2 Q11: the number of arbitrary constants in the general solution of a fourth-order equation is (A) 0 (B) 2 (C) 3 (D) 4', E('(D) 4') + ' (equal to the order)')
b('Ex 9.2 Q12: the number of arbitrary constants in a particular solution of a third-order equation is (A) 3 (B) 2 (C) 1 (D) 0', E('(D) 0') + ' (constants have been fixed)')

# ---------------------------------------------------------------- 9.4 Separable
d.sec('9.4-variables-separable')
b('Variables separable: what does it mean and how do you solve it?', 'dy/dx = f(x) g(y) can be rearranged as ' + T('dy/g(y) = f(x) dx') + '. Integrate both sides and add ONE constant. (Check any g(y) = 0 root as a separate solution.)')
steps_card(d, 'Variables separable', 'Solve dy/dx = e^(x + y).', 'dy/dx = e^(x + y), y(0) = 0', [
    'Split the exponent: dy/dx = eˣ · e^y',
    'Separate: e^(−y) dy = eˣ dx',
    'Integrate: −e^(−y) = eˣ + C',
    'General solution: eˣ + e^(−y) = C′ (this is option A in Ex 9.3 Q23)'], 2, 'Separable equation dy/dx = e^(x + y)', 'e^(-y) dy = e^x dx gives e^x + e^(-y) = C')
b('Example 4/5 type: solve dy/dx = −4xy² (y ≠ 0).', 'dy/y² = −4x dx → −1/y = −2x² + C → ' + N('1/y = 2x² + C′') + ' (also y = 0 is a solution)')
b('When is a first-order equation separable?', 'When the right side factorises as f(x)·g(y). Then move all y’s to one side and all x’s to the other and integrate both sides')
d.sec('9.4-exercise-9-3')
ode_cards('Ex 9.3 Q1')
ode_cards('Ex 9.3 Q2')
ode_cards('Ex 9.3 Q3')
ode_cards('Ex 9.3 Q4')
ode_cards('Ex 9.3 Q5')
ode_cards('Ex 9.3 Q6')
ode_cards('Ex 9.3 Q7')
ode_cards('Ex 9.3 Q8')
ode_cards('Ex 9.3 Q9')
ode_cards('Ex 9.3 Q10')
d.sec('9.4-exercise-9-3-particular')
b('Particular solution: method.', 'Find the general solution with its constant C, then ' + T('substitute the given point (x₀, y₀)') + ' to find C. The answer must not contain C')
for q in ['Ex 9.3 Q11', 'Ex 9.3 Q12', 'Ex 9.3 Q13', 'Ex 9.3 Q14', 'Ex 9.3 Q15', 'Ex 9.3 Q16', 'Ex 9.3 Q17', 'Ex 9.3 Q18']:
    ode_cards(q)
b('Ex 9.3 Q19: a balloon’s volume changes at a constant rate; radius 3 initially, 6 after 3 s. Find the radius after t seconds.', 'dV/dt = k with V = (4/3)πr³, so r³ = r₀³ + Kt: 27 + 3K = 216 → K = 63. ' + N('r = (63t + 27)^(1/3)'))
sm.growth_doubling(d)
b('Ex 9.3 Q20: principal grows continuously at r% per year. Find r if ₹100 doubles in 10 years (log 2 = 0.6931).', 'P = P₀ e^(rt/100): 2 = e^(r/10) → r = 10 log 2 = ' + N('6.93%'))
b('Ex 9.3 Q21: ₹1000 at 5% continuously compounded: worth after 10 years (e^0.5 = 1.648)?', 'P = 1000 e^(0.05 × 10) = 1000 e^0.5 = ' + N('₹1648'))
b('Ex 9.3 Q22: a culture of 1,00,000 bacteria grows 10% in 2 hours. In how many hours does it reach 2,00,000?', 'dp/dt = kp, p = p₀e^(kt): 1.1 = e^(2k) → k = ½ log(11/10). Doubling: t = log 2/k = ' + N('2 log 2 / log(11/10) hours'))
b('Ex 9.3 Q23: the general solution of dy/dx = e^(x + y) is (A) eˣ + e^(−y) = C (B) eˣ + e^y = C (C) e^(−x) + e^y = C (D) e^(−x) + e^(−y) = C', 'e^(−y) dy = eˣ dx → −e^(−y) = eˣ + C. ' + E('(A)'))
b('Newton’s law of cooling (JEE): the model and its solution.', 'dT/dt = −k(T − Tₛ): the rate of cooling is proportional to the temperature difference. Solution: ' + T('T − Tₛ = (T₀ − Tₛ) e^(−kt)'))
b('Radioactive decay: model and half-life?', 'dN/dt = −λN gives N = N₀ e^(−λt). Half-life T = ' + T('(log 2)/λ'))

# ---------------------------------------------------------------- 9.5 Homogeneous
d.sec('9.5-homogeneous')
b('Homogeneous function of degree n.', 'F(λx, λy) = ' + T('λⁿ F(x, y)') + ' for every λ ≠ 0. Examples: y² + 2xy (degree 2), 2x − 3y (degree 1), cos(y/x) (degree 0), but sin x + cos y is not homogeneous')
b('Homogeneous differential equation: definition.', 'dy/dx = F(x, y) with F homogeneous of ' + T('degree 0') + ', i.e. F(x, y) = g(y/x). Equivalently P dx + Q dy = 0 where P and Q are homogeneous of the same degree')
b('Method for a homogeneous equation dy/dx = g(y/x).', 'Put ' + T('y = vx') + ', dy/dx = v + x dv/dx. Then x dv/dx = g(v) − v: separate variables. Replace v by y/x at the end. If the equation is written as dx/dy = h(x/y), use x = vy')
sm.homogeneous_rays(d)
b('Ex 9.4 Q16: dx/dy = h(x/y) is solved by the substitution (A) y = vx (B) v = yx (C) x = vy (D) x = v', 'Because h depends on x/y: ' + E('(C) x = vy'))
b('Ex 9.4 Q17: which is homogeneous? (A) (4x + 6y + 5)dy − (3y + 2x + 4)dx = 0 (B) (xy)dx − (x³ + y³)dy = 0 (C) (x³ + 2y²)dx + 2xy dy = 0 (D) y²dx + (x² − xy − y²)dy = 0', 'Only (D) has coefficients of the same degree (2) in both terms. ' + E('(D)'))
d.sec('9.5-exercise-9-4')
for k in range(1, 11):
    ode_cards('Ex 9.4 Q%d' % k if k > 9 else 'Ex 9.4 Q%d' % k)
d.sec('9.5-exercise-9-4-particular')
for k in range(11, 16):
    ode_cards('Ex 9.4 Q%d' % k)

# ---------------------------------------------------------------- 9.6 Linear
d.sec('9.6-linear')
b('First-order linear differential equation: standard forms.', T('dy/dx + P y = Q') + ' (P, Q functions of x) or ' + T('dx/dy + P₁ x = Q₁') + ' (P₁, Q₁ functions of y)')
b('Integrating factor and solution of dy/dx + P y = Q.', T('IF = e^(∫P dx)') + '. Multiply through: d/dx(y · IF) = Q · IF, so ' + T('y · IF = ∫ Q · IF dx + C'))
steps_card(d, 'Linear equation · Example 15', 'Solve dy/dx + y/x = x² (x > 0).', 'P = 1/x, Q = x²', [
    'IF = e^(∫1/x dx) = e^(log x) = x',
    'Multiply: d/dx (xy) = x · x² = x³',
    'Integrate: xy = x⁴/4 + C',
    'Solution: y = x³/4 + C/x'], 1, 'Solving a linear equation with an integrating factor', 'dy/dx + P y = Q: IF = e^(integral of P); y IF = integral Q IF dx + C; example y\' + y/x = x^2 gives xy = x^4/4 + C')
b('When should you use dx/dy + P₁x = Q₁ instead?', 'When the equation is linear in x but not in y, e.g. y dx + (x − y²) dy = 0 or (x + y) dy/dx = 1. Then IF = e^(∫P₁ dy)')
b('Trap: dropping the constant of integration in the IF exponent, or forgetting to divide the final answer by the IF.', 'The IF needs no constant, but after ∫Q·IF dx + C you must ' + T('divide by the IF') + ' to get y. Also make the coefficient of dy/dx equal to 1 first (divide by cos²x, x, etc.)')
d.sec('9.6-exercise-9-5')
for k in range(1, 13):
    ode_cards('Ex 9.5 Q%d:' % k)
d.sec('9.6-exercise-9-5-particular')
for k in range(13, 18):
    ode_cards('Ex 9.5 Q%d:' % k)
b('Ex 9.5 Q18: the integrating factor of x dy/dx − y = 2x² is (A) e^(−x) (B) e^(−y) (C) 1/x (D) x', 'Divide by x: y′ − y/x = 2x, P = −1/x: IF = e^(−log x) = ' + E('(C) 1/x'))
b('Ex 9.5 Q19: the integrating factor of (1 − y²) dx/dy + yx = ay (−1 < y < 1) is (A) 1/(y² − 1) (B) 1/√(y² − 1) (C) 1/(1 − y²) (D) 1/√(1 − y²)', 'dx/dy + y/(1 − y²) x = ay/(1 − y²): IF = e^(∫ y/(1 − y²) dy) = e^(−½ log(1 − y²)) = ' + E('(D) 1/√(1 − y²)'))

# ---------------------------------------------------------------- Miscellaneous
d.sec('9.7-miscellaneous')
table_card(d, 'Misc Q1: order and degree', 'Find the order and degree.', [
    ('(i) d²y/dx² + 5x (dy/dx)² − 6y = log x', 'order 2, degree 1', False),
    ('(ii) (dy/dx)³ − 4 (dy/dx)² + 7y = sin x', 'order 1, degree 3', False),
    ('(iii) d⁴y/dx⁴ − sin(d³y/dx³) = 0', 'order 4, degree not defined', False)], term='Misc Ex 9 Q1: order and degree')
b('Misc Q2(i): verify xy = a eˣ + b e^(−x) + x² solves x d²y/dx² + 2 dy/dx − xy + x² − 2 = 0.', 'Differentiate xy: y + xy′ = aeˣ − be^(−x) + 2x; again: 2y′ + xy″ = aeˣ + be^(−x) + 2 = (xy − x²) + 2. So xy″ + 2y′ − xy + x² − 2 = 0 ✓')
b('Misc Q2(ii): verify y = eˣ(a cos x + b sin x) solves y″ − 2y′ + 2y = 0.', 'y′ = eˣ[(a + b)cos x + (b − a)sin x], y″ = eˣ[2b cos x − 2a sin x] = 2eˣ(b cos x − a sin x). Then y″ − 2y′ + 2y = 0 ✓')
b('Misc Q2(iii): verify y = x sin 3x solves y″ + 9y − 6 cos 3x = 0.', 'y′ = sin 3x + 3x cos 3x; y″ = 6 cos 3x − 9x sin 3x. So y″ + 9y = 6 cos 3x ✓')
b('Misc Q2(iv): verify x² = 2y² log y solves (x² + y²) dy/dx − xy = 0.', 'Differentiate: 2x = 4y y′ log y + 2y y′ = 2y y′(2 log y + 1). Using 2 log y = x²/y²: y′ = x y/(x² + y²) ✓')
b('Misc Q3: prove x² − y² = c(x² + y²)² is the general solution of (x³ − 3xy²) dx = (y³ − 3x²y) dy.', 'Let u = x² − y², w = x² + y²: c = u/w². Differentiate: (2x − 2y y′)w² − u · 2w(2x + 2y y′) = 0 → (x − y y′)(x² + y²) − 2(x² − y²)(x + y y′) = 0 → y′(y³ − 3x²y) = x³ − 3xy². ' + E('✓'))
ode_cards('Misc Q4')
ode_cards('Misc Q5')
ode_cards('Misc Q6')
ode_cards('Misc Q7')
ode_cards('Misc Q8')
ode_cards('Misc Q9')
ode_cards('Misc Q10')
ode_cards('Misc Q11')
ode_cards('Misc Q12')
ode_cards('Misc Q13')
b('Misc Q13: the general solution of y dx − x dy = 0 is (A) xy = C (B) x = Cy² (C) y = Cx (D) y = Cx²', 'dy/y = dx/x → y = Cx: ' + E('(C)'))
b('Misc Q14: the general solution of dx/dy + P₁x = Q₁ is (A) y e^(∫P₁ dy) = ∫(Q₁e^(∫P₁ dy)) dy + C (B) y e^(∫P₁ dx) = ∫(Q₁e^(∫P₁ dx)) dx + C (C) x e^(∫P₁ dy) = ∫(Q₁e^(∫P₁ dy)) dy + C (D) x e^(∫P₁ dx) = ∫(Q₁e^(∫P₁ dx)) dx + C', 'The unknown is x and the variable is y, so IF = e^(∫P₁ dy): ' + E('(C)'))
ode_cards('Misc Q15')
b('Misc Q15: the general solution of eˣ dy + (y eˣ + 2x) dx = 0 is (A) x eʸ + x² = C (B) x eʸ + y² = C (C) y eˣ + x² = C (D) y eʸ + x² = C', E('(C) y eˣ + x² = C'))

# ---------------------------------------------------------------- Exam patterns
d.sec('9.z-exam-patterns')
b('Which method for which type? (decision table)', T('Separable') + ': dy/dx = f(x)g(y). ' + T('Homogeneous') + ': dy/dx = F(y/x) (put y = vx). ' + T('Linear') + ': dy/dx + Py = Q (IF = e^(∫P)). ' + T('Linear in x') + ': dx/dy + P₁x = Q₁. Also try a substitution t = x + y, t = x − y, t = ax + by + c when those combinations recur')
b('Substitution for dy/dx = f(ax + by + c)?', 'Put ' + T('t = ax + by + c') + ': dt/dx = a + b f(t), which is separable')
b('Solve dy/dx = (x + y + 1)² (idea).', 't = x + y + 1: dt/dx = 1 + t². So tan⁻¹t = x + C and ' + N('x + y + 1 = tan(x + C)'))
b('Solve dy/dx = sin²(x − y + 1).', 'Put t = x − y + 1: dt/dx = 1 − sin²t = cos²t, so sec²t dt = dx: ' + N('tan(x − y + 1) = x + C'))
b('Orthogonal trajectories (idea).', 'For a family F(x, y, c) = 0 with slope dy/dx = m(x, y), the orthogonal family has slope −1/m. Example: y = cx has slope y/x; orthogonal slope −x/y: x² + y² = k')
b('Differential equation of all lines through the origin, and of all circles centred at the origin?', 'Lines y = cx: ' + N('y′ = y/x') + '. Circles x² + y² = r²: ' + N('x + y y′ = 0') + ' (they are orthogonal families)')
b('Solve dy/dx = y/x + tan(y/x).', 'y = vx: x dv/dx = tan v, so cot v dv = dx/x: ' + N('sin(y/x) = Cx'))
b('The equation of the curve through (1, 1) whose slope at (x, y) is y/x?', 'dy/y = dx/x: y = Cx with C = 1: ' + N('y = x'))
b('A tank problem: dV/dt = −k√V. Solution?', '√V = √V₀ − kt/2: ' + N('the tank empties in t = 2√V₀/k'))
b('How many independent arbitrary constants are in y = A e^(x + B)?', 'A e^(x + B) = (A e^B) eˣ: only ' + N('1') + ' independent constant (A and B combine)')

# ---------------------------------------------------------------- How it is asked
d.sec('9.z-how-its-asked')
b('MCQ: the order and degree of (d²y/dx²)³ + (dy/dx)⁴ + y = 0 are<br>(a) 2, 3 (b) 3, 2 (c) 2, 4 (d) 4, 2', E('(a) order 2, degree 3'))
b('MCQ: the degree of y′ + (y″)^(1/2) = x is<br>(a) 1 (b) 2 (c) 1/2 (d) not defined', 'Isolate and square: y″ = (x − y′)², a polynomial in the derivatives where the highest derivative y″ has power 1: ' + E('(a) 1'))
b('MCQ: the general solution of dy/dx = y is<br>(a) y = Ceˣ (b) y = x + C (c) y = C/x (d) y = ln x + C', E('(a)'))
b('MCQ: the solution of dy/dx = 2x with y(0) = 3 is<br>(a) y = x² + 3 (b) y = x² (c) y = 2x + 3 (d) y = x² − 3', E('(a) y = x² + 3'))
b('MCQ: the integrating factor of dy/dx + y = e^(2x) is<br>(a) eˣ (b) e^(−x) (c) e^(2x) (d) x', 'e^(∫1 dx) = ' + E('(a) eˣ'))
b('MCQ: the integrating factor of dy/dx + (2/x) y = x is<br>(a) x² (b) 2x (c) e^x (d) 1/x²', 'e^(2 log x) = ' + E('(a) x²'))
b('MCQ: y = vx substitution is used for<br>(a) homogeneous equations (b) linear equations (c) exact equations (d) all', E('(a)'))
b('MCQ: the number of arbitrary constants in y = a + b x + c x² is<br>(a) 1 (b) 2 (c) 3 (d) 0', E('(c) 3') + ' (the ODE eliminating them is y‴ = 0, order 3)')
b('MCQ: the differential equation of the family y = mx + c (m, c arbitrary) is<br>(a) y″ = 0 (b) y′ = 0 (c) y″ = y (d) y′ = m', E('(a) y″ = 0'))
b('MCQ: the solution of dy/dx = x/y is<br>(a) y² − x² = C (b) y − x = C (c) xy = C (d) y = Cx', 'y dy = x dx: ' + E('(a)'))
b('Integer answer (JEE Main): if the order of the differential equation of the family y = a sin x + b cos x is m and its degree is n, then m + n =?', 'y″ + y = 0: order 2, degree 1: ' + N('3'))
b('Integer answer: the number of arbitrary constants in the general solution of y‴ − y = 0 is?', N('3'))
b('Integer answer: the solution of dy/dx = 3x²y with y(0) = 1 gives y(1) = e^k. Find k.', 'y = e^(x³): k = ' + N('1'))
b('Assertion–Reason.<br><b>A:</b> the degree of sin(y′) + y″ = 0 is not defined.<br><b>R:</b> the equation is not a polynomial in the derivatives.<br>(a) Both true, R explains A (b) Both true, R does not (c) A true, R false (d) A false, R true', E('(a)'))
b('Assertion–Reason.<br><b>A:</b> a particular solution of a differential equation contains no arbitrary constant.<br><b>R:</b> it is obtained by giving specific values to the constants of the general solution.<br>(a) Both true, R explains A (b) Both true, R does not (c) A true, R false (d) A false, R true', E('(a)'))
b('True/False: y = x is a solution of x dy/dx = y.', E('True') + ': x · 1 = x')
b('True/False: every first-order equation can be solved by separating variables.', X('False') + ': only when the right side factorises as f(x)g(y); otherwise use homogeneous or linear methods')
b('2-mark: find the order and degree of y″ + (y′)³ + y = 0.', N('order 2, degree 1'))
b('2-mark: solve dy/dx = e^x.', N('y = eˣ + C'))
b('3-mark: solve dy/dx = (1 + y²)/(1 + x²).', 'tan⁻¹y = tan⁻¹x + C: ' + N('(y − x)/(1 + xy) = C′'))
b('3-mark: find the particular solution of dy/dx = 2xy with y(0) = 1.', 'dy/y = 2x dx: log y = x² + C, C = 0: ' + N('y = e^(x²)'))
b('4-mark: solve x dy/dx = y + x², given y(1) = 0.', 'Linear: y′ − y/x = x, IF = 1/x: y/x = x + C; y(1) = 0 gives C = −1: ' + N('y = x² − x'))
b('4-mark: show that (x² + y²) dx − 2xy dy = 0 is homogeneous and solve it.', 'y = vx: x dv/dx = (1 + v²)/(2v) − v = (1 − v²)/(2v). 2v/(1 − v²) dv = dx/x: −log|1 − v²| = log x + c. ' + N('x² − y² = Cx'))
b('Case-based: a culture has 500 bacteria, and its growth rate is proportional to its size. It doubles in 3 hours. Find the number after 9 hours.', 'P = P₀e^(kt) with e^(3k) = 2: after 9 h the population has doubled three times: 500 × 2³ = ' + N('4000'))
b('Case-based: a body at 100°C is placed in a room at 20°C and cools to 60°C in 10 minutes. What is its temperature after another 10 minutes (Newton’s law)?', 'T − 20 = 80e^(−kt); at t = 10: 40 = 80e^(−10k), so e^(−10k) = ½. At t = 20: T − 20 = 80 × ¼ = 20, so ' + N('T = 40°C'))

print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
