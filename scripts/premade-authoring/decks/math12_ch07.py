import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_math as sm
import math12_ch07_data as data

bad = data.verify()
assert not bad, bad

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Mathematics', 'class12-mathematics-ch07-integrals')
d = Deck('Chapter 7: Integrals', 'Class 12', ['class-12', 'mathematics', 'ch-7'])
d.description = 'Antiderivatives, substitution, trigonometric identities, standard forms, partial fractions, integration by parts, definite integrals, the fundamental theorems and properties, with every exercise verified.'
b = d.basic


def ind_cards(prefix):
    for tag, q, ans, hint, f, F, pts in data.IND:
        if tag.startswith(prefix):
            b(tag + ': ' + q, N(ans) + '<br><small>' + hint + '</small>')


def def_cards(prefix):
    for tag, q, ans, hint, f, lo, hi, val, chk in data.DEF:
        if tag.startswith(prefix):
            b(tag + ': ' + q, N(ans) + '<br><small>' + hint + '</small>')


# ---------------------------------------------------------------- 7.2 Concepts
d.sec('7.2-integration-basics')
b('What is integration?', 'The ' + T('inverse process of differentiation') + ': given f, find F with F′ = f. Then ∫ f(x) dx = F(x) + C')
b('What is the “+ C”?', 'The ' + T('constant of integration') + ': F(x) + C is also an antiderivative for every constant C. So an indefinite integral is a family of curves, all vertical translates of one another')
b('Standard integrals to memorise (algebraic and exponential).', '∫xⁿ dx = xⁿ⁺¹/(n + 1) (n ≠ −1); ∫ 1/x dx = log|x|; ∫ eˣ dx = eˣ; ∫ aˣ dx = aˣ/log a; ∫ dx = x')
b('Standard integrals to memorise (trigonometric).', '∫ sin x = −cos x; ∫ cos x = sin x; ∫ sec²x = tan x; ∫ cosec²x = −cot x; ∫ sec x tan x = sec x; ∫ cosec x cot x = −cosec x; ∫ tan x = log|sec x|; ∫ cot x = log|sin x|; ∫ sec x = log|sec x + tan x|; ∫ cosec x = log|cosec x − cot x|')
b('Standard integrals to memorise (inverse trig).', '∫ dx/√(1 − x²) = sin⁻¹x; ∫ dx/(1 + x²) = tan⁻¹x; ∫ dx/(x√(x² − 1)) = sec⁻¹x')
b('Linearity of the integral?', T('∫[k₁f + k₂g] = k₁∫f + k₂∫g') + '. But ∫ f·g ≠ ∫f · ∫g and ∫ f/g ≠ ∫f/∫g')
b('Trap: ∫ (fg) dx = (∫ f dx)(∫ g dx)?', X('False') + '. Example: ∫ x·x dx = x³/3 but (∫x dx)² = x⁴/4. Use substitution or parts for products')
b('How do you check an integral?', T('Differentiate your answer') + ': it must give back the integrand. Every exercise card in this deck was checked that way by computer')
b('Remark: does every function have an elementary antiderivative?', X('No') + ': ∫ e^(−x²) dx, ∫ sin x/x dx, ∫ √(1 + x³) dx cannot be written with elementary functions, though the antiderivatives exist')
b('Integration methods: overview.', '1) Inspection/standard forms. 2) ' + T('Substitution') + ' (when the integrand contains f(g(x)) g′(x)). 3) ' + T('Trigonometric identities') + '. 4) ' + T('Partial fractions') + ' for rational functions. 5) ' + T('By parts') + ' for products. Special forms: ∫ dx/(ax² + bx + c), ∫ (px + q)/(ax² + bx + c), ∫ √(ax² + bx + c)')
d.sec('7.2-exercise-7-1')
ind_cards('Ex 7.1')
b('Ex 7.1 Q21: an antiderivative of (√x + 1/√x) is (A) ⅓x^(1/3) + 2x^(1/2) (B) ⅔x^(2/3) + ½x² (C) ⅔x^(3/2) + 2x^(1/2) (D) (3/2)x^(3/2) + ½x^(1/2)', 'x^(1/2) → ⅔x^(3/2); x^(−1/2) → 2x^(1/2). ' + E('(C)'))
b('Ex 7.1 Q22: d/dx f(x) = 4x³ − 3/x⁴ with f(2) = 0. Then f(x) = ?', 'f = x⁴ + 1/x³ + C. f(2) = 16 + 1/8 + C = 0 → C = −129/8. ' + E('(A) x⁴ + 1/x³ − 129/8'))

