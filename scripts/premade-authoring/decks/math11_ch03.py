import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase as sc
import showcase_math as sm
M = 'media/'

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Mathematics', 'class11-mathematics-ch03-trigonometric-functions')
d = Deck('Chapter 3: Trigonometric Functions', 'Class 11', ['class-11', 'mathematics', 'ch-3'])
d.description = 'Radian measure, trig functions and graphs, identities, compound and multiple angles, trig equations, and exam-style problems.'

# ---------------------------------------------------------------- 3.2 Angles
d.sec('3.2-angles')
d.basic('What is an angle, in terms of rotation?', 'The amount of ' + T('rotation') + ' of a ray from the initial side to the terminal side')
d.basic('Sign of an angle by direction of rotation?', 'Anticlockwise: ' + T('positive') + '. Clockwise: ' + X('negative'))
d.basic('Define 1 degree.', 'Rotation of ' + r'\(\tfrac{1}{360}\)' + ' of a full revolution')
d.basic('1° in minutes, and 1′ in seconds?', N('1° = 60′') + ', ' + N('1′ = 60″'))
d.basic('Define 1 radian.', 'The angle at the centre subtended by an arc ' + T('equal in length to the radius'), definitionImage=M + 'fig_3_4_radian.webp')
d.basic('Arc length l, radius r, angle θ (in radians): relation?', r'\(l = r\theta\)')
d.basic('A full circle is how many radians?', r'\(2\pi\)' + ' rad (' + N('360°') + ')')
d.basic('Radian → degree conversion?', r'\(D = \dfrac{180}{\pi} \times R\)' +'<br><small>D = degrees, R = radians</small>')
d.basic('Degree → radian conversion?', r'\(R = \dfrac{\pi}{180} \times D\)')
d.basic('1 radian ≈ ? degrees', N('57°16′') + ' (approx.)')
d.basic('1 degree ≈ ? radians', N('0.01746 rad'))
table_card(d, '3.2.4 · Degree ↔ radian', 'Radian measure?', [
    ('30°', 'π/6', False), ('45°', 'π/4', False), ('60°', 'π/3', False), ('90°', 'π/2', False),
    ('180°', 'π', False), ('270°', '3π/2', False)], term='Common angles in radians')
d.basic('Convert 40°20′ to radians.', r'\(\dfrac{121\pi}{540}\)' + ' rad')
d.basic('Minute hand 1.5 cm long. Distance moved by its tip in 40 min?', r'\(l = 1.5 \times \tfrac{4\pi}{3} = 2\pi\)' + ' ≈ ' + N('6.28 cm'))
d.basic('Equal arcs subtend 65° and 110° in two circles. Ratio of radii r₁ : r₂?', N('22 : 13') + ' (r ∝ 1/θ)')

# ---------------------------------------------------------------- 3.3 Trig functions
d.sec('3.3-trig-functions')
d.basic('On the unit circle, a point at angle x has coordinates?', r'\((\cos x,\ \sin x)\)')
d.occlusion('Fig. 3.6 · The unit circle', M + 'fig_3_6_unit_circle.webp', (901, 809), [
    ('(cos x, sin x)', [520, 185, 142, 50], False), ('(0, 1)', [318, 166, 95, 40]), ('(−1, 0)', [50, 344, 160, 50]),
    ('(1, 0)', [674, 359, 100, 48]), ('(0, −1)', [300, 607, 122, 50])], printed=True)
d.basic('Pythagorean identity from the unit circle?', r'\(\cos^2 x + \sin^2 x = 1\)')
d.basic('Identity involving tan and sec?', r'\(1 + \tan^2 x = \sec^2 x\)')
d.basic('Identity involving cot and cosec?', r'\(1 + \cot^2 x = \operatorname{cosec}^2 x\)')
d.basic('For which x is sin x = 0?', r'\(x = n\pi,\ n \in \mathbb{Z}\)')
d.basic('For which x is cos x = 0?', r'\(x = (2n+1)\dfrac{\pi}{2},\ n \in \mathbb{Z}\)')
table_card(d, '3.3 · Standard values', 'sin of each angle?', [
    ('0', '0', False), ('π/6', '1/2', False), ('π/4', '1/√2', False), ('π/3', '√3/2', False), ('π/2', '1', False)],
    note='cos runs the same values in reverse order', term='Standard values of sin')
table_card(d, '3.3 · Standard values', 'tan of each angle?', [
    ('0', '0', False), ('π/6', '1/√3', False), ('π/4', '1', False), ('π/3', '√3', False), ('π/2', 'not defined', True)],
    term='Standard values of tan')
