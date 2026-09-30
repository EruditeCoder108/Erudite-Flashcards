import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_math as sm

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Mathematics', 'class12-mathematics-ch02-inverse-trigonometric-functions')
d = Deck('Chapter 2: Inverse Trigonometric Functions', 'Class 12', ['class-12', 'mathematics', 'ch-2'])
d.description = 'Principal value branches, graphs, standard values, properties and identities, simplification by substitution, composite functions, equations, and exam-style problems.'
b = d.basic

# ---------------------------------------------------------------- 2.1-2.2 Basic concepts
d.sec('2.2-basic-concepts')
b('When does a function f have an inverse?', 'Exactly when f is ' + T('one-one and onto') + ' (bijective). Then f⁻¹ has domain = range of f and range = domain of f')
b('Why do the six trig functions have no inverse on their natural domains?', 'They are ' + T('periodic, so not one-one') + ' (sin 0 = sin π). So we restrict each to a piece where it is a bijection')
sm.inv_restrict_sine(d)
b('What is a “branch” of an inverse trig function? What is the principal value branch?', 'Each restriction interval (e.g. [−π/2, π/2], [π/2, 3π/2], …) gives a different branch. The branch with the ' + T('range containing 0 / the smallest positive angles') + ' is the principal value branch. Unless told otherwise we always use it')
table_card(d, 'Principal value branches', 'Give the domain and the range (principal value branch) of each function.', [
    ('sin⁻¹', 'domain [−1, 1] → range [−π/2, π/2]', False),
    ('cos⁻¹', 'domain [−1, 1] → range [0, π]', False),
    ('tan⁻¹', 'domain R → range (−π/2, π/2)', False),
    ('cot⁻¹', 'domain R → range (0, π)', False),
    ('sec⁻¹', 'domain R − (−1, 1) → range [0, π] − {π/2}', False),
    ('cosec⁻¹', 'domain R − (−1, 1) → range [−π/2, π/2] − {0}', False)], term='Domains and ranges of inverse trig functions',
    note='Domain of f⁻¹ = range of f; range of f⁻¹ = restricted domain of f')
sm.principal_arcs(d)
b('Mnemonic: which inverse functions can give negative values?', T('sin⁻¹, tan⁻¹, cosec⁻¹') + ' (range in [−π/2, π/2]). ' + T('cos⁻¹, cot⁻¹, sec⁻¹') + ' are never negative (range in [0, π]). The “co-” functions cos⁻¹, cot⁻¹ share (0, π); sec⁻¹ follows cos⁻¹')
b('What is a “principal value”?', 'The value of an inverse trig function that lies in its ' + T('principal branch') + '.<br>Example: the principal value of sin⁻¹(½) is π/6, not 5π/6 or π/6 + 2π')
b('Trap: is sin⁻¹x the same as (sin x)⁻¹?', X('No') + '. sin⁻¹x = arcsin x is the inverse function. (sin x)⁻¹ = 1/sin x = cosec x. sin⁻¹(½) = π/6 but (sin ½)⁻¹ ≈ 2.09')
b('If y = sin⁻¹x, what can you say about sin y and about y?', 'sin y = x with ' + T('−π/2 ≤ y ≤ π/2') + ' (and x ∈ [−1, 1]). Always check the range of y: that is what makes the answer unique')
b('Ex 2.1 Q13: If sin⁻¹x = y, then (A) 0 ≤ y ≤ π (B) −π/2 ≤ y ≤ π/2 (C) 0 < y < π (D) −π/2 < y < π/2', 'The range of sin⁻¹ is the closed interval: ' + E('(B)'))
b('Which inverse trig functions have gaps in the range, and where?', T('sec⁻¹') + ' never equals π/2 (sec y = ∞ there)<br>' + T('cosec⁻¹') + ' never equals 0<br>' + T('tan⁻¹') + ' never reaches ±π/2<br>' + T('cot⁻¹') + ' never reaches 0 or π')

d.sec('2.2-graphs')
sm.sin_inverse_mirror(d)
b('How is the graph of f⁻¹ obtained from the graph of f?', 'Reflect in the line ' + T('y = x') + ': (a, b) on f ↔ (b, a) on f⁻¹. That also swaps domain and range')
sm.inverse_graphs(d)
b('Which inverse trig graphs are increasing? Decreasing?', T('Increasing') + ': sin⁻¹, tan⁻¹, and sec⁻¹ on each of its two branches. ' + T('Decreasing') + ': cos⁻¹, cot⁻¹, and cosec⁻¹ on each of its two branches. Sanity check: cos⁻¹ and cot⁻¹ fall from π to 0')
b('Which inverse trig functions are odd, which are not?', T('Odd') + ': sin⁻¹, tan⁻¹, cosec⁻¹<br>' + T('Neither even nor odd') + ': cos⁻¹, cot⁻¹, sec⁻¹<br>These satisfy f(−x) = π − f(x), i.e. symmetric about the point (0, π/2)')
b('Which inverse trig functions have horizontal asymptotes?', T('tan⁻¹') + ': y = ±π/2. ' + T('cot⁻¹') + ': y = 0 and y = π. ' + T('sec⁻¹') + ': y = π/2. ' + T('cosec⁻¹') + ': y = 0. sin⁻¹ and cos⁻¹ have none (bounded domain)')
sm.inverse_complementary(d)