# ---------------------------------------------------------------- 7.3 Methods
d.sec('7.3-substitution-theory')
b('Integration by substitution: idea.', 'Put ' + T('t = g(x)') + ', dt = g′(x) dx, so ∫ f(g(x)) g′(x) dx = ∫ f(t) dt. Choose t as the “inside” whose derivative also appears (up to a constant). Return to x at the end')
b('Which substitution for which pattern?', T('f′(x)/f(x)') + ' → log|f|. ' + T('f′(x)[f(x)]ⁿ') + ' → fⁿ⁺¹/(n + 1). ' + T('e^(f)f′') + ' → e^f. ' + T('√(ax + b)') + ' → t = ax + b or t² = ax + b. ' + T('sinⁿ cos (odd power)') + ' → t = the other function')
b('∫ tan x dx, ∫ cot x dx?', T('log|sec x|') + ' (= −log|cos x|) and ' + T('log|sin x|') + '. tan x = sin x/cos x: t = cos x')
b('∫ sec x dx and ∫ cosec x dx?', T('log|sec x + tan x|') + ' and ' + T('log|cosec x − cot x|') + '. Multiply by (sec x + tan x)/(sec x + tan x)')
b('Example: ∫ sin³x dx and ∫ cos²x dx?', 'sin³x = sin x(1 − cos²x), t = cos x: ' + N('−cos x + cos³x/3') + '. cos²x = (1 + cos 2x)/2: ' + N('x/2 + sin 2x/4'))
b('Trig identities most used in integration.', 'sin²θ = (1 − cos 2θ)/2; cos²θ = (1 + cos 2θ)/2; 2 sin A cos B = sin(A + B) + sin(A − B); 2 cos A cos B = cos(A + B) + cos(A − B); 2 sin A sin B = cos(A − B) − cos(A + B)')
d.sec('7.3-exercise-7-2')
ind_cards('Ex 7.2')
d.sec('7.3-exercise-7-3')
ind_cards('Ex 7.3')

# ---------------------------------------------------------------- 7.4 Standard forms
d.sec('7.4-standard-forms-theory')
b('Six standard integrals of the form 1/(x² ± a²).', '∫ dx/(x² − a²) = (1/2a) log|(x − a)/(x + a)|; ∫ dx/(a² − x²) = (1/2a) log|(a + x)/(a − x)|; ∫ dx/(x² + a²) = (1/a) tan⁻¹(x/a); ∫ dx/√(x² − a²) = log|x + √(x² − a²)|; ∫ dx/√(a² − x²) = sin⁻¹(x/a); ∫ dx/√(x² + a²) = log|x + √(x² + a²)|')
b('How do you integrate 1/(ax² + bx + c) or 1/√(ax² + bx + c)?', T('Complete the square') + ' to get (x + p)² ± q², then use the standard form with t = x + p')
b('How do you integrate (px + q)/(ax² + bx + c) or (px + q)/√(ax² + bx + c)?', 'Write px + q = ' + T('A (derivative of the denominator or radicand) + B') + '. The A-part gives log or a square root; the B-part is a standard form after completing the square')
d.sec('7.4-exercise-7-4')
ind_cards('Ex 7.4')

