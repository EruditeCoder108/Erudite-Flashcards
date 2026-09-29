"""Animated / bespoke maths cards on the warm paper theme (showcase.PAPER, mcard, Plane).

Same sanitiser rules as showcase.py: class-styled SVG, no scripts/SMIL/gradients/clipPath,
KaTeX does not render here (use Unicode, <sup>, <sub>). Put each chapter's cards under a
`# Maths N Ch M` header.
"""
import math
from showcase import PAPER, PAPER_ARROWS, mcard, mkeyframes, Plane, _card

# ================================================================ Maths 11 Ch 1 Sets
# Two-set Venn geometry in a 300 x 200 viewBox. Circles r=58 centred (115,100) and (185,100);
# they meet at (150, 100 -/+ 46.25).
_R = 'M10,10 H290 V190 H10 Z'
_CA = 'M57,100 a58,58 0 1 0 116,0 a58,58 0 1 0 -116,0 Z'
_CB = 'M127,100 a58,58 0 1 0 116,0 a58,58 0 1 0 -116,0 Z'
_LENS = 'M150,53.75 A58,58 0 0 1 150,146.25 A58,58 0 0 1 150,53.75 Z'
_UNION = 'M150,53.75 A58,58 0 1 0 150,146.25 A58,58 0 1 0 150,53.75 Z'
_AMB = 'M150,53.75 A58,58 0 1 0 150,146.25 A58,58 0 0 1 150,53.75 Z'
_BMA = 'M150,53.75 A58,58 0 1 1 150,146.25 A58,58 0 0 0 150,53.75 Z'
REGIONS = {
    'A': [(_CA, '')], 'B': [(_CB, '')],
    'AuB': [(_UNION, '')], 'AnB': [(_LENS, '')],
    'A-B': [(_AMB, '')], 'B-A': [(_BMA, '')],
    'sym': [(_AMB, ''), (_BMA, '')],
    "A'": [(_R + _CA, 'evenodd')], "B'": [(_R + _CB, 'evenodd')],
    "(AuB)'": [(_R + _UNION, 'evenodd')], "(AnB)'": [(_R + _LENS, 'evenodd')],
}


def venn_frame(letters=True):
    o = (f'<path class="f0" d="{_R}"></path>'
         f'<circle class="ghost" cx="115" cy="100" r="58"></circle><circle class="ghost" cx="185" cy="100" r="58"></circle>')
    if letters:
        o += ('<text class="lbi" x="20" y="28">U</text>'
              '<text class="t1" x="84" y="72" text-anchor="middle">A</text><text class="t1" x="216" y="72" text-anchor="middle">B</text>')
    return o


def venn_shade(key, cls='ns1', fx='fx d2'):
    return ''.join(f'<path class="{cls} {fx}" d="{d}"' + (f' fill-rule="{fr}"' if fr else '') + '></path>'
                   for d, fr in REGIONS[key])


def venn_outline():
    return ('<circle class="c0" cx="115" cy="100" r="58"></circle><circle class="c0" cx="185" cy="100" r="58"></circle>'
            '<text class="t1" x="84" y="72" text-anchor="middle">A</text><text class="t1" x="216" y="72" text-anchor="middle">B</text>'
            '<text class="lbi" x="20" y="28">U</text>')


def venn_card(deck, q, key, note, term, definition, cls='ns1'):
    front = f'<path class="f0" d="{_R}"></path>' + venn_outline()
    back = venn_shade(key, cls)
    # shading under the outlines so labels stay readable
    mcard(deck, 'Venn diagrams · shade it', q, f'<path class="f0" d="{_R}"></path>', back + venn_outline(), note,
          term, definition, hint='Picture the shaded region, then flip.', vb='0 0 300 200', front_only=venn_outline())


def venn_cards(deck):
    venn_card(deck, 'Shade A ∪ B on a Venn diagram.', 'AuB',
              '<p><b>A ∪ B</b> = everything in A <i>or</i> B (or both): the two whole circles.</p>',
              'Venn shading: A ∪ B', 'A ∪ B is both circles together, the overlap included')
    venn_card(deck, 'Shade A ∩ B on a Venn diagram.', 'AnB',
              '<p><b>A ∩ B</b> = in A <i>and</i> B: only the lens where the circles overlap.</p>',
              'Venn shading: A ∩ B', 'A ∩ B is only the overlapping lens', cls='ns3')
    venn_card(deck, 'Shade A − B on a Venn diagram.', 'A-B',
              '<p><b>A − B</b> = in A but <span class="no">not</span> in B: A’s crescent with the overlap removed.</p>'
              '<p>Also written <b>A ∩ B′</b>.</p>',
              'Venn shading: A − B', 'A − B is the part of A outside B (equals A ∩ B′)', cls='ns2')
    venn_card(deck, 'Shade A′ (complement of A) on a Venn diagram.', "A'",
              '<p><b>A′ = U − A</b>: everything in the rectangle <span class="no">outside</span> circle A, including all of B that is not in A.</p>',
              'Venn shading: A′', 'A′ is everything in U outside A', cls='ns2')
    venn_card(deck, 'Shade (A ∪ B)′ on a Venn diagram.', "(AuB)'",
              '<p><b>(A ∪ B)′</b> = the region outside <i>both</i> circles.</p>',
              'Venn shading: (A ∪ B)′', '(A ∪ B)′ is the region outside both circles', cls='ns2')
    venn_card(deck, 'Shade (A ∩ B)′ on a Venn diagram.', "(AnB)'",
              '<p><b>(A ∩ B)′</b> = everything <span class="no">except</span> the overlap lens: it does include the crescents of A and B.</p>',
              'Venn shading: (A ∩ B)′', '(A ∩ B)′ is everything except the overlap lens', cls='ns2')
    venn_card(deck, 'Shade A Δ B (symmetric difference) on a Venn diagram.', 'sym',
              '<p><b>A Δ B = (A − B) ∪ (B − A)</b>: in exactly one of the sets, i.e. both circles minus the lens.</p>'
              '<p>n(A Δ B) = n(A) + n(B) − 2·n(A ∩ B)</p>',
              'Venn shading: symmetric difference', 'A Δ B = (A − B) ∪ (B − A): in exactly one of A, B; n = n(A)+n(B)−2n(A∩B)', cls='ns4')


def de_morgan_cards(deck):
    def panel(ty, shaded_paths, label):
        return (f'<text class="lbl" x="150" y="{ty - 6}" text-anchor="middle">{label}</text>'
                f'<g transform="translate(75,{ty}) scale(.5)"><path class="f0" d="{_R}"></path>'
                f'{shaded_paths}'
                '<circle class="c0" cx="115" cy="100" r="58"></circle><circle class="c0" cx="185" cy="100" r="58"></circle>'
                '<text class="t1 tb" x="84" y="72" text-anchor="middle">A</text><text class="t1 tb" x="216" y="72" text-anchor="middle">B</text></g>')
    css = '.pp .tb{font-size:20px}.pp .st1{animation-delay:.3s}.pp .st2{animation-delay:1.1s}.pp .st3{animation-delay:1.9s}'
    vb = '0 0 300 290'

    for tag, q, lhs, rhs, left_key, note, term, definition in [
        ('De Morgan’s law 1 · intuition', 'Why is (A ∪ B)′ = A′ ∩ B′ ?', '(A ∪ B)′', 'A′ ∩ B′', "(AuB)'",
         '<p><b>Not in (A or B)</b> = <b>not in A and not in B</b>.</p>'
         '<p>Red = outside A, blue = outside B; purple (both) = outside both circles.</p>',
         'De Morgan: (A ∪ B)′ = A′ ∩ B′ (Venn reasoning)',
         '(A ∪ B)′ = A′ ∩ B′: not in the union means outside A and outside B; the outside-A and outside-B regions overlap only outside both circles'),
        ('De Morgan’s law 2 · intuition', 'Why is (A ∩ B)′ = A′ ∪ B′ ?', '(A ∩ B)′', 'A′ ∪ B′', "(AnB)'",
         '<p><b>Not in (A and B)</b> = <b>outside A or outside B</b>.</p>'
         '<p>Red + blue cover everything except the lens.</p><p>Trick: <b>break the bar, flip the sign</b>.</p>',
         'De Morgan: (A ∩ B)′ = A′ ∪ B′ (Venn reasoning)',
         '(A ∩ B)′ = A′ ∪ B′: failing to be in both means being outside A or outside B, which covers everything except the lens')]:
        left = venn_shade(left_key, 'ns2', 'fx st1')
        right = venn_shade("A'", 'ns2', 'fx st2') + venn_shade("B'", 'ns1', 'fx st3')
        front = panel(24, '', lhs) + panel(176, '', rhs) + '<text class="t4" x="150" y="152" text-anchor="middle">= ?</text>'
        back = panel(24, left, lhs) + panel(176, right, rhs) + '<text class="t3" x="150" y="152" text-anchor="middle">=</text>'
        mcard(deck, tag, q, '', back, note, term, definition, css=css, front_only=front,
              hint='Shade each side and compare.', vb=vb)


# ---------------------------------------------------------------- intervals on the number line
def _nl(lo, hi):
    """Number line from lo to hi mapped to x in 20..280."""
    return lambda v: 20 + (v - lo) / (hi - lo) * 260


def interval_card(deck, a, b, ac, bc, notation, setb, note, term):
    """(a,b) style interval: `ac`/`bc` = endpoint included? a/b may be None for infinite ends."""
    lo, hi = -4, 8
    X = _nl(lo, hi)
    ticks = ''.join(f'<line class="ax" x1="{X(v):.1f}" y1="71" x2="{X(v):.1f}" y2="79"></line>'
                    f'<text class="num" x="{X(v):.1f}" y="95">{v}</text>' for v in range(lo + 1, hi))
    axis = f'<line class="ax" x1="10" y1="75" x2="290" y2="75" marker-end="url(#pk)"></line>' + ticks
    xa = X(a) if a is not None else 14
    xb = X(b) if b is not None else 286
    seg = f'<line class="c1 draw" pathLength="100" x1="{xa:.1f}" y1="75" x2="{xb:.1f}" y2="75"></line>'
    ends = ''
    if a is not None:
        ends += (f'<circle class="d1s fx d3" cx="{xa:.1f}" cy="75" r="5.5"></circle>' if ac
                 else f'<circle class="f0 fx d3" cx="{xa:.1f}" cy="75" r="5.5"></circle>')
    else:
        ends += '<text class="t1 fx d3" x="14" y="58">←</text>'
    if b is not None:
        ends += (f'<circle class="d1s fx d3" cx="{xb:.1f}" cy="75" r="5.5"></circle>' if bc
                 else f'<circle class="f0 fx d3" cx="{xb:.1f}" cy="75" r="5.5"></circle>')
    else:
        ends += '<text class="t1 fx d3" x="270" y="58">→</text>'
    mcard(deck, 'Intervals · number line', f'Draw the interval {notation} on the real line and write it in set-builder form.',
          axis, seg + ends, f'<p><b>{setb}</b></p><p>{note}</p>', term,
          f'{notation} = {setb}. {note}', css='', hint='Which ends get a filled dot, which an open one?', vb='0 0 300 110')


def interval_cards(deck):
    interval_card(deck, -1, 3, False, True, '(−1, 3]', '{x ∈ R : −1 &lt; x ≤ 3}',
                  'Round bracket → open circle (endpoint excluded). Square bracket → filled dot (endpoint included).',
                  'Interval (−1, 3] on the number line')
    interval_card(deck, 2, 6, True, True, '[2, 6]', '{x ∈ R : 2 ≤ x ≤ 6}',
                  'Closed interval: both endpoints belong. Its length is b − a = 4.', 'Closed interval [2, 6] on the number line')
    interval_card(deck, -2, None, True, False, '[−2, ∞)', '{x ∈ R : x ≥ −2}',
                  '∞ is not a number, so its side always takes a <b>round</b> bracket.', 'Interval [−2, ∞) on the number line')