# ---------------------------------------------------------------- Standard values
d.sec('2.2-standard-values')
table_card(d, 'Standard principal values', 'Find the principal values.', [
    ('sin⁻¹(1/2)', 'π/6', False), ('sin⁻¹(−1/2)', '−π/6', False), ('cos⁻¹(1/2)', 'π/3', False), ('cos⁻¹(−1/2)', '2π/3', False),
    ('tan⁻¹(1)', 'π/4', False), ('tan⁻¹(−√3)', '−π/3', False), ('cot⁻¹(−1/√3)', '2π/3', False),
    ('sec⁻¹(2)', 'π/3', False), ('sec⁻¹(−2)', '2π/3', False), ('cosec⁻¹(−2)', '−π/6', False)], term='Standard principal values',
    note='Use the branch: a negative argument gives a negative answer for sin⁻¹, tan⁻¹, cosec⁻¹; and π − (positive value) for cos⁻¹, cot⁻¹, sec⁻¹')
b('Negative arguments: sin⁻¹(−x), tan⁻¹(−x), cosec⁻¹(−x)?', T('sin⁻¹(−x) = −sin⁻¹x') + ', ' + T('tan⁻¹(−x) = −tan⁻¹x') + ', ' + T('cosec⁻¹(−x) = −cosec⁻¹x') + ' (odd functions)')
b('Negative arguments: cos⁻¹(−x), cot⁻¹(−x), sec⁻¹(−x)?', T('cos⁻¹(−x) = π − cos⁻¹x') + ', ' + T('cot⁻¹(−x) = π − cot⁻¹x') + ', ' + T('sec⁻¹(−x) = π − sec⁻¹x') + '. Check: cos⁻¹(−½) = π − π/3 = 2π/3')
b('Reciprocal arguments: sin⁻¹(1/x), cos⁻¹(1/x), tan⁻¹(1/x)?', T('sin⁻¹(1/x) = cosec⁻¹x') + '<br>' + T('cos⁻¹(1/x) = sec⁻¹x') + '<br>(both for |x| ≥ 1)<br>' + T('tan⁻¹(1/x) = cot⁻¹x') + ' for x > 0 (for x < 0: cot⁻¹x − π)')
b('Example 1: principal value of sin⁻¹(1/√2)?', 'sin y = 1/√2 with y ∈ [−π/2, π/2]: ' + N('π/4'))
b('Example 2: principal value of cot⁻¹(−1/√3)?', 'cot⁻¹(−x) = π − cot⁻¹x = π − π/3 = ' + N('2π/3') + ' (range (0, π), cot 2π/3 = −1/√3 ✓)')
b('Ex 2.1 Q1: sin⁻¹(−1/2)?', 'Negative, in [−π/2, 0]: ' + N('−π/6'))
b('Ex 2.1 Q2: cos⁻¹(√3/2)?', 'cos π/6 = √3/2 and π/6 ∈ [0, π]: ' + N('π/6'))
b('Ex 2.1 Q3: cosec⁻¹(2)?', 'sin y = ½: ' + N('π/6') + ' (y ∈ [−π/2, π/2], y ≠ 0)')
b('Ex 2.1 Q4: tan⁻¹(−√3)?', 'tan⁻¹ is odd: −tan⁻¹√3 = ' + N('−π/3'))
b('Ex 2.1 Q5: cos⁻¹(−1/2)?', 'π − π/3 = ' + N('2π/3'))
b('Ex 2.1 Q6: tan⁻¹(−1)?', N('−π/4'))
b('Ex 2.1 Q7: sec⁻¹(2/√3)?', 'cos y = √3/2 → ' + N('π/6'))
b('Ex 2.1 Q8: cot⁻¹(√3)?', 'tan y = 1/√3, y ∈ (0, π): ' + N('π/6'))
b('Ex 2.1 Q9: cos⁻¹(−1/√2)?', 'π − π/4 = ' + N('3π/4'))
b('Ex 2.1 Q10: cosec⁻¹(−√2)?', '−cosec⁻¹√2 = ' + N('−π/4'))
b('Ex 2.1 Q11: tan⁻¹(1) + cos⁻¹(−1/2) + sin⁻¹(−1/2)?', 'π/4 + 2π/3 − π/6 = (3π + 8π − 2π)/12 = ' + N('3π/4'))
b('Ex 2.1 Q12: cos⁻¹(1/2) + 2 sin⁻¹(1/2)?', 'π/3 + 2(π/6) = ' + N('2π/3'))
b('Ex 2.1 Q14: tan⁻¹√3 − sec⁻¹(−2) = ? (A) π (B) −π/3 (C) π/3 (D) 2π/3', 'π/3 − (π − π/3) = π/3 − 2π/3 = ' + E('(B) −π/3'))