d.basic('Periods of sin, cos and tan?', 'sin, cos: ' + r'\(2\pi\)' + '; tan: ' + r'\(\pi\)')
d.basic(r'\(\sin(2n\pi + x)\) and \(\cos(2n\pi + x)\) = ?', r'\(\sin x\)' + ' and ' + r'\(\cos x\)' + ' (period ' + r'\(2\pi\)' + ')')
d.basic('Is sin an even or odd function? And cos?', r'\(\sin(-x) = -\sin x\)' + ' (' + T('odd') + '); ' + r'\(\cos(-x) = \cos x\)' + ' (' + T('even') + ')')

d.sec('3.3.1-signs')
sc.astc(d)
d.basic('cos x = −3/5 and x is in quadrant III. sin x and tan x?', r'\(\sin x = -\tfrac45,\ \tan x = \tfrac43\)')
d.basic('cot x = −5/12 and x is in quadrant II. sin x and cos x?', r'\(\sin x = \tfrac{12}{13},\ \cos x = -\tfrac{5}{13}\)')

d.sec('3.3.3-graphs')
sc.sin_cos_graph(d)
for fn, name, note in [
        ('sin x', 'fig_3_8_sin', 'period 2π, range [−1, 1]'),
        ('cos x', 'fig_3_9_cos', 'period 2π, range [−1, 1]'),
        ('tan x', 'fig_3_10_tan', 'period π, asymptotes at odd multiples of π/2'),
        ('cot x', 'fig_3_11_cot', 'period π, asymptotes at multiples of π'),
        ('sec x', 'fig_3_12_sec', 'never between −1 and 1; asymptotes at odd multiples of π/2'),
        ('cosec x', 'fig_3_13_cosec', 'never between −1 and 1; asymptotes at multiples of π')]:
    d.basic('Which function is this graph?', T('y = ' + fn) + '<br><small>' + note + '</small>', termImage=M + name + '.webp')

d.sec('3.3.2-domain-range')
table_card(d, '3.3.2 · Domain and range', 'Range of each function?', [
    ('sin x, cos x', '[−1, 1]', False), ('tan x, cot x', 'R (all reals)', False),
    ('sec x, cosec x', '(−∞, −1] ∪ [1, ∞)', False)], term='Range of trig functions')
table_card(d, '3.3.2 · Domain and range', 'Domain of each function?', [
    ('sin x, cos x', 'R', False), ('tan x, sec x', 'R − {(2n+1)π/2}', False), ('cot x, cosec x', 'R − {nπ}', False)],
    term='Domain of trig functions')
d.basic('As x goes from 0 to π/2, how do sin x and cos x change?', 'sin x ' + T('increases') + ' 0 → 1; cos x ' + T('decreases') + ' 1 → 0')
d.basic('sin(31π/3) = ?', r'\(\sin\!\left(10\pi + \tfrac{\pi}{3}\right) = \dfrac{\sqrt3}{2}\)')
d.basic('cos(−1710°) = ?', r'\(\cos(-1710^\circ + 1800^\circ) = \cos 90^\circ = 0\)')

# ---------------------------------------------------------------- 3.4 Sum and difference
d.sec('3.4-compound-angles')
d.basic(r'\(\cos(x + y) = ?\)', r'\(\cos x\cos y - \sin x\sin y\)')
d.basic(r'\(\cos(x - y) = ?\)', r'\(\cos x\cos y + \sin x\sin y\)')
d.basic(r'\(\sin(x + y) = ?\)', r'\(\sin x\cos y + \cos x\sin y\)')
d.basic(r'\(\sin(x - y) = ?\)', r'\(\sin x\cos y - \cos x\sin y\)')
d.basic(r'\(\tan(x + y) = ?\)', r'\(\dfrac{\tan x + \tan y}{1 - \tan x\tan y}\)')
d.basic(r'\(\tan(x - y) = ?\)', r'\(\dfrac{\tan x - \tan y}{1 + \tan x\tan y}\)')
d.basic(r'\(\cot(x + y) = ?\)', r'\(\dfrac{\cot x\cot y - 1}{\cot y + \cot x}\)')
d.basic(r'\(\cot(x - y) = ?\)', r'\(\dfrac{\cot x\cot y + 1}{\cot y - \cot x}\)')

d.sec('3.4-allied-angles')
d.basic('Quick rule for allied angles like (π/2 ± x), (π ± x), (3π/2 ± x)?',
        'Odd multiple of π/2: ' + T('sin ↔ cos, tan ↔ cot') + '. Even multiple: ' + T('same function') + '. Sign: the original function in that quadrant')