DOT = {'c1': 'd1s', 'c2': 'd2s', 'c3': 'd3s', 'c4': 'd4s'}


def interval_ops_cards(deck):
    lo, hi = -2, 9
    X = _nl(lo, hi)

    def band(y, a, b, ac, bc, cls, fx=''):
        o = f'<line class="{cls} {fx}" x1="{X(a):.1f}" y1="{y}" x2="{X(b):.1f}" y2="{y}"></line>'
        o += (f'<circle class="{DOT[cls]} {fx}" cx="{X(a):.1f}" cy="{y}" r="4.5"></circle>' if ac
              else f'<circle class="f0 {cls} {fx}" cx="{X(a):.1f}" cy="{y}" r="4.5"></circle>')
        o += (f'<circle class="{DOT[cls]} {fx}" cx="{X(b):.1f}" cy="{y}" r="4.5"></circle>' if bc
              else f'<circle class="f0 {cls} {fx}" cx="{X(b):.1f}" cy="{y}" r="4.5"></circle>')
        return o

    def axis(y):
        return (f'<line class="ax" x1="10" y1="{y}" x2="290" y2="{y}" marker-end="url(#pk)"></line>'
                + ''.join(f'<line class="ax" x1="{X(v):.1f}" y1="{y - 3}" x2="{X(v):.1f}" y2="{y + 3}"></line>'
                          f'<text class="num" x="{X(v):.1f}" y="{y + 15}">{v}</text>' for v in range(lo + 1, hi)))

    # A = [1, 5], B = (3, 8)
    base = (axis(170) + '<text class="t1" x="14" y="48">A = [1, 5]</text><text class="t2" x="14" y="88">B = (3, 8)</text>'
            + band(56, 1, 5, True, True, 'c1') + band(96, 3, 8, False, False, 'c2'))
    guide = (f'<line class="guide" x1="{X(3):.1f}" y1="40" x2="{X(3):.1f}" y2="170"></line>'
             f'<line class="guide" x1="{X(5):.1f}" y1="40" x2="{X(5):.1f}" y2="170"></line>')
    inter = band(136, 3, 5, False, True, 'c3', 'fx d3') + '<text class="t3 fx d3" x="14" y="128">A ∩ B = (3, 5]</text>'
    union = ''
    mcard(deck, 'Intervals · intersection', 'A = [1, 5] and B = (3, 8). Find A ∩ B.', base, guide.replace('class="guide"', 'class="guide fx d2"') + inter,
          '<p><b>A ∩ B = (3, 5]</b>: the stretch where both bands are present.</p>'
          '<p>At <b>3</b>: in A but not in B → excluded. At <b>5</b>: in both → included.</p>'
          '<p class="no">Trap: the endpoint is in the intersection only if it is in <u>both</u> sets.</p>',
          'Intersection of intervals [1,5] ∩ (3,8)', '[1,5] ∩ (3,8) = (3,5]; an endpoint stays only if it belongs to both intervals')

    base = (axis(170) + '<text class="t1" x="14" y="48">A = [1, 5]</text><text class="t2" x="14" y="88">B = (3, 8)</text>'
            + band(56, 1, 5, True, True, 'c1') + band(96, 3, 8, False, False, 'c2'))
    uni = band(136, 1, 8, True, False, 'c4', 'fx d3') + '<text class="t4 fx d3" x="14" y="128">A ∪ B = [1, 8)</text>'
    mcard(deck, 'Intervals · union', 'Same A = [1, 5] and B = (3, 8). Find A ∪ B.', base,
          guide.replace('class="guide"', 'class="guide fx d2"') + uni,
          '<p><b>A ∪ B = [1, 8)</b>: the bands overlap, so they join into one interval.</p>'
          '<p>Left end 1 comes from A (closed), right end 8 from B (open).</p>'
          '<p class="no">Trap: (1, 3) ∪ (3, 5) is <u>not</u> (1, 5): the point 3 is missing.</p>',
          'Union of intervals [1,5] ∪ (3,8)', '[1,5] ∪ (3,8) = [1,8); two intervals merge only if they overlap or touch with an included point')


# ---------------------------------------------------------------- subset doubling
def subsets_doubling(deck):
    import itertools
    els = ['a', 'b', 'c']
    subs = []
    for k in range(4):
        subs += [c for c in itertools.combinations(els, k)]
    chips = ''
    for i, s in enumerate(subs):
        label = 'φ' if not s else '{' + ', '.join(s) + '}'
        chips += f'<span class="ch fx d{min(i // 2 + 1, 6)}">{label}</span>'
    css = ('.pp .sub{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 4px}'
           '.pp .ch{padding:6px 12px;border-radius:10px;background:#fff;border:1px solid #e8e1d2;font:600 15px Georgia,serif;color:#1d5fd6}'
           '.pp .row{display:flex;gap:10px;align-items:center;margin:6px 0;font-size:14px}'
           '.pp .row b{color:#c77700;font-size:16px}')
    q = 'How many subsets does {a, b, c} have, and why is the general answer 2ⁿ?'
    front = (f'<div class="w pp"><p class="tag">Subsets · counting</p><h2>{q}</h2>'
             '<div class="row">For each element you choose: <b>in</b> or <b>out</b>.</div>'
             '<p class="hint">List all subsets of {a, b, c} before flipping.</p></div>')
    back = (f'<div class="w pp"><p class="tag">Subsets · counting</p><h2>{q}</h2><div class="sub">{chips}</div>'
            '<div class="eq fx d5"><p>3 elements × (in / out) → 2 × 2 × 2 = <b>2³ = 8</b> subsets.</p>'
            '<p>General: n(P(A)) = <b>2ⁿ</b>; proper subsets <b>2ⁿ − 1</b>; non-empty proper <b>2ⁿ − 2</b>.</p></div></div>')
    _card(deck, 'Number of subsets of {a, b, c}: each element is in or out',
          'A set of n elements has 2ⁿ subsets: for each element choose in or out; {a,b,c} has 8', PAPER + css, front, back)


# ---------------------------------------------------------------- three-set inclusion-exclusion
def _venn3(cx, cy, r, nums, cls):
    ax, ay, bx, by, ccx, ccy = cx - .55 * r, cy - .32 * r, cx + .55 * r, cy - .32 * r, cx, cy + .55 * r
    pos = {'A': (cx - 1.02 * r, cy - .6 * r), 'B': (cx + 1.02 * r, cy - .6 * r), 'C': (cx, cy + 1.28 * r),
           'AB': (cx, cy - .72 * r), 'AC': (cx - .6 * r, cy + .38 * r), 'BC': (cx + .6 * r, cy + .38 * r), 'ABC': (cx, cy - .02 * r)}
    o = ''.join(f'<circle class="{cls}" cx="{x:.1f}" cy="{y:.1f}" r="{r}"></circle>' for x, y in [(ax, ay), (bx, by), (ccx, ccy)])
    for k, (x, y) in pos.items():
        o += f'<text class="{ {1: "t3", 2: "t4", 3: "t2", 0: "t2"}.get(nums[k], "t1") } pcount" x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle">{nums[k]}</text>'
    return o


def inclusion_exclusion3(deck):
    keys = ['A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC']
    steps = [
        ({'A': 1, 'B': 1, 'C': 1, 'AB': 2, 'AC': 2, 'BC': 2, 'ABC': 3}, 'Add n(A) + n(B) + n(C)', '', 'overlaps counted 2×, centre 3×'),
        ({'A': 1, 'B': 1, 'C': 1, 'AB': 1, 'AC': 1, 'BC': 1, 'ABC': 0}, 'Subtract each pair:', 'n(A∩B), n(B∩C), n(A∩C)', 'centre removed 3 times → 0'),
        ({k: 1 for k in keys}, 'Add back n(A∩B∩C)', '', 'every region counted exactly once'),
    ]
    rows = ''
    for i, (nums, cap, cap2, sub) in enumerate(steps):
        y = 4 + i * 96
        rows += (f'<g class="fx d{2 * i + 1}"><g transform="translate(0,{y})">'
                 + _venn3(58, 46, 27, nums, 'ghost') +
                 f'<text class="t{[1, 2, 3][i]}" x="122" y="28">{cap}</text>'
                 + (f'<text class="t{[1, 2, 3][i]}" x="122" y="45">{cap2}</text>' if cap2 else '') +
                 f'<text class="sm" x="122" y="{62 if cap2 else 46}">{sub}</text></g></g>')
    front = _venn3(150, 120, 62, {k: '?' for k in keys}, 'ghost') + '<text class="sm" x="150" y="282" text-anchor="middle">A, B, C overlap in seven regions</text>'
    css = '.pp .pcount{font-size:12px}'
    mcard(deck, 'Inclusion–exclusion · three sets', 'Derive n(A ∪ B ∪ C): why add, subtract, then add back?', '', rows,
          '<p><b>n(A∪B∪C) = n(A) + n(B) + n(C) − n(A∩B) − n(B∩C) − n(A∩C) + n(A∩B∩C)</b></p>',
          'n(A ∪ B ∪ C) by inclusion–exclusion',
          'n(A∪B∪C) = n(A)+n(B)+n(C) − n(A∩B) − n(B∩C) − n(A∩C) + n(A∩B∩C); each region ends up counted once',
          css=css, vb='0 0 300 290', hint='Track how many times the middle region is counted.', front_only=front)


# ================================================================ Maths 11 Ch 2 Relations and functions
def _plane(xmin, xmax, ymin, ymax, pad=(26, 12, 14, 22), h=190):
    return Plane(xmin, xmax, ymin, ymax, 300, h, pad)