# ---------------------------------------------------------------- 2.3 Properties
d.sec('2.3-properties')
b('When is sin(sin⁻¹x) = x? When is sin⁻¹(sin x) = x?', 'sin(sin⁻¹x) = x for ' + T('x ∈ [−1, 1]') + ' (always safe)<br>sin⁻¹(sin x) = x only for ' + T('x ∈ [−π/2, π/2]') + '<br>Same pattern for the others, each with its own principal interval')
b('Which composite is always safe: f(f⁻¹(x)) or f⁻¹(f(x))?', T('f(f⁻¹(x)) = x') + ' whenever x is in the domain of f⁻¹. ' + T('f⁻¹(f(x)) = x') + ' only if x lies in the principal interval')
b('Example 6: sin⁻¹(sin 3π/5)?', '3π/5 ∉ [−π/2, π/2]. Use sin(3π/5) = sin(π − 3π/5) = sin(2π/5), and 2π/5 ∈ [−π/2, π/2]: ' + N('2π/5'))
table_card(d, 'sin⁻¹(sin θ) by intervals', 'Reduce sin⁻¹(sin θ) to a value in [−π/2, π/2].', [
    ('θ ∈ [−π/2, π/2]', 'θ', False), ('θ ∈ [π/2, 3π/2]', 'π − θ', False), ('θ ∈ [3π/2, 5π/2]', 'θ − 2π', False), ('θ ∈ [5π/2, 7π/2]', '3π − θ', False)],
    term='sin⁻¹(sin θ) reduction table', note='Sketch the zigzag graph if you forget: slope +1 then −1 alternately, period 2π')
sm._zig(d, 'sin')
sm._zig(d, 'cos')
sm._zig(d, 'tan')
b('Compute sin⁻¹(sin 10). (Radians)', '10 rad ∈ [5π/2, 7π/2] = [7.85, 10.99], so shift into [−π/2, π/2]:<br>' + N('3π − 10 ≈ −0.575') + '<br>Check: sin 10 ≈ −0.544 and sin(−0.575) ≈ −0.544')
b('Compute cos⁻¹(cos 10), tan⁻¹(tan 5).', 'cos⁻¹(cos 10) = 4π − 10 ≈ ' + N('2.566') + ' (in [0, π]). tan⁻¹(tan 5) = 5 − 2π ≈ ' + N('−1.283') + ' (in (−π/2, π/2))')
b('Compute cos⁻¹(cos 7π/6) and tan⁻¹(tan 7π/6). (Misc Q1, Q2 style)', 'cos⁻¹(cos 7π/6) = cos⁻¹(cos 5π/6) = ' + N('5π/6') + '. tan⁻¹(tan 7π/6) = tan⁻¹(tan π/6) = ' + N('π/6') + ' (tan has period π)')
b('Ex 2.2 Q10: sin⁻¹(sin 2π/3)?', 'sin(2π/3) = sin(π/3) = √3/2 → ' + N('π/3'))
b('Ex 2.2 Q11: tan⁻¹(tan 3π/4)?', 'tan(3π/4) = −1 → ' + N('−π/4'))
b('Ex 2.2 Q13: cos⁻¹(cos 7π/6)? (A) 7π/6 (B) 5π/6 (C) π/3 (D) π/6', '7π/6 ∉ [0, π]; cos(7π/6) = cos(2π − 7π/6) = cos(5π/6): ' + E('(B) 5π/6'))
b('Ex 2.2 Q14: sin[π/3 − sin⁻¹(−1/2)]? (A) 1/2 (B) 1/3 (C) 1/4 (D) 1', 'sin⁻¹(−½) = −π/6, so sin(π/3 + π/6) = sin(π/2) = ' + E('(D) 1'))
b('Ex 2.2 Q15: tan⁻¹√3 − cot⁻¹(−√3)? (A) π (B) −π/2 (C) 0 (D) 2√3', 'π/3 − (π − π/6) = π/3 − 5π/6 = ' + E('(B) −π/2'))
b('Ex 2.2 Q12: tan[sin⁻¹(3/5) + cot⁻¹(3/2)]?', 'tan A = 3/4, tan B = 2/3: (3/4 + 2/3)/(1 − 1/2) = (17/12)/(1/2) = ' + N('17/6'))
b('Find sin(cos⁻¹(3/5)) and tan(sin⁻¹(5/13)).', 'Triangle 3-4-5: sin = ' + N('4/5') + '<br>Triangle 5-12-13: tan = ' + N('5/12') + '<br>Method: draw the right triangle with the angle and read the ratio')
b('Method: evaluate trig(inverse trig(x)) such as sec²(tan⁻¹2) + cosec²(cot⁻¹3).', 'Use identities directly: sec²θ = 1 + tan²θ = 1 + 4 = 5; cosec²φ = 1 + cot²φ = 1 + 9 = 10. Total ' + N('15'))
b('Simplify cos(2 tan⁻¹(1/7)) and sin(2 tan⁻¹(1/3)).', 'With t = tan θ:<br>cos 2θ = (1 − t²)/(1 + t²) = (48/49)/(50/49) = ' + N('24/25') + '<br>sin 2θ = 2t/(1 + t²) = (2/3)/(10/9) = ' + N('3/5'))