# ---------------------------------------------------------------- 7.5 Partial fractions
d.sec('7.5-partial-fractions-theory')
b('When do you use partial fractions?', 'For a rational function P(x)/Q(x). If deg P ≥ deg Q, ' + T('divide first') + ' (polynomial + proper fraction); then factor Q and split')
table_card(d, 'Partial fractions · forms', 'Write the form of the partial fractions.', [
    ('(px + q)/((x − a)(x − b))', 'A/(x − a) + B/(x − b)', False),
    ('(px + q)/(x − a)²', 'A/(x − a) + B/(x − a)²', False),
    ('(px² + qx + r)/((x − a)(x − b)(x − c))', 'A/(x − a) + B/(x − b) + C/(x − c)', False),
    ('(px² + qx + r)/((x − a)²(x − b))', 'A/(x − a) + B/(x − a)² + C/(x − b)', False),
    ('(px² + qx + r)/((x − a)(x² + bx + c))', 'A/(x − a) + (Bx + C)/(x² + bx + c)', False)], term='Forms of partial fractions', note='An irreducible quadratic gets a linear numerator; a repeated factor gets one term per power')
b('Quick way to find A, B, C (cover-up).', 'For a simple factor (x − a): ' + T('A = value of the rest of the fraction at x = a') + '. Otherwise equate coefficients or substitute convenient x values')
d.sec('7.5-exercise-7-5')
ind_cards('Ex 7.5')

# ---------------------------------------------------------------- 7.6 By parts
d.sec('7.6-integration-by-parts-theory')
b('Integration by parts formula.', T('∫ u v′ dx = u v − ∫ u′ v dx') + '. Derived from the product rule d(uv) = u dv + v du')
b('How do you choose u? (ILATE)', 'Order of priority for u: ' + T('I') + 'nverse trig, ' + T('L') + 'ogarithm, ' + T('A') + 'lgebraic, ' + T('T') + 'rigonometric, ' + T('E') + 'xponential. The first type in this list is u; the other is dv')
b('∫ log x dx and ∫ tan⁻¹x dx: the trick?', 'Take dv = dx (u = the function): ∫ log x dx = ' + N('x log x − x') + ' and ∫ tan⁻¹x dx = ' + N('x tan⁻¹x − ½ log(1 + x²)'))
b('The eˣ[f(x) + f′(x)] rule.', T('∫ eˣ[f(x) + f′(x)] dx = eˣ f(x) + C') + '. Spot f and f′ side by side; the by-parts integrals cancel (Example 22)')
b('Cyclic integrals: ∫ eˣ sin x dx.', 'Parts twice and the original integral reappears: I = eˣ sin x − eˣ cos x − I, so ' + N('I = eˣ(sin x − cos x)/2'))
b('Three special integrals by parts (7.6.2).', '∫√(x² − a²) = (x/2)√(x² − a²) − (a²/2) log|x + √(x² − a²)|; ∫√(x² + a²) = (x/2)√(x² + a²) + (a²/2) log|x + √(x² + a²)|; ∫√(a² − x²) = (x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a)')
d.sec('7.6-exercise-7-6')
ind_cards('Ex 7.6')
d.sec('7.6-exercise-7-7')
ind_cards('Ex 7.7')

# ---------------------------------------------------------------- 7.7-7.8 Definite
d.sec('7.7-definite-integral-theory')
sm.riemann_refine(d)
b('Definition of the definite integral.', T('∫ₐᵇ f(x) dx = lim n→∞ Σ f(xᵢ) Δx') + ', Δx = (b − a)/n: the signed area between the curve and the x-axis from a to b')
sm.signed_area_sine(d)
sm.area_function_strips(d)
b('First fundamental theorem of calculus.', 'If f is continuous on [a, b] and A(x) = ∫ₐˣ f(t) dt then ' + T('A′(x) = f(x)') + '. (Ex 7.9 Q10: if f(x) = ∫₀ˣ t sin t dt then f′(x) = x sin x.)')
b('Second fundamental theorem of calculus.', 'If F is any antiderivative of the continuous f: ' + T('∫ₐᵇ f(x) dx = F(b) − F(a)') + ' (written [F(x)]ₐᵇ). The constant C cancels')
b('Definite integral: does it depend on the variable name?', X('No') + ': ∫ₐᵇ f(x) dx = ∫ₐᵇ f(t) dt. It is a number, not a function of x')
b('Substitution in a definite integral: what changes?', 'Change the ' + T('limits') + ' with the variable: x = a ↔ t = g(a), x = b ↔ t = g(b). Then you never return to x')
b('Example: ∫₀¹ tan⁻¹x/(1 + x²) dx?', 't = tan⁻¹x: limits 0 → π/4: ∫ t dt = ' + N('π²/32'))
b('Example: ∫₁² dx/(x(x + 1))?', '1/x − 1/(x + 1): [log(x/(x + 1))]₁² = log(2/3) − log(1/2) = ' + N('log(4/3)'))
b('Example: ∫₀^(π/4) sin³2t cos 2t dt?', 'u = sin 2t: ½∫₀¹ u³ du = ' + N('1/8'))
d.sec('7.8-exercise-7-8')
def_cards('Ex 7.8')
d.sec('7.9-exercise-7-9')
def_cards('Ex 7.9')
b('Ex 7.9 Q10: if f(x) = ∫₀ˣ t sin t dt, then f′(x) = (A) cos x + x sin x (B) x sin x (C) x cos x (D) sin x + x cos x', 'First fundamental theorem: f′(x) = x sin x. ' + E('(B)'))