def cartesian_grid(deck):
    P = _plane(0, 5, 0, 5, pad=(28, 14, 14, 26), h=200)
    xt = [(v, str(v)) for v in range(1, 5)]
    base = P.axes(xt, xt, grid=True, xl='first', yl='second')
    ab = [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
    ba = [(3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3)]
    dots_ab = ''.join(P.dot(x, y, 'd1s', 5.5) for x, y in ab)
    lab_ab = ''.join(P.text(x, y, f'({x},{y})', 't1', 'middle', dy=-9) for x, y in ab if (x, y) != (3, 3))
    back = ''.join(P.dot(x, y, 'd2s', 5.5, 'fx d2') for x, y in ba if (x, y) != (3, 3))
    back += ''.join(P.text(x, y, f'({x},{y})', 't2', 'middle', dy=-9, extra='fx d3') for x, y in ba if (x, y) != (3, 3) and x == 4 or (x, y) in [(3, 1), (3, 2)])
    back += P.hole(3, 3, 'c4', 7.5) + P.text(3, 3, '(3,3)', 't4', 'middle', dy=-11)
    mcard(deck, 'Cartesian product · order matters',
          'A = {1, 2, 3}, B = {3, 4}. Plot A × B (blue). Where would B × A fall, and how many points do they share?',
          base + dots_ab + lab_ab, back,
          '<p>A × B (blue) and B × A (red): 6 points each, but only <b>(3, 3)</b> is common.</p>'
          '<p>So <b>A × B ≠ B × A</b> unless A = B (or one is empty). Same count, different points.</p>',
          'A × B vs B × A on the plane: only (3,3) is common',
          'A×B ≠ B×A in general: with A={1,2,3}, B={3,4} both have 6 points but share only (3,3); n(A×B) = n(B×A) = 6',
          vb='0 0 300 200', hint='Swap the coordinates of every point.')


def arrow_diagrams(deck):
    def panel(ox, oy, arrows, nl=3, nr=3, cls='c0', tag=''):
        o = f'<g transform="translate({ox},{oy})">'
        ly = lambda i, n: 14 + i * (72 / max(n - 1, 1)) if n > 1 else 50
        o += '<ellipse class="ghost" cx="22" cy="50" rx="16" ry="46"></ellipse><ellipse class="ghost" cx="98" cy="50" rx="16" ry="46"></ellipse>'
        for i in range(nl):
            o += f'<circle class="d0s" cx="22" cy="{ly(i, nl)}" r="3.5"></circle><text class="sm" x="6" y="{ly(i, nl) + 4}" text-anchor="end">{i + 1}</text>'
        for j in range(nr):
            o += f'<circle class="d0s" cx="98" cy="{ly(j, nr)}" r="3.5"></circle><text class="sm" x="114" y="{ly(j, nr) + 4}">{"abc"[j]}</text>'
        for (i, j) in arrows:
            o += f'<line class="{cls}" x1="26" y1="{ly(i, nl)}" x2="93" y2="{ly(j, nr)}" marker-end="url(#pk)"></line>'
        return o + '</g>'
    panels = [
        (10, 6, [(0, 0), (1, 1), (2, 1)]),
        (160, 6, [(0, 0), (0, 1), (1, 2)]),
        (10, 138, [(0, 0), (1, 1)]),
        (160, 138, [(0, 0), (1, 1), (2, 2)]),
    ]
    base = ''.join(panel(ox, oy, arr) for ox, oy, arr in panels)
    marks = [(10, 6, 'ok', 'many → one is fine'), (160, 6, 'no', '1 has two images'), (10, 138, 'no', '3 has no image'), (160, 138, 'ok', 'one → one')]
    back = ''
    for k, (ox, oy, kind, why) in enumerate(marks):
        back += (f'<text class="{"t3" if kind == "ok" else "t2"} fx d{k + 1}" x="{ox + 60}" y="{oy + 116}" text-anchor="middle">'
                 f'{"✓ function" if kind == "ok" else "✗ not a function"}</text>'
                 f'<text class="sm fx d{k + 1}" x="{ox + 60}" y="{oy + 128}" text-anchor="middle">{why}</text>')
    labels = ''.join(f'<text class="lbi" x="{ox + 2}" y="{oy + 8}">({"abcd"[k]})</text>' for k, (ox, oy, _) in enumerate(panels))
    mcard(deck, 'Functions · arrow diagrams', 'Which of these arrow diagrams (left set → right set) are functions?', base + labels, back,
          '<p><b>Every</b> element of the left set needs <b>exactly one</b> arrow.</p>'
          '<p>(b) fails: two arrows from one element. (c) fails: an element with no arrow. Two elements sharing one image (a) is allowed. An unused element on the right is allowed too.</p>',
          'Which arrow diagrams are functions?', '(a) function (many-to-one allowed); (b) not: 1 has two images; (c) not: 3 has no image; (d) function',
          vb='0 0 300 288', hint='Check each left-hand element.')


def vertical_line_test(deck):
    P1 = Plane(-3, 3, -1.2, 5.5, 300, 190, (16, 10, 10, 16))
    left = (P1.axes(labels=False) + P1.curve(lambda x: x * x, 'c1', -2.3, 2.3))
    P2 = Plane(-1.2, 5.5, -3, 3, 300, 190, (16, 10, 10, 16))
    # sideways parabola x = y^2 drawn point by point
    pts = ' '.join(f'{P2.X(t * t):.1f},{P2.Y(t):.1f}' for t in [i / 20 * 2.3 - 2.3 + 0 for i in range(0, 41)])
    right = P2.axes(labels=False) + f'<polyline class="c1" points="{pts}"></polyline>'
    base = (f'<g transform="translate(0,4) scale(.5)">{left}</g><g transform="translate(150,4) scale(.5)">{right}</g>'
            '<text class="lbl" x="75" y="122" text-anchor="middle">(a) y = x²</text><text class="lbl" x="225" y="122" text-anchor="middle">(b) x = y²</text>')
    # vertical line sweeping across each panel (one hit on a, two on b)
    sweep_a = f'<g transform="translate(0,4) scale(.5)"><line class="c2 sw" x1="{P1.X(0):.1f}" y1="{P1.Y(5.5):.1f}" x2="{P1.X(0):.1f}" y2="{P1.Y(-1.2):.1f}"></line></g>'
    xb = P2.X(2.2)
    sweep_b = f'<g transform="translate(150,4) scale(.5)"><line class="c2 sw" x1="{xb:.1f}" y1="{P2.Y(3):.1f}" x2="{xb:.1f}" y2="{P2.Y(-3):.1f}"></line></g>'
    hits_b = (f'<g transform="translate(150,4) scale(.5)"><circle class="d2s" cx="{xb:.1f}" cy="{P2.Y(math.sqrt(2.2)):.1f}" r="6"></circle>'
              f'<circle class="d2s" cx="{xb:.1f}" cy="{P2.Y(-math.sqrt(2.2)):.1f}" r="6"></circle></g>')
    back = ('<text class="t3 fx d2" x="75" y="140" text-anchor="middle">✓ function</text><text class="sm fx d2" x="75" y="154" text-anchor="middle">each vertical line hits once</text>'
            '<text class="t2 fx d3" x="225" y="140" text-anchor="middle">✗ not a function</text><text class="sm fx d3" x="225" y="154" text-anchor="middle">a vertical line hits twice</text>'
            + hits_b.replace('class="d2s"', 'class="d2s fx d3"'))
    css = '.pp .sw{animation:swp 3.6s ease-in-out .3s infinite alternate both}@keyframes swp{from{transform:translateX(-52px)}to{transform:translateX(52px)}}'
    mcard(deck, 'Functions · vertical line test', 'Which curve is the graph of a function y = f(x)?', base, back,
          '<p><b>Vertical line test:</b> a curve is a function’s graph if every vertical line cuts it <b>at most once</b>.</p>'
          '<p>x = y² gives two y-values (±√x) for one x, so it fails.</p>',
          'Vertical line test: y = x² passes, x = y² fails',
          'Vertical line test: a curve is a function of x if each vertical line meets it at most once; y=x² passes, x=y² fails (two y for one x)',
          css=css, vb='0 0 300 180', front_only=sweep_a + sweep_b, hint='Imagine a vertical line sliding left to right.')


def graph_id(deck, fn, x_rng, y_rng, name, dom, rng, note, term, cls_pad=(26, 12, 14, 22), xt=None, yt=None, clip=None, asym=False):
    P = Plane(x_rng[0], x_rng[1], y_rng[0], y_rng[1], 300, 190, cls_pad)
    xt = xt if xt is not None else [(v, str(v)) for v in range(int(x_rng[0]) + 1, int(x_rng[1])) if v]
    yt = yt if yt is not None else [(v, str(v)) for v in range(int(y_rng[0]) + 1, int(y_rng[1])) if v]
    base = P.axes(xt, yt, grid=True) + P.curve(fn, 'c1', clip=clip)
    back = ''
    if asym:
        back += P.line(0, y_rng[0], 0, y_rng[1], 'guide') + P.line(x_rng[0], 0, x_rng[1], 0, 'guide')
        back = back.replace('class="guide"', 'class="guide fx d2"')
    mcard(deck, 'Standard graphs · name it', 'Name this function. What are its domain and range?', base, back,
          f'<p><b>{name}</b></p><p>Domain: <b>{dom}</b> &nbsp; Range: <b>{rng}</b></p><p>{note}</p>', term,
          f'{name}; domain {dom}; range {rng}. {note}', vb='0 0 300 190', hint='Read the shape, then the extent along each axis.')


def standard_graphs(deck):
    graph_id(deck, lambda x: x, (-4, 4), (-4, 4), 'Identity  f(x) = x', 'R', 'R',
             'A straight line through the origin at 45°; every input is its own output.', 'Graph: identity function y = x')
    graph_id(deck, lambda x: 3, (-4, 4), (-1, 5), 'Constant  f(x) = 3', 'R', '{3}',
             'A horizontal line: one output value only, so the range is a single point.', 'Graph: constant function',
             xt=[(v, str(v)) for v in (-3, -2, -1, 1, 2, 3)], yt=[(v, str(v)) for v in (1, 2, 3, 4)])
    graph_id(deck, lambda x: x * x, (-3, 3), (-1, 9), 'Square  f(x) = x²', 'R', '[0, ∞)',
             'Parabola opening up, symmetric about the y-axis (even function). Never below 0.', 'Graph: y = x²',
             xt=[(v, str(v)) for v in (-2, -1, 1, 2)], yt=[(v, str(v)) for v in (2, 4, 6, 8)])
    graph_id(deck, lambda x: x ** 3, (-2.2, 2.2), (-9, 9), 'Cube  f(x) = x³', 'R', 'R',
             'Odd function: symmetric about the origin; rises from bottom-left to top-right, flat at 0.', 'Graph: y = x³',
             xt=[(v, str(v)) for v in (-2, -1, 1, 2)], yt=[(v, str(v)) for v in (-8, -4, 4, 8)])
    graph_id(deck, lambda x: 1 / x, (-4, 4), (-4, 4), 'Reciprocal  f(x) = 1/x', 'R − {0}', 'R − {0}',
             'Two branches; the axes are asymptotes: x = 0 is not allowed and y = 0 is never reached. Odd function.', 'Graph: y = 1/x',
             clip=(-4, 4), asym=True)
    graph_id(deck, lambda x: abs(x), (-4, 4), (-1, 4), 'Modulus  f(x) = |x|', 'R', '[0, ∞)',
             'A V with vertex at the origin; the negative half of y = x is reflected upward. Even function.', 'Graph: modulus function',
             xt=[(v, str(v)) for v in (-3, -2, -1, 1, 2, 3)], yt=[(v, str(v)) for v in (1, 2, 3)])


def modulus_flip(deck):
    P = Plane(-4, 4, -4, 4, 300, 190, (26, 12, 14, 22))
    xt = [(v, str(v)) for v in (-3, -2, -1, 1, 2, 3)]
    yt = [(v, str(v)) for v in (-3, -2, -1, 1, 2, 3)]
    y0 = P.Y(0)
    base = P.axes(xt, yt, grid=True) + P.curve(lambda x: x, 'c1', 0, 4)
    left = P.curve(lambda x: x, 'c2 flip', -4, 0)
    css = (f'.pp .flip{{transform-box:view-box;transform-origin:0px {y0:.1f}px;animation:flp 2.4s ease-in-out .5s both}}'
           '@keyframes flp{from{transform:scaleY(1)}to{transform:scaleY(-1)}}')
    ghost = P.curve(lambda x: x, 'ghost', -4, 0)
    back = ghost + left + '<text class="t2 fx d3" x="196" y="150">negative half flips up ↑</text>'
    mcard(deck, 'Modulus · intuition', 'Start from y = x. What does taking |x| do to the part where x < 0?', base, back,
          '<p><b>|x|</b> keeps the x ≥ 0 part and <b>reflects the x &lt; 0 part in the x-axis</b>.</p>'
          '<p>Output is never negative → range [0, ∞). In general y = |f(x)| flips every below-axis part of y = f(x) upward.</p>',
          'y = |x| by reflecting y = x', 'Taking modulus reflects the part of the graph below the x-axis upward; |x| turns y = x into a V; range [0, ∞)',
          css=css, hint='Which half of the line is below the x-axis?', front_only=P.curve(lambda x: x, 'c1', -4, 0))


def greatest_integer_graph(deck):
    P = Plane(-3, 4, -3.5, 4.5, 300, 200, (26, 12, 14, 22))
    xt = [(v, str(v)) for v in (-2, -1, 1, 2, 3)]
    yt = [(v, str(v)) for v in (-3, -2, -1, 1, 2, 3, 4)]
    base = P.axes(xt, yt, grid=True)
    back = ''
    for k, n in enumerate(range(-3, 4)):
        d = min(k // 2 + 1, 6)
        back += (P.line(n, n, n + 1, n, 'c1').replace('class="c1"', f'class="c1 fx d{d}"') +
                 P.dot(n, n, 'd1s', 4.2, f'fx d{d}') + P.hole(n + 1, n, 'c1', 4.2).replace('class="f0 c1"', f'class="f0 c1 fx d{d}"'))
    mcard(deck, 'Greatest integer function', 'Sketch y = [x] (greatest integer ≤ x). What are [2.7], [−2.7] and [3]?', base, back,
          '<p>[2.7] = <b>2</b>, [3] = <b>3</b>, [−2.7] = <b>−3</b> (greatest integer not exceeding −2.7 is −3, <span class="no">not −2</span>).</p>'
          '<p>Steps: [x] = n for n ≤ x &lt; n + 1: <b>closed dot on the left, open on the right</b>. Range = Z.</p>',
          'Graph of the greatest integer function [x]',
          '[x] = n for n ≤ x < n+1: step graph, closed dot left end, open dot right end; domain R, range Z; [2.7]=2, [−2.7]=−3',
          vb='0 0 300 200', hint='For each interval [n, n+1), what is [x]?')


def signum_graph(deck):
    P = Plane(-4, 4, -2.5, 2.5, 300, 170, (26, 12, 14, 22))
    xt = [(v, str(v)) for v in (-3, -2, -1, 1, 2, 3)]
    yt = [(-1, '−1'), (1, '1')]
    base = P.axes(xt, yt, grid=True)
    back = (P.line(0, 1, 4, 1, 'c1 fx d2') + P.hole(0, 1, 'c1', 4.5).replace('class="f0 c1"', 'class="f0 c1 fx d2"') +
            P.line(-4, -1, 0, -1, 'c2 fx d3') + P.hole(0, -1, 'c2', 4.5).replace('class="f0 c2"', 'class="f0 c2 fx d3"') +
            P.dot(0, 0, 'd0s', 4.5, 'fx d4') +
            P.text(2, 1, 'x > 0 → 1', 't1 fx d2', 'middle', dy=-9) + P.text(-2, -1, 'x < 0 → −1', 't2 fx d3', 'middle', dy=16) +
            P.text(0.15, 0, 'f(0) = 0', 'lbl fx d4', dx=6, dy=-8))
    mcard(deck, 'Signum function', 'Sketch the signum function f(x) = 1 (x > 0), 0 (x = 0), −1 (x < 0). Domain and range?', base, back,
          '<p>Domain <b>R</b>; range <b>{−1, 0, 1}</b> (only three values).</p><p>It records only the <b>sign</b> of x. Note sgn(x) = x/|x| for x ≠ 0.</p>',
          'Graph of the signum function', 'Signum: 1 for x>0, 0 at 0, −1 for x<0; domain R, range {−1,0,1}; sgn(x) = x/|x| for x≠0',
          vb='0 0 300 170', hint='Two rays with open ends, and one isolated point.')


def shift_parabola(deck):
    P = Plane(-3, 5, -1.5, 7, 300, 200, (26, 12, 14, 22))
    xt = [(v, str(v)) for v in (-2, -1, 1, 2, 3, 4)]
    yt = [(v, str(v)) for v in (2, 4, 6)]
    base = P.axes(xt, yt, grid=True) + P.curve(lambda x: x * x, 'c1', -2.6, 2.6)
    dx, dy = P.X(2) - P.X(0), P.Y(1) - P.Y(0)
    css = (f'.pp .slide{{animation:shp 2.4s ease-in-out .6s both}}@keyframes shp{{from{{transform:translate(0,0)}}to{{transform:translate({dx:.1f}px,{dy:.1f}px)}}}}')
    moved = P.curve(lambda x: x * x, 'c2 slide', -2.6, 2.6)
    back = (moved + P.dot(2, 1, 'd2s', 4.5, 'fx d5') + P.text(2, 1, 'vertex (2, 1)', 't2 fx d5', 'middle', dy=22))
    mcard(deck, 'Graph shifts · intuition', 'Given the graph of y = x² (blue), sketch y = (x − 2)² + 1.', base, back,
          '<p><b>y = f(x − h) + k</b> slides the graph <b>h right</b> and <b>k up</b>.</p>'
          '<p>Trap: f(x − 2) moves right, not left: the input must be 2 larger to get the same output.</p>',
          'Shift y = x² to y = (x−2)² + 1', 'y = f(x−h)+k shifts the graph h units right and k units up; (x−2)²+1 has vertex (2,1)',
          css=css, hint='Where does the vertex go?')


def piecewise_v(deck):
    P = Plane(-4, 4, -1, 5.5, 300, 190, (26, 12, 14, 22))
    xt = [(v, str(v)) for v in (-3, -2, -1, 1, 2, 3)]
    yt = [(v, str(v)) for v in (1, 2, 3, 4, 5)]
    base = P.axes(xt, yt, grid=True)
    back = (P.curve(lambda x: 1 - x, 'c2 fx d2', -4, 0) + P.curve(lambda x: 1 + x, 'c1 fx d3', 0, 4) +
            P.dot(0, 1, 'd0s', 4.5, 'fx d4') + P.text(0, 1, '(0, 1)', 'lbl fx d4', dx=8, dy=16) +
            P.text(-2.6, 3.6, '1 − x', 't2 fx d2', 'middle', dx=-20, dy=-4) + P.text(2.6, 3.6, 'x + 1', 't1 fx d3', 'middle', dx=20, dy=-4))
    mcard(deck, 'Piecewise functions (Ex. 22)', 'Sketch f(x) = 1 − x for x < 0, f(0) = 1, f(x) = x + 1 for x > 0. What single formula is it?', base, back,
          '<p>Both pieces meet at (0, 1), giving a V: <b>f(x) = |x| + 1</b>.</p>'
          '<p>Method for piecewise graphs: plot each piece on its own interval, then check the join points (open or closed dot).</p>',
          'Ex 22: piecewise graph is |x| + 1', 'f(x)=1−x (x<0), 1 (x=0), x+1 (x>0) is the graph of |x|+1, a V with vertex (0,1)',
          hint='Evaluate each piece near x = 0.')


def sum_of_graphs(deck):
    P = Plane(-3, 3, -3.5, 6.5, 300, 200, (26, 12, 14, 22))
    xt = [(v, str(v)) for v in (-2, -1, 1, 2)]
    yt = [(v, str(v)) for v in (-2, 2, 4, 6)]
    base = P.axes(xt, yt, grid=True) + P.curve(lambda x: x, 'c1', -3, 3) + P.curve(lambda x: abs(x), 'c2', -3, 3)
    back = (P.curve(lambda x: x + abs(x), 'c3 fx d2', -3, 3) +
            P.line(2, 2, 2, 4, 'guide fx d3') + P.dot(2, 4, 'd3s', 4.5, 'fx d3') + P.text(2, 4, '2 + 2 = 4', 't3 fx d3', dx=-8, dy=-8, anchor='end') +
            P.text(-2.9, 6.1, 'f + g: 0 for x &lt; 0, 2x for x ≥ 0', 't3 fx d4', dy=0))
    mcard(deck, 'Algebra of functions', 'f(x) = x (blue) and g(x) = |x| (red). Sketch (f + g)(x) by adding heights.', base, back,
          '<p><b>(f + g)(x) = f(x) + g(x)</b>: add the two heights at each x.</p>'
          '<p>For x ≥ 0: x + x = <b>2x</b>. For x &lt; 0: x + (−x) = <b>0</b>.</p>',
          '(f+g)(x) for f = x, g = |x|', '(f+g)(x)=f(x)+g(x) pointwise; for f=x, g=|x|: 2x when x≥0 and 0 when x<0',
          hint='Read f and g at x = 2, then at x = −2.')


def relation_arrow(deck):
    ly = lambda i: 18 + i * 28
    o = '<ellipse class="ghost" cx="80" cy="102" rx="34" ry="96"></ellipse><ellipse class="ghost" cx="220" cy="102" rx="34" ry="96"></ellipse>'
    o += '<text class="lbi" x="80" y="10" text-anchor="middle">A</text><text class="lbi" x="220" y="10" text-anchor="middle">A (codomain)</text>'
    for i in range(6):
        o += (f'<circle class="d0s" cx="80" cy="{ly(i)}" r="4"></circle><text class="lbl" x="60" y="{ly(i) + 4}" text-anchor="end">{i + 1}</text>'
              f'<circle class="d0s" cx="220" cy="{ly(i)}" r="4"></circle><text class="lbl" x="240" y="{ly(i) + 4}">{i + 1}</text>')
    back = ''
    for i in range(5):
        back += (f'<line class="c1 fx d{min(i // 2 + 1, 4)}" x1="85" y1="{ly(i)}" x2="215" y2="{ly(i + 1)}" marker-end="url(#pb)"></line>')
    back += ('<text class="t2 fx d5" x="80" y="196" text-anchor="middle">6 has no image</text>'
             '<text class="t3 fx d5" x="220" y="196" text-anchor="middle">1 is not an image</text>')
    mcard(deck, 'Relations · domain, range, codomain', 'A = {1, …, 6}, R = {(x, y) : y = x + 1} from A to A. Draw it; find domain, range, codomain.', o, back,
          '<p>Domain = <b>{1, 2, 3, 4, 5}</b> (first elements). Range = <b>{2, 3, 4, 5, 6}</b> (second elements). Codomain = <b>{1, …, 6}</b> (the whole target set).</p>'
          '<p>Range ⊂ codomain. Because 6 has no arrow, this R is <b>not a function</b>.</p>',
          'Arrow diagram of y = x + 1 on {1..6}: domain, range, codomain',
          'R={(1,2),(2,3),(3,4),(4,5),(5,6)}: domain {1..5}, range {2..6}, codomain {1..6}; not a function since 6 has no image',
          vb='0 0 300 204', hint='Domain = starts of arrows. Range = ends of arrows.')


# ================================================================ Maths 11 Ch 4 Complex numbers and quadratic equations
def eqplane(xmin, xmax, ymin, ymax, w=300, pad=(22, 10, 12, 20)):
    """Plane with equal x and y scale (circles stay round); returns (plane, viewBox height)."""
    s = (w - pad[0] - pad[2]) / (xmax - xmin)
    h = pad[1] + pad[3] + s * (ymax - ymin)
    return Plane(xmin, xmax, ymin, ymax, w, h, pad), round(h)


_MK = {'c0': 'pk', 'c1': 'pb', 'c2': 'pr', 'c3': 'pg', 'c4': 'po'}


def vec(P, x0, y0, x1, y1, cls='c1', extra=''):
    return (f'<line class="{cls} {extra}" x1="{P.X(x0):.1f}" y1="{P.Y(y0):.1f}" x2="{P.X(x1):.1f}" y2="{P.Y(y1):.1f}" '
            f'marker-end="url(#{_MK[cls]})"></line>')


def _xy_ticks(lo, hi, skip=(0,)):
    return [(v, str(v).replace('-', '−')) for v in range(lo, hi + 1) if v not in skip]


def argand_fig41(deck):
    P, h = eqplane(-6, 4, -3, 5, pad=(22, 10, 12, 18))
    pts = {'A': (2, 4), 'B': (-2, 3), 'C': (0, 1), 'D': (2, 0), 'E': (-5, -2), 'F': (1, -2)}
    base = P.axes(_xy_ticks(-5, 3), _xy_ticks(-2, 4), grid=True, xl='Re', yl='Im')
    for k, (x, y) in pts.items():
        base += P.dot(x, y, 'd1s', 4.5) + P.text(x, y, k, 't1', dx=7, dy=-6)
    back = ''
    for i, (k, (x, y)) in enumerate(pts.items()):
        sign = '+' if y >= 0 else '−'
        lab = f'{x}{sign}{abs(y)}i'.replace('-', '−') if x else f'{sign if y < 0 else ""}{"" if abs(y) == 1 else abs(y)}i'
        if y == 0: lab = f'{x}'
        back += P.text(x, y, lab, 't2 fx d' + str(min(i // 2 + 2, 6)), dx=7, dy=14)
    mcard(deck, 'Argand plane · Fig 4.1', 'Write the complex number represented by each of the points A–F.', base, back,
          '<p>The point <b>(x, y)</b> is the complex number <b>x + iy</b>:</p>'
          '<p>A = 2 + 4i, B = −2 + 3i, C = i, D = 2, E = −5 − 2i, F = 1 − 2i.</p>'
          '<p>Points on the <b>real axis</b> are a + 0i; points on the <b>imaginary axis</b> are 0 + bi.</p>',
          'Fig 4.1: read complex numbers off the Argand plane',
          'A=2+4i, B=−2+3i, C=i, D=2, E=−5−2i, F=1−2i: point (x,y) is x+iy; real axis a+0i, imaginary axis 0+bi',
          vb=f'0 0 300 {h}', hint='x-coordinate → real part, y-coordinate → imaginary part.')


def powers_of_i(deck):
    P, h = eqplane(-2.1, 2.1, -1.7, 1.7, pad=(14, 8, 14, 8))
    o = (P.axes(labels=False) + f'<circle class="ghost" cx="{P.X(0):.1f}" cy="{P.Y(0):.1f}" r="{P.X(1) - P.X(0):.1f}"></circle>')
    lab = (P.text(1, 0, '1', 't1', dx=8, dy=-6) + P.text(0, 1, 'i', 't1', dx=8, dy=-2) + P.text(-1, 0, '−1', 't1', dx=-8, dy=-6, anchor='end') +
           P.text(0, -1, '−i', 't1', dx=8, dy=14))
    base = o + lab + ''.join(P.dot(x, y, 'd0s', 4) for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)])
    x0, y0 = P.X(1), P.Y(0)
    pts = [(P.X(x) - x0, P.Y(y) - y0) for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 0)]]
    css = mkeyframes('hop', pts, 4, 'ease-in-out', 0.3)
    back = (f'<g transform="translate({x0:.1f},{y0:.1f})"><circle class="d2s hop" cx="0" cy="0" r="7"></circle></g>'
            + P.text(1, 0, 'i⁰, i⁴, i⁸…', 't2 fx d2', dx=8, dy=14) + P.text(0, 1, 'i¹, i⁵…', 't2 fx d2', dx=8, dy=12) +
            P.text(-1, 0, 'i², i⁶…', 't2 fx d2', dx=-8, dy=14, anchor='end') + P.text(0, -1, 'i³, i⁷…', 't2 fx d2', dx=8, dy=-4))
    mcard(deck, 'Powers of i · intuition', 'Each multiplication by i moves one step. Find i⁴³ and i⁻³⁵.', base, back,
          '<p>Each step multiplies by i: a <b>quarter-turn anticlockwise</b>. After 4 steps you are home: <b>i⁴ = 1</b>.</p>'
          '<p>So only the <b>remainder of n ÷ 4</b> matters: 43 = 4·10 + 3 → i⁴³ = i³ = <b>−i</b>. For −35 = 4·(−9) + 1 → i⁻³⁵ = i¹ = <b>i</b>.</p>',
          'Powers of i cycle every 4 steps', 'i^n depends only on n mod 4: i^0=1, i^1=i, i^2=−1, i^3=−i; i^43 = −i and i^−35 = i',
          css=css, vb=f'0 0 300 {h}', hint='Where does 4 quarter-turns bring you?')


def multiply_by_i(deck):
    P, h = eqplane(-4, 5, -1, 5, pad=(20, 8, 12, 16))
    ox, oy = P.X(0), P.Y(0)
    base = (P.axes(_xy_ticks(-3, 4), _xy_ticks(1, 4), grid=True, xl='Re', yl='Im') + vec(P, 0, 0, 3, 2, 'c1') + P.dot(3, 2, 'd1s', 4) +
            P.text(3, 2, 'z = 3 + 2i', 't1', dx=6, dy=-6))
    css = (f'.pp .r90{{transform-box:view-box;transform-origin:{ox:.1f}px {oy:.1f}px;animation:rr 2.2s ease-in-out .5s both}}'
           '@keyframes rr{from{transform:rotate(0deg)}to{transform:rotate(-90deg)}}')
    back = (f'<g class="r90">{vec(P, 0, 0, 3, 2, "c2")}</g>' +
            P.dot(-2, 3, 'd2s', 4, 'fx d4') + P.text(-2, 3, 'iz = −2 + 3i', 't2 fx d4', dx=-6, dy=-8, anchor='middle') +
            f'<path class="guide fx d3" d="M {P.X(1.5):.1f} {P.Y(1):.1f} A {P.X(1.8) - ox:.1f} {P.X(1.8) - ox:.1f} 0 0 0 {P.X(-0.5):.1f} {P.Y(1.7):.1f}"></path>' +
            P.text(0.55, 0.45, '90°', 'lbl fx d4', dx=12, dy=-8))
    mcard(deck, 'Multiplying by i · geometry', 'Compute i(3 + 2i). What does multiplying by i do to a point on the Argand plane?', base, back,
          '<p>i(3 + 2i) = 3i + 2i² = <b>−2 + 3i</b>: the point (3, 2) → (−2, 3).</p>'
          '<p><b>× i = rotate 90° anticlockwise</b> about the origin (length unchanged). × i² = rotate 180° = negate.</p>',
          'Multiplying by i rotates by 90° anticlockwise', 'i(x+iy) = −y + ix: multiplication by i rotates the point 90° anticlockwise about the origin; z=3+2i goes to −2+3i',
          css=css, vb=f'0 0 300 {h}', hint='Compute it algebraically, then picture where (3, 2) goes.')


def conjugate_mirror(deck):
    P, h = eqplane(-5.6, 5.6, -5.4, 5.4, pad=(12, 6, 12, 6))
    ox, oy = P.X(0), P.Y(0)
    r = P.X(5) - ox
    base = (P.axes(labels=False) + f'<circle class="ghost" cx="{ox:.1f}" cy="{oy:.1f}" r="{r:.1f}"></circle>' +
            vec(P, 0, 0, 3, 4, 'c1') + P.dot(3, 4, 'd1s', 4.5) + P.text(3, 4, 'z = 3 + 4i', 't1', dx=8, dy=-4) +
            P.text(0, 0, '|z| = 5', 'sm', dx=24, dy=-14))
    back = (P.line(3, 4, 3, -4, 'guide fx d2') + P.dot(3, -4, 'd2s', 4.5, 'fx d2') + P.text(3, -4, 'z̄ = 3 − 4i', 't2 fx d2', dx=8, dy=14) +
            P.dot(-3, 4, 'd3s', 4.5, 'fx d3') + P.text(-3, 4, '−z̄ = −3 + 4i', 't3 fx d3', dx=-8, dy=-4, anchor='end') +
            P.dot(-3, -4, 'd4s', 4.5, 'fx d4') + P.text(-3, -4, '−z = −3 − 4i', 't4 fx d4', dx=-8, dy=14, anchor='end'))
    mcard(deck, 'Conjugate and negative · geometry', 'Plot z = 3 + 4i, its conjugate z̄, −z and −z̄. What are their moduli?', base, back,
          '<p><b>z̄</b> = mirror image of z in the <b>real axis</b>. <b>−z</b> = reflection through the <b>origin</b>. <b>−z̄</b> = mirror image in the <b>imaginary axis</b>.</p>'
          '<p>All four lie on the same circle: |z| = |z̄| = |−z| = √(3² + 4²) = <b>5</b>.</p>',
          'Conjugate is the mirror image in the real axis', 'z̄ reflects z in the real axis; −z is the reflection through the origin; z, z̄, −z, −z̄ all have modulus 5 for z=3+4i',
          vb=f'0 0 300 {h}', hint='Reflect in the real axis, then through the origin.')


def parallelogram_add(deck):
    P, h = eqplane(-1, 6, -1, 4.6, pad=(20, 8, 12, 16))
    base = (P.axes(_xy_ticks(1, 5), _xy_ticks(1, 4), grid=True, xl='Re', yl='Im') + vec(P, 0, 0, 3, 1, 'c1') + vec(P, 0, 0, 1, 2, 'c2') +
            P.text(3, 1, 'z₁ = 3 + i', 't1', dx=6, dy=16) + P.text(1, 2, 'z₂ = 1 + 2i', 't2', dx=-6, dy=-8, anchor='middle'))
    dx, dy = P.X(3) - P.X(0), P.Y(1) - P.Y(0)
    css = (f'.pp .slide2{{animation:sl2 1.6s ease-in-out .6s both}}@keyframes sl2{{from{{transform:translate(0,0)}}to{{transform:translate({dx:.1f}px,{dy:.1f}px)}}}}')
    back = (f'<g class="slide2">{vec(P, 0, 0, 1, 2, "c2")}</g>' +
            P.line(1, 2, 4, 3, 'guide fx d3') + P.line(3, 1, 4, 3, 'guide fx d3') +
            vec(P, 0, 0, 4, 3, 'c3', 'fx d4') + P.dot(4, 3, 'd3s', 4.5, 'fx d4') + P.text(4, 3, 'z₁ + z₂ = 4 + 3i', 't3 fx d4', dx=-4, dy=-8, anchor='middle'))
    mcard(deck, 'Addition · vector picture', 'Add z₁ = 3 + i and z₂ = 1 + 2i geometrically.', base, back,
          '<p>z₁ + z₂ = (3 + 1) + (1 + 2)i = <b>4 + 3i</b>: the diagonal of the parallelogram (place z₂ at the tip of z₁).</p>'
          '<p>Hence the <b>triangle inequality</b>: |z₁ + z₂| ≤ |z₁| + |z₂|, with equality only when the two point the same way.</p>',
          'Addition of complex numbers is vector addition (parallelogram)', 'z1+z2 is the diagonal of the parallelogram on z1, z2; |z1+z2| ≤ |z1|+|z2| (triangle inequality)',
          css=css, vb=f'0 0 300 {h}', hint='Slide z₂ so its tail sits on z₁’s tip.')


def roots_of_unity_cards(deck):
    P, h = eqplane(-1.6, 1.6, -1.35, 1.35, pad=(12, 6, 12, 6))
    ox, oy = P.X(0), P.Y(0)
    r = P.X(1) - ox
    circ = f'<circle class="ghost" cx="{ox:.1f}" cy="{oy:.1f}" r="{r:.1f}"></circle>'
    c = math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3)
    base = P.axes(labels=False) + circ + P.dot(1, 0, 'd1s', 5) + P.text(1, 0, '1', 't1', dx=8, dy=-6)
    back = (P.poly([(1, 0), (c[0], c[1]), (c[0], -c[1])], 'f3 fx d3') +
            P.dot(c[0], c[1], 'd2s', 5, 'fx d2') + P.text(c[0], c[1], 'ω = −½ + (√3/2)i', 't2 fx d2', dx=-8, dy=-6, anchor='middle') +
            P.dot(c[0], -c[1], 'd2s', 5, 'fx d2') + P.text(c[0], -c[1], 'ω² = −½ − (√3/2)i', 't2 fx d2', dx=-8, dy=16, anchor='middle') +
            P.text(0.2, 0, '120°', 'sm fx d3', dy=-4))
    mcard(deck, 'Cube roots of unity', 'Solve z³ = 1 and plot the roots.', base, back,
          '<p>z³ − 1 = (z − 1)(z² + z + 1) = 0 → z = <b>1</b> or z = (−1 ± i√3)/2 = <b>ω, ω²</b>.</p>'
          '<p>The three roots sit on the unit circle <b>120° apart</b>: an equilateral triangle. Similarly the n-th roots of unity form a regular n-gon.</p>',
          'Cube roots of unity form an equilateral triangle', 'z^3=1: roots 1, ω, ω² = (−1±i√3)/2, 120° apart on the unit circle (equilateral triangle)',
          vb=f'0 0 300 {h}', hint='Factorise z³ − 1 first.')

    P2, h2 = eqplane(-0.45, 1.55, -0.35, 1.15, pad=(14, 6, 14, 6))
    w = (c[0], c[1]); w2 = (c[0], -c[1])
    base2 = P2.axes(labels=False)
    back2 = (vec(P2, 0, 0, 1, 0, 'c1', 'fx d1') + P2.text(0.5, 0, '1', 't1 fx d1', dy=-8) +
             vec(P2, 1, 0, 1 + w[0], w[1], 'c2', 'fx d2') + P2.text(1 + w[0] / 2, w[1] / 2, 'ω', 't2 fx d2', dx=10, dy=-4) +
             vec(P2, 1 + w[0], w[1], 1 + w[0] + w2[0], w[1] + w2[1], 'c3', 'fx d3') + P2.text(1 + w[0] + w2[0] / 2, w[1] + w2[1] / 2, 'ω²', 't3 fx d3', dx=-14, dy=-2) +
             P2.dot(0, 0, 'd0s', 4, 'fx d3'))
    mcard(deck, 'Cube roots of unity · sum', 'Why is 1 + ω + ω² = 0? Add the three roots as vectors head to tail.', base2, back2,
          '<p>The three unit vectors at 0°, 120° and 240° form a closed triangle, so they sum to <b>zero</b>.</p>'
          '<p>Algebra: ω satisfies ω² + ω + 1 = 0 and ω³ = 1. So ω² = 1/ω = ω̄ and ω̄ = ω².</p>',
          '1 + ω + ω² = 0 by vector addition', '1+ω+ω²=0 because the three cube roots are equally spaced unit vectors that close a triangle; ω³=1',
          vb=f'0 0 300 {h2}', hint='Draw 1, then ω from its tip, then ω².')