d.sec('2.3-identities')
b('Double-angle forms of tan⁻¹: 2 tan⁻¹x = ?', T('sin⁻¹(2x/(1 + x²))') + ' for |x| ≤ 1;  ' + T('cos⁻¹((1 − x²)/(1 + x²))') + ' for x ≥ 0;  ' + T('tan⁻¹(2x/(1 − x²))') + ' for |x| < 1')
b('Example 3(i): prove sin⁻¹(2x√(1 − x²)) = 2 sin⁻¹x. For which x is it valid?', 'x = sin θ: sin⁻¹(2 sin θ cos θ) = sin⁻¹(sin 2θ) = 2θ<br>Valid only if 2θ ∈ [−π/2, π/2], that is ' + T('−1/√2 ≤ x ≤ 1/√2') + '<br>Outside this range the result changes (see the next card)')
b('Example 3(ii): sin⁻¹(2x√(1 − x²)) = 2 cos⁻¹x for which x?', 'x = cos θ: sin⁻¹(sin 2θ) = 2θ needs 2θ ∈ [0, π/2] (x ≥ 0), so it holds for ' + T('1/√2 ≤ x ≤ 1') + '<br>Consistency: there sin⁻¹(2x√(1 − x²)) = π − 2 sin⁻¹x = 2 cos⁻¹x')
b('Triple-angle forms: 3 sin⁻¹x = ? 3 cos⁻¹x = ? 3 tan⁻¹x = ?', T('3 sin⁻¹x = sin⁻¹(3x − 4x³)') + ' for x ∈ [−½, ½];  ' + T('3 cos⁻¹x = cos⁻¹(4x³ − 3x)') + ' for x ∈ [½, 1];  ' + T('3 tan⁻¹x = tan⁻¹((3x − x³)/(1 − 3x²))') + ' for |x| < 1/√3')
b('Ex 2.2 Q1: prove 3 sin⁻¹x = sin⁻¹(3x − 4x³), x ∈ [−½, ½].', 'x = sin θ, θ ∈ [−π/6, π/6]. sin⁻¹(3 sin θ − 4 sin³θ) = sin⁻¹(sin 3θ) = 3θ, since 3θ ∈ [−π/2, π/2]. ' + N('= 3 sin⁻¹x'))
b('Ex 2.2 Q2: prove 3 cos⁻¹x = cos⁻¹(4x³ − 3x), x ∈ [½, 1].', 'x = cos θ, θ ∈ [0, π/3]. cos⁻¹(4cos³θ − 3cos θ) = cos⁻¹(cos 3θ) = 3θ since 3θ ∈ [0, π]. ' + N('= 3 cos⁻¹x'))
b('Sum formula for tan⁻¹: tan⁻¹x + tan⁻¹y = ?', T('tan⁻¹((x + y)/(1 − xy))') + ' if xy < 1<br>' + T('π + tan⁻¹((x + y)/(1 − xy))') + ' if xy > 1 and x, y > 0<br>' + T('−π + …') + ' if xy > 1 and x, y < 0')
sm.tan_sum_circle(d)
b('Difference formula for tan⁻¹: tan⁻¹x − tan⁻¹y = ?', T('tan⁻¹((x − y)/(1 + xy))') + ', valid for xy > −1')
b('sin⁻¹x + sin⁻¹y = ? and cos⁻¹x + cos⁻¹y = ? (standard forms)', T('sin⁻¹(x√(1 − y²) + y√(1 − x²))') + ' when the sum lies in [−π/2, π/2]; ' + T('cos⁻¹(xy − √(1 − x²)√(1 − y²))') + ' when x + y ≥ 0')
b('Prove tan⁻¹(1/2) + tan⁻¹(1/3) = π/4.', 'xy = 1/6 < 1: tan⁻¹((½ + ⅓)/(1 − 1/6)) = tan⁻¹((5/6)/(5/6)) = tan⁻¹1 = ' + N('π/4'))
b('Prove tan⁻¹1 + tan⁻¹2 + tan⁻¹3 = π.', 'tan⁻¹2 + tan⁻¹3 = 3π/4 (xy = 6 > 1, add π to tan⁻¹(−1)); plus π/4 = ' + N('π'))
b('Machin-type: 4 tan⁻¹(1/5) − tan⁻¹(1/239) = ?', N('π/4') + '. 2 tan⁻¹(1/5) = tan⁻¹(5/12), 4 tan⁻¹(1/5) = tan⁻¹(120/119); subtract tan⁻¹(1/239) to get tan⁻¹1')
b('Telescoping: Σ tan⁻¹(1/(n² + n + 1)) for n = 1 to ∞?', 'tan⁻¹(1/(1 + n(n + 1))) = tan⁻¹(n + 1) − tan⁻¹n. Sum = lim tan⁻¹(N + 1) − tan⁻¹1 = π/2 − π/4 = ' + N('π/4'))
b('Trap: is sin⁻¹x + sin⁻¹y always sin⁻¹(x√(1−y²) + y√(1−x²))?', X('No') + '. For x = y = 1: sin⁻¹1 + sin⁻¹1 = π, but the right side is sin⁻¹(0) = 0. The formula needs the sum to stay in [−π/2, π/2]')

