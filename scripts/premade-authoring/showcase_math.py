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