def quadratic_discriminant(deck):
    P = Plane(-2.2, 4.2, -4.6, 6.2, 300, 200, (24, 10, 12, 18))
    xt = _xy_ticks(-1, 3)
    yt = [(v, str(v).replace('-', '−')) for v in (-4, -2, 2, 4, 6)]
    f = lambda c: (lambda x: x * x - 2 * x + c)
    base = P.axes(xt, yt, grid=True) + P.curve(f(-3), 'c2', -1.9, 3.9) + P.curve(f(1), 'c3', -0.5, 2.5) + P.curve(f(2), 'c1', -0.5, 2.5)
    back = (P.dot(-1, 0, 'd2s', 4.5, 'fx d2') + P.dot(3, 0, 'd2s', 4.5, 'fx d2') + P.dot(1, 0, 'd3s', 4.5, 'fx d3') +
            '')
    mcard(deck, 'Quadratics · discriminant picture', 'y = x² − 2x + c for c = −3 (red), 1 (green), 2 (blue). How many x-axis crossings does each have?', base, back,
          '<p><b>D = b² − 4ac = 4 − 4c</b>. c = −3: D = 16 > 0 → two real roots (−1, 3). c = 1: D = 0 → one repeated root (x = 1). c = 2: D = −4 &lt; 0 → the parabola never meets the axis.</p>'
          '<p>When D &lt; 0 the roots are still there, just not on the real line: <b>1 ± i</b> (a conjugate pair).</p>',
          'Discriminant and x-axis crossings', 'D>0: two real roots (parabola cuts x-axis twice); D=0: touches once; D<0: no real roots, a complex conjugate pair, e.g. x²−2x+2 has 1±i',
          vb='0 0 300 200', hint='Compute b² − 4ac for each c.')