d.sec('2.3-simplification')
table_card(d, 'Substitutions', 'Which substitution simplifies each expression?', [
    ('√(1 − x²)', 'x = sin θ (or cos θ)', False), ('√(1 + x²)', 'x = tan θ', False), ('√(x² − 1)', 'x = sec θ', False),
    ('√(a² − x²)', 'x = a sin θ', False), ('√(a² + x²)', 'x = a tan θ', False), ('√((1 − x)/(1 + x)), √(1 + x) ± √(1 − x)', 'x = cos 2θ', False),
    ('(2x)/(1 + x²), (1 − x²)/(1 + x²)', 'x = tan θ (gives sin 2θ, cos 2θ)', False), ('3x − 4x³, 4x³ − 3x', 'x = sin θ / cos θ (gives sin 3θ, cos 3θ)', False)], term='Substitutions for simplifying inverse trig expressions',
    note='After substituting, use an identity to get one trig function of a multiple angle, then cancel with the inverse. Always check the interval')
b('Example 4: write tan⁻¹(cos x/(1 − sin x)), −3π/2 < x < π/2, in simplest form.', 'cos x/(1 − sin x) = (cos²(x/2) − sin²(x/2))/(cos(x/2) − sin(x/2))² = (cos(x/2) + sin(x/2))/(cos(x/2) − sin(x/2)) = tan(π/4 + x/2). Since π/4 + x/2 ∈ (−π/2, π/2): ' + N('π/4 + x/2'))
b('Example 5: write cot⁻¹(1/√(x² − 1)), x > 1, in simplest form.', 'x = sec θ: √(x² − 1) = tan θ so cot⁻¹(cot θ) = θ = ' + N('sec⁻¹x'))
b('Ex 2.2 Q3: simplify tan⁻¹((√(1 + x²) − 1)/x), x ≠ 0.', 'x = tan θ: (sec θ − 1)/tan θ = (1 − cos θ)/sin θ = tan(θ/2). So ' + N('½ tan⁻¹x'))
b('Ex 2.2 Q4: simplify tan⁻¹√((1 − cos x)/(1 + cos x)), 0 < x < π.', '(1 − cos x)/(1 + cos x) = tan²(x/2): tan⁻¹(tan(x/2)) = ' + N('x/2') + ' (x/2 ∈ (0, π/2))')
b('Ex 2.2 Q5: simplify tan⁻¹((cos x − sin x)/(cos x + sin x)), −π/4 < x < 3π/4.', 'Divide by cos x: (1 − tan x)/(1 + tan x) = tan(π/4 − x), and π/4 − x ∈ (−π/2, π/2): ' + N('π/4 − x'))
b('Ex 2.2 Q6: simplify tan⁻¹(x/√(a² − x²)), |x| < a.', 'x = a sin θ: tan⁻¹(sin θ/cos θ) = θ = ' + N('sin⁻¹(x/a)'))
b('Ex 2.2 Q7: simplify tan⁻¹((3a²x − x³)/(a³ − 3ax²)), a > 0, −a/√3 < x < a/√3.', 'x = a tan θ: (3 tan θ − tan³θ)/(1 − 3 tan²θ) = tan 3θ, and 3θ ∈ (−π/2, π/2): ' + N('3 tan⁻¹(x/a)'))
b('Ex 2.2 Q8: tan⁻¹[2 cos(2 sin⁻¹(1/2))]?', '2 sin⁻¹(½) = π/3, 2 cos(π/3) = 1, tan⁻¹1 = ' + N('π/4'))
b('Ex 2.2 Q9: tan ½[sin⁻¹(2x/(1 + x²)) + cos⁻¹((1 − y²)/(1 + y²))], |x| < 1, y > 0, xy < 1?', 'sin⁻¹(2x/(1 + x²)) = 2 tan⁻¹x and cos⁻¹((1 − y²)/(1 + y²)) = 2 tan⁻¹y. So tan(tan⁻¹x + tan⁻¹y) = ' + N('(x + y)/(1 − xy)'))
b('Simplify tan⁻¹(√(1 + x²) − x).', 'x = tan θ, θ ∈ (−π/2, π/2): sec θ − tan θ = (1 − sin θ)/cos θ = tan(π/4 − θ/2), and π/4 − θ/2 ∈ (0, π/2). So ' + N('π/4 − ½ tan⁻¹x'))
b('Simplify sin⁻¹(2x/(1 + x²)) for x ≥ 1 (a common trap).', 'x = tan θ with θ ∈ [π/4, π/2), so 2θ ∈ [π/2, π):<br>sin⁻¹(sin 2θ) = π − 2θ = ' + N('π − 2 tan⁻¹x') + '<br>' + X('Trap') + ': 2 tan⁻¹x holds only for |x| ≤ 1')
b('Simplify cos⁻¹((1 − x²)/(1 + x²)) for x ≥ 0 and for x < 0.', 'x ≥ 0: ' + N('2 tan⁻¹x') + '. x < 0: the value must be ≥ 0, so ' + N('−2 tan⁻¹x') + ' (= 2 tan⁻¹|x|)')