table_card(d, '3.4 · Allied angles', 'Simplify each.', [
    ('cos(π/2 − x)', 'sin x', False), ('sin(π/2 + x)', 'cos x', False), ('cos(π/2 + x)', '−sin x', True),
    ('sin(π − x)', 'sin x', False), ('cos(π − x)', '−cos x', True), ('sin(π + x)', '−sin x', True),
    ('sin(2π − x)', '−sin x', True)], term='Allied angle reductions')

d.sec('3.4-values')
d.basic('sin 15° = ?', r'\(\dfrac{\sqrt3 - 1}{2\sqrt2}\)' + '  (= cos 75°)')
d.basic('cos 15° = ?', r'\(\dfrac{\sqrt3 + 1}{2\sqrt2}\)' + '  (= sin 75°)')
d.basic('tan 15° and tan 75°?', r'\(2 - \sqrt3\)' + ' and ' + r'\(2 + \sqrt3\)')
d.basic('tan(13π/12) = ?', r'\(\tan\!\left(\pi + \tfrac{\pi}{12}\right) = \tan 15^\circ = 2 - \sqrt3\)')

d.sec('3.4-multiple-angles')
d.basic(r'Three forms of \(\cos 2x\)?', r'\(\cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x\)')
d.basic(r'\(\cos 2x\) in terms of tan?', r'\(\dfrac{1 - \tan^2 x}{1 + \tan^2 x}\)')
d.basic(r'\(\sin 2x = ?\)  (two forms)', r'\(2\sin x\cos x = \dfrac{2\tan x}{1 + \tan^2 x}\)')
d.basic(r'\(\tan 2x = ?\)', r'\(\dfrac{2\tan x}{1 - \tan^2 x}\)')
d.basic(r'\(\sin 3x = ?\)', r'\(3\sin x - 4\sin^3 x\)')
d.basic(r'\(\cos 3x = ?\)', r'\(4\cos^3 x - 3\cos x\)')
d.basic(r'\(\tan 3x = ?\)', r'\(\dfrac{3\tan x - \tan^3 x}{1 - 3\tan^2 x}\)')
d.basic(r'Express \(\sin^2 x\) and \(\cos^2 x\) in terms of cos 2x.', r'\(\sin^2 x = \dfrac{1 - \cos 2x}{2},\ \cos^2 x = \dfrac{1 + \cos 2x}{2}\)')

d.sec('3.4-sum-to-product')
d.basic(r'\(\cos x + \cos y = ?\)', r'\(2\cos\dfrac{x+y}{2}\cos\dfrac{x-y}{2}\)')
d.basic(r'\(\cos x - \cos y = ?\)', r'\(-2\sin\dfrac{x+y}{2}\sin\dfrac{x-y}{2}\)')
d.basic(r'\(\sin x + \sin y = ?\)', r'\(2\sin\dfrac{x+y}{2}\cos\dfrac{x-y}{2}\)')
d.basic(r'\(\sin x - \sin y = ?\)', r'\(2\cos\dfrac{x+y}{2}\sin\dfrac{x-y}{2}\)')
d.basic(r'\(2\cos x\cos y = ?\)', r'\(\cos(x + y) + \cos(x - y)\)')
d.basic(r'\(-2\sin x\sin y = ?\)', r'\(\cos(x + y) - \cos(x - y)\)')
d.basic(r'\(2\sin x\cos y = ?\)', r'\(\sin(x + y) + \sin(x - y)\)')
d.basic(r'\(2\cos x\sin y = ?\)', r'\(\sin(x + y) - \sin(x - y)\)')

# ---------------------------------------------------------------- Exam favourites (beyond the NCERT text)
d.sec('exam-extra')
d.basic(r'Maximum and minimum of \(a\sin x + b\cos x\)?', r'\(\pm\sqrt{a^2 + b^2}\)')
d.basic('sin 18° and cos 36°?', r'\(\sin 18^\circ = \dfrac{\sqrt5 - 1}{4},\ \cos 36^\circ = \dfrac{\sqrt5 + 1}{4}\)')
d.basic(r'\(\sin x\,\sin(60^\circ - x)\,\sin(60^\circ + x) = ?\)', r'\(\tfrac14\sin 3x\)')
d.basic(r'\(\cos x\,\cos(60^\circ - x)\,\cos(60^\circ + x) = ?\)', r'\(\tfrac14\cos 3x\)')
d.basic(r'If \(A + B = 45^\circ\), then \((1 + \tan A)(1 + \tan B) = ?\)', N('2'))