def polar_form_card(deck):
    P, h = eqplane(-2.2, 2.2, -0.6, 2, pad=(14, 6, 14, 10))
    ox, oy = P.X(0), P.Y(0)
    base = (P.axes(labels=False) + vec(P, 0, 0, -1, 1, 'c1') + P.dot(-1, 1, 'd1s', 4.5) + P.text(-1, 1, 'z = −1 + i', 't1', dx=-8, dy=-6, anchor='middle'))
    ra = 0.55 * (P.X(1) - ox)
    back = (f'<path class="c2 fx d2" d="M {ox + ra:.1f} {oy:.1f} A {ra:.1f} {ra:.1f} 0 0 0 {ox + ra * math.cos(3 * math.pi / 4):.1f} {oy - ra * math.sin(3 * math.pi / 4):.1f}"></path>' +
            P.text(0.5, 0.4, 'θ = 135°', 't2 fx d2', dx=6, dy=0) +
            P.line(-1, 0, -1, 1, 'guide fx d3') + P.text(-1, 0, 'reference angle 45°', 'sm fx d3', dx=-4, dy=14, anchor='middle') +
            P.text(-1, 1, '|z| = √2', 't3 fx d4', dx=14, dy=-22))
    mcard(deck, 'Polar form · argument', 'Write z = −1 + i in polar form r(cos θ + i sin θ). Which quadrant decides θ?', base, back,
          '<p>r = |z| = √((−1)² + 1²) = <b>√2</b>. z is in <b>quadrant II</b>, reference angle tan⁻¹(1/1) = π/4, so <b>θ = π − π/4 = 3π/4</b>.</p>'
          '<p>z = √2 (cos 3π/4 + i sin 3π/4).</p>'
          '<p class="no">Trap: tan⁻¹(y/x) = tan⁻¹(−1) = −π/4 is the wrong quadrant. Always sketch the point first.</p>',
          'Polar form of −1 + i: pick the quadrant first', 'For z=−1+i: r=√2, θ=3π/4 (second quadrant); tan⁻¹(y/x) alone gives −π/4 (wrong quadrant)',
          vb=f'0 0 300 {h}', hint='Sketch the point before computing the angle.')