d.sec('2.3-miscellaneous')
b('Misc Q1: cos⁻¹(cos 13π/6)?', '13π/6 = 2π + π/6, so cos(13π/6) = cos(π/6): ' + N('π/6'))
b('Misc Q2: tan⁻¹(tan 7π/6)?', 'tan(7π/6) = tan(π/6): ' + N('π/6'))
b('Misc Q3: prove 2 sin⁻¹(3/5) = tan⁻¹(24/7).', 'sin θ = 3/5 → tan θ = 3/4. tan 2θ = (3/2)/(1 − 9/16) = 24/7, and 2θ < π/2 (θ ≈ 36.9°). ' + E('✓'))
b('Misc Q4: prove sin⁻¹(8/17) + sin⁻¹(3/5) = tan⁻¹(77/36).', 'tan A = 8/15, tan B = 3/4: (8/15 + 3/4)/(1 − 2/5) = (77/60)/(3/5) = 77/36, and A + B < π/2. ' + E('✓'))
b('Misc Q5: prove cos⁻¹(4/5) + cos⁻¹(12/13) = cos⁻¹(33/65).', 'cos(A + B) = (4/5)(12/13) − (3/5)(5/13) = (48 − 15)/65 = 33/65, and A + B ∈ [0, π]. ' + E('✓'))
b('Misc Q6: prove cos⁻¹(12/13) + sin⁻¹(3/5) = sin⁻¹(56/65).', 'sin(A + B) = (5/13)(4/5) + (12/13)(3/5) = (20 + 36)/65 = 56/65, and A + B < π/2. ' + E('✓'))
b('Misc Q7: prove tan⁻¹(63/16) = sin⁻¹(5/13) + cos⁻¹(3/5).', 'tan A = 5/12, tan B = 4/3: (5/12 + 4/3)/(1 − 5/9) = (21/12)/(4/9) = 63/16, A + B ∈ (0, π/2). ' + E('✓'))
b('Misc Q8: prove tan⁻¹√x = ½ cos⁻¹((1 − x)/(1 + x)), x ∈ [0, 1].', 'x = tan²θ: (1 − tan²θ)/(1 + tan²θ) = cos 2θ, and cos⁻¹(cos 2θ) = 2θ since 2θ ∈ [0, π/2]. So RHS = θ = tan⁻¹√x. ' + E('✓'))
b('Misc Q9: prove cot⁻¹((√(1 + sin x) + √(1 − sin x))/(√(1 + sin x) − √(1 − sin x))) = x/2, x ∈ (0, π/4).', 'Write 1 ± sin x = (cos(x/2) ± sin(x/2))². The fraction becomes 2cos(x/2)/2sin(x/2) = cot(x/2), and x/2 ∈ (0, π/8). ' + E('✓'))
b('Misc Q10: prove tan⁻¹((√(1 + x) − √(1 − x))/(√(1 + x) + √(1 − x))) = π/4 − ½ cos⁻¹x, −1/√2 ≤ x ≤ 1.', 'x = cos 2θ: √(1 + x) = √2 cos θ, √(1 − x) = √2 sin θ. Ratio (cos θ − sin θ)/(cos θ + sin θ) = tan(π/4 − θ). Answer π/4 − θ = ' + N('π/4 − ½ cos⁻¹x'))
b('Misc Q11: solve 2 tan⁻¹(cos x) = tan⁻¹(2 cosec x).', 'tan(2A) = 2cos x/(1 − cos²x) = 2 cos x/sin²x. Set equal to 2/sin x: cos x = sin x. ' + N('x = nπ + π/4') + ' (n ∈ Z)')
b('Misc Q12: solve tan⁻¹((1 − x)/(1 + x)) = ½ tan⁻¹x, x > 0.', 'LHS = π/4 − tan⁻¹x, so π/4 = (3/2) tan⁻¹x, tan⁻¹x = π/6: ' + N('x = 1/√3'))
b('Misc Q13: sin(tan⁻¹x), |x| < 1, equals (A) x/√(1 − x²) (B) 1/√(1 − x²) (C) 1/√(1 + x²) (D) x/√(1 + x²)', 'Triangle with legs x and 1, hypotenuse √(1 + x²): sin = ' + E('(D) x/√(1 + x²)'))
b('Misc Q14: sin⁻¹(1 − x) − 2 sin⁻¹x = π/2, then x = (A) 0, ½ (B) 1, ½ (C) 0 (D) ½', 'Let θ = sin⁻¹x: sin⁻¹(1 − x) = π/2 + 2θ, so 1 − x = cos 2θ = 1 − 2x².<br>That gives x(2x − 1) = 0.<br>x = ½ fails: sin⁻¹(½) − π/3 = −π/6 ≠ π/2.<br>x = 0 works: ' + E('(C) 0'))