# ================================================================ Upgrade: animations, more values, equations, exam patterns
d.sec('3.3-unit-circle-animations')
sm.unit_circle_values(d)
sm.circle_to_wave(d)
b = d.basic
b('Trig ratios of 15° and 75°: sin, cos, tan?', r'\(\sin 75^\circ = \cos 15^\circ = \dfrac{\sqrt6 + \sqrt2}{4},\ \sin 15^\circ = \cos 75^\circ = \dfrac{\sqrt6 - \sqrt2}{4},\ \tan 75^\circ = 2 + \sqrt3\)')
b('Quick check of sin 15° = (√6 − √2)/4.', '(√3 − 1)/(2√2) rationalised: (√3 − 1)√2/4 = (√6 − √2)/4 ≈ ' + N('0.2588') + ' ✓')
b('Degree to radian: 1° = ? and convert 225° and 15° to radians.', r'\(1^\circ = \dfrac{\pi}{180}\)' + ' rad; 225° = ' + N('5π/4') + ', 15° = ' + N('π/12'))
b('Trap: is sin(A + B) = sin A + sin B?', X('No') + '. sin 90° = 1 but sin 45° + sin 45° = √2. Sine is not linear: use sin A cos B + cos A sin B')
b('Trap: sin²x is (sin x)², but sin x² means?', T('sin(x²)') + '. Also sin⁻¹x is the inverse function, not 1/sin x (that is cosec x)')

d.sec('3.z-triangle-identities')
b('If A + B + C = π, then tan A + tan B + tan C = ?', T('tan A tan B tan C') + '. Because tan(A + B) = −tan C. Also cot A cot B + cot B cot C + cot C cot A = 1')
b('If A + B + C = π: sin 2A + sin 2B + sin 2C = ? and cos A + cos B + cos C = ?', T('4 sin A sin B sin C') + ' and ' + T('1 + 4 sin(A/2) sin(B/2) sin(C/2)'))
b('Product of cosines: cos 20° cos 40° cos 60° cos 80° = ?', 'cos 20° cos 40° cos 80° = 1/8 (using cos x cos(60° − x) cos(60° + x) = ¼ cos 3x with x = 20°: ¼ · ½ = 1/8); × cos 60° = ' + N('1/16'))
b('sin 10° sin 30° sin 50° sin 70° = ?', 'sin 10° sin 50° sin 70° = ¼ sin 30° = 1/8; × sin 30° = ' + N('1/16'))
b('Prove tan 20° + tan 40° + √3 tan 20° tan 40° = √3.', 'tan 60° = (tan 20° + tan 40°)/(1 − tan 20° tan 40°) = √3 → tan 20° + tan 40° = √3(1 − tan 20° tan 40°) ✓')
b('Sum of a series of cosines: cos x + cos 2x + … + cos nx (idea)?', 'Multiply by 2 sin(x/2) and use 2 sin(x/2) cos kx = sin((k + ½)x) − sin((k − ½)x): the terms telescope to ' + T('sin(nx/2) cos((n + 1)x/2) / sin(x/2)'))
b('Express sin x + cos x as a single sine. Range?', r'\(\sqrt2\sin\!\left(x + \dfrac{\pi}{4}\right)\)' + ', range ' + N('[−√2, √2]'))
b('Range of 3 sin x + 4 cos x? Of sin²x + cos⁴x?', N('[−5, 5]') + ' and ' + N('[3/4, 1]') + ' (sin²x + cos⁴x = 1 − cos²x + cos⁴x = (cos²x − ½)² + ¾)')
b('Minimum of sec²x + cosec²x?', 'sec²x + cosec²x = 4/sin²2x ≥ ' + N('4'))
b('Value of sin 18° via a quick derivation (idea).', 'Let θ = 18°: 5θ = 90° so sin 2θ = cos 3θ → 2 sin θ cos θ = 4cos³θ − 3 cos θ → 4 sin²θ + 2 sin θ − 1 = 0 → ' + N('sin 18° = (√5 − 1)/4'))

d.sec('3.z-trig-equations')
sm.trig_equation_circle(d)
table_card(d, 'General solutions', 'Write the general solution (n ∈ Z).', [
    ('sin x = 0', 'x = nπ', False), ('cos x = 0', 'x = (2n + 1)π/2', False), ('tan x = 0', 'x = nπ', False),
    ('sin x = sin α', 'x = nπ + (−1)ⁿ α', False), ('cos x = cos α', 'x = 2nπ ± α', False), ('tan x = tan α', 'x = nπ + α', False),
    ('sin²x = sin²α', 'x = nπ ± α', False)], term='General solutions of trig equations')