# ---------------------------------------------------------------- 7.10 Properties
d.sec('7.10-properties-theory')
table_card(d, 'Properties of definite integrals', 'State the property.', [
    ('P₁', '∫ₐᵇ f = −∫ᵦᵃ f; ∫ₐᵃ f = 0', False),
    ('P₂', '∫ₐᵇ f = ∫ₐᶜ f + ∫꜀ᵇ f (split at any c)', False),
    ('P₃', '∫ₐᵇ f(x) dx = ∫ₐᵇ f(a + b − x) dx (King)', False),
    ('P₄', '∫₀ᵃ f(x) dx = ∫₀ᵃ f(a − x) dx', False),
    ('P₅', '∫₀^(2a) f(x) dx = ∫₀ᵃ f(x) dx + ∫₀ᵃ f(2a − x) dx', False),
    ('P₆', '∫₀^(2a) f = 2∫₀ᵃ f if f(2a − x) = f(x); = 0 if f(2a − x) = −f(x)', False),
    ('P₇', '∫_(−a)^(a) f = 2∫₀ᵃ f if f even; = 0 if f odd', False)], term='Properties of definite integrals', note='P₃/P₄ are the “King property”; P₇ handles symmetric limits')
sm.king_property(d)
sm.even_odd_integrals(d)
b('How to use P₃ (King) in practice?', 'Call the integral I, replace x by a + b − x to get a second expression, ' + T('add the two') + ': if f(x) + f(a + b − x) is simple (often 1 or a constant), 2I = ∫(that) and I follows. Typical: ratios like sin/(sin + cos), log(1 + tan x)')
b('Trap: splitting an integral with |x − c| or [x].', 'Split at the point where the inside changes sign (or at each integer) and remove the modulus on each piece. Never integrate |f| by integrating f')
b('Wallis-type shortcut (JEE): ∫₀^(π/2) sinⁿx dx = ∫₀^(π/2) cosⁿx dx = ?', 'n even: ((n − 1)/n)((n − 3)/(n − 2))···(1/2)(π/2). n odd: ((n − 1)/n)((n − 3)/(n − 2))···(2/3). Examples: n = 2: π/4; n = 3: 2/3; n = 4: 3π/16; n = 5: 8/15')
d.sec('7.10-exercise-7-10')
def_cards('Ex 7.10')
b('Ex 7.10 Q19: show ∫₀ᵃ f(x)g(x) dx = 2∫₀ᵃ f(x) dx if f(x) = f(a − x) and g(x) + g(a − x) = 4.', 'I = ∫ f(x)g(x) = ∫ f(a − x)g(a − x) = ∫ f(x)g(a − x). Add: 2I = ∫ f(x)[g(x) + g(a − x)] = 4∫f. So ' + E('I = 2∫₀ᵃ f ✓'))

# ---------------------------------------------------------------- Misc
d.sec('7.11-miscellaneous')
ind_cards('Misc')
def_cards('Misc')
b('Misc Q40: if f(a + b − x) = f(x), then ∫ₐᵇ x f(x) dx = (A) ((a + b)/2)∫ₐᵇ f(b − x) dx (B) ((a + b)/2)∫ₐᵇ f(b + x) dx (C) ((b − a)/2)∫ₐᵇ f(x) dx (D) ((a + b)/2)∫ₐᵇ f(x) dx', 'King: I = ∫(a + b − x)f(x) dx, so 2I = (a + b)∫ f. ' + E('(D)'))