# ---------------------------------------------------------------- Beyond: domain, range, equations
d.sec('2.z-domain-range-equations')
b('Domain of sin⁻¹(2x − 1)?', '−1 ≤ 2x − 1 ≤ 1 → ' + N('0 ≤ x ≤ 1'))
b('Domain of cos⁻¹(x² − 4)?', '−1 ≤ x² − 4 ≤ 1 → 3 ≤ x² ≤ 5 → ' + N('x ∈ [−√5, −√3] ∪ [√3, √5]'))
b('Domain of sec⁻¹(2x + 1)?', '|2x + 1| ≥ 1 → 2x + 1 ≥ 1 or ≤ −1 → ' + N('x ≥ 0 or x ≤ −1'))
b('Range of f(x) = sin⁻¹x + cos⁻¹x + tan⁻¹x?', 'sin⁻¹x + cos⁻¹x = π/2 on [−1, 1], so f = π/2 + tan⁻¹x with range ' + N('[π/4, 3π/4]'))
b('Range of f(x) = 2 sin⁻¹x + cos⁻¹x?', 'f = sin⁻¹x + π/2, x ∈ [−1, 1]: ' + N('[0, π]'))
b('Range of f(x) = cos⁻¹x − sin⁻¹x?', 'f = π/2 − 2 sin⁻¹x for x ∈ [−1, 1], and sin⁻¹x ∈ [−π/2, π/2]: ' + N('[−π/2, 3π/2]'))
b('Solve sin⁻¹x + sin⁻¹(1 − x) = cos⁻¹x.', 'sin⁻¹(1 − x) = cos⁻¹x − sin⁻¹x = π/2 − 2 sin⁻¹x. Take sine: 1 − x = cos(2 sin⁻¹x) = 1 − 2x², so x(2x − 1) = 0. Both check: x = 0 gives π/2 = π/2; x = ½ gives π/6 + π/6 = π/3 = cos⁻¹½. ' + N('x = 0 or ½'))
b('Solve tan⁻¹(x − 1) + tan⁻¹x + tan⁻¹(x + 1) = tan⁻¹3x.', 'tan⁻¹(x − 1) + tan⁻¹(x + 1) = tan⁻¹(2x/(2 − x²)). Adding tan⁻¹x and equating tan: x = 0 or ' + N('x = ±1/2') + '. All three satisfy the original')
b('Solve cos(2 sin⁻¹x) = 1/9.', 'cos 2θ = 1 − 2x² = 1/9 → x² = 4/9 → ' + N('x = ±2/3'))
b('Solve 2 tan⁻¹(sin x) = tan⁻¹(2 sec x).', 'tan(2A) = 2 sin x/(1 − sin²x) = 2 sin x/cos²x = 2/cos x → sin x = cos x: ' + N('x = π/4') + ' in (−π/2, π/2)')
b('Find the number of real solutions of tan⁻¹√(x(x + 1)) + sin⁻¹√(x² + x + 1) = π/2.', 'The second root needs x² + x + 1 ≤ 1, i.e. x² + x ≤ 0, while the first needs x² + x ≥ 0. So x² + x = 0: ' + N('x = 0 or x = −1') + ', and both give 0 + π/2 = π/2. Answer: 2 solutions')
b('If sin⁻¹x + sin⁻¹y + sin⁻¹z = 3π/2, find x + y + z.', 'Each term is at most π/2, so all three must equal π/2: x = y = z = 1. Hence ' + N('x + y + z = 3'))
b('If tan⁻¹x + tan⁻¹y + tan⁻¹z = π then x + y + z = ?', 'tan(A + B + C) = 0 → ' + N('x + y + z = xyz'))