def locus_cards(deck):
    P, h = eqplane(-2, 4.2, -2, 3.6, pad=(18, 6, 12, 14))
    ox, oy = P.X(0), P.Y(0)
    s = P.X(1) - ox
    cx, cy = P.X(1), P.Y(1)
    base = (P.axes(_xy_ticks(-1, 3), _xy_ticks(-1, 3), grid=True, xl='Re', yl='Im') + P.dot(1, 1, 'd1s', 4) + P.text(1, 1, 'c = 1 + i', 't1', dx=6, dy=16))
    back = (f'<circle class="f1 fx d2" cx="{cx:.1f}" cy="{cy:.1f}" r="{2 * s:.1f}"></circle>' + P.dot(1, 1, 'd1s', 4, 'fx d2') + P.line(1, 1, 3, 1, 'c2 fx d3') +
            P.text(2, 1, 'r = 2', 't2 fx d3', 'middle', dy=-6))
    mcard(deck, 'Locus · circle', 'Describe the set of z with |z − (1 + i)| = 2.', base, back,
          '<p>|z − c| is the <b>distance</b> from z to c. So all z at distance 2 from 1 + i: a <b>circle</b>, centre (1, 1), radius 2.</p>'
          '<p>|z − c| &lt; r is the inside, |z − c| &gt; r the outside. Algebra check: (x − 1)² + (y − 1)² = 4.</p>',
          'Locus |z − c| = r is a circle', '|z−c|=r is the circle with centre c and radius r; |z−c|<r is its interior; |z−(1+i)|=2 is (x−1)²+(y−1)²=4',
          vb=f'0 0 300 {h}', hint='Read |z − c| as “distance from z to c”.')

    P, h = eqplane(-2, 3, -2, 3, pad=(18, 6, 12, 14))
    base = (P.axes(_xy_ticks(-1, 2), _xy_ticks(-1, 2), grid=True, xl='Re', yl='Im') + P.dot(0, 1, 'd1s', 4.5) + P.text(0, 1, 'i', 't1', dx=-10, dy=-4) +
            P.dot(1, 0, 'd2s', 4.5) + P.text(1, 0, '1', 't2', dx=6, dy=14))
    back = (P.line(-1.6, -1.6, 2.6, 2.6, 'c3 fx d2') + P.dot(0.5, 0.5, 'd3s', 4, 'fx d3') +
            P.line(0, 1, 1, 0, 'guide fx d3') + P.text(2.6, 2.4, 'y = x', 't3 fx d2', anchor='end', dx=-8, dy=-8))
    mcard(deck, 'Locus · perpendicular bisector', 'Describe the set of z with |z − i| = |z − 1|.', base, back,
          '<p>Points equidistant from i (0, 1) and 1 (1, 0): the <b>perpendicular bisector</b> of the segment joining them, the line <b>y = x</b>.</p>'
          '<p>Algebra: x² + (y − 1)² = (x − 1)² + y² ⟹ −2y = −2x ⟹ y = x.</p>',
          'Locus |z − a| = |z − b| is a perpendicular bisector', '|z−a|=|z−b| is the perpendicular bisector of the segment joining a and b; |z−i|=|z−1| is the line y=x',
          vb=f'0 0 300 {h}', hint='Equal distances from two fixed points.')


# ================================================================ Maths 11 Ch 5 Linear inequalities
def nl_answer(deck, q, segs, note, term, definition, lo=-4, hi=8, tag='Inequalities · number line', hint='Solve first, then mark the endpoints.', extra_marks=''):
    """Number-line answer card. segs = [(a, b, a_closed, b_closed, cls)]; a/b None = infinite."""
    X = _nl(lo, hi)
    ticks = ''.join(f'<line class="ax" x1="{X(v):.1f}" y1="71" x2="{X(v):.1f}" y2="79"></line>'
                    f'<text class="num" x="{X(v):.1f}" y="95">{str(v).replace("-", "−")}</text>' for v in range(lo + 1, hi))
    axis = '<line class="ax" x1="8" y1="75" x2="292" y2="75" marker-end="url(#pk)"></line><line class="ax" x1="8" y1="75" x2="14" y2="75"></line>' + ticks
    back = ''
    for k, (a, b, ac, bc, cls) in enumerate(segs):
        xa = X(a) if a is not None else 10
        xb = X(b) if b is not None else 290
        fx = f'fx d{min(k + 2, 5)}'
        d0 = DOT[cls]
        back += f'<line class="{cls} {fx}" x1="{xa:.1f}" y1="75" x2="{xb:.1f}" y2="75"></line>'
        if a is not None:
            back += (f'<circle class="{d0} {fx}" cx="{xa:.1f}" cy="75" r="5.5"></circle>' if ac else f'<circle class="f0 {cls} {fx}" cx="{xa:.1f}" cy="75" r="5.5"></circle>')
        else:
            back += f'<path class="{d0} {fx}" d="M 10 75 l 9 -5 v 10 Z"></path>'
        if b is not None:
            back += (f'<circle class="{d0} {fx}" cx="{xb:.1f}" cy="75" r="5.5"></circle>' if bc else f'<circle class="f0 {cls} {fx}" cx="{xb:.1f}" cy="75" r="5.5"></circle>')
        else:
            back += f'<path class="{d0} {fx}" d="M 290 75 l -9 -5 v 10 Z"></path>'
    mcard(deck, tag, q, axis, back + extra_marks, note, term, definition, vb='0 0 300 110', hint=hint)


