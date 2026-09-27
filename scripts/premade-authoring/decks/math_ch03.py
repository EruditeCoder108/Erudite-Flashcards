import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase as sc
M = 'media/'

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Mathematics', 'class11-mathematics-ch03-trigonometric-functions')
d = Deck('Chapter 3: Trigonometric Functions', 'Class 11', ['class-11', 'mathematics', 'ch-3'])

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

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