# ---------------------------------------------------------------- How it is asked
d.sec('2.z-how-its-asked')
b('MCQ: sin⁻¹(sin 5π/6) =<br>(a) 5π/6 (b) π/6 (c) −π/6 (d) 7π/6', 'sin(5π/6) = sin(π/6): ' + E('(b) π/6'))
b('MCQ: cos⁻¹(−1/2) − sin⁻¹(−1/2) =<br>(a) π/2 (b) 5π/6 (c) 2π/3 (d) π', '2π/3 + π/6 = ' + E('(b) 5π/6'))
b('MCQ: tan⁻¹(1) + tan⁻¹(2) + tan⁻¹(3) =<br>(a) π (b) π/2 (c) 3π/4 (d) 0', E('(a) π'))
b('MCQ: sin⁻¹(1/2) + cos⁻¹(1/2) =<br>(a) π/6 (b) π/3 (c) π/2 (d) 2π/3', 'Complementary: ' + E('(c) π/2'))
b('MCQ: the principal value of cosec⁻¹(−2) is<br>(a) π/6 (b) −π/6 (c) −π/3 (d) 5π/6', 'cosec⁻¹ is odd: ' + E('(b) −π/6'))
b('MCQ: the domain of sin⁻¹(3x − 1) is<br>(a) [0, 2/3] (b) [−2/3, 0] (c) [0, 1] (d) R', '−1 ≤ 3x − 1 ≤ 1 → 0 ≤ x ≤ 2/3: ' + E('(a)'))
b('MCQ: cos(sin⁻¹(3/5) + cos⁻¹(3/5)) =<br>(a) 1 (b) 0 (c) 24/25 (d) 7/25', 'sum = π/2, cos = ' + E('(b) 0'))
b('MCQ: tan(2 tan⁻¹(1/5) − π/4) =<br>(a) 7/17 (b) −7/17 (c) 5/12 (d) 17/7', 'tan 2θ = (2/5)/(24/25) = 5/12; (5/12 − 1)/(1 + 5/12) = (−7/12)/(17/12) = ' + E('(b) −7/17'))
b('MCQ: sin⁻¹x + cos⁻¹x + cot⁻¹x + tan⁻¹x for x > 0 =<br>(a) π (b) π/2 (c) 2π (d) 0', 'sin⁻¹x + cos⁻¹x = π/2 and tan⁻¹x + cot⁻¹x = π/2: ' + E('(a) π'))
b('MCQ: sin⁻¹(x) + sin⁻¹(1 − x) = cos⁻¹x has a solution x =<br>(a) 1 (b) 0 (c) 1/2 (d) both (b) and (c)', 'x = 0: 0 + π/2 = π/2 ✓. x = ½: π/6 + π/6 = π/3 ✓. ' + E('(d)') + ' (x = 1 fails: π/2 + 0 ≠ 0)')
b('MCQ: the value of tan⁻¹2 + tan⁻¹3 is<br>(a) π/4 (b) 3π/4 (c) −π/4 (d) π/2', 'xy = 6 > 1, so add π to tan⁻¹(−1): ' + E('(b) 3π/4'))
b('Integer answer (JEE Main): the value of 12 (sin⁻¹(1/2) + tan⁻¹(1/√3) + cos⁻¹(1/2))/π is?', '(π/6 + π/6 + π/3) × 12/π = (2π/3)(12/π) = ' + N('8'))
b('Integer answer: if tan⁻¹x + tan⁻¹(1/2) = π/4, then 3x =?', 'x = tan(π/4 − tan⁻¹(1/2)) = (1 − 1/2)/(1 + 1/2) = 1/3, so 3x = ' + N('1'))
b('Assertion–Reason.<br><b>A:</b> sin⁻¹(sin 2π/3) = 2π/3.<br><b>R:</b> sin⁻¹(sin x) = x for all x ∈ R.<br>(a) Both true, R explains A (b) Both true, R does not (c) A false, R false (d) A true, R false', E('(c)') + ': sin⁻¹(sin 2π/3) = π/3, and sin⁻¹(sin x) = x only for x ∈ [−π/2, π/2]')
b('Assertion–Reason.<br><b>A:</b> tan⁻¹x + cot⁻¹x = π/2 for all real x.<br><b>R:</b> tan⁻¹x and cot⁻¹x are complementary angles for every x.<br>(a) Both true, R explains A (b) Both true, R does not (c) A true, R false (d) A false, R true', E('(a)') + ': for x > 0 the right-triangle picture; for x < 0 also true since tan⁻¹(−x) = −tan⁻¹x and cot⁻¹(−x) = π − cot⁻¹x')
b('True/False: cos⁻¹(−x) = −cos⁻¹x.', X('False') + '. cos⁻¹(−x) = π − cos⁻¹x (cos⁻¹ takes only values in [0, π])')
b('True/False: tan⁻¹x has range [−π/2, π/2].', X('False') + '. The range is the open interval (−π/2, π/2)')
b('2-mark: find the principal value of sin⁻¹(−√3/2) + cos⁻¹(−√3/2).', 'sin⁻¹(−√3/2) = −π/3; cos⁻¹(−√3/2) = 5π/6. Sum ' + N('π/2') + ' (also directly from sin⁻¹t + cos⁻¹t = π/2)')
b('3-mark: prove tan⁻¹(1/4) + tan⁻¹(2/9) = ½ cos⁻¹(3/5).', 'LHS: (1/4 + 2/9)/(1 − 1/18) = (17/36)/(17/18) = ½, so LHS = tan⁻¹(½). RHS: cos 2θ = 3/5 → tan²θ = (1 − 3/5)/(1 + 3/5) = ¼ → tan θ = ½. ' + E('✓'))
b('3-mark: prove sin⁻¹(3/5) − sin⁻¹(8/17) = cos⁻¹(84/85).', 'A = sin⁻¹(3/5), B = sin⁻¹(8/17)<br>cos(A − B) = (4/5)(15/17) + (3/5)(8/17) = (60 + 24)/85 = 84/85<br>A − B ∈ [0, π], so A − B = cos⁻¹(84/85). ' + E('✓'))
b('4-mark: find the value of x if tan⁻¹(2x) + tan⁻¹(3x) = π/4.', '(5x)/(1 − 6x²) = 1 → 6x² + 5x − 1 = 0 → x = 1/6 or x = −1<br>x = −1 fails: both terms are negative, so the sum ≠ π/4<br>' + N('x = 1/6'))
b('4-mark: prove that cos⁻¹(x) + cos⁻¹((x/2) + (√(3 − 3x²))/2) = π/3, x ∈ [½, 1].', 'x = cos θ, θ ∈ [0, π/3]<br>The second argument is (cos θ)/2 + (√3/2) sin θ = cos(θ − π/3)<br>π/3 − θ ∈ [0, π/3], so it gives π/3 − θ<br>Sum ' + E('π/3 ✓'))
b('Case-based: a 2 m tall screen has its lower edge 1 m above your eye level, at horizontal distance d. The viewing angle is tan⁻¹(3/d) − tan⁻¹(1/d). Find it for d = 3 m.', 'tan⁻¹(1) − tan⁻¹(1/3) = tan⁻¹((1 − 1/3)/(1 + 1/3)) = tan⁻¹(½) ≈ ' + N('26.6°') + '<br>The angle is largest at d = √3 m, where the two tangents multiply to 1')


print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