b('Solve 2 sin²x + sin x − 1 = 0.', '(2 sin x − 1)(sin x + 1) = 0 → sin x = ½ → ' + N('x = nπ + (−1)ⁿπ/6') + '; or sin x = −1 → ' + N('x = 2nπ − π/2'))
b('Solve cos 2x = cos x.', '2x = 2nπ ± x → ' + N('x = 2nπ/3') + ' (n ∈ Z) (from + : x = 2nπ; from − : 3x = 2nπ)')
b('Solve tan x = √3 and sin x = −1/2 in [0, 2π).', N('x = π/3, 4π/3') + ' and ' + N('x = 7π/6, 11π/6'))
b('Solve sin x + cos x = 1.', 'Divide by √2: sin(x + π/4) = 1/√2 → x + π/4 = nπ + (−1)ⁿπ/4 → ' + N('x = 2nπ or x = 2nπ + π/2'))
b('Trap: solving sin x cos x = sin x by dividing by sin x.', X('You lose the roots of sin x = 0') + '. Factorise instead: sin x (cos x − 1) = 0 → x = nπ or x = 2nπ (so x = nπ overall)')
b('Method: solving trig equations.', '1) Reduce to one function (identities). 2) Factorise (never cancel a factor that can be 0). 3) Use the general solution formulas. 4) Restrict to the required interval by choosing integer n')
b('Number of real solutions of sin x = x/10?', 'The graphs y = sin x and y = x/10 can meet only for |x| ≤ 10: 3 crossings for x > 0, 3 for x < 0 and x = 0, so ' + N('7'))

d.sec('3.z-how-its-asked')
b('MCQ: The value of sin 105° is<br>(a) (√3 + 1)/(2√2) (b) (√3 − 1)/(2√2) (c) 1/2 (d) √3/2', 'sin 105° = cos 15° = ' + E('(a)'))
b('MCQ: The value of cos 15° cos 75° is<br>(a) 1/2 (b) 1/4 (c) √3/4 (d) 1/8', 'cos 75° = sin 15°: ½ sin 30° = ' + E('(b) 1/4'))
b('MCQ: sin²x + cos²x = 1 has the solution set<br>(a) R (b) φ (c) {nπ} (d) {π/2}', 'It is an identity: ' + E('(a) all real x'))
b('MCQ: The period of sin x cos x is<br>(a) 2π (b) π (c) π/2 (d) 4π', 'sin x cos x = ½ sin 2x: ' + E('(b) π'))
b('MCQ: If tan θ = 3/4 and θ is in quadrant III, then sin θ =<br>(a) 3/5 (b) −3/5 (c) 4/5 (d) −4/5', 'Both sin and cos are negative in III: ' + E('(b) −3/5'))
b('MCQ: The value of tan 1° tan 2° … tan 89° is<br>(a) 0 (b) 1 (c) ∞ (d) 2', 'tan k° tan(90° − k°) = 1 pairs up: ' + E('(b) 1'))
b('MCQ: The minimum value of 2 sin x + 3 cos x is<br>(a) −5 (b) −√13 (c) −13 (d) −1', '−√(4 + 9) = ' + E('(b) −√13'))
b('MCQ: The radian measure of 75° is<br>(a) 5π/12 (b) 7π/12 (c) 5π/6 (d) 3π/4', '75π/180 = ' + E('(a) 5π/12'))
b('Integer answer (JEE Main): the value of 16 sin 10° sin 30° sin 50° sin 70° is?', '16 × 1/16 = ' + N('1'))
b('Integer answer: the number of solutions of sin x = 1/2 in [0, 4π]?', 'Two in each turn: ' + N('4'))
b('Assertion–Reason.<br><b>A:</b> sin 2x = 2 sin x for all x.<br><b>R:</b> sin 2x = 2 sin x cos x.<br>(a) Both true, R explains A (b) Both true, R does not (c) A false, R true (d) Both false', E('(c)') + ': true only if cos x = 1')
b('True/False: tan x is defined for all real x.', X('False') + ': not defined at odd multiples of π/2 (x = (2n + 1)π/2)')
b('2-mark: find the value of sin 15° cos 15°.', '½ sin 30° = ' + N('1/4'))
b('3-mark: prove (sin 3x + sin x)/(cos 3x + cos x) = tan 2x.', 'Sum-to-product: 2 sin 2x cos x / (2 cos 2x cos x) = ' + N('tan 2x') + ' (cos x ≠ 0)')
b('Case-based: a Ferris wheel of radius 20 m turns once per minute; height h(t) = 22 + 20 sin(2πt/60 − π/2). Minimum and maximum heights?', 'sin ∈ [−1, 1]: ' + N('2 m') + ' and ' + N('42 m') + ' (boarding point is at the bottom, t = 0)')

print('cards', len(d.cards))
os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