# ---------------------------------------------------------------- Exam patterns
d.sec('7.z-exam-patterns')
b('∫ 1/(a sin x + b cos x) dx pattern?', 'Write a sin x + b cos x = R sin(x + φ), R = √(a² + b²): ' + T('(1/R) log|tan((x + φ)/2)|'))
b('∫ dx/(a + b cos x) pattern.', 'Use t = tan(x/2): cos x = (1 − t²)/(1 + t²), dx = 2dt/(1 + t²). It becomes a rational integral in t')
b('∫ e^(ax) sin(bx) dx and ∫ e^(ax) cos(bx) dx?', T('e^(ax)(a sin bx − b cos bx)/(a² + b²)') + ' and ' + T('e^(ax)(a cos bx + b sin bx)/(a² + b²)'))
b('∫ sin²x cos²x dx?', 'sin²x cos²x = ¼ sin²2x = (1 − cos 4x)/8: ' + N('x/8 − sin 4x/32'))
b('∫ 1/(1 + sin x) dx and ∫ 1/(1 + cos x) dx?', 'Multiply by the conjugate: ' + N('tan x − sec x') + ' and ' + N('tan(x/2)'))
b('∫ x eˣ dx, ∫ x² eˣ dx?', N('(x − 1)eˣ') + ' and ' + N('(x² − 2x + 2)eˣ') + '; in general integrate xⁿeˣ by parts n times')
b('Area under a curve as an integral (preview of Chapter 8).', 'Area between y = f(x), the x-axis, x = a and x = b (f ≥ 0) is ' + T('∫ₐᵇ f(x) dx') + '. For instance the area under y = x² from 0 to 2 is 8/3')
b('∫₀^(π/2) sinⁿx/(sinⁿx + cosⁿx) dx for any n?', N('π/4') + ' by the King property (the two integrands sum to 1)')
b('∫₀^(π/2) log sin x dx?', N('−(π/2) log 2') + ' (I = ∫ log sin = ∫ log cos by King; adding, 2I = ∫ log(sin 2x/2) = ½∫₀^π log sin u du − (π/2) log 2 = I − (π/2) log 2)')
b('∫₋ₐᵃ x² dx and ∫₋ₐᵃ x³ dx?', N('2a³/3') + ' and ' + N('0'))
b('Derivative of ∫ from a to g(x) of f(t) dt with respect to x (Leibniz)?', T('f(g(x)) · g′(x)') + '. Example: d/dx ∫₀^(x²) sin t dt = 2x sin x²')
b('lim x→0 (1/x)∫₀ˣ cos t² dt?', 'By the first fundamental theorem and L′Hôpital: cos 0 = ' + N('1'))