def sign_flip(deck):
    lo, hi = -4, 4
    X = _nl(lo, hi)
    ticks = ''.join(f'<line class="ax" x1="{X(v):.1f}" y1="71" x2="{X(v):.1f}" y2="79"></line><text class="num" x="{X(v):.1f}" y="95">{str(v).replace("-", "−")}</text>' for v in range(lo + 1, hi))
    axis = '<line class="ax" x1="8" y1="75" x2="292" y2="75" marker-end="url(#pk)"></line>' + ticks
    a0, b0 = X(2), X(3)
    front = (f'<circle class="d1s" cx="{a0:.1f}" cy="75" r="6"></circle><text class="t1" x="{a0:.1f}" y="58" text-anchor="middle">2</text>'
             f'<circle class="d2s" cx="{b0:.1f}" cy="75" r="6"></circle><text class="t2" x="{b0:.1f}" y="58" text-anchor="middle">3</text>'
             '<text class="lbl" x="150" y="28" text-anchor="middle">2 &lt; 3</text>')
    da, db = X(-2) - a0, X(-3) - b0
    css = (f'.pp .mv1{{animation:m1 2.2s ease-in-out .6s both}}@keyframes m1{{from{{transform:translateX(0)}}to{{transform:translateX({da:.1f}px)}}}}'
           f'.pp .mv2{{animation:m2 2.2s ease-in-out .6s both}}@keyframes m2{{from{{transform:translateX(0)}}to{{transform:translateX({db:.1f}px)}}}}')
    back = (f'<g class="mv1"><circle class="d1s" cx="{a0:.1f}" cy="75" r="6"></circle></g><g class="mv2"><circle class="d2s" cx="{b0:.1f}" cy="75" r="6"></circle></g>'
            f'<text class="t1 fx d5" x="{X(-2):.1f}" y="58" text-anchor="middle">−2</text><text class="t2 fx d5" x="{X(-3):.1f}" y="58" text-anchor="middle">−3</text>'
            '<text class="t3 fx d5" x="150" y="28" text-anchor="middle">−3 &lt; −2 : order reversed</text>')
    mcard(deck, 'Reversing the sign · intuition', 'Multiply both sides of 2 < 3 by −1. Which way does the inequality go, and why?', axis, back,
          '<p>Multiplying by −1 <b>mirrors the number line</b> about 0: 2 → −2 and 3 → −3. The larger number is now on the left, so <b>&lt; becomes &gt;</b>: −2 &gt; −3.</p>'
          '<p>Rule: multiply or divide by a <b>negative</b> → flip the sign. By a positive → no change.</p>',
          'Multiplying by a negative number reverses the inequality', 'Multiplying or dividing an inequality by a negative number mirrors the number line, so the inequality sign reverses: 2<3 gives −2>−3',
          css=css, vb='0 0 300 110', front_only=front, hint='Where do 2 and 3 land after the mirror?')


def wavy_curve(deck):
    P = Plane(-0.8, 5.2, -5, 5, 300, 200, (20, 10, 12, 30))
    f = lambda x: (x - 1) * (x - 2) * (x - 4) / 1.5
    xt = [(v, str(v)) for v in (1, 2, 4)]
    base = P.axes(xt, [], labels=False) + P.curve(f, 'c1', -0.7, 5.1, clip=(-4.9, 4.9))
    y0 = P.Y(0)
    y1 = P.Y(-4.8)
    signs = (f'<text class="t3 bigs fx d2" x="{P.X(0.2):.1f}" y="{y1:.1f}" text-anchor="middle">−</text>'
             f'<text class="t2 bigs fx d2" x="{P.X(1.5):.1f}" y="{y1:.1f}" text-anchor="middle">+</text>'
             f'<text class="t3 bigs fx d2" x="{P.X(3):.1f}" y="{y1:.1f}" text-anchor="middle">−</text>'
             f'<text class="t2 bigs fx d2" x="{P.X(4.7):.1f}" y="{y1:.1f}" text-anchor="middle">+</text>')
    band = (f'<line class="c3 fx d3" x1="{P.X(-0.7):.1f}" y1="{y0 + 18:.1f}" x2="{P.X(1):.1f}" y2="{y0 + 18:.1f}"></line>'
            f'<line class="c3 fx d3" x1="{P.X(2):.1f}" y1="{y0 + 18:.1f}" x2="{P.X(4):.1f}" y2="{y0 + 18:.1f}"></line>'
            + P.dot(1, 0, 'd3s', 4.5, 'fx d3') + P.dot(2, 0, 'd3s', 4.5, 'fx d3') + P.dot(4, 0, 'd3s', 4.5, 'fx d3'))
    mcard(deck, 'Wavy-curve method · beyond the textbook', 'Solve (x − 1)(x − 2)(x − 4) ≤ 0 using signs.', base, signs + band,
          '<p>Roots 1, 2, 4 split the line into 4 pieces. Start with <b>+ on the far right</b> (leading coefficient positive) and <b>alternate at every simple root</b>: + − + −.</p>'
          '<p>Want ≤ 0 → the “−” pieces with roots included: <b>(−∞, 1] ∪ [2, 4]</b>.</p>'
          '<p class="no">A repeated root (x − 2)² does not change the sign.</p>',
          'Solve a polynomial inequality by the wavy-curve method',
          '(x−1)(x−2)(x−4) ≤ 0: signs alternate +,−,+,− from the right across simple roots; solution (−∞,1] ∪ [2,4]; repeated roots do not flip the sign',
          hint='Mark roots, start + on the right, alternate.', css='.pp .bigs{font-size:22px}')


def modulus_band(deck):
    lo, hi = -2, 8
    X = _nl(lo, hi)
    ticks = ''.join(f'<line class="ax" x1="{X(v):.1f}" y1="71" x2="{X(v):.1f}" y2="79"></line><text class="num" x="{X(v):.1f}" y="95">{str(v).replace("-", "−")}</text>' for v in range(lo + 1, hi))
    axis = '<line class="ax" x1="8" y1="75" x2="292" y2="75" marker-end="url(#pk)"></line>' + ticks
    front = f'<circle class="d0s" cx="{X(3):.1f}" cy="75" r="5"></circle><text class="lbl" x="{X(3):.1f}" y="58" text-anchor="middle">3</text>'
    back = (f'<line class="c1 fx d2" x1="{X(1):.1f}" y1="75" x2="{X(5):.1f}" y2="75"></line>'
            f'<circle class="f0 c1 fx d2" cx="{X(1):.1f}" cy="75" r="5.5"></circle><circle class="f0 c1 fx d2" cx="{X(5):.1f}" cy="75" r="5.5"></circle>'
            f'<path class="guide fx d3" d="M {X(3):.1f} 42 L {X(5):.1f} 42"></path><text class="t2 fx d3" x="{X(4):.1f}" y="36" text-anchor="middle">distance &lt; 2</text>'
            f'<path class="guide fx d3" d="M {X(3):.1f} 42 L {X(1):.1f} 42"></path>')
    mcard(deck, 'Modulus inequalities · intuition', 'Solve |x − 3| < 2 by reading it as a distance.', axis, back,
          '<p>|x − 3| is the <b>distance from x to 3</b>. “Distance &lt; 2” means x lies within 2 of 3: <b>1 &lt; x &lt; 5</b>.</p>'
          '<p><b>|x − a| &lt; r ⟺ a − r &lt; x &lt; a + r</b> (one band, AND).<br><b>|x − a| &gt; r ⟺ x &lt; a − r or x &gt; a + r</b> (two outer rays, OR).</p>',
          '|x − a| < r as a distance band', '|x−a|<r means a−r<x<a+r (within distance r of a); |x−a|>r means x<a−r or x>a+r; |x−3|<2 gives (1,5)',
          vb='0 0 300 110', front_only=front, hint='Read |x − a| as the distance between x and a.')


def half_plane(deck):
    P, h = eqplane(-1.5, 5, -1.5, 3.8, pad=(20, 6, 12, 16))
    # line 2x + 3y = 6 : y = 2 - 2x/3
    line = lambda x: 2 - 2 * x / 3
    base = P.axes(_xy_ticks(-1, 4), _xy_ticks(-1, 3), grid=True, xl='x', yl='y') + P.line(-1.2, line(-1.2), 4.8, line(4.8), 'c1')
    poly = [(-1.5, line(-1.5)), (5, line(5)), (5, -1.5), (-1.5, -1.5)]
    back = (P.poly(poly, 'ns1 fx d3') + P.dot(0, 0, 'd2s', 4.5, 'fx d2') + P.text(0, 0, '(0,0): 0 ≤ 6 ✓', 't2 fx d2', dx=8, dy=-8) +
            P.text(2.8, 1.6, '2x + 3y ≤ 6', 't1 fx d3', dx=6, dy=-2))
    mcard(deck, 'Two variables · half-plane · beyond the textbook', 'Represent 2x + 3y ≤ 6 on the plane. How do you decide which side to shade?', base, back,
          '<p>1) Draw the line 2x + 3y = 6 through (3, 0) and (0, 2). <b>Solid</b> for ≤ or ≥; <b>dashed</b> for &lt; or &gt;.</p>'
          '<p>2) Test the origin: 0 ≤ 6 is true → shade the side <b>containing (0, 0)</b>. (If the line passes through the origin, test another point.)</p>',
          'Graph a linear inequality in two variables (test-point method)', 'Draw the boundary line (solid for ≤ ≥, dashed for < >), then shade the side containing a test point that satisfies the inequality, e.g. origin for 2x+3y≤6',
          vb=f'0 0 300 {h}', hint='Find where the boundary line cuts the axes.')


def feasible_region(deck):
    P, h = eqplane(-0.8, 5.2, -0.8, 4.2, pad=(20, 6, 12, 16))
    base = (P.axes(_xy_ticks(1, 4), _xy_ticks(1, 3), grid=True, xl='x', yl='y') + P.line(1, -0.6, 1, 3.9, 'c2') + P.line(-0.2, 4.2, 4.8, -0.8, 'c1'))
    back = (P.poly([(1, 0), (4, 0), (1, 3)], 'ns3 fx d3') +
            P.dot(1, 0, 'd3s', 4.5, 'fx d4') + P.dot(4, 0, 'd3s', 4.5, 'fx d4') + P.dot(1, 3, 'd3s', 4.5, 'fx d4') +
            P.text(1, 0, '(1, 0)', 'lbl fx d4', dx=-4, dy=16, anchor='middle') + P.text(4, 0, '(4, 0)', 'lbl fx d4', dx=4, dy=16, anchor='middle') +
            P.text(1, 3, '(1, 3)', 'lbl fx d4', dx=10, dy=-6))
    mcard(deck, 'System of inequalities · beyond the textbook', 'Show the solution region of x + y ≤ 4, x ≥ 1 and y ≥ 0.', base, back,
          '<p>The solution of a system is the <b>overlap</b> of all the half-planes: here the triangle with corners (1, 0), (4, 0), (1, 3).</p>'
          '<p>Corner points come from pairs of boundary lines. (This is exactly the <b>feasible region</b> of linear programming in Class 12.)</p>',
          'Solution region of a system of linear inequalities', 'The solution of a system is the common part of the half-planes; x+y≤4, x≥1, y≥0 gives the triangle (1,0),(4,0),(1,3) (feasible region)',
          vb=f'0 0 300 {h}', hint='Shade each half-plane; keep the overlap.')