# ---------------------------------------------------------------- How it is asked
d.sec('7.z-how-its-asked')
b('MCQ: ∫ (x + 1/x) dx =<br>(a) x²/2 + log|x| + C (b) x² + log x (c) 1 + 1/x² (d) x²/2 − 1/x²', E('(a)'))
b('MCQ: ∫ eˣ(tan x + sec²x) dx =<br>(a) eˣ tan x + C (b) eˣ sec x + C (c) eˣ + C (d) eˣ sec²x + C', 'form eˣ[f + f′] with f = tan x: ' + E('(a)'))
b('MCQ: ∫₋₁¹ dx/(1 + x²) =<br>(a) π/2 (b) π/4 (c) 0 (d) π', 'tan⁻¹1 − tan⁻¹(−1) = π/4 + π/4 = ' + E('(a) π/2'))
b('MCQ: ∫₀^(π/2) sin x/(sin x + cos x) dx =<br>(a) π/4 (b) π/2 (c) 0 (d) 1', E('(a) π/4'))
b('MCQ: ∫₋₂² |x| dx =<br>(a) 4 (b) 0 (c) 2 (d) 8', '2 × ∫₀² x dx = ' + E('(a) 4'))
b('MCQ: ∫ 1/(x log x) dx =<br>(a) log|log x| + C (b) 1/log x (c) log x (d) x log x', 't = log x: ' + E('(a)'))
b('MCQ: ∫ x e^(x²) dx =<br>(a) ½ e^(x²) + C (b) e^(x²) (c) 2e^(x²) (d) x e^(x²)/2', E('(a)'))
b('MCQ: d/dx ∫₀^(x²) sin t dt =<br>(a) 2x sin x² (b) sin x² (c) cos x² (d) 2x cos x²', E('(a)') + ' (Leibniz)')
b('MCQ: ∫₀^π cos x dx =<br>(a) 0 (b) 1 (c) 2 (d) −1', 'sin π − sin 0 = ' + E('(a) 0'))
b('MCQ: ∫ tan²x dx =<br>(a) tan x − x + C (b) tan x + x (c) sec x (d) tan³x/3', E('(a)'))
b('Integer answer (JEE Main): ∫₀^π sin²x dx = π/k. Find k.', 'The average of sin² is ½, so the integral is π/2: k = ' + N('2'))
b('Integer answer: ∫₋₁¹ (x³ + 3x² + 5) dx = ?', 'The odd part cancels: 2∫₀¹(3x² + 5) dx = 2(1 + 5) = ' + N('12'))
b('Integer answer: ∫₁⁴ (|x − 2| + |x − 3|) dx = ?', 'Piecewise: on [1, 2] the integrand is 5 − 2x (integral 2); on [2, 3] it is 1 (integral 1); on [3, 4] it is 2x − 5 (integral 2). Total ' + N('5'))
b('Assertion–Reason.<br><b>A:</b> ∫₋ₐᵃ x⁵ dx = 0.<br><b>R:</b> the integral of an odd function over [−a, a] is 0.<br>(a) Both true, R explains A (b) Both true, R does not (c) A true, R false (d) A false, R true', E('(a)'))
b('Assertion–Reason.<br><b>A:</b> ∫ (1/x) dx = log x + C for all x ≠ 0.<br><b>R:</b> d/dx log|x| = 1/x for x ≠ 0.<br>(a) Both true, R explains A (b) A false, R true (c) A true, R false (d) Both false', E('(b)') + ': the correct antiderivative is log|x| + C (log x alone needs x > 0)')
b('True/False: ∫ₐᵇ f(x) dx = ∫ᵦᵃ f(x) dx.', X('False') + ': swapping the limits changes the sign')
b('True/False: the definite integral of a continuous function on [a, b] is always positive.', X('False') + ': it is signed area; ∫₀^(2π) sin x dx = 0')
b('2-mark: ∫ (3x² + 2x + 1) dx.', N('x³ + x² + x + C'))
b('2-mark: ∫₀¹ (2x + 1) dx.', '[x² + x]₀¹ = ' + N('2'))
b('3-mark: ∫ x cos x dx.', 'u = x: x sin x − ∫ sin x dx = ' + N('x sin x + cos x + C'))
b('3-mark: ∫₀^(π/2) cos²x dx.', 'cos² = (1 + cos 2x)/2: [x/2 + sin 2x/4] = ' + N('π/4'))
b('4-mark: ∫ 1/((x − 1)(x − 2)) dx.', '1/(x − 2) − 1/(x − 1): ' + N('log|(x − 2)/(x − 1)| + C'))
b('4-mark: ∫₀^(π/4) log(1 + tan x) dx.', 'King property: 2I = (π/4) log 2. ' + N('I = (π/8) log 2'))
b('Case-based: water flows into a tank at r(t) = 3t² litres/min. How much flows in from t = 0 to t = 4?', '∫₀⁴ 3t² dt = [t³]₀⁴ = ' + N('64 litres'))
b('Case-based: velocity v(t) = t² − 4t + 3 m/s. Find the displacement from t = 0 to 3 and the distance travelled.', 'Displacement ∫₀³ v dt = [t³/3 − 2t² + 3t]₀³ = ' + N('0 m') + '. v changes sign at t = 1 and 3: distance = ∫₀¹ v + |∫₁³ v| = 4/3 + 4/3 = ' + N('8/3 m'))

print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