# ================================================================ Maths 11 Ch 6 Permutations and combinations
def tree_pants_shirts(deck):
    ys = [38, 112, 186]
    def node(x, y, t, cls='f0'):
        return f'<circle class="{cls}" cx="{x}" cy="{y}" r="15"></circle><text class="lbl" x="{x}" y="{y + 4}" text-anchor="middle">{t}</text>'
    base = f'<circle class="f1" cx="24" cy="112" r="8"></circle><text class="sm" x="24" y="136" text-anchor="middle">start</text>'
    back = ''
    k = 0
    for i, y in enumerate(ys):
        k += 1
        back += (f'<line class="c0 fx d{k}" x1="30" y1="112" x2="92" y2="{y}"></line><g class="fx d{k}">{node(107, y, "P" + str(i + 1))}</g>')
        for j, dy in enumerate((-19, 19)):
            k2 = min(k + 1 + j, 6)
            back += (f'<line class="c1 fx d{k2}" x1="122" y1="{y}" x2="196" y2="{y + dy}"></line>'
                     f'<g class="fx d{k2}"><rect class="f1" x="198" y="{y + dy - 12}" width="64" height="24" rx="8"></rect>'
                     f'<text class="lbl" x="230" y="{y + dy + 4}" text-anchor="middle">P{i + 1}S{j + 1}</text></g>')
    front = ''.join(node(107, y, 'P' + str(i + 1)) for i, y in enumerate(ys)) + '<text class="t1" x="150" y="20" text-anchor="middle">3 pants, 2 shirts</text>'
    back += '<text class="t4 fx d6" x="150" y="230" text-anchor="middle">3 × 2 = 6 outfits</text>'
    mcard(deck, 'Multiplication principle · tree diagram', 'Mohan has 3 pants and 2 shirts. How many pant–shirt outfits? Draw the tree.', '', back,
          '<p>Each of the <b>3</b> pants pairs with <b>2</b> shirts → <b>3 × 2 = 6</b> outfits. Choices in <b>stages</b> multiply.</p>'
          '<p>For three stages (2 bags, 3 tiffin boxes, 2 bottles): 2 × 3 × 2 = <b>12</b>.</p>',
          'Multiplication principle: tree of 3 pants × 2 shirts', 'If one event can happen in m ways and then another in n ways, the pair can happen in m×n ways; 3 pants × 2 shirts = 6',
          vb='0 0 300 240', front_only=front, hint='Each pant has how many shirt options?')


def slot_method(deck):
    def boxes(lbl_cls, vals, order):
        o = ''
        for i, (name, v, o_) in enumerate(zip(['Hundreds', 'Tens', 'Units'], vals, order)):
            x = 22 + i * 90
            o += f'<rect class="f0" x="{x}" y="60" width="76" height="60" rx="10"></rect><text class="sm" x="{x + 38}" y="52" text-anchor="middle">{name}</text>'
        return o
    base = boxes('', ['', '', ''], [0, 0, 0])
    nums = [('3', 't1'), ('4', 't1'), ('2', 't2')]
    back = ''
    order = {2: 1, 1: 2, 0: 3}
    delays = {2: 2, 1: 3, 0: 4}
    for i, (v, c) in enumerate(nums):
        x = 22 + i * 90
        back += (f'<text class="{c} bign fx d{delays[i]}" x="{x + 38}" y="102" text-anchor="middle">{v}</text>'
                 f'<circle class="f4 fx d{delays[i]}" cx="{x + 12}" cy="72" r="9"></circle><text class="lbl fx d{delays[i]}" x="{x + 12}" y="76" text-anchor="middle">{order[i]}</text>')
    back += ('<text class="t2 fx d2" x="248" y="146" text-anchor="middle">2 or 4</text>'
             '<text class="sm fx d3" x="158" y="146" text-anchor="middle">4 left</text>'
             '<text class="sm fx d4" x="68" y="146" text-anchor="middle">3 left</text>'
             '<text class="t3 fx d5" x="150" y="182" text-anchor="middle">3 × 4 × 2 = 24</text>')
    mcard(deck, 'Slot method · restricted place first', 'How many 3-digit even numbers can be made from 1, 2, 3, 4, 5 with no repetition?', base, back,
          '<p>Fill the <b>restricted place first</b>: the units digit must be 2 or 4 → 2 ways. Then the tens digit: 4 digits left. Then hundreds: 3 left.</p>'
          '<p><b>2 × 4 × 3 = 24</b>. If you fill hundreds first, the number of choices for the units digit depends on what you used: messy.</p>',
          'Slot method: fill the restricted position first', 'Even 3-digit numbers from 1..5 without repetition: units digit 2 or 4 (2 ways), then tens (4), then hundreds (3): 24; fill the restricted place first',
          css='.pp .bign{font-size:30px}', vb='0 0 300 196', hint='Which place has a condition?')


def pascal_triangle(deck):
    rows = [[C_ for C_ in _pascal_row(n)] for n in range(7)]
    o = ''
    for n, row in enumerate(rows):
        y = 26 + n * 30
        for k, v in enumerate(row):
            x = 172 + (k - n / 2) * 38
            cls = 'lbl'
            if n == 6 and k == 2: cls = 't3'
            if n == 5 and k in (1, 2): cls = 't4'
            o += f'<text class="{cls} pt fx d{min(n // 2 + 1, 5)}" x="{x:.1f}" y="{y}" text-anchor="middle">{v}</text>'
        o += f'<text class="sm fx d{min(n // 2 + 1, 5)}" x="8" y="{y}">n = {n}</text>'
    back = o + (f'<line class="guide fx d5" x1="{172 + (1 - 5 / 2) * 38:.1f}" y1="{26 + 5 * 30 + 4}" x2="{172 + (2 - 6 / 2) * 38 + 4:.1f}" y2="{26 + 6 * 30 - 14}"></line>'
                f'<line class="guide fx d5" x1="{172 + (2 - 5 / 2) * 38:.1f}" y1="{26 + 5 * 30 + 4}" x2="{172 + (2 - 6 / 2) * 38 - 4:.1f}" y2="{26 + 6 * 30 - 14}"></line>')
    front = '<text class="lbl" x="150" y="100" text-anchor="middle">row n lists ⁿC₀, ⁿC₁, …, ⁿCₙ</text><text class="t1" x="150" y="130" text-anchor="middle">1 &#160; 1 1 &#160; 1 2 1 &#160; 1 3 3 1 …</text>'
    mcard(deck, 'Pascal’s triangle · nCr', 'Build Pascal’s triangle. How does it prove ⁿCᵣ + ⁿCᵣ₋₁ = ⁿ⁺¹Cᵣ?', '', back,
          '<p>Each entry = the <b>sum of the two above it</b>: 5 + 10 = 15 → ⁵C₁ + ⁵C₂ = ⁶C₂.</p>'
          '<p>Rows are <b>symmetric</b> (ⁿCᵣ = ⁿCₙ₋ᵣ) and row n sums to <b>2ⁿ</b> (1, 2, 4, 8, 16, 32, 64).</p>',
          'Pascal’s triangle and Pascal’s rule', 'Each entry of Pascal’s triangle is the sum of the two above: nCr + nC(r−1) = (n+1)Cr; rows are symmetric and sum to 2^n',
          css='.pp .pt{font-size:15px}', vb='0 0 300 214', front_only=front, hint='Add the two numbers above.')


def _pascal_row(n):
    from math import comb
    return [comb(n, k) for k in range(n + 1)]


def circular_seating(deck):
    cx, cy, r = 150, 100, 58
    seats = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    base = (f'<circle class="ghost" cx="{cx}" cy="{cy}" r="{r}"></circle><circle class="f0" cx="{cx}" cy="{cy}" r="30"></circle>'
            '<text class="sm" x="150" y="104" text-anchor="middle">table</text>')
    people = ''
    css = ''
    for k, name in enumerate('ABCD'):
        x0, y0 = seats[k]
        pts = [(seats[(k + s) % 4][0] - x0, seats[(k + s) % 4][1] - y0) for s in range(5)]
        css += mkeyframes(f'sit{k}', pts, 6, 'steps(1,end)', 0.4)
        people += (f'<g transform="translate({x0},{y0})"><g class="sit{k}"><circle class="f{k + 1}" cx="0" cy="0" r="14"></circle>'
                   f'<text class="lbl" x="0" y="4" text-anchor="middle">{name}</text></g></g>')
    front_people = ''.join(f'<circle class="f{k + 1}" cx="{x}" cy="{y}" r="14"></circle><text class="lbl" x="{x}" y="{y + 4}" text-anchor="middle">{"ABCD"[k]}</text>' for k, (x, y) in enumerate(seats))
    mcard(deck, 'Circular arrangements · beyond the textbook', 'In how many ways can 4 people sit around a round table?', base, people,
          '<p>Turning everyone one seat round gives the <b>same</b> arrangement (same neighbours). The 4 rotations count as one.</p>'
          '<p>So fix one person and arrange the other 3: <b>(4 − 1)! = 6</b>. In general <b>(n − 1)!</b>; for necklaces (which can be flipped) <b>(n − 1)!/2</b>.</p>',
          'Circular permutations: (n − 1)!', 'n people around a round table: (n−1)! arrangements, since rotations are equal (fix one person); necklace/garland with flipping: (n−1)!/2',
          css=css, vb='0 0 300 200', front_only=front_people, hint='Do rotations count as different?')


def gaps_method(deck):
    girls = ''.join(f'<circle class="f2" cx="{40 + i * 48}" cy="100" r="14"></circle><text class="lbl" x="{40 + i * 48}" y="104" text-anchor="middle">G</text>' for i in range(5))
    gaps = ''.join(f'<text class="t1 fx d1" x="{16 + i * 48}" y="104" text-anchor="middle">×</text><text class="sm fx d1" x="{16 + i * 48}" y="124" text-anchor="middle">{i + 1}</text>' for i in range(6))
    boys = ''.join(f'<circle class="f1 fx d{k + 3}" cx="{16 + g * 48}" cy="60" r="12"></circle><text class="lbl fx d{k + 3}" x="{16 + g * 48}" y="64" text-anchor="middle">B</text>'
                   f'<line class="guide fx d{k + 3}" x1="{16 + g * 48}" y1="72" x2="{16 + g * 48}" y2="90"></line>' for k, g in enumerate((0, 2, 5)))
    mcard(deck, 'Gaps method · no two together', '5 girls and 3 boys sit in a row so that no two boys are together. How many arrangements?', girls, gaps + boys +
          '<text class="t3 fx d5" x="150" y="170" text-anchor="middle">5! × ⁶P₃ = 120 × 120 = 14400</text>',
          '<p>Seat the <b>girls first</b>: 5! ways. They create <b>6 gaps</b> (×) including both ends. Boys go into 3 different gaps, in order: ⁶P₃ = 120.</p>'
          '<p>Total 5! × ⁶P₃ = <b>14400</b>. Method for “not together”: arrange the others first, then insert.</p>',
          'Gaps method: no two boys together (Example 24)', '5 girls in 5! ways create 6 gaps; choose and order 3 gaps for the boys: 6P3; total 5!·6P3 = 14400',
          vb='0 0 300 184', hint='Seat the girls first. How many gaps do they make?')
