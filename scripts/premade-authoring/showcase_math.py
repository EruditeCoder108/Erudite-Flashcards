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


# ================================================================ Maths 11 Ch 7 Binomial theorem
def expansion_choices(deck):
    import itertools
    groups = []
    for k in range(4):
        groups.append([''.join('b' if i in pos else 'a' for i in range(3)) for pos in itertools.combinations(range(3), k)])
    rows = ''
    for k, g in enumerate(groups):
        chips = ''.join(f'<span class="ch">{w}</span>' for w in g)
        rows += (f'<div class="row fx d{k + 1}"><div class="chs">{chips}</div><div class="res">{len(g)} × a<sup>{3 - k}</sup>b<sup>{k}</sup></div></div>')
    css = ('.pp .chs{display:flex;gap:6px;flex-wrap:wrap;flex:1}.pp .ch{padding:4px 9px;border-radius:9px;background:#fff;border:1px solid #e8e1d2;'
           'font:600 15px Georgia,serif;color:#1d5fd6;letter-spacing:.06em}.pp .row{display:flex;gap:8px;align-items:center;padding:7px 0;border-bottom:1px dashed #e3dac6}'
           '.pp .res{font-weight:700;color:#c77700;min-width:88px;text-align:right}')
    q = 'Why is the coefficient of aⁿ⁻ʳbʳ in (a + b)ⁿ equal to ⁿCᵣ? Expand (a + b)³ by choosing a letter from each bracket.'
    front = (f'<div class="w pp"><p class="tag">Binomial theorem · why ⁿCᵣ</p><h2>{q}</h2>'
             '<p class="lbl">(a + b)(a + b)(a + b): from each bracket you pick <b>a</b> or <b>b</b>. List all 2 × 2 × 2 = 8 picks and group them by how many b’s you picked.</p>'
             '<p class="hint">Count the picks in each group.</p></div>')
    back = (f'<div class="w pp"><p class="tag">Binomial theorem · why ⁿCᵣ</p><h2>{q}</h2>{rows}'
            '<div class="eq fx d5"><p>Picks with r b’s = ways to choose <b>which r brackets</b> give b = <b>ⁿCᵣ</b>.</p>'
            '<p>(a + b)³ = a³ + 3a²b + 3ab² + b³ and the 8 picks split as 1 + 3 + 3 + 1.</p></div></div>')
    _card(deck, 'Why the binomial coefficient is ⁿCᵣ (choose which brackets give b)',
          'In (a+b)^n each term aⁿ⁻ʳbʳ arises by choosing b from r of the n brackets, in nCr ways', PAPER + css, front, back)


def coefficient_bars(deck):
    from math import comb
    n = 10
    vals = [comb(n, k) for k in range(n + 1)]
    mx = max(vals)
    base_y = 150
    bars, labs = '', ''
    for k, v in enumerate(vals):
        h = 110 * v / mx
        x = 10 + k * 26
        cls = 'f4' if k == n // 2 else 'f1'
        bars += (f'<rect class="{cls} grow gd{k}" x="{x}" y="{base_y - h:.1f}" width="22" height="{h:.1f}" rx="3"></rect>')
        labs += f'<text class="num" x="{x + 11}" y="{base_y - h - 4:.1f}">{v}</text><text class="sm" x="{x + 11}" y="{base_y + 13}" text-anchor="middle">{k}</text>'
    css = ('.pp .grow{transform-box:fill-box;transform-origin:50% 100%;animation:gr 1.2s ease-out both}@keyframes gr{from{transform:scaleY(0)}to{transform:scaleY(1)}}'
           + ''.join(f'.pp .gd{k}{{animation-delay:{0.3 + 0.12 * min(k, n - k):.2f}s}}' for k in range(n + 1)))
    axis = f'<line class="ax" x1="6" y1="{base_y}" x2="296" y2="{base_y}"></line><text class="sm" x="150" y="176" text-anchor="middle">r  (coefficient of xʳ in (1 + x)¹⁰)</text>'
    mcard(deck, 'Binomial coefficients · shape', 'Sketch ¹⁰C₀ … ¹⁰C₁₀. Which is the greatest, and what is the pattern?', axis,
          bars + labs,
          '<p>Symmetric bell: ¹⁰Cᵣ = ¹⁰C₁₀₋ᵣ. Rising to the <b>middle coefficient ¹⁰C₅ = 252</b>, then falling. Total 2¹⁰ = 1024.</p>'
          '<p>Rule: n even → one middle coefficient ⁿCₙ/₂; n odd → two equal middle ones, ⁿC₍ₙ₋₁₎/₂ = ⁿC₍ₙ₊₁₎/₂.</p>',
          'Greatest binomial coefficient is the middle one', 'ⁿCr is largest at r = n/2 (n even) or r=(n±1)/2 (n odd, two equal); symmetric; ¹⁰C₅ = 252 is the greatest for n = 10',
          css=css, vb='0 0 300 184', hint='Compare ¹⁰C₄, ¹⁰C₅, ¹⁰C₆.')


def small_x_approx(deck):
    P = Plane(-0.32, 0.36, -0.3, 4.4, 300, 200, (26, 10, 12, 20))
    xt = [(-0.2, '−0.2'), (0.2, '0.2')]
    yt = [(1, '1'), (2, '2'), (3, '3'), (4, '4')]
    base = P.axes(xt, yt, grid=True, xl='x', yl='y') + P.curve(lambda x: (1 + x) ** 5, 'c1', -0.3, 0.34)
    back = (P.curve(lambda x: 1 + 5 * x, 'c2 fx d2', -0.3, 0.34, clip=(-0.3, 4.4)) + P.curve(lambda x: 1 + 5 * x + 10 * x * x, 'c3 fx d3', -0.3, 0.34, clip=(-0.3, 4.4)) +
            P.text(-0.3, 4.15, '(1 + x)⁵', 't1 fx d2', dx=30) + P.text(-0.3, 3.6, '1 + 5x', 't2 fx d2', dx=30) + P.text(-0.3, 3.05, '1 + 5x + 10x²', 't3 fx d3', dx=30))
    mcard(deck, 'Binomial approximation', 'For small x, approximate (1 + x)⁵ using the first few terms. Which is closer?', base, back,
          '<p>(1 + x)⁵ = 1 + 5x + 10x² + 10x³ + … Near x = 0 the higher powers shrink fast, so <b>(1 + x)ⁿ ≈ 1 + nx</b>; one more term gives 1 + nx + n(n − 1)x²/2 (even closer).</p>'
          '<p>Example (Misc Q4): (0.99)⁵ = (1 − 0.01)⁵ ≈ 1 − 0.05 + 0.001 = <b>0.951</b> (true value 0.95099…).</p>',
          '(1 + x)ⁿ ≈ 1 + nx for small x', 'For small x, (1+x)^n ≈ 1 + nx (tangent) and ≈ 1 + nx + n(n−1)x²/2 (better); (0.99)^5 ≈ 1 − 0.05 + 0.001 = 0.951',
          vb='0 0 300 200', hint='Which powers of x matter near 0?')


# ================================================================ Maths 11 Ch 8 Sequences and series
def infinite_gp_strip(deck):
    x0, w, y = 20, 130, 70          # 1 unit = 130 px, so 2 units = 260
    segs, labs = '', ''
    pos, ln = 0.0, 1.0
    for k in range(9):
        xa, xb = x0 + pos * w, x0 + (pos + ln) * w
        cls = 'f1' if k % 2 == 0 else 'f4'
        segs += f'<rect class="{cls} fx d{min(k // 2 + 1, 6)}" x="{xa:.1f}" y="{y}" width="{max(xb - xa - 1, 1):.1f}" height="34" rx="2"></rect>'
        if k < 5:
            labs += f'<text class="lbl fx d{min(k // 2 + 1, 6)}" x="{(xa + xb) / 2:.1f}" y="{y + 22}" text-anchor="middle">{["1", "½", "¼", "⅛", "1/16"][k]}</text>'
        pos += ln
        ln /= 2
    axis = (f'<line class="ax" x1="{x0}" y1="122" x2="{x0 + 2 * w + 10}" y2="122"></line>'
            + ''.join(f'<line class="ax" x1="{x0 + v * w / 2:.1f}" y1="118" x2="{x0 + v * w / 2:.1f}" y2="126"></line><text class="num" x="{x0 + v * w / 2:.1f}" y="140">{v / 2:g}</text>' for v in range(5)))
    limit = (f'<line class="guide fx d5" x1="{x0 + 2 * w}" y1="52" x2="{x0 + 2 * w}" y2="122"></line>'
             f'<text class="t2 fx d5" x="{x0 + 2 * w}" y="44" text-anchor="middle">limit 2</text>')
    mcard(deck, 'Infinite G.P. · intuition', 'Add 1 + ½ + ¼ + ⅛ + … forever. Does the sum grow without bound? What does it approach?', axis, segs + labs + limit,
          '<p>Each new piece is half of the gap left, so the running total creeps up to <b>2</b> but never passes it.</p>'
          '<p>Formula: a G.P. with |r| &lt; 1 has infinite sum <b>S∞ = a/(1 − r)</b> = 1/(1 − ½) = 2.</p>'
          '<p class="no">If |r| ≥ 1 the terms do not shrink and the sum does not settle.</p>',
          'Infinite G.P. sum: 1 + 1/2 + 1/4 + … = 2', 'Infinite G.P. with |r|<1 sums to a/(1−r); 1+1/2+1/4+… approaches 2; no finite sum if |r| ≥ 1',
          vb='0 0 300 150', hint='How much of the remaining gap does each term fill?')


def ap_vs_gp(deck):
    P = Plane(0, 6.8, 0, 8.2, 300, 200, (26, 10, 12, 22))
    xt = [(v, str(v)) for v in range(1, 7)]
    yt = [(v, str(v)) for v in (2, 4, 6, 8)]
    ap = [1 + 1.2 * (n - 1) for n in range(1, 7)]
    gp = [1.5 ** (n - 1) for n in range(1, 7)]
    base = P.axes(xt, yt, grid=True, xl='n', yl='aₙ')
    pts_ap = ''.join(P.dot(n, v, 'd1s', 4.5, f'fx d{min(n // 2 + 1, 4)}') for n, v in zip(range(1, 7), ap))
    pts_gp = ''.join(P.dot(n, v, 'd2s', 4.5, f'fx d{min(n // 2 + 1, 4)}') for n, v in zip(range(1, 7), gp))
    lines = (P.curve(lambda x: 1 + 1.2 * (x - 1), 'c1 fx d5', 1, 6.3, extra='') + P.curve(lambda x: 1.5 ** (x - 1), 'c2 fx d5', 1, 6.3))
    lines = lines.replace('class="c1 fx d5"', 'class="c1 fx d5 thin"').replace('class="c2 fx d5"', 'class="c2 fx d5 thin"')
    back = pts_ap + pts_gp + lines + P.text(1.1, 7.6, 'AP: d = 1.2  (straight line)', 't1 fx d2') + P.text(1.1, 6.9, 'GP: r = 1.5  (curves upward)', 't2 fx d2')
    mcard(deck, 'Sequences as functions · AP vs GP', 'Plot the terms (n, aₙ) of an A.P. (a = 1, d = 1.2) and a G.P. (a = 1, r = 1.5). What shapes do they lie on?', base, back,
          '<p>A sequence is a function on the natural numbers. <b>A.P.</b>: aₙ = a + (n − 1)d is <b>linear</b> in n (constant <b>difference</b>): points on a straight line.</p>'
          '<p><b>G.P.</b>: aₙ = a·rⁿ⁻¹ is <b>exponential</b> in n (constant <b>ratio</b>): points on a curve that bends upward (for r &gt; 1).</p>',
          'AP is linear, GP is exponential', 'AP: a_n = a+(n−1)d is linear in n (constant difference); GP: a_n = a r^(n−1) is exponential in n (constant ratio)',
          css='.pp .thin{stroke-width:1.5;stroke-dasharray:4 3;opacity:.7}', vb='0 0 300 200', hint='Constant difference or constant ratio?')


def gauss_staircase(deck):
    n = 6
    cs = 28
    x0, y0 = 60, 20
    def cell(col, row, cls, fx=''):
        return f'<rect class="{cls} {fx}" x="{x0 + col * cs}" y="{y0 + row * cs}" width="{cs - 2}" height="{cs - 2}" rx="3"></rect>'
    blue = ''.join(cell(c, (n + 1) - 1 - i, 'f1') for c in range(n) for i in range(c + 1))
    red = ''.join(cell(c, i, 'f2', 'fx d3') for c in range(n) for i in range(n - c))
    base = blue
    labels = (f'<text class="t1" x="{x0 + 40}" y="{y0 + (n + 1) * cs - 10}" >1+2+…+{n}</text>')
    back = (red + f'<text class="lbl fx d4" x="{x0 - 8}" y="{y0 + (n + 1) * cs / 2 + 4}" text-anchor="end">{n + 1}</text>'
            f'<text class="lbl fx d4" x="{x0 + n * cs / 2}" y="{y0 + (n + 1) * cs + 16}" text-anchor="middle">{n}</text>')
    mcard(deck, 'Sum of the first n natural numbers · picture', 'Why is 1 + 2 + 3 + … + n = n(n + 1)/2? Use a staircase of squares (n = 6).', base, back +
          f'<text class="t3 fx d5" x="{x0 + n * cs / 2}" y="{y0 + (n + 1) * cs + 34}" text-anchor="middle">2 × (1+…+6) = 6 × 7 = 42 → sum = 21</text>',
          '<p>Two identical staircases (blue and a rotated red copy) fit into an <b>n × (n + 1) rectangle</b>: 2S = n(n + 1).</p>'
          '<p><b>S = n(n + 1)/2</b>. This is Gauss’s pairing trick: (1 + n) + (2 + n − 1) + … has n/2 pairs each summing to n + 1.</p>',
          'Sum of first n natural numbers via a staircase', '1+2+…+n = n(n+1)/2: two staircases make an n×(n+1) rectangle, so 2S = n(n+1); e.g. n=6 gives 21',
          vb='0 0 300 246', hint='What shape do two copies make?')


def am_gm_semicircle(deck):
    cx, cy, R = 150, 150, 120
    a_len, b_len = 48, 192           # a = 1, b = 4 at 48 px per unit -> diameter 240 = 5 units
    xs = cx - R + a_len
    h = math.sqrt(R * R - (xs - cx) ** 2)
    base = (f'<path class="c0" d="M {cx - R} {cy} A {R} {R} 0 0 1 {cx + R} {cy} Z" fill="none"></path>'
            f'<text class="t1" x="{cx - R + a_len / 2}" y="{cy + 18}" text-anchor="middle">a = 1</text><text class="t1" x="{xs + b_len / 2}" y="{cy + 18}" text-anchor="middle">b = 4</text>'
            f'<line class="c1" x1="{xs}" y1="{cy}" x2="{xs}" y2="{cy - h:.1f}"></line>')
    back = (f'<line class="c2 fx d2" x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - R}"></line>'
            + f'<text class="t2 fx d3" x="{cx + 8}" y="{cy - R / 2}">AM = 2.5</text>'
            f'<text class="t1 fx d2" x="{xs + 6}" y="{cy - h / 2:.1f}">GM = 2</text>'
            f'<line class="guide fx d4" x1="{xs}" y1="{cy - h:.1f}" x2="{cx}" y2="{cy - h:.1f}"></line>')
    mcard(deck, 'AM ≥ GM · geometric proof', 'Take a semicircle on diameter a + b (a = 1, b = 4). Show where AM and GM appear, and why AM ≥ GM.', base, back,
          '<p>Radius = (a + b)/2 = <b>AM</b>. The perpendicular at the join point has height √(ab) = <b>GM</b> (geometric mean theorem).</p>'
          '<p>A chord’s perpendicular can never exceed the radius: <b>GM ≤ AM</b>, with equality only when a = b (the join is the centre).</p>',
          'AM ≥ GM from a semicircle', 'On a semicircle of diameter a+b, the radius is AM=(a+b)/2 and the perpendicular at the join is GM=√(ab), never longer than the radius, so AM ≥ GM with equality iff a=b',
          vb='0 0 300 190', hint='Which segment is the radius, which is the height?')


# ================================================================ Maths 11 Ch 9 Straight lines
def slope_sweep(deck):
    P, h = eqplane(-3.4, 3.4, -2.6, 2.6, pad=(10, 6, 10, 6))
    ox, oy = P.X(0), P.Y(0)
    s = P.X(1) - ox
    L = 2.9 * s
    base = P.axes(labels=False)
    marks = ''
    for ang, txt, dx, dy, anc in [(0, 'm = 0', 8, -6, 'start'), (45, 'm = 1', 6, -6, 'start'), (90, 'm undefined', 8, 4, 'start'), (135, 'm = −1', -6, -6, 'end')]:
        a = math.radians(ang)
        x2, y2 = ox + L * math.cos(a), oy - L * math.sin(a)
        marks += (f'<line class="guide" x1="{ox:.1f}" y1="{oy:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"></line>'
                  f'<text class="t2" x="{x2 + dx:.1f}" y="{y2 + dy:.1f}" text-anchor="{anc}">{txt}</text>')
    css = (f'.pp .sweep{{transform-box:view-box;transform-origin:{ox:.1f}px {oy:.1f}px;animation:swp2 7s linear infinite}}'
           '@keyframes swp2{from{transform:rotate(0deg)}to{transform:rotate(-180deg)}}')
    line = f'<line class="c1 sweep" x1="{ox - L:.1f}" y1="{oy:.1f}" x2="{ox + L:.1f}" y2="{oy:.1f}"></line>'
    mcard(deck, 'Slope · inclination', 'A line turns anticlockwise from 0° to 180°. How does its slope m = tan θ change?', base, line + marks,
          '<p>θ = 0°: m = 0. Rising to 45°: m = 1. At <b>90°</b> the line is vertical: <b>slope undefined</b>. Past 90° the slope jumps to −∞ and rises through −1 (135°) back to 0.</p>'
          '<p>So: acute angle → positive slope; obtuse angle → negative slope. Slope of the x-axis is 0; of the y-axis undefined.</p>',
          'Slope as tan of the inclination', 'm = tan θ for inclination 0 ≤ θ < 180°, θ ≠ 90°: 0 at 0°, 1 at 45°, undefined at 90°, −1 at 135°; positive for acute, negative for obtuse',
          css=css, vb=f'0 0 300 {h}', hint='Picture tan θ as θ sweeps from 0° to 180°.')


def two_answers_angle(deck):
    P, h = eqplane(-3.2, 3.2, -2.4, 2.4, pad=(10, 6, 10, 6))
    ox, oy = P.X(0), P.Y(0)
    s = P.X(1) - ox
    def ray(m, cls, extra='', L=3.0):
        a = math.atan(m)
        return (f'<line class="{cls} {extra}" x1="{ox - L * s * math.cos(a):.1f}" y1="{oy + L * s * math.sin(a):.1f}" '
                f'x2="{ox + L * s * math.cos(a):.1f}" y2="{oy - L * s * math.sin(a):.1f}"></line>')
    base = P.axes(labels=False) + ray(0.5, 'c1', L=2.6) + '<text class="t1" x="240" y="72">m₁ = ½</text>'
    back = (ray(3, 'c2', 'fx d2', L=0.8) + ray(-1 / 3, 'c3', 'fx d3', L=2.6) +
            '<text class="t2 fx d2" x="176" y="30">m = 3</text><text class="t3 fx d3" x="34" y="66">m = −⅓</text>')
    mcard(deck, 'Angle between lines · two answers', 'One line has slope ½. Another makes an angle of 45° with it. Find the other slope.', base, back,
          '<p>tan 45° = |(m − ½)/(1 + m/2)| = 1 ⇒ (m − ½) = ±(1 + m/2) ⇒ <b>m = 3</b> or <b>m = −⅓</b>.</p>'
          '<p>Two lines lie at 45° on either side of the given one. The acute angle formula <b>tan θ = |(m₁ − m₂)/(1 + m₁m₂)|</b> has a modulus, so it always gives two solutions when θ is known.</p>',
          'Example 2: two lines at 45° to a line of slope 1/2', 'tan θ = |(m1−m2)/(1+m1 m2)|; with m1=1/2 and θ=45° the other slope is 3 or −1/3 (one line on each side)',
          vb=f'0 0 300 {h}', hint='The modulus in the angle formula gives ± cases.')


def foot_and_image(deck):
    P, h = eqplane(-2, 4.2, -0.8, 3.6, pad=(16, 6, 12, 14))
    line = lambda x: (x + 4) / 3
    base = (P.axes(labels=False) + P.line(-2, line(-2), 4.2, line(4.2), 'c0') + P.dot(1, 2, 'd1s', 4.5) + P.text(1, 2, 'P(1, 2)', 't1', dx=-8, dy=-8, anchor='end') +
            P.text(3.4, line(3.4), 'x − 3y + 4 = 0', 'sm', dy=-22, dx=-12, anchor='end'))
    back = (P.line(1, 2, 1.2, 1.4, 'guide fx d2') + P.dot(1.1, 1.7, 'd3s', 4, 'fx d2') + P.text(1.1, 1.7, 'foot M', 't3 fx d2', dx=10, dy=6) +
            P.dot(1.2, 1.4, 'd2s', 4.5, 'fx d3') + P.text(1.2, 1.4, 'Q(6/5, 7/5)', 't2 fx d3', dx=8, dy=16))
    mcard(deck, 'Image in a line (mirror)', 'Find the image of P(1, 2) in the line x − 3y + 4 = 0.', base, back,
          '<p>The line is the <b>perpendicular bisector</b> of PQ. Two conditions: (i) PQ ⟂ line (slope of PQ = −3); (ii) the midpoint of PQ lies on the line.</p>'
          '<p>Shortcut: (x′ − x₁)/A = (y′ − y₁)/B = <b>−2(Ax₁ + By₁ + C)/(A² + B²)</b>. Here −2(−1)/10 = 0.2 → Q = (1 + 0.2, 2 − 0.6) = <b>(6/5, 7/5)</b>.</p>',
          'Reflection of a point in a line (Example 13)', 'Image Q of P(1,2) in x−3y+4=0: PQ ⟂ line and midpoint on line; formula (x′−x1)/A=(y′−y1)/B=−2(Ax1+By1+C)/(A²+B²); Q=(6/5,7/5)',
          vb=f'0 0 300 {h}', hint='Use “perpendicular” and “midpoint on the line”.')


def light_ray(deck):
    P, h = eqplane(-0.4, 6, -3.6, 3.8, pad=(14, 6, 10, 16))
    base = (P.axes(labels=False) + P.dot(1, 2, 'd1s', 4.5) + P.text(1, 2, '(1, 2)', 't1', dx=-6, dy=-8, anchor='end') + P.dot(5, 3, 'd1s', 4.5) + P.text(5, 3, '(5, 3)', 't1', dx=4, dy=-8, anchor='end'))
    back = (P.dot(5, -3, 'd2s', 4.5, 'fx d2') + P.text(5, -3, '(5, −3) image', 't2 fx d2', dx=-6, dy=16, anchor='end') + P.line(1, 2, 5, -3, 'guide fx d2') +
            P.line(1, 2, 2.6, 0, 'c3 fx d3') + P.line(2.6, 0, 5, 3, 'c3 fx d3') + P.dot(2.6, 0, 'd3s', 5, 'fx d3') + P.text(2.6, 0, 'A(13/5, 0)', 't3 fx d3', dx=-8, dy=18, anchor='end'))
    mcard(deck, 'Reflection of light · Misc Q21', 'A ray from (1, 2) reflects on the x-axis at A and passes through (5, 3). Find A.', base, back,
          '<p>Reflect (5, 3) in the x-axis to (5, −3). The reflected ray <b>appears to come from the image</b>, so A lies on the straight line from (1, 2) to (5, −3).</p>'
          '<p>Slope = −5/4: y − 2 = −(5/4)(x − 1); set y = 0: x = 1 + 8/5 = <b>13/5</b>. A = (13/5, 0).</p>',
          'Light reflection: use the image point', 'Reflect the target in the mirror line; the light path is the straight line to the image: A(13/5,0) for (1,2)→x-axis→(5,3)',
          vb=f'0 0 300 {h}', hint='Where would the ray go if the mirror were not there?')


def distance_to_line(deck):
    P, h = eqplane(-0.8, 4.4, -0.8, 3.4, pad=(16, 6, 12, 14))
    ln = lambda x: (10 - 3 * x) / 4
    base = (P.axes(labels=False) + P.line(-0.4, ln(-0.4), 4.2, ln(4.2), 'c0') + P.text(3.1, ln(3.1), '3x + 4y − 10 = 0', 'sm', dx=6, dy=-8) +
            P.dot(0, 0, 'd1s', 4.5) + P.text(0, 0, 'O', 't1', dx=-12, dy=14))
    back = (P.line(0, 0, 1.2, 1.6, 'c2 fx d2') + P.dot(1.2, 1.6, 'd2s', 4.5, 'fx d2') + P.text(0.6, 0.8, 'd', 't2 fx d2', dx=-12, dy=-2) +
            P.text(1.2, 1.6, 'foot (6/5, 8/5)', 'sm fx d2', dx=10, dy=-8))
    mcard(deck, 'Distance of a point from a line', 'Find the distance of the origin from 3x + 4y − 10 = 0 and the foot of the perpendicular.', base, back,
          '<p><b>d = |Ax₁ + By₁ + C| / √(A² + B²)</b> = |0 + 0 − 10|/5 = <b>2</b>.</p>'
          '<p>Foot: move from O along the normal (3, 4)/5 by 2 → (6/5, 8/5). Check: 3(6/5) + 4(8/5) = 10 ✓.</p>'
          '<p class="no">Trap: the absolute value, and √(A² + B²) not A² + B².</p>',
          'Distance from a point to a line', 'd = |Ax1+By1+C|/√(A²+B²); origin to 3x+4y−10=0 is 2 with foot (6/5, 8/5)',
          vb=f'0 0 300 {h}', hint='Which quantity goes in the numerator?')


# ================================================================ Maths 11 Ch 10 Conic sections
def cone_sections(deck):
    a = math.radians(28)          # generator angle with the axis
    def panel(ox, oy, lab, ang_deg, cut_dx, name, cls):
        """Cone side view (vertex at top), with a cutting-plane line whose angle with the axis is ang_deg."""
        H, V = 52, 0
        cx = ox + 60
        o = (f'<line class="c0" x1="{cx}" y1="{oy}" x2="{cx - H * math.tan(a):.1f}" y2="{oy + H}"></line><line class="c0" x1="{cx}" y1="{oy}" x2="{cx + H * math.tan(a):.1f}" y2="{oy + H}"></line>'
             f'<line class="c0" x1="{cx}" y1="{oy}" x2="{cx - H * math.tan(a):.1f}" y2="{oy - H}"></line><line class="c0" x1="{cx}" y1="{oy}" x2="{cx + H * math.tan(a):.1f}" y2="{oy - H}"></line>'
             f'<line class="ghost" x1="{cx}" y1="{oy - H - 6}" x2="{cx}" y2="{oy + H + 6}"></line>')
        # plane: line through point (cx + cut_dx, oy + 22) making angle ang with the axis (vertical)
        px, py = cx + cut_dx, oy + 24
        t = math.radians(ang_deg)
        dx, dy = math.sin(t) * 50, math.cos(t) * 50
        o += f'<line class="{cls}" x1="{px - dx:.1f}" y1="{py + dy:.1f}" x2="{px + dx:.1f}" y2="{py - dy:.1f}"></line>'
        return o
    front, back = '', ''
    specs = [(0, 0, 'a', 90, 0, 'Circle', 'c1'), (150, 0, 'b', 62, 0, 'Ellipse', 'c3'), (0, 160, 'c', 28, 6, 'Parabola', 'c4'), (150, 160, 'd', 10, 0, 'Hyperbola', 'c2')]
    for ox, oy, lab, ang, dx_, name, cls in specs:
        front += panel(ox, oy + 52, lab, ang, dx_, name, cls)
        col = {'c1': 't1', 'c3': 't3', 'c4': 't4', 'c2': 't2'}[cls]
        back += f'<text class="{col} fx d2" x="{ox + 60}" y="{oy + 132}" text-anchor="middle">{name}</text>'
    conds = ['β = 90°', 'α < β < 90°', 'β = α', 'β < α']
    for (ox, oy, *_r), c in zip(specs, conds):
        back += f'<text class="sm fx d3" x="{ox + 60}" y="{oy + 146}" text-anchor="middle">{c}</text>'
    mcard(deck, 'Conic sections · cone slices', 'A plane cuts a double cone. Name the curve in each of the four cases.', front, back,
          '<p>α = half-angle of the cone; β = angle the plane makes with the axis.</p>'
          '<p><b>β = 90°</b> → circle. <b>α &lt; β &lt; 90°</b> → ellipse. <b>β = α</b> (parallel to a generator) → parabola. <b>β &lt; α</b> (cuts both nappes) → hyperbola.</p>'
          '<p>Through the vertex you get degenerate cases: a point, a line, or a pair of lines.</p>',
          'Conic sections from a cone: circle, ellipse, parabola, hyperbola', 'Plane at β to the axis of a cone of half-angle α: β=90° circle; α<β<90° ellipse; β=α parabola; β<α hyperbola; through the vertex: point, line, two lines',
          vb='0 0 300 320', hint='Compare the tilt of the plane with the generator of the cone.')


def parabola_focus_directrix(deck):
    P, h = eqplane(-2.4, 6.2, -4.6, 4.6, pad=(12, 6, 10, 6))
    base = (P.axes(labels=False) + P.curve(lambda x: math.sqrt(4 * x) if x >= 0 else None, 'c1', 0, 5.8, clip=(-9, 9)) + P.curve(lambda x: -math.sqrt(4 * x) if x >= 0 else None, 'c1', 0, 5.8, clip=(-9, 9)) +
            P.dot(1, 0, 'd2s', 5) + P.text(1, 0, 'F(a, 0)', 't2', dx=6, dy=16) + P.line(-1, -4.5, -1, 4.5, 'c4') + P.text(-1, 4.2, 'x = −a', 't4', dx=-6, anchor='end'))
    back = ''
    for k, (px, py) in enumerate([(1, 2), (4, 4), (2.25, 3)]):
        py = math.sqrt(4 * px) if k != 2 else 3.0
        px = py * py / 4
        back += (P.line(px, py, -1, py, 'c4 fx d' + str(k + 2)) + P.line(px, py, 1, 0, 'c2 fx d' + str(k + 2)) + P.dot(px, py, 'd1s', 4.5, 'fx d' + str(k + 2)))
    mcard(deck, 'Parabola · focus and directrix', 'y² = 4ax with a = 1. For any point P on it compare PF (to the focus) with the perpendicular PD to the directrix.', base, back,
          '<p><b>PF = PD</b> for every point (red = orange in length). That is the definition.</p>'
          '<p>Derivation: √((x − a)² + y²) = x + a ⇒ <b>y² = 4ax</b>. The vertex is midway between focus and directrix; latus rectum <b>4a</b>.</p>',
          'Parabola: every point is equidistant from focus and directrix', 'Parabola y²=4ax: PF = PD for all P; focus (a,0), directrix x=−a, vertex origin, latus rectum 4a',
          vb=f'0 0 300 {h}', hint='Measure from P to F and from P to the line.')


def ellipse_string(deck):
    P, h = eqplane(-6.4, 6.4, -3.8, 3.8, pad=(8, 6, 8, 6))
    base = (P.axes(labels=False) + P.curve(lambda x: 3 * math.sqrt(max(0, 1 - x * x / 25)), 'c1', -5, 5, clip=(-9, 9), n=200) +
            P.curve(lambda x: -3 * math.sqrt(max(0, 1 - x * x / 25)), 'c1', -5, 5, clip=(-9, 9), n=200) +
            P.dot(-4, 0, 'd2s', 5) + P.dot(4, 0, 'd2s', 5) + P.text(-4, 0, 'F₁', 't2', dx=-6, dy=16, anchor='end') + P.text(4, 0, 'F₂', 't2', dx=6, dy=16))
    back = ''
    for k, (px, py, d1, d2) in enumerate([(0, 3, 5, 5), (3, 2.4, 7.4, 2.6), (-5, 0, 1, 9)]):
        back += (P.line(px, py, -4, 0, 'c3 fx d' + str(k + 2)) + P.line(px, py, 4, 0, 'c4 fx d' + str(k + 2)) + P.dot(px, py, 'd1s', 4.5, 'fx d' + str(k + 2)))
    lab = (P.text(0.2, 3, '5 + 5', 't3 fx d2', dx=6, dy=-8) + P.text(3, 2.4, '7.4 + 2.6', 't3 fx d3', dx=6, dy=-8) + P.text(-5, 0, '1 + 9', 't3 fx d4', dx=8, dy=-8))
    mcard(deck, 'Ellipse · sum of distances', 'x²/25 + y²/9 = 1 has foci (±4, 0). Check PF₁ + PF₂ at (0, 3), (3, 2.4) and (−5, 0).', base, back + lab,
          '<p>Every point gives the <b>same sum 10 = 2a</b>: a piece of string of length 2a pinned at the foci traces the ellipse.</p>'
          '<p>Relation: <b>c² = a² − b²</b>, here 16 = 25 − 9. Eccentricity e = c/a = 4/5 (&lt; 1). The sum must exceed the distance between the foci (2c = 8).</p>',
          'Ellipse: PF1 + PF2 = 2a', 'Ellipse x²/25+y²/9=1: foci (±4,0), PF1+PF2 = 10 = 2a at every point; c² = a² − b², e = c/a = 4/5',
          vb=f'0 0 300 {h}', hint='Add the two focal distances at three points.')


def hyperbola_difference(deck):
    P, h = eqplane(-8.6, 8.6, -6.4, 6.4, pad=(8, 6, 8, 6))
    f = lambda x: 4 * math.sqrt(max(0, x * x / 9 - 1))
    base = (P.axes(labels=False) + P.curve(f, 'c1', 3, 8.4, clip=(-9, 9), n=200) + P.curve(lambda x: -f(x), 'c1', 3, 8.4, clip=(-9, 9), n=200) +
            P.curve(f, 'c1', -8.4, -3, clip=(-9, 9), n=200) + P.curve(lambda x: -f(x), 'c1', -8.4, -3, clip=(-9, 9), n=200) +
            P.line(-8, -32 / 3, 8, 32 / 3, 'guide') + P.line(-8, 32 / 3, 8, -32 / 3, 'guide') +
            P.dot(-5, 0, 'd2s', 5) + P.dot(5, 0, 'd2s', 5) + P.text(5, 0, 'F₂', 't2', dx=6, dy=16) + P.text(-5, 0, 'F₁', 't2', dx=-6, dy=16, anchor='end'))
    back = ''
    for k, (px, py) in enumerate([(3, 0), (5, 16 / 3)]):
        back += (P.line(px, py, -5, 0, 'c3 fx d' + str(k + 2)) + P.line(px, py, 5, 0, 'c4 fx d' + str(k + 2)) + P.dot(px, py, 'd1s', 4.5, 'fx d' + str(k + 2)))
    back += P.text(5, 16 / 3, '11.33 − 5.33 = 6', 't3 fx d3', dx=-8, dy=-8, anchor='end') + P.text(3, 0, '8 − 2 = 6', 't3 fx d2', dx=8, dy=-8)
    mcard(deck, 'Hyperbola · difference of distances', 'x²/9 − y²/16 = 1 has foci (±5, 0). Find |PF₁ − PF₂| at (3, 0) and (5, 16/3).', base, back,
          '<p>The <b>difference is constant = 2a = 6</b> at every point (farther minus nearer).</p>'
          '<p>Relation: <b>c² = a² + b²</b> (25 = 9 + 16), e = c/a = 5/3 &gt; 1. The dashed lines y = ±(b/a)x are the asymptotes.</p>',
          'Hyperbola: |PF1 − PF2| = 2a', 'Hyperbola x²/9−y²/16=1: foci (±5,0), |PF1−PF2| = 6 = 2a; c² = a² + b²; e = 5/3; asymptotes y = ±(4/3)x',
          vb=f'0 0 300 {h}', hint='Farther distance minus nearer distance.')


def eccentricity_line(deck):
    X = lambda e: 16 + e * 64
    zones = ('<rect class="ns1" x="16" y="56" width="4" height="26"></rect>'
             f'<rect class="ns3 fx d2" x="20" y="56" width="{X(1) - 20:.1f}" height="26"></rect>'
             f'<rect class="ns2 fx d3" x="{X(1) + 3:.1f}" y="56" width="{X(4) - X(1) - 3:.1f}" height="26"></rect>')
    axis = ('<line class="ax" x1="10" y1="82" x2="290" y2="82" marker-end="url(#pk)"></line>'
            + ''.join(f'<line class="ax" x1="{X(e):.1f}" y1="78" x2="{X(e):.1f}" y2="86"></line><text class="num" x="{X(e):.1f}" y="100">{e}</text>' for e in (0, 1, 2, 3)))
    labs = ('<text class="t1 fx d1" x="16" y="46">e = 0 circle</text><text class="t3 fx d2" x="80" y="72">ellipse</text>'
            f'<text class="t4 fx d3" x="{X(1) - 6:.1f}" y="46" text-anchor="middle">e = 1 parabola</text><text class="t2 fx d3" x="{X(2):.1f}" y="72" text-anchor="middle">hyperbola  e &gt; 1</text>')
    mcard(deck, 'Eccentricity · the whole family', 'Place the circle, ellipse, parabola and hyperbola on an eccentricity scale.', axis, zones + labs,
          '<p><b>e = c/a</b> measures how stretched the curve is. <b>e = 0</b> circle (foci coincide). <b>0 &lt; e &lt; 1</b> ellipse. <b>e = 1</b> parabola. <b>e &gt; 1</b> hyperbola.</p>'
          '<p>Unified definition: distance to the focus = e × distance to the directrix.</p>',
          'Eccentricity: circle 0, ellipse <1, parabola 1, hyperbola >1', 'e=0 circle, 0<e<1 ellipse, e=1 parabola, e>1 hyperbola; PF = e·PD for a conic with focus and directrix',
          vb='0 0 300 120', hint='What is c/a for each curve?')


def abc_triangles(deck):
    def tri(ox, oy, p, q, r, labs, cls):
        s = 22
        x0, y0 = ox, oy
        return (f'<polygon class="{cls}" points="{x0},{y0} {x0 + q * s},{y0} {x0 + q * s},{y0 - p * s}"></polygon>'
                f'<text class="lbl" x="{x0 + q * s / 2}" y="{y0 + 14}" text-anchor="middle">{labs[1]}</text>'
                f'<text class="lbl" x="{x0 + q * s + 6}" y="{y0 - p * s / 2}">{labs[0]}</text>'
                f'<text class="t2" x="{x0 + q * s / 2 - 14}" y="{y0 - p * s / 2 - 6}" text-anchor="middle">{labs[2]}</text>')
    base = ('<text class="sm" x="80" y="30" text-anchor="middle">Ellipse</text><text class="sm" x="225" y="30" text-anchor="middle">Hyperbola</text>')
    back = (tri(30, 130, 3, 4, 5, ('b = 3', 'c = 4', 'a = 5'), 'f3 fx d2') + tri(170, 130, 4, 3, 5, ('b = 4', 'a = 3', 'c = 5'), 'f2 fx d3') +
            '<text class="t3 fx d2" x="80" y="168" text-anchor="middle">a² = b² + c²</text><text class="t2 fx d3" x="225" y="168" text-anchor="middle">c² = a² + b²</text>')
    mcard(deck, 'Conics · which is the hypotenuse?', 'Ellipse: a² = b² + c². Hyperbola: c² = a² + b². Draw a right triangle for each with the numbers 3, 4, 5.', base, back,
          '<p>Ellipse: the <b>semi-major axis a</b> is the hypotenuse (a is the largest): 5² = 3² + 4², e = c/a = 4/5.</p>'
          '<p>Hyperbola: the <b>focal distance c</b> is the hypotenuse (c is the largest): 5² = 3² + 4², e = c/a = 5/3.</p>'
          '<p>Memory: in both, the biggest of a, c is the hypotenuse, and b is the leftover leg.</p>',
          'a, b, c triangles for ellipse and hyperbola', 'Ellipse a²=b²+c² (a hypotenuse, e=c/a<1); hyperbola c²=a²+b² (c hypotenuse, e=c/a>1)',
          vb='0 0 300 180', hint='Which of a, c is the largest in each conic?')


def parabola_reflector(deck):
    P, h = eqplane(-0.4, 6.2, -3.8, 3.8, pad=(10, 6, 10, 6))
    base = (P.axes(labels=False) + P.curve(lambda x: 2 * math.sqrt(x) if x >= 0 else None, 'c1', 0, 3.4, clip=(-9, 9), n=160) +
            P.curve(lambda x: -2 * math.sqrt(x) if x >= 0 else None, 'c1', 0, 3.4, clip=(-9, 9), n=160) + P.dot(1, 0, 'd2s', 5) + P.text(1, 0, 'F', 't2', dx=6, dy=16))
    back = ''
    for k, y in enumerate([2.6, 1.6, 0.8, -0.8, -1.6, -2.6]):
        x = y * y / 4
        dl = 'fx d' + str(2 + k % 3)
        back += P.line(6, y, x, y, 'c4 ' + dl) + P.line(x, y, 1, 0, 'c2 ' + dl) + P.dot(x, y, 'd1s', 3.5, dl)
    mcard(deck, 'Parabola · reflecting property', 'Rays parallel to the axis hit the parabola y² = 4x. Where do they go after reflecting?', base, back,
          '<p>All reflect through the <b>focus</b>. Reversed, a source at the focus sends a parallel beam: headlights and torches. Incoming parallel signals concentrate at the focus: satellite dishes, telescopes, solar cookers.</p>'
          '<p>Example 17: focus 5 cm from the vertex, mirror 45 cm deep: y² = 20x, at x = 45, y = ±30, so AB = <b>60 cm</b>.</p>',
          'Reflecting property of the parabola', 'Rays parallel to the axis of a parabola reflect through the focus; used in headlights, dishes, telescopes; y²=20x at depth 45 gives width 60',
          vb=f'0 0 300 {h}', hint='Where would all the rays meet?')


def ladder_ellipse(deck):
    P, h = eqplane(-1, 16, -1, 15.5, pad=(8, 6, 8, 8))
    base = (P.axes(labels=False) + P.line(15, 0, 0, 0, 'c0'))
    curve = ''.join(P.line(9 * math.cos(math.radians(t)), 6 * math.sin(math.radians(t)), 9 * math.cos(math.radians(t + 3)), 6 * math.sin(math.radians(t + 3)), 'c1') for t in range(0, 360, 3))
    quarter = ''.join(P.line(9 * math.cos(math.radians(t)), 6 * math.sin(math.radians(t)), 9 * math.cos(math.radians(t + 3)), 6 * math.sin(math.radians(t + 3)), 'c1') for t in range(0, 90, 3))
    back = quarter
    for k, th in enumerate([25, 45, 70]):
        t = math.radians(th)
        A = (15 * math.cos(t) - 0, 0)
        A = (15 * math.cos(t), 0)
        B = (0, 15 * math.sin(t))
        Px, Py = 9 * math.cos(t), 6 * math.sin(t)
        # rod from A(x-axis) to B(y-axis); P is 6 from A: A + 6*(B-A)/15
        Px, Py = A[0] + 6 * (B[0] - A[0]) / 15, 6 * B[1] / 15
        back += P.line(A[0], 0, 0, B[1], 'c3 fx d' + str(k + 2)) + P.dot(Px, Py, 'd2s', 4, 'fx d' + str(k + 2))
    mcard(deck, 'Locus · sliding rod (Example 19)', 'A rod AB of length 15 slides with A on the x-axis and B on the y-axis. P is on it with AP = 6. Find the path of P.', '', back + P.axes(labels=False),
          '<p>If AB makes angle θ with OX: <b>x = PB cos θ = 9cos θ</b> and <b>y = AP sin θ = 6 sin θ</b>. Eliminating θ: <b>x²/81 + y²/36 = 1</b>, an ellipse.</p>'
          '<p>Only when P is the midpoint (AP = PB) does it become a circle. Each end of the rod traces a line; an interior point traces an ellipse.</p>',
          'Sliding ladder: an interior point traces an ellipse', 'Rod of length 15 with AP=6, PB=9 sliding on the axes: P=(9cosθ, 6sinθ), so x²/81 + y²/36 = 1, an ellipse',
          vb=f'0 0 300 {h}', hint='Express x and y using the angle the rod makes with the axis.')


# ================================================================ Maths 11 Ch 11 Three-dimensional geometry
class Axes3D:
    """Oblique projection: y to the right, z up, x towards the viewer (down-left)."""
    def __init__(s, ox=110, oy=170, u=30, kx=0.55):
        s.ox, s.oy, s.u, s.kx = ox, oy, u, kx

    def pt(s, x, y, z):
        return (s.ox + s.u * (y - s.kx * x), s.oy - s.u * (z - s.kx * x * 0.75))

    def line(s, a, b, cls='c0', extra=''):
        (x1, y1), (x2, y2) = s.pt(*a), s.pt(*b)
        return f'<line class="{cls} {extra}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"></line>'

    def dot(s, p, cls='d1s', r=4.5, extra=''):
        x, y = s.pt(*p)
        return f'<circle class="{cls} {extra}" cx="{x:.1f}" cy="{y:.1f}" r="{r}"></circle>'

    def text(s, p, t, cls='lbl', dx=0, dy=0, anchor='start', extra=''):
        x, y = s.pt(*p)
        return f'<text class="{cls} {extra}" x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}">{t}</text>'

    def axes(s, lx=3.8, ly=6.4, lz=4.6):
        return (s.line((0, 0, 0), (lx, 0, 0), 'ax') + s.line((0, 0, 0), (0, ly, 0), 'ax') + s.line((0, 0, 0), (0, 0, lz), 'ax') +
                s.text((lx, 0, 0), 'x', 'lbi', dx=-12, dy=8) + s.text((0, ly, 0), 'y', 'lbi', dx=6, dy=4) + s.text((0, 0, lz), 'z', 'lbi', dx=6, dy=4) +
                s.text((0, 0, 0), 'O', 'lbl', dx=-10, dy=12))

    def box(s, p, cls='guide', extra=''):
        x, y, z = p
        edges = [((0, 0, 0), (x, 0, 0)), ((0, 0, 0), (0, y, 0)), ((0, 0, 0), (0, 0, z)), ((x, 0, 0), (x, y, 0)), ((x, 0, 0), (x, 0, z)),
                 ((0, y, 0), (x, y, 0)), ((0, y, 0), (0, y, z)), ((0, 0, z), (x, 0, z)), ((0, 0, z), (0, y, z)), ((x, y, 0), (x, y, z)), ((x, 0, z), (x, y, z)), ((0, y, z), (x, y, z))]
        return ''.join(s.line(a, b, cls, extra) for a, b in edges)


def point_in_space(deck):
    A = Axes3D()
    P = (3, 4, 2)
    base = A.axes() + A.dot(P, 'd1s', 5) + A.text(P, 'P(3, 4, 2)', 't1', dx=8, dy=-6)
    back = (A.box(P, 'guide fx d2') + A.dot((3, 0, 0), 'd3s', 4, 'fx d2') + A.text((3, 0, 0), 'A(3,0,0)', 'sm fx d2', dx=-8, dy=4, anchor='end') +
            A.dot((3, 4, 0), 'd2s', 4, 'fx d3') + A.text((3, 4, 0), 'M(3,4,0)', 'sm fx d3', dx=6, dy=14) +
            A.line((3, 4, 0), P, 'c2 fx d3') + A.text((3, 4, 1), 'z = 2', 't2 fx d3', dx=8, dy=20) + A.text((1.5, 0, 0), 'x = 3', 't3 fx d2', dx=-8, dy=14, anchor='end') +
            A.text((0, 2, 0), 'y = 4', 't4 fx d2', dy=14, dx=8))
    mcard(deck, 'Coordinates in space', 'Locate P(3, 4, 2). Which foot points does the box create, and what are the octant and distances from the planes?', base, back,
          '<p>Go 3 along the x-axis, 4 parallel to the y-axis (reaching M in the XY-plane), then 2 up: P(3, 4, 2) in octant <b>I</b>.</p>'
          '<p>Distances: from the <b>YZ-plane = |x| = 3</b>, ZX-plane = |y| = 4, XY-plane = |z| = 2. Foot on the XY-plane is (3, 4, 0); on the x-axis (3, 0, 0).</p>',
          'Locating a point in 3-D: the coordinate box', 'P(x,y,z): x,y,z are distances from YZ, ZX, XY planes; drop a perpendicular to XY-plane at M(x,y,0) then go z up; P(3,4,2) lies in octant I',
          vb='0 0 300 240', hint='Build the box from the origin.')


def space_diagonal(deck):
    A = Axes3D(ox=90, oy=178, u=26)
    P = (2, 3, 6)
    base = A.axes(lx=2.6, ly=5.4, lz=6.8) + A.dot(P, 'd1s', 5) + A.text(P, 'Q(2, 3, 6)', 't1', dx=8, dy=-4)
    back = (A.box(P, 'guide fx d2') + A.line((0, 0, 0), (2, 3, 0), 'c3 fx d2') + A.text((1, 1.5, 0), '√13', 't3 fx d2', dx=6, dy=16) +
            A.line((0, 0, 0), P, 'c2 fx d3') + A.text((1, 1.5, 3), 'OQ = 7', 't2 fx d3', dx=-10, dy=-4, anchor='end'))
    mcard(deck, 'Distance formula in 3-D', 'Find the distance from the origin to Q(2, 3, 6). Explain with a box.', base, back,
          '<p>Floor diagonal: √(2² + 3²) = √13. Then the vertical side 6: OQ² = (√13)² + 6² = 13 + 36 = 49 ⇒ <b>OQ = 7</b>.</p>'
          '<p>Two Pythagoras steps give <b>PQ = √((x₂ − x₁)² + (y₂ − y₁)² + (z₂ − z₁)²)</b>, the space diagonal of the cuboid on PQ.</p>',
          'Distance in space as a cuboid diagonal', 'PQ = √((x2−x1)²+(y2−y1)²+(z2−z1)²): floor diagonal then Pythagoras again; origin to (2,3,6) is 7',
          vb='0 0 300 230', hint='Do Pythagoras twice.')


# ================================================================ Maths 11 Ch 12 Limits and derivatives
def secant_to_tangent(deck):
    P = Plane(0, 3.3, -3, 47, 300, 210, (30, 10, 12, 22))
    xt = [(1, '1'), (2, '2'), (3, '3')]
    yt = [(10, '10'), (20, '20'), (30, '30'), (40, '40')]
    s = lambda t: 4.9 * t * t
    base = (P.axes(xt, yt, grid=True, xl='t (s)', yl='s (m)') + P.curve(s, 'c1', 0, 3.2, clip=(-3, 47)) + P.dot(2, 19.6, 'd0s', 5) + P.text(2, 19.6, 'A (t = 2)', 'lbl', dx=8, dy=16))
    def sec(h, cls, fx):
        m = 19.6 + 4.9 * h
        return P.curve(lambda t: 19.6 + m * (t - 2), f'{cls} {fx}', 1.0, 3.2, clip=(-3, 47))
    back = (sec(1, 'c4', 'fx d1') + P.dot(3, s(3), 'd4s', 4, 'fx d1') + sec(0.5, 'c4', 'fx d2') + P.dot(2.5, s(2.5), 'd4s', 4, 'fx d2') +
            sec(0.1, 'c4', 'fx d3') + P.curve(lambda t: 19.6 + 19.6 * (t - 2), 'c2 fx d4', 1.0, 3.2, clip=(-3, 47)) +
            P.text(0.15, 42, 'secant slopes 24.5, 22.05, 20.09 …', 't4 fx d3') + P.text(0.15, 36, 'tangent slope 19.6 m/s', 't2 fx d4'))
    mcard(deck, 'Derivative · from secants to the tangent', 'A body falls s = 4.9t² metres. Find its velocity at t = 2 s from average velocities over shrinking intervals.', base, back,
          '<p>Average velocity over [2, 2 + h] = (s(2 + h) − s(2))/h = <b>19.6 + 4.9h</b>: 24.5, 22.05, 20.09 … as h → 0 it tends to <b>19.6 m/s</b>.</p>'
          '<p>Geometrically the <b>secant</b> slopes tend to the <b>tangent</b> slope. The derivative s′(2) = lim (s(2 + h) − s(2))/h = 19.6 = instantaneous velocity.</p>',
          'Instantaneous velocity as the limit of average velocities (secant to tangent)', 'Derivative = limit of secant slopes as h→0; for s=4.9t² at t=2 the average velocity 19.6+4.9h tends to 19.6 m/s = slope of the tangent',
          vb='0 0 300 210', hint='What happens to the average velocity as the interval shrinks?')


def hole_limit(deck):
    P = Plane(-1, 4.6, -1, 6.6, 300, 200, (26, 10, 12, 22))
    xt = [(1, '1'), (2, '2'), (3, '3'), (4, '4')]
    yt = [(2, '2'), (4, '4'), (6, '6')]
    base = P.axes(xt, yt, grid=True) + P.curve(lambda x: x + 2, 'c1', -0.6, 4.4) + P.hole(2, 4, 'c1', 5.5)
    back = (P.line(2, 0, 2, 4, 'guide fx d2') + P.line(0, 4, 2, 4, 'guide fx d2') + P.text(0.2, 4, 'limit = 4', 't2 fx d2', dy=-8) +
            P.text(2, 0, 'f(2) undefined', 'sm fx d2', dx=6, dy=-8))
    mcard(deck, 'Limits · removable hole', 'f(x) = (x² − 4)/(x − 2). Find the limit as x → 2 even though f(2) is undefined.', base, back,
          '<p>0/0 form: factorise. (x − 2)(x + 2)/(x − 2) = x + 2 for x ≠ 2, so <b>lim = 2 + 2 = 4</b>.</p>'
          '<p>The graph is the line y = x + 2 with a <b>hole at (2, 4)</b>. A limit describes where the curve is heading, not what happens at the point itself.</p>',
          'Limit at a hole: (x²−4)/(x−2) → 4', 'lim x→2 (x²−4)/(x−2) = 4 after cancelling the common factor; graph is y=x+2 with a hole at (2,4); limit ignores the value at the point',
          vb='0 0 300 200', hint='Factorise before substituting.')


def left_right_limits(deck):
    P = Plane(-3.4, 3.6, -0.6, 3.6, 300, 180, (24, 10, 12, 20))
    xt = [(-2, '−2'), (-1, '−1'), (1, '1'), (2, '2')]
    yt = [(1, '1'), (2, '2'), (3, '3')]
    base = (P.axes(xt, yt, grid=True) + P.line(-3.2, 1, 0, 1, 'c1') + P.dot(0, 1, 'd1s', 5) + P.line(0, 2, 3.4, 2, 'c1') + P.hole(0, 2, 'c1', 5))
    back = (P.text(-1.5, 1, 'left limit = 1', 't3 fx d2', 'middle', dy=-12) + P.text(1.8, 2, 'right limit = 2', 't2 fx d2', 'middle', dy=-12) +
            P.text(0, 3.2, 'no limit', 't2 fx d3', 'middle'))
    mcard(deck, 'One-sided limits', 'f(x) = 1 for x ≤ 0 and f(x) = 2 for x > 0. What are the left and right limits at 0? Does the limit exist?', base, back,
          '<p>Left-hand limit (x → 0⁻) = <b>1</b>; right-hand limit (x → 0⁺) = <b>2</b>. They differ, so <b>lim x→0 f(x) does not exist</b>, even though f(0) = 1 is defined.</p>'
          '<p>Rule: <b>the limit exists ⟺ left limit = right limit</b> (both finite).</p>',
          'Left and right limits differ: the no limit', 'lim exists iff left and right limits are equal; step function 1 (x≤0), 2 (x>0) has LHL 1, RHL 2 at 0, so no limit though f(0)=1',
          vb='0 0 300 180', hint='Approach 0 from each side separately.')


def sandwich_circle(deck):
    P, h = eqplane(-0.35, 1.55, -0.3, 1.9, pad=(10, 6, 10, 8))
    x = 0.9
    cx, cy = math.cos(x), math.sin(x)
    ox, oy = P.X(0), P.Y(0)
    r = P.X(1) - ox
    base = (P.axes(labels=False) + f'<path class="c0" d="M {P.X(1):.1f} {P.Y(0):.1f} A {r:.1f} {r:.1f} 0 0 0 {P.X(0):.1f} {P.Y(1):.1f}" fill="none"></path>' +
            P.line(0, 0, cx, cy, 'c0') + P.line(0, 0, 1, math.tan(x), 'c0') + P.dot(cx, cy, 'd0s', 3.5) + P.text(cx, cy, 'C', 'lbl', dx=-12, dy=-4) + P.text(1, 0, 'A', 'lbl', dx=4, dy=14) +
            P.text(1, math.tan(x), 'B', 'lbl', dx=6, dy=4) + P.text(0, 0, 'O', 'lbl', dx=-10, dy=14))
    arc_pts = ' '.join(f'{P.X(math.cos(t)):.1f},{P.Y(math.sin(t)):.1f}' for t in [x * i / 30 for i in range(31)])
    back = (P.line(cx, 0, cx, cy, 'c2 fx d2') + P.text(cx, cy / 2, 'sin x', 't2 fx d2', dx=6) +
            f'<polyline class="c3 fx d3" points="{arc_pts}"></polyline>' + P.text(1.03, 0.4, 'x', 't3 fx d3', dx=10, dy=-14) +
            P.line(1, 0, 1, math.tan(x), 'c1 fx d4') + P.text(1, math.tan(x) / 2, 'tan x', 't1 fx d4', dx=8))
    mcard(deck, 'sin x / x · sandwich', 'In the unit circle compare CD = sin x, arc AC = x and AB = tan x. What follows for lim sin x / x?', base, back,
          '<p>Area △OAC &lt; sector OAC &lt; △OAB ⇒ <b>sin x &lt; x &lt; tan x</b> (0 &lt; x &lt; π/2). Divide by sin x and invert: <b>cos x &lt; sin x / x &lt; 1</b>.</p>'
          '<p>As x → 0, cos x → 1, so by the <b>sandwich theorem lim sin x / x = 1</b> (x in radians!). Then lim (1 − cos x)/x = 0 and lim tan x / x = 1.</p>',
          'Sandwich proof of lim sin x / x = 1', 'sin x < x < tan x gives cos x < sin x/x < 1; by the sandwich theorem lim x→0 sin x/x = 1 (radians); also lim tan x/x = 1 and lim (1−cos x)/x = 0',
          vb=f'0 0 300 {h}', hint='Compare two triangles and a sector.')


def sinc_graph(deck):
    P = Plane(-9.6, 9.6, -0.5, 1.25, 300, 170, (20, 10, 10, 22))
    xt = [(-6.283, '−2π'), (-3.1416, '−π'), (3.1416, 'π'), (6.283, '2π')]
    yt = [(1, '1'), (0.5, '½')]
    base = P.axes(xt, yt, grid=True) + P.curve(lambda x: math.sin(x) / x if abs(x) > 1e-9 else None, 'c1', -9.4, 9.4, n=300, clip=(-1, 2))
    back = P.hole(0, 1, 'c1', 5) + P.text(0, 1, 'limit 1, f(0) undefined', 't2 fx d2', dx=10, dy=-10) + P.text(-9.4, 0.4, 'squeezed by ±1/|x|', 'sm fx d3', dx=2)
    mcard(deck, 'Graph of sin x / x', 'Sketch y = sin x / x. What happens at x = 0 and as |x| grows?', base, back,
          '<p>At x = 0 the function is undefined (0/0) but the curve <b>heads to 1</b>: a removable hole at (0, 1). Because |sin x| ≤ 1, the oscillations are squeezed between ±1/|x| and die out.</p>',
          'Graph of sin x / x', 'sin x/x has a removable discontinuity at 0 with limit 1, is even, and decays to 0 as |x| grows (squeezed between ±1/|x|)',
          vb='0 0 300 170', hint='Numerator oscillates; denominator grows.')


def parabola_tangents(deck):
    P = Plane(-2.6, 3.4, -1.5, 9.6, 300, 200, (24, 10, 12, 20))
    xt = [(-2, '−2'), (-1, '−1'), (1, '1'), (2, '2'), (3, '3')]
    yt = [(2, '2'), (4, '4'), (6, '6'), (8, '8')]
    base = P.axes(xt, yt, grid=True) + P.curve(lambda x: x * x, 'c1', -2.4, 3.1, clip=(-1.5, 9.6))
    back = ''
    for k, a in enumerate([-1, 0, 1, 2]):
        m = 2 * a
        back += (P.curve(lambda x, a=a, m=m: a * a + m * (x - a), 'c2 fx d' + str(k + 2), a - 1.1, a + 1.1, clip=(-1.5, 9.6)) + P.dot(a, a * a, 'd2s', 4, 'fx d' + str(k + 2)) +
                 P.text(a, a * a, f'm = {m}'.replace('-', '−'), 't2 fx d' + str(k + 2), 'middle', dy=-10 if a != 0 else 18))
    mcard(deck, 'Derivative as slope of the tangent', 'Draw tangents to y = x² at x = −1, 0, 1, 2. Read off their slopes and guess f′(x).', base, back,
          '<p>Slopes −2, 0, 2, 4 = <b>2x</b>. So d(x²)/dx = 2x: the derivative is a <b>new function giving the slope at every point</b>.</p>'
          '<p>First principle: f′(x) = lim (f(x + h) − f(x))/h = lim ((x + h)² − x²)/h = lim (2x + h) = 2x.</p>',
          'f′(x) is the slope of the tangent: (x²)′ = 2x', 'Tangents to y=x² at x=−1,0,1,2 have slopes −2,0,2,4 = 2x; f′(x)=lim (f(x+h)−f(x))/h; (x²)′=2x',
          vb='0 0 300 200', hint='Estimate the slope at each marked point.')


# ================================================================ Maths 11 Ch 13 Statistics
def batsmen_dotplots(deck):
    A = [30, 91, 0, 64, 42, 80, 30, 5, 117, 71]
    B = [53, 46, 48, 50, 53, 53, 58, 60, 57, 52]
    X = lambda v: 20 + v * 2.3
    def row(y, data, cls, name):
        o = f'<line class="ax" x1="14" y1="{y}" x2="292" y2="{y}"></line>'
        o += ''.join(f'<line class="ax" x1="{X(v):.1f}" y1="{y - 3}" x2="{X(v):.1f}" y2="{y + 3}"></line><text class="num" x="{X(v):.1f}" y="{y + 15}">{v}</text>' for v in range(0, 121, 20))
        seen = {}
        for v in data:
            k = seen.get(v, 0)
            seen[v] = k + 1
            o += f'<circle class="{cls}" cx="{X(v):.1f}" cy="{y - 9 - 9 * k}" r="4"></circle>'
        return o + f'<text class="lbl" x="14" y="{y - 40}">{name}</text>'
    base = row(90, A, 'd1s', 'Batsman A') + row(190, B, 'd2s', 'Batsman B')
    back = (f'<line class="c3 fx d2" x1="{X(53):.1f}" y1="30" x2="{X(53):.1f}" y2="200"></line><text class="t3 fx d2" x="{X(53) + 4:.1f}" y="24">mean = median = 53</text>'
            f'<line class="c1 fx d3" x1="{X(0):.1f}" y1="112" x2="{X(117):.1f}" y2="112"></line><text class="t1 fx d3" x="{X(60):.1f}" y="127" text-anchor="middle">range 117, σ ≈ 36</text>'
            f'<line class="c2 fx d4" x1="{X(46):.1f}" y1="212" x2="{X(60):.1f}" y2="212"></line><text class="t2 fx d4" x="{X(53):.1f}" y="227" text-anchor="middle">range 14, σ ≈ 4.2</text>')
    mcard(deck, 'Why dispersion matters', 'Two batsmen both average 53 with median 53. Who is more consistent, and what number shows it?', base, back,
          '<p>Central tendency alone is not enough. B’s scores cluster (46–60); A’s are scattered (0–117).</p>'
          '<p>A single number for the spread is a <b>measure of dispersion</b>: range 117 vs 14; standard deviation ≈ 36.1 vs 4.2. Smaller = more consistent.</p>',
          'Same mean, different spread: range and standard deviation', 'Batsmen A and B both have mean=median=53, but range 117 vs 14 and SD about 36.1 vs 4.2, so B is more consistent',
          vb='0 0 300 240', hint='Compare how the dots are spread around 53.')


def shift_and_scale(deck):
    X = lambda v: 20 + v * 22
    data = [1, 2, 3]
    ticks = lambda y: ''.join(f'<line class="ax" x1="{X(v):.1f}" y1="{y - 3}" x2="{X(v):.1f}" y2="{y + 3}"></line><text class="num" x="{X(v):.1f}" y="{y + 14}">{v}</text>' for v in range(0, 13))
    base = (f'<line class="ax" x1="14" y1="70" x2="292" y2="70"></line>{ticks(70)}<line class="ax" x1="14" y1="170" x2="292" y2="170"></line>{ticks(170)}'
            '<text class="lbl" x="14" y="30">data 1, 2, 3   (x̄ = 2, σ² = 2/3)</text><text class="lbl" x="14" y="130">data 1, 2, 3   (x̄ = 2, σ² = 2/3)</text>')
    dots = lambda y, cls: ''.join(f'<circle class="{cls}" cx="{X(v):.1f}" cy="{y - 10}" r="5"></circle>' for v in data)
    css = (f'.pp .sh{{animation:shf 2.2s ease-in-out .6s both}}@keyframes shf{{from{{transform:translateX(0)}}to{{transform:translateX({4 * 22}px)}}}}'
           f'.pp .sc{{transform-origin:{X(0):.1f}px 0;animation:scl 2.2s ease-in-out .6s both}}@keyframes scl{{from{{transform:translateX(0)}}to{{transform:translateX(0)}}}}')
    # scaling about 0: each dot moves from X(v) to X(2v): translate by X(v)-X(0)... use per-dot classes
    css = (f'.pp .sh{{animation:shf 2.2s ease-in-out .6s both}}@keyframes shf{{from{{transform:translateX(0)}}to{{transform:translateX({4 * 22}px)}}}}'
           + ''.join(f'.pp .s{v}{{animation:sc{v} 2.2s ease-in-out .6s both}}@keyframes sc{v}{{from{{transform:translateX(0)}}to{{transform:translateX({v * 22}px)}}}}' for v in data))
    move1 = f'<g class="sh">{dots(70, "d1s")}</g>'
    move2 = ''.join(f'<g class="s{v}"><circle class="d2s" cx="{X(v):.1f}" cy="160" r="5"></circle></g>' for v in data)
    back = (move1 + move2 + '<text class="t3 fx d5" x="14" y="52">+4 →  x̄ = 6, σ² = 2/3 (unchanged)</text><text class="t2 fx d5" x="14" y="112">×2 →  x̄ = 4, σ² = 8/3 (×4)</text>')
    front = f'{dots(70, "d1s")}{dots(170, "d2s")}'.replace('cy="160"', 'cy="160"')
    mcard(deck, 'Change of origin and scale', 'Add 4 to every observation; separately multiply every observation by 2. What happens to the mean and the variance?', base + '', back,
          '<p><b>Shift (x + a):</b> mean + a, <b>variance unchanged</b> (spread unaffected). <b>Scale (kx):</b> mean × k, variance × <b>k²</b>, SD × |k|.</p>'
          '<p>Together: for y = ax + b, ȳ = a x̄ + b, σ_y = |a| σ_x. (Examples 13 and 15.)</p>',
          'Effect of shift and scale on mean and variance', 'y=x+a: mean shifts by a, variance unchanged; y=kx: mean×k, variance×k², SD×|k|; y=ax+b gives SD |a|σ',
          css=css, front_only=front.replace('<circle class="d2s" cx="42.0" cy="160"', '<circle class="d2s" cx="42.0" cy="160"'), vb='0 0 300 190', hint='Does the spread change when everything slides?')


def histogram_sd(deck):
    classes = [(30, 3), (40, 7), (50, 12), (60, 15), (70, 8), (80, 3), (90, 2)]
    X = lambda v: 20 + (v - 30) * 3.9
    base_y = 150
    bars = ''
    for k, (lo, f) in enumerate(classes):
        hgt = f * 7.5
        bars += f'<rect class="f1 grow gd{k}" x="{X(lo):.1f}" y="{base_y - hgt:.1f}" width="{10 * 3.9 - 2:.1f}" height="{hgt:.1f}"></rect><text class="num" x="{X(lo) + 19:.1f}" y="{base_y - hgt - 4:.1f}">{f}</text>'
    css = ('.pp .grow{transform-box:fill-box;transform-origin:50% 100%;animation:gr 1s ease-out both}@keyframes gr{from{transform:scaleY(0)}to{transform:scaleY(1)}}'
           + ''.join(f'.pp .gd{k}{{animation-delay:{0.2 + 0.1 * k:.1f}s}}' for k in range(7)))
    axis = (f'<line class="ax" x1="14" y1="{base_y}" x2="296" y2="{base_y}"></line>'
            + ''.join(f'<line class="ax" x1="{X(v):.1f}" y1="{base_y}" x2="{X(v):.1f}" y2="{base_y + 4}"></line><text class="num" x="{X(v):.1f}" y="{base_y + 16}">{v}</text>' for v in range(30, 101, 10)))
    back = (f'<rect class="ns3 fx d4" x="{X(62 - 14.18):.1f}" y="30" width="{28.36 * 3.9:.1f}" height="{base_y - 30}"></rect>'
            f'<line class="c2 fx d4" x1="{X(62):.1f}" y1="24" x2="{X(62):.1f}" y2="{base_y}"></line><text class="t2 fx d4" x="{X(62):.1f}" y="18" text-anchor="middle">x̄ = 62</text>'
            f'<text class="t3 fx d5" x="{X(62):.1f}" y="46" text-anchor="middle">x̄ ± σ  (47.8 to 76.2)</text>')
    mcard(deck, 'Example 10 · mean and standard deviation', 'Frequencies 3, 7, 12, 15, 8, 3, 2 on classes 30–40 … 90–100. Find the mean, variance and standard deviation.', axis + bars, back,
          '<p>Mid-points 35, 45, …, 95. Σfx = 3100, N = 50 → <b>x̄ = 62</b>. Σf(x − x̄)² = 10050 → <b>variance = 201</b>, <b>σ = √201 ≈ 14.18</b>.</p>'
          '<p>Most of the data lies within x̄ ± σ (the shaded band). σ has the same unit as the data; variance has the square of the unit.</p>',
          'Grouped data: mean 62, variance 201, SD 14.18', 'Classes 30-100 with f=3,7,12,15,8,3,2: mean 62, variance 201, SD ≈ 14.18',
          css=css, vb='0 0 300 172', hint='Use class mid-points and the frequencies.')


# ================================================================ Maths 11 Ch 14 Probability
def dice_grid(deck):
    x0, y0, s = 40, 22, 38
    def cell(a, b, cls):
        return f'<rect class="{cls}" x="{x0 + (b - 1) * s}" y="{y0 + (a - 1) * s}" width="{s - 3}" height="{s - 3}" rx="4"></rect>'
    base = ''.join(cell(a, b, 'f0') for a in range(1, 7) for b in range(1, 7))
    base += ''.join(f'<text class="num" x="{x0 + (b - 1) * s + 17}" y="{y0 - 6}">{b}</text><text class="num" x="{x0 - 10}" y="{y0 + (b - 1) * s + 20}">{b}</text>' for b in range(1, 7))
    base += '<text class="sm" x="150" y="6" text-anchor="middle">second die →</text>'
    back = ''
    for a in range(1, 7):
        for b in range(1, 7):
            if a + b == 7:
                back += cell(a, b, 'f4 fx d2') + f'<text class="lbl fx d2" x="{x0 + (b - 1) * s + 17}" y="{y0 + (a - 1) * s + 20}" text-anchor="middle">7</text>'
            elif a + b >= 10:
                back += cell(a, b, 'f2 fx d3')
    back += '<text class="t4 fx d2" x="150" y="270">sum = 7: 6/36 = 1/6</text><text class="t2 fx d3" x="150" y="286">sum ≥ 10: 6/36 = 1/6</text>'
    mcard(deck, 'Sample space of two dice', 'Two dice are rolled. How many equally likely outcomes are there? Shade the events “sum = 7” and “sum ≥ 10”.', base, back,
          '<p>36 ordered pairs (first die, second die), all equally likely: n(S) = 36.</p>'
          '<p>Sum 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) → <b>6/36 = 1/6</b> (the most likely sum). Sum ≥ 10: (4,6), (5,5), (5,6), (6,4), (6,5), (6,6) → <b>6/36 = 1/6</b>.</p>'
          '<p class="no">Trap: (1,6) and (6,1) are different outcomes.</p>',
          'Two-dice sample space of 36 outcomes', 'Two dice: 36 equally likely ordered pairs; P(sum 7) = 6/36 = 1/6, the most likely; P(sum ≥ 10) = 6/36; (1,6) and (6,1) are different',
          vb='0 0 300 296', hint='Order matters: the dice are distinguishable.')


def coin_tree(deck):
    lv = [(20, 108)]
    o = ''
    x = [20, 100, 180, 260]
    ys = {0: [108], 1: [66, 150], 2: [42, 90, 130, 170]}
    labels3 = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']
    y3 = [22, 52, 76, 104, 118, 146, 166, 194]
    y3 = [16 + i * 24.5 for i in range(8)]
    ys2 = [(y3[2 * i] + y3[2 * i + 1]) / 2 for i in range(4)]
    ys1 = [(ys2[0] + ys2[1]) / 2, (ys2[2] + ys2[3]) / 2]
    o = ''
    back = ''
    o += '<circle class="f1" cx="14" cy="108" r="6"></circle>'
    for i, y in enumerate(ys1):
        back += f'<line class="c0 fx d1" x1="18" y1="108" x2="84" y2="{y:.1f}"></line><text class="lbl fx d1" x="94" y="{y + 4:.1f}">{"HT"[i]}</text>'
        for j in range(2):
            y2 = ys2[2 * i + j]
            back += f'<line class="c0 fx d2" x1="100" y1="{y:.1f}" x2="160" y2="{y2:.1f}"></line><text class="lbl fx d2" x="170" y="{y2 + 4:.1f}">{"HT"[i]}{"HT"[j]}</text>'
            for k in range(2):
                idx = 4 * i + 2 * j + k
                back += (f'<line class="c1 fx d3" x1="192" y1="{y2:.1f}" x2="236" y2="{y3[idx]:.1f}"></line>'
                         f'<text class="lbl fx d3" x="242" y="{y3[idx] + 4:.1f}">{labels3[idx]}</text>')
    back += '<text class="t3 fx d5" x="14" y="16">8 leaves = 2 × 2 × 2</text>'
    mcard(deck, 'Three coins · tree of outcomes', 'Three coins are tossed. List the sample space with a tree and find P(exactly two heads) and P(at least two heads).', o, back,
          '<p>2 × 2 × 2 = <b>8</b> equally likely outcomes. Exactly two heads: HHT, HTH, THH → <b>3/8</b>. At least two heads: those three plus HHH → <b>4/8 = 1/2</b>.</p>',
          'Tree diagram for three coins', 'Three coins: 8 equally likely outcomes; P(exactly 2 heads)=3/8, P(at least 2 heads)=1/2, P(3 heads)=1/8',
          vb='0 0 300 212', hint='Branch H/T at each toss.')


def prob_venn(deck):
    front = ('<path class="f0" d="M10,10 H290 V190 H10 Z"></path><circle class="c0" cx="115" cy="100" r="58"></circle><circle class="c0" cx="185" cy="100" r="58"></circle>'
             '<text class="t1" x="84" y="66" text-anchor="middle">E</text><text class="t2" x="216" y="66" text-anchor="middle">F</text><text class="lbi" x="20" y="28">S</text>'
             '<text class="lbl" x="150" y="104" text-anchor="middle">0.02</text>')
    back = (f'<path class="ns1 fx d2" d="{_AMB}"></path><path class="ns2 fx d3" d="{_BMA}"></path><path class="ns3 fx d2" d="{_LENS}"></path>'
            f'<path class="ns4 fx d4" d="{_R + _UNION}" fill-rule="evenodd"></path>'
            '<text class="t1 fx d2" x="88" y="104" text-anchor="middle">0.03</text><text class="t2 fx d3" x="212" y="104" text-anchor="middle">0.08</text>'
            '<text class="t4 fx d4" x="250" y="176" text-anchor="middle">0.87</text>')
    mcard(deck, 'Example 7 · Venn probabilities', 'P(E) = 0.05, P(F) = 0.10, P(E ∩ F) = 0.02. Fill each region. Find P(neither), P(not both) and P(exactly one).', front, back,
          '<p>E only = 0.05 − 0.02 = <b>0.03</b>; F only = 0.10 − 0.02 = <b>0.08</b>. P(E ∪ F) = 0.13 → P(neither) = <b>0.87</b>.</p>'
          '<p>P(not both) = 1 − 0.02 = <b>0.98</b>. P(exactly one) = 0.03 + 0.08 = <b>0.11</b>. Regions of the Venn diagram add to 1.</p>',
          'Venn diagram probabilities for two events', 'P(E)=0.05, P(F)=0.10, P(E∩F)=0.02: E only 0.03, F only 0.08, neither 0.87, not both 0.98, exactly one 0.11',
          vb='0 0 300 200', hint='Subtract the overlap from each event.')


# ================================================================ Maths 11 Ch 3 Trigonometric functions (upgrade)
def unit_circle_values(deck):
    P, h = eqplane(-1.6, 1.6, -1.35, 1.35, pad=(8, 6, 8, 6))
    ox, oy = P.X(0), P.Y(0)
    r = P.X(1) - ox
    base = P.axes(labels=False) + f'<circle class="ghost" cx="{ox:.1f}" cy="{oy:.1f}" r="{r:.1f}"></circle>'
    css = (f'.pp .spin{{transform-box:view-box;transform-origin:{ox:.1f}px {oy:.1f}px;animation:sp 8s linear infinite}}@keyframes sp{{from{{transform:rotate(0)}}to{{transform:rotate(-360deg)}}}}')
    pts = [(0, '(1, 0)'), (30, '(√3/2, ½)'), (45, '(1/√2, 1/√2)'), (60, '(½, √3/2)'), (90, '(0, 1)')]
    back = ''
    for k, (a, lab) in enumerate(pts):
        t = math.radians(a)
        x, y = math.cos(t), math.sin(t)
        anc = 'start' if x > 0.2 else ('middle' if x <= 0.2 else 'start')
        back += P.dot(x, y, 'd2s', 4.5, 'fx d' + str(k + 1)) + P.text(x, y, lab, 't2 fx d' + str(k + 1), 'start' if a < 90 else 'middle', dx=8 if a < 90 else 0, dy=-8 if a not in (0,) else 14)
        if a: back += P.line(0, 0, x, y, 'guide fx d' + str(k + 1))
    back += f'<g class="spin"><line class="c1" x1="{ox:.1f}" y1="{oy:.1f}" x2="{ox + r:.1f}" y2="{oy:.1f}"></line><circle class="d1s" cx="{ox + r:.1f}" cy="{oy:.1f}" r="4.5"></circle></g>'
    mcard(deck, 'Unit circle · special angles', 'A point at angle θ on the unit circle is (cos θ, sin θ). Give the coordinates at 0°, 30°, 45°, 60°, 90°.', base, back,
          '<p>x-coordinate = <b>cos θ</b>, y-coordinate = <b>sin θ</b>. Values: 30° → (√3/2, ½); 45° → (1/√2, 1/√2); 60° → (½, √3/2).</p>'
          '<p>Memory: sin goes 0, ½, 1/√2, √3/2, 1 (write as √0/2, √1/2, √2/2, √3/2, √4/2); cos runs the same list backwards.</p>',
          'Unit circle coordinates at special angles', 'Point at angle θ on the unit circle is (cos θ, sin θ); 30°: (√3/2, 1/2); 45°: (1/√2, 1/√2); 60°: (1/2, √3/2); sin values √0/2 .. √4/2',
          css=css, vb=f'0 0 300 {h}', hint='Read cos as the x-coordinate and sin as the y-coordinate.')


def circle_to_wave(deck):
    cx, cy, R = 62, 100, 44
    X = lambda t: 130 + t * 27
    base = (f'<circle class="ghost" cx="{cx}" cy="{cy}" r="{R}"></circle><line class="ax" x1="{cx - 56}" y1="{cy}" x2="{cx + 56}" y2="{cy}"></line><line class="ax" x1="{cx}" y1="{cy - 56}" x2="{cx}" y2="{cy + 56}"></line>'
            f'<line class="ax" x1="126" y1="{cy}" x2="296" y2="{cy}"></line><line class="ax" x1="130" y1="{cy - 56}" x2="130" y2="{cy + 56}"></line>'
            + ''.join(f'<text class="num" x="{X(v):.1f}" y="{cy + 14}">{lab}</text>' for v, lab in [(math.pi / 2, 'π/2'), (math.pi, 'π'), (3 * math.pi / 2, '3π/2'), (2 * math.pi, '2π')][:0]))
    wave = ' '.join(f'{X(t):.1f},{cy - R * math.sin(t):.1f}' for t in [i * math.pi / 30 for i in range(0, 61)])
    back = f'<polyline class="c1 draw" pathLength="100" points="{wave}"></polyline>'
    for k, deg in enumerate([30, 90, 150, 210, 270, 330]):
        t = math.radians(deg)
        px, py = cx + R * math.cos(t), cy - R * math.sin(t)
        back += (f'<circle class="d2s fx d{min(k // 2 + 2, 6)}" cx="{px:.1f}" cy="{py:.1f}" r="3.5"></circle>'
                 f'<line class="guide fx d{min(k // 2 + 2, 6)}" x1="{px:.1f}" y1="{py:.1f}" x2="{X(t):.1f}" y2="{py:.1f}"></line>'
                 f'<circle class="d1s fx d{min(k // 2 + 2, 6)}" cx="{X(t):.1f}" cy="{py:.1f}" r="3.5"></circle>')
    back += (f'<text class="num" x="{X(math.pi):.1f}" y="{cy + 26}">π</text><text class="num" x="{X(2 * math.pi):.1f}" y="{cy + 26}">2π</text>')
    mcard(deck, 'Sine graph from the unit circle', 'How does the sine curve come from the unit circle? Follow the height of a point as θ goes from 0 to 2π.', base, back,
          '<p>The <b>height</b> of the point at angle θ is sin θ. Carry each height across to the matching θ on the horizontal axis and join the dots: the sine wave.</p>'
          '<p>One turn of the circle = one period <b>2π</b>; max 1 at π/2, min −1 at 3π/2; zeros at 0, π, 2π. Cosine is the same wave started a quarter-turn earlier.</p>',
          'The sine wave is the height of a point moving round the unit circle', 'sin θ is the height of the point at angle θ on the unit circle; plotting height against θ gives the sine wave with period 2π, range [−1,1]',
          vb='0 0 300 190', hint='Track only the vertical position.')


def trig_equation_circle(deck):
    P, h = eqplane(-1.6, 1.6, -1.35, 1.35, pad=(8, 6, 8, 6))
    ox, oy = P.X(0), P.Y(0)
    r = P.X(1) - ox
    base = P.axes(labels=False) + f'<circle class="ghost" cx="{ox:.1f}" cy="{oy:.1f}" r="{r:.1f}"></circle>' + P.line(-1.5, 0.5, 1.5, 0.5, 'c2')
    s3 = math.sqrt(3) / 2
    back = (P.dot(s3, 0.5, 'd1s', 5, 'fx d2') + P.dot(-s3, 0.5, 'd1s', 5, 'fx d3') + P.line(0, 0, s3, 0.5, 'guide fx d2') + P.line(0, 0, -s3, 0.5, 'guide fx d3') +
            P.text(s3, 0.5, '30°', 't1 fx d2', dx=8, dy=-8) + P.text(-s3, 0.5, '150°', 't1 fx d3', dx=-8, dy=-8, anchor='end'))
    mcard(deck, 'Solving sin x = ½', 'Solve sin x = ½ on the unit circle. What is the general solution?', base, back,
          '<p>sin x = y-coordinate = ½: the horizontal line y = ½ meets the circle at <b>30°</b> and <b>150°</b> (π − π/6).</p>'
          '<p>Adding full turns: x = 2nπ + π/6 or 2nπ + 5π/6, combined as <b>x = nπ + (−1)ⁿ π/6</b> (n ∈ Z).</p>',
          'General solution of sin x = 1/2 from the unit circle', 'sin x = 1/2 has solutions 30° and 150° in one turn; general solution x = nπ + (−1)^n π/6',
          vb=f'0 0 300 {h}', hint='Where is the y-coordinate equal to ½?')


# ================================================================ Maths 12 Ch 1 Relations and Functions
_DR = '.pp .dr{stroke:#c93b3f;stroke-width:2.2;stroke-dasharray:5 4;fill:none;stroke-linecap:round}'


def rst_digraph(deck):
    """Ex. 4 relation on {1,2,3} as a digraph: reflexive = a loop on every node."""
    pos = {1: (60, 150), 2: (150, 40), 3: (240, 150)}
    def loop(n, cls, extra=''):
        x, y = pos[n]
        dx = {1: -1, 2: 0, 3: 1}[n]
        dy = {1: 0.6, 2: -1, 3: 0.6}[n]
        cx, cy = x + dx * 26, y + dy * 26
        return f'<circle class="{cls} {extra}" cx="{cx:.1f}" cy="{cy:.1f}" r="13"></circle>'
    def arr(a, b, cls, mk, extra='', bend=0):
        (x0, y0), (x1, y1) = pos[a], pos[b]
        vx, vy = x1 - x0, y1 - y0
        L = math.hypot(vx, vy)
        ux, uy = vx / L, vy / L
        sx, sy, ex, ey = x0 + ux * 17, y0 + uy * 17, x1 - ux * 20, y1 - uy * 20
        if bend:
            mx, my = (sx + ex) / 2 - uy * bend, (sy + ey) / 2 + ux * bend
            return f'<path class="{cls} {extra}" d="M{sx:.1f},{sy:.1f} Q{mx:.1f},{my:.1f} {ex:.1f},{ey:.1f}" marker-end="url(#{mk})"></path>'
        return f'<line class="{cls} {extra}" x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" marker-end="url(#{mk})"></line>'
    nodes = ''.join(f'<circle class="f0" cx="{x}" cy="{y}" r="15"></circle><text class="lbl" x="{x}" y="{y + 4}" text-anchor="middle">{n}</text>' for n, (x, y) in pos.items())
    base = nodes + ''.join(loop(n, 'c1') for n in pos) + arr(1, 2, 'c1', 'pb', bend=0) + arr(2, 3, 'c1', 'pb')
    back = (arr(2, 1, 'dr', 'pr', 'fx d2', bend=-24) + arr(1, 3, 'dr', 'pr', 'fx d3', bend=16)
            + '<text class="t2 fx d2" x="52" y="78" text-anchor="middle">(2,1) missing</text>'
            + '<text class="t2 fx d3" x="150" y="182" text-anchor="middle">(1,3) missing</text>'
            + '<text class="t3 fx d1" x="240" y="34" text-anchor="middle">loops: reflexive ✓</text>')
    mcard(deck, 'Reading a relation as a graph', 'R = {(1,1), (2,2), (3,3), (1,2), (2,3)} on {1, 2, 3}. Is it reflexive, symmetric, transitive?', base, back,
          '<p><b>Reflexive ✓</b> every element has a loop. <b>Symmetric ✗</b>: 1 → 2 has no return arrow 2 → 1. <b>Transitive ✗</b>: 1 → 2 → 3 needs the shortcut 1 → 3.</p>'
          '<p>Test for each property: loops everywhere / every arrow returns / every two-step path has a shortcut.</p>',
          'Reflexive, symmetric, transitive read from a digraph',
          'Draw arrows a→b for (a,b) in R. Reflexive: a loop at every node. Symmetric: every arrow has a return arrow. Transitive: every two-step path a→b→c has the direct arrow a→c. Example 4: reflexive only',
          css=_DR, vb='0 0 300 200', hint='Look for loops, return arrows and shortcuts.')


def equiv_classes_mod3(deck):
    """R = {(a,b): 3 | a-b} on Z splits Z into three classes."""
    xs = list(range(-4, 8))
    X = lambda v: 24 + (v + 4) * 23.5
    row = {0: 84, 1: 124, 2: 164}
    fmt = lambda v: str(v).replace('-', '−')
    base = ''.join(f'<circle class="f0" cx="{X(v):.1f}" cy="30" r="9"></circle><text class="lbl" x="{X(v):.1f}" y="34" text-anchor="middle">{fmt(v)}</text>' for v in xs)
    back = ''
    for v in xs:
        k = v % 3
        back += (f'<circle class="f{k + 1} fx d{k + 1}" cx="{X(v):.1f}" cy="{row[k]}" r="9"></circle>'
                 f'<text class="lbl fx d{k + 1}" x="{X(v):.1f}" y="{row[k] + 4}" text-anchor="middle">{fmt(v)}</text>')
    for k, tcls in enumerate(['t1', 't2', 't3']):
        back += f'<text class="{tcls} fx d{k + 1}" x="8" y="{row[k] - 16}">[{k}] = {{3r + {k}}}</text>'
    back += '<text class="sm fx d4" x="150" y="192" text-anchor="middle">same remainder ⇒ same class</text>'
    mcard(deck, 'Equivalence classes', 'R = {(a, b) : 3 divides a − b} on Z is an equivalence relation. Sort the integers into its equivalence classes.', base, back,
          '<p>Three classes, by remainder on division by 3: <b>[0] = {…, −3, 0, 3, 6, …}</b>, <b>[1] = {…, −2, 1, 4, 7, …}</b>, <b>[2] = {…, −4, −1, 2, 5, …}</b>.</p>'
          '<p>Classes are <b>disjoint</b>, their <b>union is Z</b>, and everything inside one class is related. Every equivalence relation partitions its set.</p>',
          'Equivalence classes of congruence mod 3',
          'R = {(a,b): 3 | a−b} on Z is an equivalence relation with three classes [0], [1], [2] (remainders 0, 1, 2); they are disjoint and their union is Z',
          vb='0 0 300 200', hint='Group numbers with the same remainder mod 3.')


def _fn_panel(ox, oy, arrows, nl, nr, hit=None):
    ly = lambda i, n: 14 + i * (72 / max(n - 1, 1))
    o = f'<g transform="translate({ox},{oy})">'
    o += '<ellipse class="ghost" cx="22" cy="50" rx="16" ry="46"></ellipse><ellipse class="ghost" cx="98" cy="50" rx="16" ry="46"></ellipse>'
    for i in range(nl):
        o += f'<circle class="d0s" cx="22" cy="{ly(i, nl):.1f}" r="3.5"></circle><text class="sm" x="6" y="{ly(i, nl) + 4:.1f}" text-anchor="end">{i + 1}</text>'
    for j in range(nr):
        o += f'<circle class="d0s" cx="98" cy="{ly(j, nr):.1f}" r="3.5"></circle><text class="sm" x="114" y="{ly(j, nr) + 4:.1f}">{"abcd"[j]}</text>'
    for (i, j) in arrows:
        o += f'<line class="c0" x1="26" y1="{ly(i, nl):.1f}" x2="93" y2="{ly(j, nr):.1f}" marker-end="url(#pk)"></line>'
    return o + '</g>', ly


def inj_surj_panels(deck):
    specs = [
        (10, 6, [(0, 0), (1, 1), (2, 2)], 3, 4, 'One-one, not onto', 'd unused'),
        (160, 6, [(0, 0), (1, 0), (2, 1)], 3, 3, 'Many-one, not onto', 'a hit twice, c unused'),
        (10, 138, [(0, 0), (1, 0), (2, 1), (3, 2)], 4, 3, 'Onto, not one-one', 'a hit twice, all used'),
        (160, 138, [(0, 0), (1, 1), (2, 2)], 3, 3, 'One-one and onto', 'a bijection'),
    ]
    base = back = ''
    for k, (ox, oy, arr, nl, nr, name, why) in enumerate(specs):
        g, ly = _fn_panel(ox, oy, arr, nl, nr)
        base += g + f'<text class="lbi" x="{ox + 2}" y="{oy + 8}">({"abcd"[k]})</text>'
        hits = {}
        for _, j in arr: hits[j] = hits.get(j, 0) + 1
        for j in range(nr):
            n = hits.get(j, 0)
            if n == 0:
                back += f'<circle class="d2s fx d{k + 1}" cx="{ox + 98}" cy="{oy + ly(j, nr):.1f}" r="5.5"></circle>'
            elif n > 1:
                back += f'<circle class="d4s fx d{k + 1}" cx="{ox + 98}" cy="{oy + ly(j, nr):.1f}" r="5.5"></circle>'
        back += (f'<text class="t1 fx d{k + 1}" x="{ox + 60}" y="{oy + 116}" text-anchor="middle">{name}</text>'
                 f'<text class="sm fx d{k + 1}" x="{ox + 60}" y="{oy + 128}" text-anchor="middle">{why}</text>')
    mcard(deck, 'One-one and onto · arrow diagrams', 'Classify each function (left → right): one-one? onto?', base, back,
          '<p><b>One-one (injective):</b> no two arrows land on the same point (no orange dot). <b>Onto (surjective):</b> every right-hand point is hit (no red dot).</p>'
          '<p><b>Bijective</b> = both: a perfect pairing. Onto ⇔ range = codomain.</p>',
          'Injective, surjective and bijective from arrow diagrams',
          'One-one: no two arrows meet at one image; onto: every element of the codomain is hit. (a) one-one not onto; (b) neither; (c) onto not one-one; (d) bijective',
          vb='0 0 300 288', hint='Look for shared targets and unused targets.')


def horizontal_line_test(deck):
    P1 = Plane(-3, 3, -1.6, 5.5, 300, 190, (16, 10, 10, 16))
    P2 = Plane(-2.4, 2.4, -5.5, 5.5, 300, 190, (16, 10, 10, 16))
    base = (f'<g transform="translate(0,4) scale(.5)">{P1.axes(labels=False)}{P1.curve(lambda x: x * x, "c1", -2.3, 2.3)}</g>'
            f'<g transform="translate(150,4) scale(.5)">{P2.axes(labels=False)}{P2.curve(lambda x: x ** 3, "c1", -1.76, 1.76)}</g>'
            '<text class="lbl" x="75" y="122" text-anchor="middle">(a) f(x) = x²</text><text class="lbl" x="225" y="122" text-anchor="middle">(b) f(x) = x³</text>')
    ya, yb = P1.Y(2.2), P2.Y(2.2)
    sweep_a = f'<g transform="translate(0,4) scale(.5)"><line class="c2 sw" x1="{P1.X(-3):.1f}" y1="{ya:.1f}" x2="{P1.X(3):.1f}" y2="{ya:.1f}"></line></g>'
    sweep_b = f'<g transform="translate(150,4) scale(.5)"><line class="c2 sw" x1="{P2.X(-2.4):.1f}" y1="{yb:.1f}" x2="{P2.X(2.4):.1f}" y2="{yb:.1f}"></line></g>'
    ha = (f'<g transform="translate(0,4) scale(.5)"><circle class="d2s fx d3" cx="{P1.X(math.sqrt(2.2)):.1f}" cy="{ya:.1f}" r="6"></circle>'
          f'<circle class="d2s fx d3" cx="{P1.X(-math.sqrt(2.2)):.1f}" cy="{ya:.1f}" r="6"></circle></g>')
    hb = f'<g transform="translate(150,4) scale(.5)"><circle class="d3s fx d3" cx="{P2.X(2.2 ** (1 / 3)):.1f}" cy="{yb:.1f}" r="6"></circle></g>'
    back = ('<text class="t2 fx d2" x="75" y="140" text-anchor="middle">✗ not one-one</text><text class="sm fx d2" x="75" y="154" text-anchor="middle">a horizontal line hits twice</text>'
            '<text class="t3 fx d3" x="225" y="140" text-anchor="middle">✓ one-one</text><text class="sm fx d3" x="225" y="154" text-anchor="middle">every horizontal line hits once</text>'
            '<text class="sm fx d4" x="150" y="176" text-anchor="middle">(x² also misses y &lt; 0, so it is not onto R)</text>' + ha + hb)
    css = '.pp .sw{animation:swh 3.6s ease-in-out .3s infinite alternate both}@keyframes swh{from{transform:translateY(-44px)}to{transform:translateY(44px)}}'
    mcard(deck, 'Horizontal line test', 'f : R → R. Which graph is one-one? Which is onto?', base, back,
          '<p><b>Horizontal line test:</b> f is <b>one-one</b> iff every horizontal line cuts the graph <b>at most once</b>; f is <b>onto R</b> iff every horizontal line cuts it <b>at least once</b>.</p>'
          '<p>x² fails both (twice for y &gt; 0, never for y &lt; 0). x³ passes both: a bijection R → R.</p>',
          'Horizontal line test for one-one and onto',
          'Horizontal line test: one-one iff each horizontal line meets the graph at most once; onto R iff each meets it at least once. x² is neither; x³ is bijective',
          css=css, vb='0 0 300 190', front_only=sweep_a + sweep_b, hint='Slide a horizontal line up and down.')


def composition_chain(deck):
    xA, xB, xC = 30, 150, 270
    yA = [30, 80, 130, 180]
    yB = [30, 80, 130, 180]
    yC = [55, 105, 155]
    def col(x, ys, labs):
        return ''.join(f'<circle class="f0" cx="{x}" cy="{y}" r="11"></circle><text class="lbl" x="{x}" y="{y + 4}" text-anchor="middle">{l}</text>' for y, l in zip(ys, labs))
    def line(x0, y0, x1, y1, cls, mk, extra=''):
        vx, vy = x1 - x0, y1 - y0
        L = math.hypot(vx, vy)
        return f'<line class="{cls} {extra}" x1="{x0 + vx / L * 13:.1f}" y1="{y0 + vy / L * 13:.1f}" x2="{x1 - vx / L * 14:.1f}" y2="{y1 - vy / L * 14:.1f}" marker-end="url(#{mk})"></line>'
    f = {0: 0, 1: 1, 2: 2, 3: 2}      # 2->3, 3->4, 4->5, 5->5 (indices in B = 3,4,5,9)
    g = {0: 0, 1: 0, 2: 1, 3: 1}      # 3->7, 4->7, 5->11, 9->11
    base = col(xA, yA, [2, 3, 4, 5]) + col(xB, yB, [3, 4, 5, 9]) + col(xC, yC, [7, 11, 15])
    base += ''.join(line(xA, yA[i], xB, yB[j], 'c1', 'pb') for i, j in f.items())
    base += ''.join(line(xB, yB[i], xC, yC[j], 'c2', 'pr') for i, j in g.items())
    base += '<text class="t1" x="90" y="14" text-anchor="middle">f</text><text class="t2" x="210" y="14" text-anchor="middle">g</text><text class="sm" x="30" y="14" text-anchor="middle">A</text><text class="sm" x="150" y="14" text-anchor="middle">B</text><text class="sm" x="270" y="14" text-anchor="middle">C</text>'
    back = ''
    gof = {0: 0, 1: 0, 2: 1, 3: 1}
    def seg(x0, y0, x1, y1, extra):
        vx, vy = x1 - x0, y1 - y0
        L = math.hypot(vx, vy)
        return f'<line class="c4 {extra}" x1="{x0 + vx / L * 13:.1f}" y1="{y0 + vy / L * 13:.1f}" x2="{x1 - vx / L * 14:.1f}" y2="{y1 - vy / L * 14:.1f}" marker-end="url(#po)"></line>'
    chains = ['2 → 3 → 7', '3 → 4 → 7', '4 → 5 → 11', '5 → 5 → 11']
    for k, (i, j) in enumerate(gof.items()):
        back += seg(xA, yA[i], xB, yB[f[i]], f'fx d{k + 1}') + seg(xB, yB[f[i]], xC, yC[j], f'fx d{k + 1}')
        back += f'<text class="t4 fx d{k + 1}" x="{60 + (k % 2) * 130}" y="{206 + (k // 2) * 15}">{chains[k]}</text>'
    back += '<text class="sm fx d5" x="150" y="238" text-anchor="middle">gof = {(2,7), (3,7), (4,11), (5,11)}: 15 and 9 unused</text>'
    mcard(deck, 'Composition of functions', 'f : {2,3,4,5} → {3,4,5,9} and g : {3,4,5,9} → {7,11,15} are given by the arrows. Find gof.', base, back,
          '<p><b>gof(x) = g(f(x))</b>: apply f first, then g. Follow each element along blue then red.</p>'
          '<p>gof(2) = g(3) = 7, gof(3) = g(4) = 7, gof(4) = g(5) = 11, gof(5) = g(5) = 11. So gof = {(2,7), (3,7), (4,11), (5,11)}.</p>',
          'gof follows f then g',
          'gof(x) = g(f(x)) apply f first; Example 15: gof(2)=7, gof(3)=7, gof(4)=11, gof(5)=11 (15 is not hit)',
          vb='0 0 300 246', hint='Follow each element through both arrow sets.')


def inverse_mirror(deck):
    P, h = eqplane(-3, 3, -3, 3, pad=(14, 8, 8, 14))
    base = (P.axes(labels=False) + P.line(-3, -3, 3, 3, 'guide') + P.curve(lambda x: x ** 3, 'c1', -1.45, 1.45, clip=(-3, 3))
            + P.text(1.2, 0.3, 'y = f(x)', 't1', dx=6, dy=4) + P.text(2.6, 2.75, 'y = x', 'sm', dx=-4, dy=14, anchor='end'))
    cb = lambda x: math.copysign(abs(x) ** (1 / 3), x)
    back = (P.curve(cb, 'c2 draw', -3, 3, n=200).replace('class="c2 draw"', 'class="c2 draw" pathLength="100"')
            + P.dot(1.4, 1.4 ** 3, 'd1s', 4.5, 'fx d2') + P.dot(1.4 ** 3, 1.4, 'd2s', 4.5, 'fx d2')
            + P.line(1.4, 1.4 ** 3, 1.4 ** 3, 1.4, 'guide fx d3')
            + P.text(1.4 ** 3, 1.4, 'f⁻¹', 't2 fx d3', dx=6, dy=16))
    mcard(deck, 'Inverse function · mirror image', 'f(x) = x³ is one-one and onto R. How are the graphs of f and f⁻¹ related?', base, back,
          '<p>If f(a) = b then f⁻¹(b) = a: the point (a, b) becomes (b, a). Every point is <b>reflected in the line y = x</b>.</p>'
          '<p>Only a <b>bijection</b> has an inverse (one-one so it can be undone, onto so every y has a source). Here f⁻¹(x) = ∛x. Check: f⁻¹(f(x)) = x and f(f⁻¹(y)) = y.</p>',
          'Graph of f⁻¹ is the mirror image of f in y = x',
          'f⁻¹ swaps (a,b) to (b,a): the graph of f⁻¹ is the reflection of f in y = x; only bijections are invertible; for f(x)=x³, f⁻¹(x)=cube root of x',
          vb=f'0 0 300 {h}', hint='Swap x and y for every point.')


# ================================================================ Maths 12 Ch 2 Inverse trigonometric functions
def _pi_ticks(vals, unit=None):
    """Ticks at v * pi/2 (vals in half-turns of pi/2) with labels like π/2, π, 3π/2."""
    out = []
    for v in vals:
        lab = {1: 'π/2', -1: '−π/2', 2: 'π', -2: '−π', 3: '3π/2', -3: '−3π/2', 4: '2π', -4: '−2π'}[v]
        out.append((v * math.pi / 2, lab))
    return out


def inv_restrict_sine(deck):
    P = Plane(-5.2, 5.2, -1.7, 1.7, 300, 190, (14, 10, 10, 20))
    xt = _pi_ticks([-3, -2, -1, 1, 2, 3])
    base = P.axes(xt, [(1, '1'), (-1, '−1')], grid=True) + P.curve(math.sin, 'c0', -4.9, 4.9, n=240)
    base += P.line(-5.1, 0.5, 5.1, 0.5, 'c2')
    sols = [math.pi / 6, 5 * math.pi / 6, -7 * math.pi / 6]
    dots = ''.join(P.dot(x, 0.5, 'd2s', 4.5) for x in sols)
    back = (P.curve(math.sin, 'c1', -math.pi / 2, math.pi / 2, n=80) + P.dot(math.pi / 6, 0.5, 'd1s', 5.5, 'fx d2')
            + P.text(math.pi / 2, 1, 'π/2', 't1 fx d2', dx=6, dy=-4) + P.text(-math.pi / 2, -1, '−π/2', 't1 fx d2', anchor='end', dx=-6, dy=14))
    mcard(deck, 'Why restrict the domain?', 'sin x = ½ has infinitely many solutions, so sin is not one-one on R. Which piece do we keep to define sin⁻¹?', base + dots, back,
          '<p>An inverse needs a <b>bijection</b>. Keep one piece where sin is one-one and takes <b>every value in [−1, 1]</b> once: <b>[−π/2, π/2]</b>, the <b>principal branch</b>. Then sin⁻¹ : [−1, 1] → [−π/2, π/2].</p>'
          '<p>Other pieces (like [π/2, 3π/2]) would work too, but this one contains 0 and both positive and negative angles, so it is the standard choice.</p>',
          'Principal branch of sin⁻¹ comes from restricting sin to [−π/2, π/2]',
          'sin is not one-one on R; restricting to [−π/2, π/2] makes it a bijection onto [−1,1]; that piece defines the principal branch of sin⁻¹',
          vb='0 0 300 190', hint='Where does the red line cut the curve? Keep one piece only.')


def sin_inverse_mirror(deck):
    P, h = eqplane(-2.3, 2.3, -2.3, 2.3, pad=(14, 8, 8, 14))
    pt = _pi_ticks([1, -1])
    base = (P.axes([(1, '1'), (-1, '−1')], [(v, l) for v, l in pt], grid=False, labels=False) + P.line(-2.2, -2.2, 2.2, 2.2, 'guide')
            + P.curve(math.sin, 'c1', -math.pi / 2, math.pi / 2, n=80) + P.text(1.0, 1.0, 'y = sin x', 't1', dx=6, dy=18))
    back = (P.curve(math.asin, 'c2 draw', -1, 1, n=120).replace('class="c2 draw"', 'class="c2 draw" pathLength="100"')
            + P.dot(1, math.pi / 2, 'd2s', 4.5, 'fx d2') + P.dot(-1, -math.pi / 2, 'd2s', 4.5, 'fx d2')
            + P.text(0.1, 1.9, 'y = sin⁻¹x', 't2 fx d3', dx=6, dy=0))
    mcard(deck, 'Graph of sin⁻¹', 'Reflect the principal branch of y = sin x in the line y = x. What are the domain and range of the new curve?', base, back,
          '<p>Swap x and y for every point: (a, b) on sin becomes (b, a) on sin⁻¹. Ends: (π/2, 1) ↦ (1, π/2) and (−π/2, −1) ↦ (−1, −π/2).</p>'
          '<p><b>Domain [−1, 1], range [−π/2, π/2].</b> An increasing, odd function through the origin.</p>',
          'sin⁻¹ graph is the mirror image of sin on [−π/2, π/2]',
          'sin⁻¹ : [-1,1] -> [-pi/2, pi/2] is the reflection of sin restricted to [-pi/2, pi/2] in y = x; increasing and odd',
          vb=f'0 0 300 {h}', hint='Swap the roles of x and y.')


def principal_arcs(deck):
    P, h = eqplane(-1.6, 2.4, -1.5, 1.7, pad=(8, 6, 8, 6))
    ox, oy = P.X(0), P.Y(0)
    r = P.X(1) - ox
    base = P.axes(labels=False) + f'<circle class="ghost" cx="{ox:.1f}" cy="{oy:.1f}" r="{r:.1f}"></circle>'
    r1, r2 = r * 1.3, r * 1.13
    right = f'<path class="c1 fx d2" d="M{ox:.1f},{oy + r1:.1f} A{r1:.1f},{r1:.1f} 0 0 0 {ox:.1f},{oy - r1:.1f}"></path>'
    top = f'<path class="c2 fx d3" d="M{ox + r2:.1f},{oy:.1f} A{r2:.1f},{r2:.1f} 0 0 0 {ox - r2:.1f},{oy:.1f}"></path>'
    back = (right + top
            + P.text(1.42, 0.5, 'sin⁻¹', 't1 fx d2') + P.text(1.42, 0.32, 'tan⁻¹', 't1 fx d2') + P.text(1.42, 0.14, 'cosec⁻¹', 't1 fx d2') + P.text(1.42, -0.16, '−π/2…π/2', 't1 fx d2')
            + P.text(-1.55, 1.58, 'cos⁻¹, cot⁻¹, sec⁻¹', 't2 fx d3') + P.text(-1.55, 1.38, '0 … π', 't2 fx d3'))
    mcard(deck, 'Principal values on the circle', 'Which half of the unit circle holds the principal values of sin⁻¹, tan⁻¹, cosec⁻¹? Which half holds cos⁻¹, cot⁻¹, sec⁻¹?', base, back,
          '<p><b>Right half</b> (quadrants IV and I, angles from −π/2 to π/2): <b>sin⁻¹, tan⁻¹, cosec⁻¹</b>. They can be negative.</p>'
          '<p><b>Upper half</b> (quadrants I and II, angles from 0 to π): <b>cos⁻¹, cot⁻¹, sec⁻¹</b>. Never negative.</p>'
          '<p>Excluded end-points: tan⁻¹ (±π/2), cot⁻¹ (0, π), cosec⁻¹ (0), sec⁻¹ (π/2).</p>',
          'Principal value ranges: right half circle vs upper half circle',
          'sin^-1, tan^-1, cosec^-1 take values in the right half (-pi/2 to pi/2, negative allowed); cos^-1, cot^-1, sec^-1 in the upper half (0 to pi)',
          vb=f'0 0 300 {h}', hint='Think: which angles have negative sine? Negative cosine?')


def inverse_complementary(deck):
    A, B, C = (40, 176), (220, 176), (220, 56)
    base = (f'<polygon class="f0" points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}"></polygon>'
            f'<polyline class="c0" points="{B[0] - 12},{B[1]} {B[0] - 12},{B[1] - 12} {B[0]},{B[1] - 12}"></polyline>'
            f'<text class="lbl" x="231" y="118">x</text><text class="lbl" x="118" y="192" text-anchor="middle">√(1 − x²)</text>'
            f'<text class="lbl" x="108" y="106" text-anchor="end">1</text>')
    a1 = f'<path class="c1 fx d2" d="M{A[0] + 42},{A[1]} A42,42 0 0 0 {A[0] + 42 * math.cos(math.atan2(A[1] - C[1], C[0] - A[0])):.1f},{A[1] - 42 * math.sin(math.atan2(A[1] - C[1], C[0] - A[0])):.1f}"></path>'
    ang_c = math.atan2(C[1] - A[1], C[0] - A[0])   # direction of hypotenuse from A
    # arc at C between CB (down) and CA
    ca = math.atan2(A[1] - C[1], A[0] - C[0])
    a2 = f'<path class="c2 fx d3" d="M{C[0]},{C[1] + 34} A34,34 0 0 1 {C[0] + 34 * math.cos(ca):.1f},{C[1] + 34 * math.sin(ca):.1f}"></path>'
    back = (a1 + a2 + '<text class="t1 fx d2" x="94" y="170">sin⁻¹x</text><text class="t2 fx d3" x="160" y="82" text-anchor="middle">cos⁻¹x</text>'
            '<text class="t4 fx d4" x="150" y="30" text-anchor="middle">sin⁻¹x + cos⁻¹x = π/2</text>')
    mcard(deck, 'sin⁻¹x + cos⁻¹x', 'In this right triangle (hypotenuse 1, one leg x), name the two acute angles. What is their sum?', base, back,
          '<p>The angle opposite the side x has sine x: it is <b>sin⁻¹x</b>. The other angle has cosine x: it is <b>cos⁻¹x</b>. Acute angles of a right triangle add to π/2:</p>'
          '<p><b>sin⁻¹x + cos⁻¹x = π/2</b>, for x ∈ [−1, 1]. Same idea: <b>tan⁻¹x + cot⁻¹x = π/2</b> (x ∈ R) and <b>sec⁻¹x + cosec⁻¹x = π/2</b> (|x| ≥ 1).</p>'
          '<p>The same triangle also gives sin⁻¹x = tan⁻¹(x/√(1 − x²)) = cos⁻¹√(1 − x²) for 0 ≤ x < 1.</p>',
          'Complementary inverse trig identities from a right triangle',
          'sin^-1 x + cos^-1 x = pi/2 (x in [-1,1]); tan^-1 x + cot^-1 x = pi/2; sec^-1 x + cosec^-1 x = pi/2 (|x|>=1); triangle with hypotenuse 1 and leg x',
          vb='0 0 300 200', hint='Complementary acute angles.')


def _inv_graph(deck, name, pieces, fn, x_rng, y_rng, xt, yt, dom, rng, note, term, guides=(), dots=(), holes=(), tag='Inverse trig graphs · name it'):
    P = Plane(x_rng[0], x_rng[1], y_rng[0], y_rng[1], 300, 190, (16, 10, 10, 20))
    base = P.axes(xt, yt, grid=True, labels=False)
    for a, b in pieces:
        base += P.curve(fn, 'c1', a, b, n=200, clip=(y_rng[0], y_rng[1]))
    back = ''
    for kind, v in guides:
        back += (P.line(x_rng[0], v, x_rng[1], v, 'guide fx d2') if kind == 'h' else P.line(v, y_rng[0], v, y_rng[1], 'guide fx d2'))
    for (x, y) in dots:
        back += P.dot(x, y, 'd1s', 4.5, 'fx d2')
    for (x, y) in holes:
        back += P.hole(x, y, 'c1', 4.5).replace('class="f0 c1 "', 'class="f0 c1 fx d2"')
    mcard(deck, tag, 'Name this function. What are its domain and range?', base, back,
          f'<p><b>{name}</b></p><p>Domain: <b>{dom}</b> &nbsp; Range: <b>{rng}</b></p><p>{note}</p>', term,
          f'{name}; domain {dom}; range {rng}. {note}', vb='0 0 300 190', hint='Read the shape, then the extent along each axis.')


def inverse_graphs(deck):
    pi = math.pi
    cbrt = lambda v: v
    _inv_graph(deck, 'y = cos⁻¹x', [(-1, 1)], math.acos, (-2.4, 2.4), (-0.6, 3.8), [(1, '1'), (-1, '−1')], [(pi / 2, 'π/2'), (pi, 'π')],
               '[−1, 1]', '[0, π]', 'Decreasing; cos⁻¹0 = π/2; cos⁻¹(−x) = π − cos⁻¹x, so the graph is symmetric about (0, π/2).', 'cos⁻¹ graph',
               guides=[('h', pi / 2)], dots=[(1, 0), (-1, pi)])
    _inv_graph(deck, 'y = tan⁻¹x', [(-5.85, 5.85)], math.atan, (-6, 6), (-2.1, 2.1), [(-4, '−4'), (-2, '−2'), (2, '2'), (4, '4')], [(pi / 2, 'π/2'), (-pi / 2, '−π/2')],
               'R', '(−π/2, π/2)', 'Increasing, odd, with horizontal asymptotes y = ±π/2 (never reached).', 'tan⁻¹ graph', guides=[('h', pi / 2), ('h', -pi / 2)])
    _inv_graph(deck, 'y = cot⁻¹x', [(-5.85, 5.85)], lambda x: pi / 2 - math.atan(x), (-6, 6), (-0.6, 3.8), [(-4, '−4'), (-2, '−2'), (2, '2'), (4, '4')], [(pi / 2, 'π/2'), (pi, 'π')],
               'R', '(0, π)', 'Decreasing, with horizontal asymptotes y = 0 and y = π; cot⁻¹x = π/2 − tan⁻¹x.', 'cot⁻¹ graph', guides=[('h', 0), ('h', pi)])
    _inv_graph(deck, 'y = sec⁻¹x', [(1, 5.85), (-5.85, -1)], lambda x: math.acos(1 / x), (-6, 6), (-0.6, 3.8), [(-4, '−4'), (-2, '−2'), (-1, '−1'), (1, '1'), (2, '2'), (4, '4')], [(pi / 2, 'π/2'), (pi, 'π')],
               'R − (−1, 1)', '[0, π] − {π/2}', 'Two branches; asymptote y = π/2; sec⁻¹x = cos⁻¹(1/x).', 'sec⁻¹ graph', guides=[('h', pi / 2)], dots=[(1, 0), (-1, pi)])
    _inv_graph(deck, 'y = cosec⁻¹x', [(1, 5.85), (-5.85, -1)], lambda x: math.asin(1 / x), (-6, 6), (-2.1, 2.1), [(-4, '−4'), (-2, '−2'), (-1, '−1'), (1, '1'), (2, '2'), (4, '4')], [(pi / 2, 'π/2'), (-pi / 2, '−π/2')],
               'R − (−1, 1)', '[−π/2, π/2] − {0}', 'Two branches; asymptote y = 0; cosec⁻¹x = sin⁻¹(1/x); odd function.', 'cosec⁻¹ graph', guides=[('h', 0)], dots=[(1, pi / 2), (-1, -pi / 2)])


def _zig(deck, kind):
    pi = math.pi
    cfg = {
        'sin': (lambda x: math.asin(math.sin(x)), (-1.9, 1.9), 'y = sin⁻¹(sin x)', '[−π/2, π/2]', 'Equal to x only on [−π/2, π/2]; then a zigzag of slope ±1 with period 2π. Range [−π/2, π/2]: e.g. sin⁻¹(sin 2π/3) = π − 2π/3 = π/3.',
                'Graph of sin⁻¹(sin x) is a zigzag',
                [(pi / 2, 'π/2'), (-pi / 2, '−π/2')], -pi / 2, pi / 2),
        'cos': (lambda x: math.acos(math.cos(x)), (-0.6, 3.8), 'y = cos⁻¹(cos x)', '[0, π]', 'Equal to |x| for x ∈ [−π, π]; zigzag between 0 and π, period 2π, even function. Range [0, π]: e.g. cos⁻¹(cos 7π/6) = 2π − 7π/6 = 5π/6.',
                'Graph of cos⁻¹(cos x) is a zigzag',
                [(pi / 2, 'π/2'), (pi, 'π')], 0, pi),
        'tan': (lambda x: (math.atan(math.tan(x)) if abs(math.cos(x)) > 0.05 else None), (-2.1, 2.1), 'y = tan⁻¹(tan x)', '(−π/2, π/2)', 'Equal to x on (−π/2, π/2), then repeats with period π (a sawtooth); undefined at odd multiples of π/2. Range (−π/2, π/2): e.g. tan⁻¹(tan 3π/4) = 3π/4 − π = −π/4.',
                'Graph of tan⁻¹(tan x) is a sawtooth',
                [(pi / 2, 'π/2'), (-pi / 2, '−π/2')], -pi / 2, pi / 2),
    }
    fn, yr, name, rng, note, term, yt, ylo, yhi = cfg[kind]
    P = Plane(-7.2, 7.2, yr[0], yr[1], 300, 190, (14, 10, 10, 20))
    xt = _pi_ticks([-4, -2, 2, 4])
    base = P.axes(xt, yt, grid=True, labels=False) + P.line(-pi / 2 if kind != 'cos' else 0, -pi / 2 if kind != 'cos' else 0, pi / 2 if kind != 'cos' else pi, pi / 2 if kind != 'cos' else pi, 'c1')
    if kind == 'cos':
        base = P.axes(xt, yt, grid=True, labels=False) + P.line(0, 0, pi, pi, 'c1')
    back = P.curve(fn, 'c2 draw', -2 * pi, 2 * pi, n=700).replace('class="c2 draw"', 'class="c2 draw" pathLength="100"')
    mcard(deck, 'Composite graphs · principal branch', f'Sketch {name} for x ∈ [−2π, 2π]. The blue piece is where it equals x (or |x|).', base, back,
          f'<p><b>{name}</b>: range <b>{rng}</b>.</p><p>{note}</p>'
          '<p>Method for a value: reduce the angle into the principal interval using the symmetry of the function, then read the inverse.</p>',
          term, f'{name} is periodic (period 2π for sin and cos, π for tan) with range {rng}; it equals x only inside the principal branch', vb='0 0 300 190',
          hint='Where is it equal to x? What happens outside?')


def tan_sum_circle(deck):
    P, h = eqplane(-1.4, 1.4, -1.0, 1.4, pad=(8, 6, 8, 6))
    ox, oy = P.X(0), P.Y(0)
    r = P.X(1) - ox
    a, b = math.atan(2), math.atan(3)
    ray = lambda ang, cls, L=1.05, extra='': P.line(0, 0, L * math.cos(ang), L * math.sin(ang), cls + ' ' + extra)
    base = P.axes(labels=False) + f'<circle class="ghost" cx="{ox:.1f}" cy="{oy:.1f}" r="{r:.1f}"></circle>' + ray(a, 'c1') + ray(b, 'c1')
    base += P.text(1.05 * math.cos(a), 1.05 * math.sin(a), 'tan⁻¹2', 't1', dx=4, dy=-4) + P.text(1.05 * math.cos(b), 1.05 * math.sin(b), 'tan⁻¹3', 't1', anchor='end', dx=-4, dy=-4)
    tot = a + b
    back = (ray(tot, 'c4', 1.05, 'fx d2') + P.text(1.05 * math.cos(tot), 1.05 * math.sin(tot), '3π/4', 't4 fx d2', anchor='end', dx=-4, dy=-4)
            + ray(-math.pi / 4, 'dr', 1.0, 'fx d3') + P.text(1.0 * math.cos(-math.pi / 4), 1.0 * math.sin(-math.pi / 4), '−π/4 ✗', 't2 fx d3', dx=4, dy=8))
    mcard(deck, 'tan⁻¹x + tan⁻¹y', 'tan⁻¹2 + tan⁻¹3 = ? The formula gives tan⁻¹((2 + 3)/(1 − 6)) = tan⁻¹(−1). Is the answer −π/4?', base, back,
          '<p>Both angles are in (0, π/2) so their sum is in (0, π): it cannot be negative. 63.4° + 71.6° = <b>135° = 3π/4</b>.</p>'
          '<p><b>tan⁻¹x + tan⁻¹y = tan⁻¹((x + y)/(1 − xy))</b> only when <b>xy &lt; 1</b>. If <b>xy &gt; 1</b> (x, y &gt; 0) add <b>π</b>: tan⁻¹2 + tan⁻¹3 = π + tan⁻¹(−1) = 3π/4. (If xy &gt; 1 with x, y &lt; 0, subtract π.)</p>',
          'tan⁻¹ addition formula and the xy > 1 correction',
          'tan^-1 x + tan^-1 y = tan^-1((x+y)/(1-xy)) if xy<1; add pi if xy>1 and x,y>0 (subtract pi if x,y<0); tan^-1 2 + tan^-1 3 = 3pi/4',
          css=_DR, vb=f'0 0 300 {h}', hint='Add the angles geometrically first.')


# ================================================================ Maths 12 Ch 3 Matrices
def _mx(x0, y0, rows, cw=32, ch=26, cls='lbl', pad=4):
    """Matrix drawn as brackets + centred text cells. Returns (svg, cell_centre(i, j))."""
    n, m = len(rows), len(rows[0])
    w, h = m * cw, n * ch
    o = (f'<path class="c0" d="M{x0 + 6},{y0 - pad} H{x0} V{y0 + h + pad} H{x0 + 6}"></path>'
         f'<path class="c0" d="M{x0 + w - 6},{y0 - pad} H{x0 + w} V{y0 + h + pad} H{x0 + w - 6}"></path>')
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            if v is None: continue
            o += f'<text class="{cls}" x="{x0 + j * cw + cw / 2:.1f}" y="{y0 + i * ch + ch / 2 + 4:.1f}" text-anchor="middle">{str(v).replace("-", "−")}</text>'
    return o, (lambda i, j: (x0 + j * cw + cw / 2, y0 + i * ch + ch / 2))


def matmul_steps(deck):
    A = [[2, 4], [3, 2]]
    B = [[1, 3], [-2, 5]]
    C = [[-6, 26], [-1, 19]]
    xa, xb, xc, y0, cw, ch = 16, 126, 236, 44, 32, 26
    ga, _ = _mx(xa, y0, A)
    gb, _ = _mx(xb, y0, B)
    gc, cc = _mx(xc, y0, [[None, None], [None, None]])
    base = ga + gb + gc + f'<text class="lbl" x="98" y="{y0 + 30}" text-anchor="middle">×</text><text class="lbl" x="208" y="{y0 + 30}" text-anchor="middle">=</text>'
    base += '<text class="sm" x="48" y="24" text-anchor="middle">A (2 × 2)</text><text class="sm" x="158" y="24" text-anchor="middle">B (2 × 2)</text><text class="sm" x="268" y="24" text-anchor="middle">AB</text>'
    back = ''
    css = ''
    steps = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for k, (i, j) in enumerate(steps):
        t0, t1 = 20 * k, 20 * k + 19.9
        css += (f'.pp .h{k}{{opacity:0;animation:hk{k} 12s linear infinite}}'
                f'@keyframes hk{k}{{0%,{t0}%{{opacity:0}}{t0 + .1}%,{t1}%{{opacity:1}}{t1 + .1}%,100%{{opacity:0}}}}'
                f'.pp .r{k}{{opacity:0;animation:rk{k} 12s linear infinite}}'
                f'@keyframes rk{k}{{0%,{t0}%{{opacity:0}}{t0 + .1}%,100%{{opacity:1}}}}')
        arow = A[i]
        bcol = [B[0][j], B[1][j]]
        val = C[i][j]
        expr = f'{arow[0]}·{bcol[0]} + {arow[1]}·({bcol[1]}) = {val}'.replace('-', '−')
        back += (f'<rect class="f4 h{k}" x="{xa - 4}" y="{y0 + i * ch}" width="{2 * cw + 8}" height="{ch}" rx="4"></rect>'
                 f'<rect class="f1 h{k}" x="{xb + j * cw}" y="{y0 - 4}" width="{cw}" height="{2 * ch + 8}" rx="4"></rect>'
                 f'<rect class="f3 h{k}" x="{xc + j * cw}" y="{y0 + i * ch}" width="{cw}" height="{ch}" rx="4"></rect>'
                 f'<text class="t4 h{k}" x="150" y="128" text-anchor="middle">c{i + 1}{j + 1} = row {i + 1} · column {j + 1}</text>'
                 f'<text class="lbl h{k}" x="150" y="148" text-anchor="middle">{expr}</text>'
                 f'<text class="t3 r{k}" x="{cc(i, j)[0]:.1f}" y="{cc(i, j)[1] + 4:.1f}" text-anchor="middle">{str(val).replace("-", "−")}</text>')
    mcard(deck, 'Matrix multiplication · row × column', 'Multiply A = [[2, 4], [3, 2]] and B = [[1, 3], [−2, 5]]. How is each entry of AB built?', base, back,
          '<p>The (i, j) entry of AB is <b>row i of A</b> times <b>column j of B</b>, multiplied term by term and added: <b>cᵢⱼ = Σ aᵢₖ bₖⱼ</b>.</p>'
          '<p>AB = [[2·1 + 4(−2), 2·3 + 4·5], [3·1 + 2(−2), 3·3 + 2·5]] = <b>[[−6, 26], [−1, 19]]</b> (Ex 3.2 Q1(iv)). Note BA = [[11, 10], [11, 2]] is different.</p>',
          'Matrix product: row of A times column of B',
          'Entry (i,j) of AB = sum over k of a_ik b_kj (row i of A dot column j of B); AB for A=[[2,4],[3,2]], B=[[1,3],[-2,5]] is [[-6,26],[-1,19]]',
          css=css, vb='0 0 300 170', hint='Walk along a row of A and down a column of B.')


def matmul_dims(deck):
    cw = 14
    def grid(x, y, r, c, cls='f0'):
        return ''.join(f'<rect class="{cls}" x="{x + j * cw}" y="{y + i * cw}" width="{cw - 1}" height="{cw - 1}" rx="2"></rect>' for i in range(r) for j in range(c))
    base = (grid(12, 46, 2, 3) + grid(92, 46, 3, 4) + grid(190, 46, 2, 4)
            + '<text class="lbl" x="68" y="76" text-anchor="middle">×</text><text class="lbl" x="170" y="76" text-anchor="middle">=</text>'
            + '<text class="lbl" x="33" y="36" text-anchor="middle">A: 2 × 3</text><text class="lbl" x="120" y="36" text-anchor="middle">B: 3 × 4</text>')
    back = ('<rect class="f4 fx d2" x="44" y="24" width="14" height="16" rx="3"></rect><rect class="f4 fx d2" x="96" y="24" width="14" height="16" rx="3"></rect>'
            '<path class="c4 fx d2" d="M52,40 V52 H103 V40" fill="none"></path>'
            + grid(190, 46, 2, 4, 'f3').replace('class="f3"', 'class="f3 fx d3"')
            + '<text class="t3 fx d3" x="218" y="36" text-anchor="middle">AB: 2 × 4</text>'
            + '<text class="t4 fx d2" x="150" y="116" text-anchor="middle">inner numbers match (3 = 3): AB is defined</text>'
            + '<text class="t3 fx d3" x="150" y="134" text-anchor="middle">outer numbers give the order: 2 × 4</text>'
            + '<text class="t2 fx d4" x="150" y="168" text-anchor="middle">BA: (3 × 4)(2 × 3) → 4 ≠ 2, not defined</text>')
    mcard(deck, 'Matrix multiplication · orders', 'A has order 2 × 3 and B has order 3 × 4. Is AB defined? Is BA? What is the order of the product?', base, back,
          '<p><b>(m × n)(n × p) = (m × p)</b>: the inner numbers must match; the outer numbers give the order.</p>'
          '<p>AB is 2 × 4. BA would need 4 = 2, so <b>BA is not defined</b>. Both AB and BA exist only if A is m × n and B is n × m; then AB is m × m and BA is n × n.</p>',
          'Order of a matrix product: inner numbers match, outer numbers remain',
          '(m x n)(n x p) = (m x p): number of columns of A must equal number of rows of B; AB may exist while BA does not',
          vb='0 0 300 180', hint='Compare the columns of A with the rows of B.')


def rotation_powers(deck):
    P, h = eqplane(-1.5, 1.5, -1.5, 1.5, pad=(8, 8, 8, 8))
    ox, oy = P.X(0), P.Y(0)
    r = P.X(1) - ox
    th = math.radians(30)
    base = P.axes(labels=False) + f'<circle class="ghost" cx="{ox:.1f}" cy="{oy:.1f}" r="{r:.1f}"></circle>' + vec(P, 0, 0, 1, 0, 'c1') + P.text(1, 0, 'v = (1, 0)', 't1', dx=-2, dy=-8, anchor='end')
    back = ''
    cols = [('c2', 'A v'), ('c4', 'A² v'), ('c3', 'A³ v')]
    for k, (cls, lab) in enumerate(cols):
        a = -(k + 1) * th
        back += vec(P, 0, 0, math.cos(a), math.sin(a), cls, f'fx d{k + 2}') + P.text(1.02 * math.cos(a), 1.02 * math.sin(a), lab, {'c2': 't2', 'c4': 't4', 'c3': 't3'}[cls] + f' fx d{k + 2}', dx=6, dy=4 + (8 if k else 0))
    mcard(deck, 'Powers of a rotation matrix', 'A = [[cos θ, sin θ], [−sin θ, cos θ]] with θ = 30°. What does A do to the vector v = (1, 0)? What are A² and Aⁿ?', base, back,
          '<p>A v = (cos θ, −sin θ): the vector is <b>rotated clockwise by θ</b>. Applying A twice rotates by 2θ, so <b>Aⁿ = [[cos nθ, sin nθ], [−sin nθ, cos nθ]]</b> (Example 23, proved by induction).</p>'
          '<p>Check with the product formula: A·Aᵏ has entries cos θ cos kθ − sin θ sin kθ = cos (k + 1)θ and so on.</p>',
          'Aⁿ for the rotation matrix is rotation by nθ',
          'A = [[cos t, sin t],[-sin t, cos t]] rotates vectors clockwise by t; A^n = [[cos nt, sin nt],[-sin nt, cos nt]] (induction, Example 23)',
          vb=f'0 0 300 {h}', hint='Follow the vector after each multiplication by A.')


def sym_skew_grid(deck):
    S = [[1, 7, 3], [7, 4, -5], [3, -5, 6]]
    K = [[0, 2, -3], [-2, 0, 4], [3, -4, 0]]
    cw, ch, y0 = 32, 28, 46
    gs, cs = _mx(20, y0, S, cw, ch)
    gk, ck = _mx(174, y0, K, cw, ch)
    base = gs + gk + '<text class="lbl" x="68" y="26" text-anchor="middle">P</text><text class="lbl" x="222" y="26" text-anchor="middle">Q</text>'
    back = ''
    pairs = [((0, 1), 'f1'), ((0, 2), 'f2'), ((1, 2), 'f3')]
    for (i, j), cls in pairs:
        for (a, b) in [(i, j), (j, i)]:
            for (x0, name) in [(20, 'S'), (174, 'K')]:
                back += f'<rect class="{cls} fx d2" x="{x0 + b * cw}" y="{y0 + a * ch}" width="{cw}" height="{ch}" rx="4"></rect>'
    back += ''.join(f'<rect class="f4 fx d3" x="{174 + i * cw}" y="{y0 + i * ch}" width="{cw}" height="{ch}" rx="4"></rect>' for i in range(3))
    back += (f'<line class="guide fx d2" x1="20" y1="{y0}" x2="{20 + 3 * cw}" y2="{y0 + 3 * ch}"></line><line class="guide fx d2" x1="174" y1="{y0}" x2="{174 + 3 * cw}" y2="{y0 + 3 * ch}"></line>'
             '<text class="t1 fx d2" x="68" y="150" text-anchor="middle">P′ = P: mirror equal</text><text class="t2 fx d3" x="222" y="150" text-anchor="middle">Q′ = −Q: mirror opposite</text>'
             '<text class="t4 fx d3" x="222" y="168" text-anchor="middle">diagonal all 0</text>')
    mcard(deck, 'Symmetric and skew-symmetric', 'Look at the entries of P and Q. Which one is symmetric and which is skew-symmetric? What pattern defines each?', base, back,
          '<p><b>Symmetric</b> (P′ = P): aᵢⱼ = aⱼᵢ. Mirror the matrix in the main diagonal and nothing changes.</p>'
          '<p><b>Skew-symmetric</b> (Q′ = −Q): aⱼᵢ = −aᵢⱼ. Mirrored entries are opposites, and since aᵢᵢ = −aᵢᵢ every <b>diagonal entry is 0</b>.</p>',
          'Symmetric vs skew-symmetric: mirror in the diagonal',
          'Symmetric: A^T = A, a_ij = a_ji. Skew-symmetric: A^T = -A, a_ji = -a_ij and the diagonal is zero',
          vb='0 0 300 180', hint='Reflect each matrix in its main diagonal.')


def inverse_2x2(deck):
    base = (_mx(110, 30, [['a', 'b'], ['c', 'd']], 34, 28)[0] + '<text class="lbl" x="100" y="63" text-anchor="end">A =</text>')
    res, _ = _mx(150, 128, [['d', '−b'], ['−c', 'a']], 38, 28)
    back = ('<line class="c3 fx d2" x1="135" y1="54" x2="153" y2="69" marker-end="url(#pg)"></line><line class="c3 fx d2" x1="153" y1="60" x2="135" y2="45" marker-end="url(#pg)"></line>'
            '<text class="t3 fx d2" x="190" y="52" text-anchor="start">swap a and d</text>'
            '<text class="t2 fx d3" x="190" y="70" text-anchor="start">flip signs of b, c</text>'
            + '<text class="lbl fx d4" x="140" y="163" text-anchor="end">A⁻¹ = 1/(ad − bc)</text>'
            + f'<g class="fx d4">{res}</g>'
            + '<text class="t4 fx d4" x="150" y="206" text-anchor="middle">needs ad − bc ≠ 0</text>')
    mcard(deck, '2 × 2 inverse shortcut', 'Find the inverse of A = [[a, b], [c, d]] when ad − bc ≠ 0.', base, back,
          '<p><b>A⁻¹ = (1/(ad − bc)) [[d, −b], [−c, a]]</b>: swap the diagonal, negate the other two entries, divide by ad − bc.</p>'
          '<p>Example (the book’s A = [[2, 3], [1, 2]]): ad − bc = 1, so A⁻¹ = [[2, −3], [−1, 2]], and AA⁻¹ = I. If ad − bc = 0 there is no inverse. (The general method uses adjoints and determinants in Chapter 4.)</p>',
          'Inverse of a 2 × 2 matrix',
          'A^-1 = 1/(ad-bc) [[d,-b],[-c,a]]: swap diagonal, negate off-diagonal, divide by determinant; needs ad-bc != 0',
          vb='0 0 300 216', hint='Swap the diagonal, flip the other two signs.')


# ================================================================ Maths 12 Ch 4 Determinants
def det_area_morph(deck):
    """Unit square is carried by A = [[3, 1], [1, 2]] to a parallelogram of area |det A| = 5."""
    P, h = eqplane(-0.8, 4.6, -0.8, 3.6, pad=(10, 8, 8, 10))
    ox, oy = P.X(0), P.Y(0)
    a, b, c, d = 3, 1, 1, 2
    base = P.axes(labels=False) + P.poly([(0, 0), (1, 0), (1, 1), (0, 1)], 'f1')
    base += vec(P, 0, 0, 1, 0, 'c1') + vec(P, 0, 0, 0, 1, 'c3') + P.text(1, 0, 'e₁', 't1', dx=4, dy=14) + P.text(0, 1, 'e₂', 't3', dx=-14, dy=4)
    tr = f'matrix({a},{-c},{-b},{d},0,0)'
    css = (f'.pp .mo{{transform-box:view-box;transform-origin:{ox:.1f}px {oy:.1f}px;animation:mo 4s ease-in-out .3s infinite alternate both}}'
           f'@keyframes mo{{from{{transform:matrix(1,0,0,1,0,0)}}to{{transform:{tr}}}}}')
    par = [(0, 0), (a, c), (a + b, c + d), (b, d)]
    sq = " ".join(f"{P.X(x):.1f},{P.Y(y):.1f}" for x, y in [(0, 0), (1, 0), (1, 1), (0, 1)])
    back = (f'<polygon class="mo f4" points="{sq}"></polygon>'
            + vec(P, 0, 0, a, c, 'c1', 'fx d2') + vec(P, 0, 0, b, d, 'c3', 'fx d2')
            + P.text(a, c, 'A e₁ = (3, 1)', 't1 fx d2', dx=6, dy=4) + P.text(b, d, 'A e₂ = (1, 2)', 't3 fx d2', dx=-6, dy=-6, anchor='end')
            + P.text(2.0, 1.5, 'area 5', 't4 fx d3', anchor='middle'))
    mcard(deck, 'Determinant as area', 'A = [[3, 1], [1, 2]] sends the unit square to a parallelogram. What is its area, and how does it relate to |A|?', base, back,
          '<p>The columns of A are the images of e₁ = (1, 0) and e₂ = (0, 1): (3, 1) and (1, 2). The unit square becomes the parallelogram they span, with area <b>|ad − bc| = |3·2 − 1·1| = 5 = |A|</b>.</p>'
          '<p>So <b>|det A| is the factor by which A scales areas</b>. If det A &lt; 0 the picture is also flipped (orientation reverses); if det A = 0 the square is squashed onto a line (no inverse).</p>',
          'Determinant is the area scale factor',
          '|det A| is the factor by which A scales areas (volumes in 3D); det A = 0 collapses the plane onto a line; sign of det gives orientation; unit square -> parallelogram of area |ad-bc|',
          css=css, vb=f'0 0 300 {h}',
          hint='Follow where the two unit vectors go.')


def triangle_det_area(deck):
    P, h = eqplane(-5.5, 6.5, -0.5, 9.5, pad=(10, 6, 8, 10))
    pts = [(3, 8), (-4, 2), (5, 1)]
    base = P.axes(labels=False) + P.poly(pts, 'f0')
    for (x, y), lab in zip(pts, ['(3, 8)', '(−4, 2)', '(5, 1)']):
        base += P.dot(x, y, 'd1s', 4.5) + P.text(x, y, lab, 't1', dx=8 if x > 0 else -8, dy=-6 if y > 5 else 14, anchor='start' if x > 0 else 'end')
    back = P.poly(pts, 'f4 fx d2') + P.text(0.7, 3.8, 'Δ = 61/2', 't4 fx d3', anchor='middle')
    mcard(deck, 'Area of a triangle', 'Find the area of the triangle with vertices (3, 8), (−4, 2) and (5, 1) using a determinant.', base, back,
          '<p><b>Δ = ½ |x₁ y₁ 1; x₂ y₂ 1; x₃ y₃ 1|</b>. Expanding: ½ [3(2 − 1) − 8(−4 − 5) + 1(−4 − 10)] = ½ (3 + 72 − 14) = <b>61/2 square units</b>.</p>'
          '<p>Take the absolute value for an area. If the area is given, use both ±. If the three points are collinear the determinant is 0.</p>',
          'Area of a triangle from vertices by determinant',
          'Area = 1/2 |det [x1 y1 1; x2 y2 1; x3 y3 1]|, absolute value; use +- when area is given; zero for collinear points; (3,8),(-4,2),(5,1) gives 61/2',
          vb=f'0 0 300 {h}', hint='Put the coordinates in the determinant with a column of 1s.')


def collinear_line(deck):
    P, h = eqplane(-1.0, 7.0, -1.0, 7.0, pad=(10, 6, 8, 10))
    s = 6.0
    pts = [(1, 5), (2.5, 3.5), (4.5, 1.5)]
    base = P.axes(labels=False) + ''.join(P.dot(x, y, 'd1s', 4.8) for x, y in pts)
    base += P.text(1, 5, 'A(a, b + c)', 't1', dx=8, dy=-8) + P.text(2.5, 3.5, 'B(b, c + a)', 't1', dx=8, dy=-8) + P.text(4.5, 1.5, 'C(c, a + b)', 't1', dx=8, dy=-8)
    back = P.line(-0.5, s + 0.5, s + 0.5, -0.5, 'c2 fx d2') + P.text(4.6, 6.4, 'x + y = a + b + c', 't2 fx d3', anchor='middle')
    mcard(deck, 'Collinear points', 'Show that A(a, b + c), B(b, c + a), C(c, a + b) are collinear.', base, back,
          '<p>The area determinant is ½ |a b+c 1; b c+a 1; c a+b 1|. Add column 1 to column 2: the second column becomes (a+b+c, a+b+c, a+b+c), a multiple of the third column, so the determinant is <b>0</b>.</p>'
          '<p>Geometrically all three points satisfy <b>x + y = a + b + c</b>: they lie on one line. <b>Three points are collinear ⇔ the area determinant is 0.</b></p>',
          'Collinearity test with a determinant',
          'Three points are collinear iff |x1 y1 1; x2 y2 1; x3 y3 1| = 0; A(a,b+c), B(b,c+a), C(c,a+b) all lie on x+y=a+b+c',
          vb=f'0 0 300 {h}', hint='What do x + y equal at each point?')


def cofactor_minor(deck):
    cw, ch, x0, y0 = 46, 34, 20, 44
    grid = ''.join(f'<rect class="f0" x="{x0 + j * cw}" y="{y0 + i * ch}" width="{cw - 2}" height="{ch - 2}" rx="4"></rect>'
                   f'<text class="lbi" x="{x0 + j * cw + cw / 2 - 1}" y="{y0 + i * ch + ch / 2 + 3}" text-anchor="middle">a{i + 1}{j + 1}</text>' for i in range(3) for j in range(3))
    base = grid + '<text class="lbl" x="12" y="25">A = [aᵢⱼ], find the minor and cofactor of a₁₂</text>'
    back = (f'<rect class="f2 fx d2" x="{x0}" y="{y0}" width="{3 * cw - 2}" height="{ch - 2}" rx="4"></rect><rect class="f2 fx d2" x="{x0 + cw}" y="{y0}" width="{cw - 2}" height="{3 * ch - 2}" rx="4"></rect>'
            + ''.join(f'<rect class="f1 fx d3" x="{x0 + j * cw}" y="{y0 + i * ch}" width="{cw - 2}" height="{ch - 2}" rx="4"></rect>' for i in (1, 2) for j in (0, 2))
            + '<text class="t2 fx d2" x="176" y="60">delete row 1, col 2</text><text class="t1 fx d3" x="176" y="82">M₁₂ = det of blue part</text>'
            '<text class="t4 fx d4" x="176" y="106">A₁₂ = −M₁₂ (sign −)</text>'
            '<text class="sm fx d4" x="176" y="128">sign pattern:</text><text class="lbl fx d4" x="176" y="146">+ − +</text><text class="lbl fx d4" x="176" y="162">− + −</text><text class="lbl fx d4" x="176" y="178">+ − +</text>')
    mcard(deck, 'Minors and cofactors', 'For a 3 × 3 determinant, how do you find the minor and the cofactor of a₁₂?', base, back,
          '<p><b>Minor Mᵢⱼ</b>: cross out row i and column j, and take the determinant of what remains (here a 2 × 2).</p>'
          '<p><b>Cofactor Aᵢⱼ = (−1)ⁱ⁺ʲ Mᵢⱼ</b>: attach the checkerboard sign (+ at a₁₁, − at a₁₂, …). Then |A| = Σⱼ aᵢⱼ Aᵢⱼ along any row or column; but multiplying a row by the cofactors of <b>another</b> row gives 0.</p>',
          'Minor and cofactor: delete row and column, then sign',
          'Minor M_ij = determinant after deleting row i and column j; cofactor A_ij = (-1)^(i+j) M_ij; |A| = sum a_ij A_ij along any row or column; a row times another row cofactors = 0',
          vb='0 0 300 200', hint='Delete the row and column of a₁₂.')


def consistency_lines(deck):
    def panel(ox, lines, cls, extra=''):
        P = Plane(-3, 5, -2, 5, 100, 100, (4, 4, 4, 4))
        s = f'<g transform="translate({ox},4)">' + P.axes(labels=False)
        for (m, k), c in zip(lines, cls):
            s += P.line(-3, m * -3 + k, 5, m * 5 + k, c + extra)
        return s + '</g>'
    # each system as y = m x + k
    A = [(-0.5, 1), (-2 / 3, 1)]                # x+2y=2, 2x+3y=3
    B = [(-1 / 3, 5 / 3), (-1 / 3, 4 / 3)]       # x+3y=5, 2x+6y=8
    C = [(-1 / 3, 5 / 3), (-1 / 3, 5 / 3)]       # x+3y=5, 2x+6y=10
    base = panel(0, A, ['c1', 'c2']) + panel(100, B, ['c1', 'c2']) + panel(200, C, ['c1', 'c2'])
    base += ''.join(f'<text class="lbi" x="{x}" y="118" text-anchor="middle">({l})</text>' for x, l in [(50, 'a'), (150, 'b'), (250, 'c')])
    back = ('<text class="t3 fx d2" x="50" y="134" text-anchor="middle">|A| ≠ 0</text><text class="sm fx d2" x="50" y="148" text-anchor="middle">unique solution</text>'
            '<text class="t2 fx d3" x="150" y="134" text-anchor="middle">|A| = 0</text><text class="t2 fx d3" x="150" y="148" text-anchor="middle">(adj A)B ≠ O</text><text class="sm fx d3" x="150" y="162" text-anchor="middle">no solution</text>'
            '<text class="t4 fx d4" x="250" y="134" text-anchor="middle">|A| = 0</text><text class="t4 fx d4" x="250" y="148" text-anchor="middle">(adj A)B = O</text><text class="sm fx d4" x="250" y="162" text-anchor="middle">infinitely many</text>')
    mcard(deck, 'Consistency of linear systems', 'Match the tests “|A| ≠ 0”, “|A| = 0 and (adj A)B ≠ O”, “|A| = 0 and (adj A)B = O” with these three pairs of lines.', base, back,
          '<p>(a) x + 2y = 2 and 2x + 3y = 3 meet at one point: <b>consistent, unique</b> (|A| = −1 ≠ 0). (b) x + 3y = 5 and 2x + 6y = 8 are parallel: <b>inconsistent</b> (Ex 4.5 Q3). (c) The same line twice: <b>consistent with infinitely many solutions</b>.</p>'
          '<p>In 3 variables the same test works: |A| ≠ 0 ⇒ unique solution X = A⁻¹B; |A| = 0 ⇒ compute (adj A)B.</p>',
          'Consistency test: |A| and (adj A)B',
          'AX=B: |A|!=0 unique solution X = A^-1 B; |A|=0 and (adj A)B != O inconsistent (no solution); |A|=0 and (adj A)B = O: infinitely many solutions or none (check); lines intersect / parallel / coincide',
          vb='0 0 300 172', hint='Unique, none, or infinitely many?')


# ================================================================ Maths 12 Ch 5 Continuity and differentiability
def _mini(ox, oy, xr, yr, size=(96, 96)):
    return Plane(xr[0], xr[1], yr[0], yr[1], size[0], size[1], (4, 4, 4, 4)), (ox, oy)


def discontinuity_types(deck):
    def wrap(P, o, body):
        return f'<g transform="translate({o[0]},{o[1]})">{P.axes(labels=False)}{body}</g>'
    # (a) hole: f(x) = (x^2 - 1)/(x - 1), f(1) = 3
    Pa, oa = _mini(2, 6, (-1, 3.5), (-1, 4))
    a = wrap(Pa, oa, Pa.curve(lambda x: x + 1, 'c1', -1, 3.4) + Pa.hole(1, 2, 'c1', 4))
    # (b) jump: f(x) = x (x <= 1), 5 (x > 1) scaled
    Pb, ob = _mini(102, 6, (-1, 3.5), (-1, 6))
    b = wrap(Pb, ob, Pb.curve(lambda x: x, 'c1', -1, 1) + Pb.curve(lambda x: 5, 'c1', 1, 3.4) + Pb.dot(1, 1, 'd1s', 3.6) + Pb.hole(1, 5, 'c1', 4))
    # (c) infinite: 1/(x - 1)
    Pc, oc = _mini(202, 6, (-1, 3.5), (-3, 3))
    c = wrap(Pc, oc, Pc.curve(lambda x: 1 / (x - 1), 'c1', -1, 0.66, clip=(-3, 3)) + Pc.curve(lambda x: 1 / (x - 1), 'c1', 1.34, 3.4, clip=(-3, 3)))
    base = a + b + c + ''.join(f'<text class="lbi" x="{x}" y="116" text-anchor="middle">({l})</text>' for x, l in [(50, 'a'), (150, 'b'), (250, 'c')])
    back = (f'<g transform="translate({oa[0]},{oa[1]})">' + Pa.dot(1, 3, 'd2s', 4, 'fx d2') + '</g>' + '<text class="t1 fx d2" x="50" y="132" text-anchor="middle">removable</text><text class="sm fx d2" x="50" y="146" text-anchor="middle">limit ≠ f(c)</text>'
            '<text class="t2 fx d3" x="150" y="132" text-anchor="middle">jump</text><text class="sm fx d3" x="150" y="146" text-anchor="middle">left ≠ right</text>'
            '<text class="t4 fx d4" x="250" y="132" text-anchor="middle">infinite</text><text class="sm fx d4" x="250" y="146" text-anchor="middle">no limit</text>')
    mcard(deck, 'Kinds of discontinuity', 'Each graph is discontinuous at x = 1. Name the three kinds of discontinuity.', base, back,
          '<p>f is continuous at c iff <b>lim x→c⁻ f(x) = lim x→c⁺ f(x) = f(c)</b>. Break any one link and the graph tears:</p>'
          '<p>(a) <b>removable</b>: the limit exists but f(1) is missing or wrong; (b) <b>jump</b>: the two one-sided limits differ (Ex 5.1 Q5, Q6); (c) <b>infinite</b>: the function blows up (Ex 5.1 Q3(b), f = 1/(x − 5)).</p>',
          'Three types of discontinuity',
          'Continuous at c iff left limit = right limit = f(c); removable (limit exists, differs from f(c)), jump (one-sided limits differ), infinite (no limit)',
          vb='0 0 300 160', hint='Where does the graph break: a hole, a gap, or a blow-up?')


def sawtooth_fractional(deck):
    P = Plane(-2.6, 3.6, -0.6, 1.7, 300, 170, (16, 10, 10, 20))
    xt = [(v, str(v).replace('-', '−')) for v in (-2, -1, 1, 2, 3)]
    base = P.axes(xt, [(1, '1')], grid=True)
    back = ''
    for n in range(-3, 4):
        x0, x1 = n, n + 1
        if x1 < -2.6 or x0 > 3.6: continue
        a, bb = max(x0, -2.6), min(x1, 3.6)
        back += P.curve(lambda x, n=n: x - n, 'c1 fx d2', a, bb, n=40)
        if x0 >= -2.6: back += P.dot(x0, 0, 'd1s', 3.8, 'fx d2')
        if x1 <= 3.6: back += P.hole(x1, 1, 'c1', 3.8).replace('class="f0 c1 "', 'class="f0 c1 fx d3"')
    mcard(deck, 'Ex 5.1 Q19 · g(x) = x − [x]', 'Sketch g(x) = x − [x] (the fractional part). Where is it continuous?', base, back,
          '<p>On each interval [n, n + 1) we have [x] = n, so g(x) = x − n: a slope-1 segment from height 0 up to (but not reaching) 1, then it drops back to 0.</p>'
          '<p>At every integer n: left limit = <b>1</b>, right limit = g(n) = <b>0</b>. So g is <b>discontinuous at all integers</b> and continuous elsewhere. The sawtooth has period 1.</p>',
          'Fractional part function x − [x] is discontinuous at integers',
          'g(x) = x - [x] has left limit 1 and right limit 0 at each integer: discontinuous at all integers, continuous elsewhere; period 1 sawtooth',
          vb='0 0 300 170', hint='Work out g on [0, 1), then repeat.')


def smooth_vs_corner(deck):
    def wrap(P, o, body):
        return f'<g transform="translate({o[0]},{o[1]})">{P.axes(labels=False)}{body}</g>'
    Pa, oa = _mini(2, 6, (-2, 2), (-0.5, 3))
    a = wrap(Pa, oa, Pa.curve(lambda x: 0.75 * x * x, 'c1', -2, 2, clip=(-0.5, 3)))
    Pb, ob = _mini(102, 6, (-1, 3), (-0.5, 2.5))
    b = wrap(Pb, ob, Pb.curve(lambda x: abs(x - 1), 'c1', -1, 3))
    Pc, oc = _mini(202, 6, (-2, 2), (-1.6, 1.6))
    c = wrap(Pc, oc, Pc.curve(lambda x: math.copysign(abs(x) ** (1 / 3), x), 'c1', -2, 2, n=200))
    base = a + b + c + ''.join(f'<text class="lbi" x="{x}" y="116" text-anchor="middle">({l})</text>' for x, l in [(50, 'a'), (150, 'b'), (250, 'c')])
    # tangent hints on the back
    back = (f'<g transform="translate({oa[0]},{oa[1]})">' + Pa.line(-1, 0, 1, 0, 'c3 fx d2').replace('<line ', '<line ') + '</g>'
            + f'<g transform="translate({ob[0]},{ob[1]})">' + Pb.line(0.2, 1.8, 1, 1, 'c2 fx d2') + Pb.line(1, 1, 1.8, 1.8, 'c4 fx d2') + '</g>'
            + f'<g transform="translate({oc[0]},{oc[1]})">' + Pc.line(0, -1.6, 0, 1.6, 'c2 fx d2') + '</g>')
    back += ('<text class="t3 fx d2" x="50" y="132" text-anchor="middle">differentiable</text><text class="sm fx d2" x="50" y="146" text-anchor="middle">one tangent</text>'
             '<text class="t2 fx d3" x="150" y="132" text-anchor="middle">corner at x = 1</text><text class="sm fx d3" x="150" y="146" text-anchor="middle">LHD −1, RHD +1</text>'
             '<text class="t4 fx d4" x="250" y="132" text-anchor="middle">vertical tangent</text><text class="sm fx d4" x="250" y="146" text-anchor="middle">slope → ∞</text>')
    mcard(deck, 'Differentiable or not?', 'Which of these graphs is differentiable everywhere shown? Where does it fail, and why?', base, back,
          '<p>Differentiable at c means the <b>tangent exists</b> (and is not vertical): the left and right derivatives at c are equal and finite.</p>'
          '<p>(a) y = x² is smooth. (b) f(x) = |x − 1| has a <b>corner</b> at x = 1: LHD = −1, RHD = +1 (Ex 5.2 Q9). (c) y = ∛x has a <b>vertical tangent</b> at 0, where the derivative is infinite. All of these are still continuous.</p>',
          'Corners and vertical tangents are where derivatives fail',
          'Differentiable at c iff left derivative = right derivative (finite): corner (|x-1| at 1) and vertical tangent (cube root at 0) are not differentiable though continuous',
          vb='0 0 300 160', hint='Can you draw one unique non-vertical tangent everywhere?')


def diff_implies_cont(deck):
    def ell(cx, cy, rx, ry):
        return f'M{cx - rx},{cy} a{rx},{ry} 0 1,0 {2 * rx},0 a{rx},{ry} 0 1,0 {-2 * rx},0 Z'
    base = ('<ellipse class="f0" cx="150" cy="96" rx="140" ry="88"></ellipse><ellipse class="f0" cx="150" cy="112" rx="108" ry="62"></ellipse><ellipse class="f0" cx="150" cy="128" rx="68" ry="32"></ellipse>'
            '<text class="lbl" x="150" y="22" text-anchor="middle">all functions</text><text class="lbl" x="150" y="64" text-anchor="middle">continuous</text><text class="lbl" x="150" y="112" text-anchor="middle">differentiable</text>')
    back = (f'<path class="ns1 fx d2" d="{ell(150, 128, 68, 32)}"></path>'
            f'<path class="ns4 fx d3" d="{ell(150, 112, 108, 62)} {ell(150, 128, 68, 32)}" fill-rule="evenodd"></path>'
            '<text class="t1 fx d2" x="150" y="138" text-anchor="middle">x², sin x, eˣ</text><text class="t4 fx d3" x="150" y="84" text-anchor="middle">|x| at 0, ∛x at 0</text>'
            '<text class="sm fx d4" x="150" y="196" text-anchor="middle">differentiable ⇒ continuous, not the converse</text>')
    mcard(deck, 'Theorem 3', 'How are “differentiable at c” and “continuous at c” related? Give an example that separates them.', base, back,
          '<p><b>Differentiable ⇒ continuous.</b> If f′(c) exists then f(x) − f(c) = [(f(x) − f(c))/(x − c)]·(x − c) → f′(c)·0 = 0, so f(x) → f(c).</p>'
          '<p><b>The converse is false:</b> f(x) = |x| is continuous at 0 but has a corner there, so it is not differentiable. Hence: not continuous ⇒ not differentiable.</p>',
          'Differentiable implies continuous (not conversely)',
          'If f is differentiable at c then f is continuous at c (Theorem 3); converse false, e.g. |x| at 0; discontinuous implies not differentiable',
          vb='0 0 300 206', hint='Which set sits inside which?')


def exp_slope_equals_height(deck):
    P = Plane(-2.6, 2.4, -1, 8.5, 300, 190, (16, 10, 10, 20))
    base = P.axes([(v, str(v).replace('-', '−')) for v in (-2, -1, 1, 2)], [(2, '2'), (4, '4'), (6, '6'), (8, '8')], grid=True) + P.curve(math.exp, 'c1', -2.6, 2.1, clip=(-1, 8.5))
    back = ''
    for k, x in enumerate([-1, 0, 1, 2]):
        y = math.exp(x)
        dx = 0.55 if x < 2 else 0.35
        back += P.line(x - dx, y - y * dx, x + dx, y + y * dx, 'c2 fx d' + str(k + 2)) + P.dot(x, y, 'd2s', 4, 'fx d' + str(k + 2))
        back += P.text(-2.5, 8.1 - k * 0.85, f'x = {x}: slope {y:.2f}'.replace('-', '−'), 't2 fx d' + str(k + 2))
    mcard(deck, 'Slope of eˣ', 'At each point of y = eˣ, compare the slope of the tangent with the height of the curve. What do you notice?', base, back,
          '<p>At x = 0 the height is 1 and the slope is 1; at x = 1 the height is e ≈ 2.72 and so is the slope; at x = 2, both are e² ≈ 7.39.</p>'
          '<p><b>d/dx (eˣ) = eˣ</b>: the slope equals the height everywhere. That is why eˣ is the only function (up to a constant multiple) that equals its own derivative, and why it models growth proportional to size.</p>',
          'The exponential function equals its own derivative',
          'd/dx e^x = e^x: the slope of y = e^x at any point equals its height; e^x is its own derivative; d/dx a^x = a^x log a',
          vb='0 0 300 190', hint='Read the height, then the steepness.')


def cycloid_parametric(deck):
    a = 1.0
    P, h = eqplane(-1.3, 6.9, -0.3, 2.5, pad=(10, 6, 6, 10))
    ox = P.X(0)
    curve_pts = ' '.join(f'{P.X(a * (t - math.sin(t))):.1f},{P.Y(a * (1 - math.cos(t))):.1f}' for t in [i * 2 * math.pi / 100 for i in range(101)])
    base = P.axes(labels=False) + f'<circle class="c0" cx="{P.X(0):.1f}" cy="{P.Y(1):.1f}" r="{P.X(1) - P.X(0):.1f}"></circle><circle class="d2s" cx="{P.X(0):.1f}" cy="{P.Y(0):.1f}" r="4"></circle>'
    back = f'<polyline class="c2 draw" pathLength="100" points="{curve_pts}"></polyline>'
    # moving rolling circle + tracer
    n = 40
    ctr = [(P.X(a * t) - P.X(0), 0) for t in [i * 2 * math.pi / n for i in range(n + 1)]]
    tr = [(P.X(a * (t - math.sin(t))) - P.X(0), P.Y(a * (1 - math.cos(t))) - P.Y(0)) for t in [i * 2 * math.pi / n for i in range(n + 1)]]
    css = (mkeyframes('rc', ctr, 6, 'linear', 0.3) + mkeyframes('rt', tr, 6, 'linear', 0.3))
    back += (f'<g class="rc"><circle class="c1" cx="{P.X(0):.1f}" cy="{P.Y(1):.1f}" r="{P.X(1) - P.X(0):.1f}"></circle></g>'
             f'<g class="rt"><circle class="d2s" cx="{P.X(0):.1f}" cy="{P.Y(0):.1f}" r="4.5"></circle></g>')
    mcard(deck, 'Parametric derivative · cycloid', 'A point on a rolling circle traces x = a(θ − sin θ), y = a(1 − cos θ). Find dy/dx.', base, back,
          '<p>dx/dθ = a(1 − cos θ) and dy/dθ = a sin θ, so <b>dy/dx = (dy/dθ)/(dx/dθ) = sin θ/(1 − cos θ) = cot(θ/2)</b>.</p>'
          '<p>Parametric rule: <b>dy/dx = (dy/dt)/(dx/dt)</b>, provided dx/dt ≠ 0. (Ex 5.6 Q6 uses y = a(1 + cos θ), which gives −cot(θ/2).) At θ = 0 the denominator vanishes: the cusp where the curve touches the ground.</p>',
          'Derivative of a parametric curve: dy/dx = (dy/dt)/(dx/dt)',
          'Parametric: dy/dx = (dy/dt)/(dx/dt); cycloid x=a(t-sin t), y=a(1-cos t) gives dy/dx = cot(t/2); Ex 5.6 Q6 variant y=a(1+cos t) gives -cot(t/2)',
          css=css, vb=f'0 0 300 {h}', hint='Differentiate x and y with respect to θ first.')


# ================================================================ Maths 12 Ch 6 Applications of derivatives
def rate_area_ring(deck):
    P, h = eqplane(-4.6, 4.6, -3.6, 3.6, pad=(8, 8, 8, 8))
    ox, oy = P.X(0), P.Y(0)
    u = P.X(1) - ox
    r1, r2 = 2.0, 2.45
    base = (P.axes(labels=False) + f'<circle class="c1" cx="{ox:.1f}" cy="{oy:.1f}" r="{r1 * u:.1f}"></circle>'
            + P.line(0, 0, r1, 0, 'c0') + P.text(1.0, 0, 'r', 'lbi', dy=-6, anchor='middle'))
    ring = f'M{ox - r2 * u:.1f},{oy:.1f} a{r2 * u:.1f},{r2 * u:.1f} 0 1,0 {2 * r2 * u:.1f},0 a{r2 * u:.1f},{r2 * u:.1f} 0 1,0 {-2 * r2 * u:.1f},0 Z M{ox - r1 * u:.1f},{oy:.1f} a{r1 * u:.1f},{r1 * u:.1f} 0 1,0 {2 * r1 * u:.1f},0 a{r1 * u:.1f},{r1 * u:.1f} 0 1,0 {-2 * r1 * u:.1f},0 Z'
    back = (f'<path class="ns4 fx d2" d="{ring}" fill-rule="evenodd"></path>' + f'<circle class="c4 fx d2" cx="{ox:.1f}" cy="{oy:.1f}" r="{r2 * u:.1f}"></circle>'
            + P.text(0, 2.9, 'ring area ≈ 2πr · Δr', 't4 fx d3', anchor='middle') + P.text(0, -3.05, 'dA/dr = 2πr', 't1 fx d4', anchor='middle'))
    mcard(deck, 'Rate of change', 'The radius of a circle grows. Why is dA/dr = 2πr? Picture the extra area when r increases by a little.', base, back,
          '<p>When r grows by Δr, the new area is a thin ring of length 2πr (the circumference) and width Δr, so ΔA ≈ 2πr · Δr and <b>dA/dr = 2πr</b>. Ex 6.1 Q1: at r = 3 the rate is 6π cm²/cm, at r = 4 it is 8π cm²/cm.</p>'
          '<p>In a related-rates problem the radius changes with time, so <b>dA/dt = 2πr · dr/dt</b> (chain rule): with r = 10 and dr/dt = 3 cm/s, dA/dt = 60π cm²/s (Q3).</p>',
          'dA/dr = 2πr and dA/dt = 2πr dr/dt',
          'A = pi r^2 gives dA/dr = 2 pi r (circumference); with time: dA/dt = 2 pi r dr/dt; related rates use the chain rule; derivative = rate of change',
          vb=f'0 0 300 {h}', hint='Draw r and r + Δr.')


def ladder_frames(deck):
    P, h = eqplane(-0.6, 5.8, -0.6, 5.8, pad=(10, 6, 6, 10))
    base = P.axes(labels=False) + f'<polygon class="f0" points="{P.X(-0.6):.1f},{P.Y(-0.6):.1f} {P.X(0):.1f},{P.Y(-0.6):.1f} {P.X(0):.1f},{P.Y(5.8):.1f} {P.X(-0.6):.1f},{P.Y(5.8):.1f}"></polygon>'
    base += P.line(3, 4, 0, 0, 'c0') if False else ''
    xs = [1.5, 3.0, 4.0, 4.6]
    base += P.line(4.0, 0, 0, 3.0, 'c1') + P.dot(4.0, 0, 'd1s', 4) + P.dot(0, 3.0, 'd1s', 4)
    back = ''
    for k, x in enumerate([1.5, 3.0, 4.6, 4.9]):
        y = math.sqrt(25 - x * x)
        back += P.line(x, 0, 0, y, 'guide fx d' + str(k + 2))
    back += (P.text(4.0, 0, 'x = 4', 't1 fx d2', anchor='middle', dy=16) + P.text(0, 3.0, 'y = 3', 't1 fx d2', dx=8, dy=4)
             + P.text(2.6, 4.8, 'x² + y² = 25', 't4 fx d3', anchor='middle'))
    mcard(deck, 'Related rates · ladder', 'A 5 m ladder slides away from a wall at 2 cm/s. How fast is its top sliding down when the foot is 4 m from the wall?', base, back,
          '<p>x² + y² = 25. Differentiate with respect to t: <b>2x dx/dt + 2y dy/dt = 0</b>, so dy/dt = −(x/y) dx/dt. With x = 4, y = 3, dx/dt = 2: dy/dt = −(4/3)·2 = <b>−8/3 cm/s</b>; the top slides down at 8/3 cm/s (Ex 6.1 Q10).</p>'
          '<p>Steps: relate the variables, differentiate w.r.t. time, substitute the instant values.</p>',
          'Related rates: differentiate the constraint with respect to time',
          'Ladder 5: x^2 + y^2 = 25 gives x dx/dt + y dy/dt = 0; at x=4, y=3, dx/dt=2: dy/dt = -8/3 cm/s; related rates: relate, differentiate w.r.t. t, substitute',
          vb=f'0 0 300 {h}', hint='Write the relation between x and y first.')


def sign_strip_cubic(deck):
    P = Plane(-2.6, 2.6, -3.2, 3.6, 300, 190, (14, 8, 30, 20))
    f = lambda x: x ** 3 - 3 * x
    base = P.axes([(-1, '−1'), (1, '1')], [(2, '2'), (-2, '−2')], grid=True, labels=False) + P.curve(f, 'c0', -2.4, 2.4, clip=(-3.2, 3.6))
    y0 = P.Y(-3.2) + 14
    back = (P.curve(f, 'c3 fx d2', -2.4, -1, clip=(-3.2, 3.6)) + P.curve(f, 'c2 fx d3', -1, 1, clip=(-3.2, 3.6)) + P.curve(f, 'c3 fx d4', 1, 2.4, clip=(-3.2, 3.6))
            + P.dot(-1, 2, 'd1s', 4.8, 'fx d3') + P.dot(1, -2, 'd1s', 4.8, 'fx d4')
            + P.text(-1, 2, 'local max', 't1 fx d3', dx=6, dy=-8) + P.text(1, -2, 'local min', 't1 fx d4', dx=-6, dy=16, anchor='end')
            + '<text class="t3 fx d2" x="%.1f" y="%.1f" text-anchor="middle">f′ +</text>' % (P.X(-1.9), P.Y(3.3))
            + '<text class="t2 fx d3" x="%.1f" y="%.1f" text-anchor="middle">f′ −</text>' % (P.X(0), P.Y(3.3))
            + '<text class="t3 fx d4" x="%.1f" y="%.1f" text-anchor="middle">f′ +</text>' % (P.X(1.9), P.Y(3.3)))
    mcard(deck, 'First derivative test', 'f(x) = x³ − 3x. Where is it increasing and where decreasing? Where are its local maximum and minimum?', base, back,
          '<p>f′(x) = 3x² − 3 = 3(x − 1)(x + 1). <b>f′ &gt; 0</b> on (−∞, −1) and (1, ∞): increasing. <b>f′ &lt; 0</b> on (−1, 1): decreasing.</p>'
          '<p><b>First derivative test:</b> where f′ changes from + to −, there is a <b>local maximum</b> (x = −1, value 2); from − to +, a <b>local minimum</b> (x = 1, value −2). No sign change ⇒ neither (a point of inflexion).</p>',
          'First derivative test: sign change of f′',
          'f increasing where f\'>0, decreasing where f\'<0; f\' changes + to - at a local max, - to + at a local min; f = x^3 - 3x has local max 2 at x=-1 and local min -2 at x=1',
          vb='0 0 300 190', hint='Find f′ and check its sign on each interval.')


def concavity_second_test(deck):
    def cell(ox, fn, rng, yr, lab, cls):
        P = Plane(rng[0], rng[1], yr[0], yr[1], 100, 100, (6, 6, 6, 6))
        return f'<g transform="translate({ox},6)">{P.axes(labels=False)}{P.curve(fn, cls, rng[0], rng[1], clip=yr)}{P.dot(0, fn(0), "d1s", 4)}</g>'
    a = cell(0, lambda x: x * x, (-1.5, 1.5), (-0.4, 2.4), 'min', 'c1')
    bb = cell(100, lambda x: -x * x, (-1.5, 1.5), (-2.4, 0.4), 'max', 'c1')
    c = cell(200, lambda x: x ** 3, (-1.3, 1.3), (-2.4, 2.4), 'flat', 'c1')
    base = a + bb + c + ''.join(f'<text class="lbi" x="{x}" y="118" text-anchor="middle">({l})</text>' for x, l in [(50, 'a'), (150, 'b'), (250, 'c')])
    back = ('<text class="t3 fx d2" x="50" y="134" text-anchor="middle">f″ = 2 &gt; 0</text><text class="sm fx d2" x="50" y="148" text-anchor="middle">local min</text>'
            '<text class="t2 fx d3" x="150" y="134" text-anchor="middle">f″ = −2 &lt; 0</text><text class="sm fx d3" x="150" y="148" text-anchor="middle">local max</text>'
            '<text class="t4 fx d4" x="250" y="134" text-anchor="middle">f″(0) = 0</text><text class="sm fx d4" x="250" y="148" text-anchor="middle">test fails</text>')
    mcard(deck, 'Second derivative test', 'At x = 0 all three curves have f′(0) = 0. Use f″ to classify (a) x², (b) −x², (c) x³.', base, back,
          '<p><b>Second derivative test:</b> if f′(c) = 0 and <b>f″(c) &gt; 0</b>, c is a local <b>minimum</b> (curve is a cup, concave up); if <b>f″(c) &lt; 0</b>, a local <b>maximum</b> (concave down).</p>'
          '<p>If f″(c) = 0 the test is <b>inconclusive</b>: x³ has f″(0) = 0 and no extremum, while x⁴ has f″(0) = 0 but a minimum. Then go back to the sign of f′.</p>',
          'Second derivative test and when it fails',
          'f\'(c)=0 and f\'\'(c)>0 gives local minimum, f\'\'(c)<0 local maximum, f\'\'(c)=0 inconclusive (x^3, x^4); use first derivative test',
          vb='0 0 300 160', hint='Sign of f″ tells you whether the curve bends up or down.')


def box_volume_opt(deck):
    P = Plane(0, 9.6, -20, 470, 190, 190, (22, 12, 8, 22))
    V = lambda x: x * (18 - 2 * x) ** 2
    left = ('<rect class="f0" x="10" y="48" width="84" height="84" rx="2"></rect>'
            '<rect class="f2" x="10" y="48" width="18" height="18"></rect><rect class="f2" x="76" y="48" width="18" height="18"></rect><rect class="f2" x="10" y="114" width="18" height="18"></rect><rect class="f2" x="76" y="114" width="18" height="18"></rect>'
            '<text class="lbl" x="52" y="150" text-anchor="middle">18 cm sheet</text><text class="t2" x="19" y="44" text-anchor="middle">x</text>')
    gr = f'<g transform="translate(106,0)">{P.axes([(3, "3"), (6, "6"), (9, "9")], [(200, "200"), (400, "400")], grid=True, labels=False)}{P.curve(V, "c1", 0, 9)}</g>'
    base = left + gr
    back = (f'<g transform="translate(106,0)">{P.dot(3, 432, "d2s", 5, "fx d2")}{P.line(3, 0, 3, 432, "guide fx d2")}'
            f'{P.text(3, 432, "max: x = 3, V = 432", "t2 fx d3", dx=8, dy=-4)}</g>')
    mcard(deck, 'Optimisation · open box', 'Squares of side x are cut from the corners of an 18 cm square tin sheet and the flaps folded up. Which x gives the maximum volume?', base, back,
          '<p>V(x) = x(18 − 2x)². <b>V′(x) = (18 − 2x)(18 − 6x) = 0</b> gives x = 9 (no box) or x = 3. V″(x) = 24x − 144 &lt; 0 at x = 3: a <b>maximum</b>, V = 3 · 12² = 432 cm³ (Ex 6.3 Q17).</p>'
          '<p>Method: 1) write the quantity in one variable, 2) set the derivative to 0, 3) verify max/min (second derivative or end-points), 4) answer with units.</p>',
          'Maximum volume of an open box from a square sheet',
          'V = x(18-2x)^2, V\' = (18-2x)(18-6x) = 0 gives x = 3, V\'\' < 0, maximum V = 432 cm^3; optimisation: one variable, derivative zero, verify, answer',
          vb='0 0 300 190', hint='Write V in terms of x, then find where V′ = 0.')


def closed_interval_extrema(deck):
    P = Plane(-2.8, 5.2, -12, 10, 300, 190, (16, 8, 10, 20))
    f = lambda x: 4 * x - x * x / 2
    base = P.axes([(-2, '−2'), (2, '2'), (4, '4')], [(-10, '−10'), (-5, '−5'), (5, '5')], grid=True, labels=False) + P.curve(f, 'c1', -2, 4.5, clip=(-12, 10))
    base += P.dot(-2, f(-2), 'd1s', 4.5) + P.dot(4.5, f(4.5), 'd1s', 4.5)
    back = (P.dot(4, 8, 'd2s', 5.5, 'fx d2') + P.text(4, 8, 'max 8', 't2 fx d2', dx=-6, dy=-8, anchor='end') + P.text(-2, f(-2), 'min −10', 't1 fx d3', dx=8, dy=4)
            + P.text(4.5, f(4.5), '7.875', 'sm fx d3', dx=-6, dy=16, anchor='end')
            + P.line(-2, -12, -2, 8, 'guide fx d3') + P.line(4.5, -12, 4.5, 8, 'guide fx d3'))
    mcard(deck, 'Absolute extrema on [a, b]', 'Find the absolute maximum and minimum of f(x) = 4x − x²/2 on [−2, 9/2].', base, back,
          '<p>On a closed interval, the extremes occur at <b>critical points or end-points</b>. f′(x) = 4 − x = 0 at x = 4: f(4) = 8. End-points: f(−2) = −10, f(9/2) = 7.875.</p>'
          '<p>Compare: <b>absolute maximum 8 (at x = 4)</b> and <b>absolute minimum −10 (at x = −2)</b>. (Ex 6.3 Q5(iii).) A continuous function on [a, b] always attains both.</p>',
          'Absolute extrema: compare critical points and end-points',
          'On [a,b] absolute max/min occur at critical points or end-points: f=4x-x^2/2 on [-2,9/2]: f(4)=8 max, f(-2)=-10 min, f(9/2)=7.875',
          vb='0 0 300 190', hint='Check the critical point and both ends.')


def nearest_point_circle(deck):
    P, h = eqplane(-4.6, 4.6, -0.8, 6.6, pad=(8, 8, 8, 8))
    ox = P.X(0)
    base = P.axes(labels=False) + P.curve(lambda x: x * x / 2, 'c1', -3.4, 3.4, clip=(-0.8, 6.6)) + P.dot(0, 5, 'd2s', 4.5) + P.text(0, 5, '(0, 5)', 't2', dx=8, dy=-6)
    r = 3.0
    back = (f'<circle class="c2 fx d2" cx="{ox:.1f}" cy="{P.Y(5):.1f}" r="{r * (P.X(1) - ox):.1f}"></circle>'
            + P.dot(2 * math.sqrt(2), 4, 'd1s', 5, 'fx d3') + P.dot(-2 * math.sqrt(2), 4, 'd1s', 5, 'fx d3')
            + P.line(0, 5, 2 * math.sqrt(2), 4, 'guide fx d3') + P.text(2 * math.sqrt(2), 4, '(2√2, 4)', 't1 fx d3', dx=6, dy=16)
            + P.text(0.9, 4.75, '3', 't2 fx d3', anchor='middle'))
    mcard(deck, 'Nearest point on a curve', 'Find the point on the parabola x² = 2y that is nearest to (0, 5).', base, back,
          '<p>Minimise the squared distance D = x² + (y − 5)² with x² = 2y: D = y² − 8y + 25 (y ≥ 0). D′ = 2y − 8 = 0 gives <b>y = 4</b>, x = ±2√2, D = 9 so the least distance is 3.</p>'
          '<p>Geometrically the circle centred at (0, 5) with radius 3 just <b>touches</b> the parabola: the nearest point is where the circle is tangent, and the line to the centre is the normal (Ex 6.3 Q27: (A) (2√2, 4)).</p>',
          'Nearest point: shrink a circle until it touches the curve',
          'Minimise squared distance x^2+(y-5)^2 on x^2=2y: y=4, x=+-2sqrt2, distance 3; circle centered at the point touches the parabola at the nearest point',
          vb=f'0 0 300 {h}', hint='Write the squared distance as a function of y.')


# ================================================================ Maths 12 Ch 7 Integrals
def area_function_strips(deck):
    P = Plane(-0.4, 4.6, -0.5, 4.4, 300, 190, (16, 8, 10, 18))
    f = lambda x: 0.35 * x * x + 0.6
    a, xe = 0.5, 3.4
    base = P.axes([(a, 'a'), (xe, 'x')], [], grid=False, labels=False) + P.curve(f, 'c1', 0, 4.4, clip=(-0.5, 4.4)) + P.text(4.3, f(4.3), 'y = f(t)', 't1', anchor='end', dy=-8)
    n = 14
    w = (xe - a) / n
    css = ''.join(f'.pp .q{k}{{animation-delay:{0.3 + 0.22 * k:.2f}s}}' for k in range(n))
    strips = ''.join(f'<polygon class="f4 fx q{k}" points="{P.X(a + k * w):.1f},{P.Y(0):.1f} {P.X(a + k * w):.1f},{P.Y(f(a + k * w)):.1f} {P.X(a + (k + 1) * w):.1f},{P.Y(f(a + (k + 1) * w)):.1f} {P.X(a + (k + 1) * w):.1f},{P.Y(0):.1f}"></polygon>' for k in range(n))
    back = strips + P.text(0.1, 4.05, 'A(x) = ∫ₐˣ f(t) dt', 't4 fx d5') + P.dot(xe, f(xe), 'd2s', 4.5, 'fx d5') + P.text(xe, f(xe), 'height f(x)', 't2 fx d5', dx=-8, dy=12, anchor='end')
    mcard(deck, 'Area function', 'Let A(x) be the area under y = f(t) from t = a to t = x. How fast does A(x) change as x increases?', base, back,
          '<p>Adding a thin strip of width Δx at x adds area ≈ f(x)·Δx, so <b>A′(x) = f(x)</b>: this is the <b>first fundamental theorem of calculus</b> (f continuous). The rate at which the area grows equals the height of the curve.</p>'
          '<p>Hence A is an antiderivative of f, and the definite integral is F(b) − F(a) for any antiderivative F (<b>second fundamental theorem</b>).</p>',
          'First fundamental theorem: derivative of the area function',
          'If A(x) = integral from a to x of f(t) dt with f continuous then A\'(x) = f(x); then integral from a to b of f = F(b) - F(a) for an antiderivative F (second fundamental theorem)',
          css=css, vb='0 0 300 190', hint='Add a thin strip and see how much area it brings.')


def riemann_refine(deck):
    P = Plane(-0.3, 2.4, -0.4, 4.6, 300, 190, (16, 8, 10, 18))
    f = lambda x: x * x
    base = P.axes([(1, '1'), (2, '2')], [(2, '2'), (4, '4')], grid=False, labels=False) + P.curve(f, 'c1', 0, 2.2, clip=(-0.4, 4.6))
    def rects(n, cls, extra):
        w = 2.0 / n
        return ''.join(f'<polygon class="{cls} {extra}" points="{P.X(k * w):.1f},{P.Y(0):.1f} {P.X(k * w):.1f},{P.Y(f((k + 1) * w)):.1f} {P.X((k + 1) * w):.1f},{P.Y(f((k + 1) * w)):.1f} {P.X((k + 1) * w):.1f},{P.Y(0):.1f}"></polygon>' for k in range(n))
    back = (rects(4, 'f2', 'fx d2') + rects(8, 'ns4', 'fx d3') + rects(16, 'ns3', 'fx d4')
            + '<text class="t2 fx d2" x="70" y="34">n = 4: 3.75</text><text class="t4 fx d3" x="70" y="50">n = 8: 3.19</text><text class="t3 fx d4" x="70" y="66">n = 16: 2.92</text><text class="t1 fx d5" x="70" y="86">n → ∞: 8/3 ≈ 2.67</text>')
    mcard(deck, 'Definite integral as a limit', 'Approximate the area under y = x² from 0 to 2 by n right-hand rectangles. What happens as n grows?', base, back,
          '<p>Right-endpoint sums: n = 4 gives 3.75, n = 8 gives 3.1875, n = 16 gives 2.9219. They are always too big (x² is increasing) but decrease towards <b>∫₀² x² dx = 8/3</b>.</p>'
          '<p><b>∫ₐᵇ f(x) dx = lim n→∞ Σ f(xᵢ)Δx</b> with Δx = (b − a)/n. By the second fundamental theorem you never need the limit: [x³/3]₀² = 8/3.</p>',
          'Definite integral as the limit of a Riemann sum',
          'Integral of f from a to b is the limit of sums f(x_i) Delta x as n -> infinity; right sums for x^2 on [0,2]: 3.75, 3.19, 2.92 -> 8/3',
          vb='0 0 300 190', hint='Make the rectangles thinner.')


def signed_area_sine(deck):
    P = Plane(-0.4, 6.9, -1.5, 1.6, 300, 170, (16, 8, 10, 18))
    base = P.axes([(math.pi, 'π'), (2 * math.pi, '2π')], [(1, '1'), (-1, '−1')], grid=True, labels=False) + P.curve(math.sin, 'c1', 0, 2 * math.pi, n=200)
    pos = [(0, 0)] + [(t, math.sin(t)) for t in [i * math.pi / 30 for i in range(31)]] + [(math.pi, 0)]
    neg = [(math.pi, 0)] + [(math.pi + t, math.sin(math.pi + t)) for t in [i * math.pi / 30 for i in range(31)]] + [(2 * math.pi, 0)]
    back = (P.poly(pos, 'f3 fx d2') + P.poly(neg, 'f2 fx d3') + P.text(1.6, 0.4, '+2', 't3 fx d2', anchor='middle') + P.text(4.7, -0.4, '−2', 't2 fx d3', anchor='middle')
            + P.text(3.5, 1.3, '∫ = 0, but area = 4', 't4 fx d4', anchor='middle'))
    mcard(deck, 'Signed area', 'Find ∫₀^(2π) sin x dx, and the total area between the curve and the x-axis on [0, 2π].', base, back,
          '<p>Areas above the axis count <b>positive</b>, below the axis <b>negative</b>: ∫₀^π sin x dx = 2 and ∫_π^(2π) sin x dx = −2, so <b>∫₀^(2π) sin x dx = 0</b>.</p>'
          '<p>The <b>area</b> (always positive) is 2 + 2 = <b>4</b>: split at the zeros and take absolute values. (Same for Ex 7.10 Q5, Q6: |x + 2|, |x − 5|.)</p>',
          'Signed area versus total area',
          'Definite integral counts area below the x-axis as negative; integral of sin from 0 to 2pi = 0 but the area is 4; split at zeros and use absolute values for area',
          vb='0 0 300 170', hint='Which parts lie below the axis?')


def even_odd_integrals(deck):
    def panel(ox, fn, rng, yr, cls_pos, cls_neg):
        P = Plane(rng[0], rng[1], yr[0], yr[1], 140, 110, (6, 6, 6, 6))
        return P, ox
    Pe = Plane(-1.7, 1.7, -0.3, 3.0, 140, 110, (6, 6, 6, 6))
    Po = Plane(-1.7, 1.7, -3.2, 3.2, 140, 110, (6, 6, 6, 6))
    def rng_pts(fn, a, b, n=30):
        return [(a, 0)] + [(a + (b - a) * i / n, fn(a + (b - a) * i / n)) for i in range(n + 1)] + [(b, 0)]
    left = f'<g transform="translate(4,10)">{Pe.axes(labels=False)}{Pe.curve(lambda x: x * x, "c1", -1.6, 1.6, clip=(-0.3, 3))}</g>'
    right = f'<g transform="translate(156,10)">{Po.axes(labels=False)}{Po.curve(lambda x: x ** 3, "c1", -1.4, 1.4, clip=(-3.2, 3.2))}</g>'
    base = left + right + '<text class="lbi" x="74" y="132" text-anchor="middle">(a) even: x²</text><text class="lbi" x="226" y="132" text-anchor="middle">(b) odd: x³</text>'
    back = (f'<g transform="translate(4,10)">{Pe.poly(rng_pts(lambda x: x * x, -1.5, 0), "f1 fx d2")}{Pe.poly(rng_pts(lambda x: x * x, 0, 1.5), "f1 fx d2")}</g>'
            f'<g transform="translate(156,10)">{Po.poly(rng_pts(lambda x: x ** 3, 0, 1.3), "f3 fx d3")}{Po.poly(rng_pts(lambda x: x ** 3, -1.3, 0), "f2 fx d3")}</g>'
            '<text class="t1 fx d2" x="74" y="148" text-anchor="middle">∫ = 2 ∫₀ᵃ f</text><text class="t4 fx d3" x="226" y="148" text-anchor="middle">∫ = 0 (cancels)</text>')
    mcard(deck, 'Even and odd functions', 'Compare ∫_(−a)^(a) f(x) dx for an even function (like x²) and an odd function (like x³).', base, back,
          '<p><b>Even</b> (f(−x) = f(x)): the two halves are mirror images, so <b>∫_(−a)^(a) f = 2∫₀ᵃ f</b>. <b>Odd</b> (f(−x) = −f(x)): the halves have opposite signs and cancel: <b>∫_(−a)^(a) f = 0</b>.</p>'
          '<p>Use it before computing: Ex 7.10 Q13, Q14 and Q20 (∫_(−π/2)^(π/2)(x³ + x cos x + tan⁵x + 1) dx = π since only the constant 1 survives).</p>',
          'Integrals of even and odd functions over [−a, a]',
          'Even f: integral over [-a,a] = 2 * integral over [0,a]; odd f: integral over [-a,a] = 0; x^3 + x cos x + tan^5 x are odd so only 1 contributes: pi',
          vb='0 0 300 160', hint='Look at the symmetry of the graph about the y-axis.')


def king_property(deck):
    P = Plane(-0.2, 1.75, -0.1, 1.15, 300, 180, (16, 8, 10, 18))
    f = lambda x: math.sin(x) / (math.sin(x) + math.cos(x))
    g = lambda x: math.cos(x) / (math.sin(x) + math.cos(x))
    base = P.axes([(math.pi / 4, 'π/4'), (math.pi / 2, 'π/2')], [(0.5, '½'), (1, '1')], grid=False, labels=False) + P.curve(f, 'c1', 0, math.pi / 2, n=120)
    back = (P.curve(g, 'c2 fx d2', 0, math.pi / 2, n=120) + P.line(math.pi / 4, -0.1, math.pi / 4, 1.1, 'guide fx d3') + P.line(0, 0.5, math.pi / 2, 0.5, 'guide fx d3')
            + P.text(1.3, 0.95, 'f(x)', 't1 fx d2') + P.text(0.1, 0.95, 'f(π/2 − x)', 't2 fx d2')
            + P.text(math.pi / 4, 1.1, 'I = π/4', 't4 fx d4', anchor='middle', dx=0, dy=-2))
    mcard(deck, 'The a + b − x trick', 'Evaluate I = ∫₀^(π/2) sin x/(sin x + cos x) dx. What does the substitution x → π/2 − x do to the graph?', base, back,
          '<p><b>∫ₐᵇ f(x) dx = ∫ₐᵇ f(a + b − x) dx</b> (property P₄): it reflects the graph about x = (a + b)/2. Here f(π/2 − x) = cos x/(sin x + cos x), so <b>f(x) + f(π/2 − x) = 1</b>.</p>'
          '<p>Adding: 2I = ∫₀^(π/2) 1 dx = π/2, so <b>I = π/4</b> (Ex 7.10 Q2, Q3, Q4 all use this). The two curves are symmetric about x = π/4 and together fill a rectangle of height 1.</p>',
          'King property: ∫f(x) = ∫f(a + b − x)',
          'Property P4: integral of f(x) from a to b equals integral of f(a+b-x); for f = sin x/(sin x+cos x) on [0,pi/2], f(x)+f(pi/2-x)=1 so I = pi/4',
          vb='0 0 300 180', hint='Reflect the curve in x = π/4.')


# ================================================================ Maths 12 Ch 8 Application of integrals
def horizontal_strips_parabola(deck):
    P = Plane(-0.5, 4.6, -0.5, 4.2, 300, 190, (16, 8, 10, 18))
    f = lambda y: y * y / 4
    base = P.axes([(1, '1'), (2, '2'), (3, '3'), (4, '4')], [(1, '1'), (2, '2'), (3, '3')], grid=False, labels=False) + P.curve(lambda x: 2 * math.sqrt(x), 'c1', 0, 4, clip=(-0.5, 4.2)) + P.line(0, 3, 4, 3, 'c2')
    base += P.text(2.4, 3.05, 'y = 3', 't2', dy=-6) + P.text(2.9, 1.7, 'y² = 4x', 't1')
    n = 12
    hh = 3.0 / n
    css = ''.join(f'.pp .q{k}{{animation-delay:{0.3 + 0.2 * k:.2f}s}}' for k in range(n))
    strips = ''.join(f'<polygon class="f1 fx q{k}" points="{P.X(0):.1f},{P.Y(k * hh):.1f} {P.X(f(k * hh)):.1f},{P.Y(k * hh):.1f} {P.X(f((k + 1) * hh)):.1f},{P.Y((k + 1) * hh):.1f} {P.X(0):.1f},{P.Y((k + 1) * hh):.1f}"></polygon>' for k in range(n))
    back = strips + P.text(0.4, 0.4, 'A = ∫₀³ x dy = 9/4', 't1 fx d5')
    mcard(deck, 'Horizontal strips · Ex 8.1 Q4', 'Find the area bounded by y² = 4x, the y-axis and the line y = 3.', base, back,
          '<p>The boundary is easier to describe as <b>x in terms of y</b> (x = y²/4), so slice horizontally: A = ∫꜀ᵈ x dy = ∫₀³ (y²/4) dy = [y³/12]₀³ = <b>27/12 = 9/4</b> (option B).</p>'
          '<p>Rule: use vertical strips (∫ y dx) when the curve is y = f(x), and horizontal strips (∫ x dy) when it is x = g(y). Choosing the right one avoids square roots and splitting the region.</p>',
          'Area with horizontal strips: A = ∫ x dy',
          'Area bounded by x = g(y), y-axis and y = c, y = d is integral of g(y) dy; y^2 = 4x with y = 3 gives 9/4 using horizontal strips',
          css=css, vb='0 0 300 190', hint='Which variable makes the boundary a simple function?')


def ellipse_quarter(deck):
    P, h = eqplane(-4.8, 4.8, -3.6, 3.6, pad=(8, 8, 8, 8))
    ox, oy = P.X(0), P.Y(0)
    a, b = 4, 3
    pts = ' '.join(f'{P.X(a * math.cos(t)):.1f},{P.Y(b * math.sin(t)):.1f}' for t in [i * 2 * math.pi / 120 for i in range(121)])
    base = P.axes(labels=False) + f'<polyline class="c1" points="{pts}"></polyline>' + P.text(4, 0, 'a = 4', 't1', dy=14, anchor='middle') + P.text(0, 3, 'b = 3', 't1', dx=8, dy=4)
    q = [(0, 0)] + [(a * math.cos(t), b * math.sin(t)) for t in [i * (math.pi / 2) / 40 for i in range(41)]]
    back = P.poly(q, 'f4 fx d2') + P.text(1.5, 1.0, '¼ of the area', 't4 fx d2', anchor='middle') + P.text(0, -3.3, 'area = πab = 12π', 't2 fx d4', anchor='middle')
    mcard(deck, 'Ex 8.1 Q1 · area of an ellipse', 'Find the area bounded by the ellipse x²/16 + y²/9 = 1.', base, back,
          '<p>By symmetry the area is 4 × (area in the first quadrant). There y = (b/a)√(a² − x²): 4 ∫₀ᵃ (b/a)√(a² − x²) dx = (4b/a)[(x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a)]₀ᵃ = (4b/a)(a²/2)(π/2) = <b>πab</b>.</p>'
          '<p>Here a = 4, b = 3: <b>12π</b>. (Ex 8.1 Q2, x²/4 + y²/9 = 1: π · 2 · 3 = 6π.) A circle is the case a = b = r: πr².</p>',
          'Area of an ellipse is πab',
          'Area of x^2/a^2 + y^2/b^2 = 1 is pi a b: four times the first quadrant integral of (b/a) sqrt(a^2 - x^2); Ex 8.1: 16,9 gives 12 pi; 4,9 gives 6 pi; circle pi r^2',
          vb=f'0 0 300 {h}', hint='Use symmetry: compute one quadrant.')


def cos_area_sign(deck):
    P = Plane(-0.4, 6.9, -1.5, 1.6, 300, 170, (16, 8, 10, 18))
    base = P.axes([(math.pi / 2, 'π/2'), (math.pi, 'π'), (3 * math.pi / 2, '3π/2'), (2 * math.pi, '2π')], [(1, '1'), (-1, '−1')], grid=True, labels=False) + P.curve(math.cos, 'c1', 0, 2 * math.pi, n=200)
    def region(a, bb):
        return [(a, 0)] + [(a + (bb - a) * i / 30, math.cos(a + (bb - a) * i / 30)) for i in range(31)] + [(bb, 0)]
    back = (P.poly(region(0, math.pi / 2), 'f3 fx d2') + P.poly(region(math.pi / 2, 3 * math.pi / 2), 'f2 fx d3') + P.poly(region(3 * math.pi / 2, 2 * math.pi), 'f3 fx d4')
            + P.text(0.7, 0.35, '1', 't3 fx d2', anchor='middle') + P.text(math.pi, -0.5, '|−2| = 2', 't2 fx d3', anchor='middle') + P.text(5.5, 0.35, '1', 't3 fx d4', anchor='middle')
            + P.text(3.2, 1.3, 'total area 1 + 2 + 1 = 4', 't4 fx d4', anchor='middle'))
    mcard(deck, 'Example 4 · area of cos x', 'Find the area bounded by y = cos x, the x-axis, x = 0 and x = 2π.', base, back,
          '<p>cos x changes sign at π/2 and 3π/2, so split: ∫₀^(π/2) cos x = 1; |∫_(π/2)^(3π/2) cos x| = |−2| = 2; ∫_(3π/2)^(2π) cos x = 1. Area = <b>1 + 2 + 1 = 4</b>.</p>'
          '<p>Never write ∫₀^(2π) cos x dx = 0 as the area: that is the <b>signed</b> integral. For area, integrate |f| by splitting at the zeros.</p>',
          'Area when the curve crosses the x-axis: split and take absolute values',
          'Area of cos x from 0 to 2pi is 4 = 1+2+1; split at zeros pi/2, 3pi/2 and add absolute values; the integral alone is 0',
          vb='0 0 300 170', hint='Where does the curve cross the axis?')


def area_between_parabolas(deck):
    P, h = eqplane(-0.6, 4.8, -0.6, 4.8, pad=(12, 8, 8, 12))
    up = lambda x: 2 * math.sqrt(x)
    lo = lambda x: x * x / 4
    base = P.axes(labels=False) + P.curve(up, 'c1', 0, 4, clip=(-0.6, 4.8)) + P.curve(lo, 'c2', 0, 4, clip=(-0.6, 4.8)) + P.text(1.0, 2.3, 'y² = 4x', 't1', dx=-4, anchor='end') + P.text(3.3, 2.4, 'x² = 4y', 't2')
    xs = [i * 4 / 60 for i in range(61)]
    region = [(x, up(x)) for x in xs] + [(x, lo(x)) for x in reversed(xs)]
    back = P.poly(region, 'f4 fx d2') + P.dot(4, 4, 'd0s', 4, 'fx d3') + P.text(4, 4, '(4, 4)', 'lbl fx d3', dx=-6, dy=-6, anchor='end') + P.text(1.8, 1.3, 'A = 16/3', 't4 fx d4', anchor='middle')
    mcard(deck, 'Area between two curves', 'Find the area enclosed between the parabolas y² = 4x and x² = 4y.', base, back,
          '<p>Intersections: y = x²/4 into y² = 4x gives x⁴/16 = 4x, so x = 0 or 4: points (0, 0) and (4, 4).</p>'
          '<p>Area = ∫₀⁴ (top − bottom) dx = ∫₀⁴ (2√x − x²/4) dx = [(4/3)x^(3/2) − x³/12]₀⁴ = 32/3 − 16/3 = <b>16/3</b>. In general the area between y² = 4ax and x² = 4ay is 16a²/3.</p>',
          'Area between curves = ∫ (upper − lower) dx',
          'Area between two curves = integral of (upper - lower) between intersection points; y^2 = 4x and x^2 = 4y meet at (0,0),(4,4) with area 16/3 (16a^2/3 in general)',
          vb=f'0 0 300 {h}', hint='Find the intersection points, then subtract lower from upper.')


def cubic_negative_area(deck):
    P = Plane(-2.5, 1.6, -9.5, 3.0, 300, 190, (16, 8, 10, 18))
    f = lambda x: x ** 3
    base = P.axes([(-2, '−2'), (-1, '−1'), (1, '1')], [(-8, '−8'), (-4, '−4'), (1, '1')], grid=True, labels=False) + P.curve(f, 'c1', -2.2, 1.3, clip=(-9.5, 3.0))
    def region(a, bb):
        return [(a, 0)] + [(a + (bb - a) * i / 30, f(a + (bb - a) * i / 30)) for i in range(31)] + [(bb, 0)]
    back = (P.poly(region(-2, 0), 'f2 fx d2') + P.poly(region(0, 1), 'f3 fx d3') + P.text(-1.4, -2.0, 'area 4', 't2 fx d2', anchor='middle') + P.text(0.55, 0.55, '¼', 't3 fx d3', anchor='middle')
            + P.text(-0.6, 2.0, '∫ = −15/4, area = 17/4', 't4 fx d4', anchor='middle'))
    mcard(deck, 'Misc Ex Q4 · y = x³', 'Area bounded by y = x³, the x-axis and the ordinates x = −2 and x = 1. Why is it not −15/4?', base, back,
          '<p>∫₋₂¹ x³ dx = [x⁴/4]₋₂¹ = 1/4 − 4 = −15/4 is the <b>signed</b> value (negative because most of the region is below the axis).</p>'
          '<p>Area = |∫₋₂⁰ x³ dx| + ∫₀¹ x³ dx = 4 + 1/4 = <b>17/4</b> (option D).</p>',
          'Signed integral versus area for y = x³',
          'y = x^3 between x = -2 and 1: integral = -15/4 but area = |-4| + 1/4 = 17/4; split at the zero x = 0',
          vb='0 0 300 190', hint='Which part lies below the axis?')


# ================================================================ Maths 12 Ch 9 Differential equations
def slope_field_family(deck):
    P = Plane(-2.6, 2.6, -2.4, 2.6, 300, 190, (12, 8, 8, 12))
    segs = ''
    for i in range(-5, 6):
        for j in range(-4, 5):
            x, y = i * 0.5, j * 0.5
            m = y                     # dy/dx = y
            dx = 0.16 / math.sqrt(1 + m * m)
            segs += P.line(x - dx, y - m * dx, x + dx, y + m * dx, 'gd')
    base = P.axes([(-2, '−2'), (-1, '−1'), (1, '1'), (2, '2')], [(-2, '−2'), (-1, '−1'), (1, '1'), (2, '2')], grid=False, labels=False) + segs
    fam = ''
    for k, C in enumerate([-1.2, -0.5, 0.5, 1.2]):
        fam += P.curve(lambda x, C=C: C * math.exp(x), 'c1 fx d2', -2.5, 2.5, clip=(-2.4, 2.6)).replace('class="c1', 'class="c0')
    back = (fam + P.curve(math.exp, 'c2 fx d3', -2.5, 2.5, clip=(-2.4, 2.6)) + P.dot(0, 1, 'd2s', 5, 'fx d3')
            + P.text(0.15, 1.15, '(0, 1)', 't2 fx d3', dx=6) + P.text(1.35, 2.1, 'y = eˣ', 't2 fx d3', anchor='end') + P.text(-2.5, 2.35, 'y = Ceˣ', 'lbl fx d2'))
    mcard(deck, 'General and particular solutions', 'The slope at every point of the plane is dy/dx = y (short segments). What do the solution curves look like, and what does the condition y(0) = 1 do?', base, back,
          '<p>Solving dy/dx = y gives the <b>general solution y = Ceˣ</b>: a whole family of curves, one for each constant C, and each is tangent to the little slope segments everywhere. The solution has <b>one arbitrary constant</b>, as many as the order of the equation.</p>'
          '<p>The condition y = 1 at x = 0 picks the single curve through (0, 1): C = 1, the <b>particular solution y = eˣ</b>. (Ex 9.2 Q11, Q12: a 4th-order equation has 4 arbitrary constants; a particular solution has none.)</p>',
          'General solution is a family of curves; the condition selects one',
          'General solution of an nth order ODE has n arbitrary constants (family of curves); a particular solution has none; dy/dx = y gives y = Ce^x, y(0)=1 gives y = e^x',
          vb='0 0 300 190', hint='Follow the slope segments.')


def homogeneous_rays(deck):
    P, h = eqplane(-3.2, 3.2, -2.4, 2.4, pad=(8, 8, 8, 8))
    segs = ''
    for ang in range(0, 360, 30):
        t = math.radians(ang)
        c, s = math.cos(t), math.sin(t)
        if abs(c) < 1e-9:
            continue
        m = (1 + math.tan(t)) if False else 0   # placeholder overwritten below
        v = s / c
        m = (1 + v * v) / (1 + v)               # slope of dy/dx = (x^2 + y^2)/(x^2 + x y) at y/x = v
        if abs(1 + v) < 1e-6 or abs(m) > 6:
            continue
        for r in (0.7, 1.4, 2.1, 2.8):
            x, y = r * c, r * s
            if abs(x) > 3 or abs(y) > 2.3:
                continue
            dx = 0.22 / math.sqrt(1 + m * m)
            segs += P.line(x - dx, y - m * dx, x + dx, y + m * dx, 'c1')
    base = P.axes(labels=False) + segs
    back = ''
    for k, ang in enumerate([20, 45, 70, 110, 200]):
        t = math.radians(ang)
        back += P.line(0, 0, 3.6 * math.cos(t), 3.6 * math.sin(t), 'guide fx d' + str(min(k // 2 + 2, 5)))
    back += P.text(-3.0, -1.9, 'slope depends only on y/x', 't4 fx d3') + P.text(-3.0, -2.2, 'same slope along each ray', 't2 fx d4')
    mcard(deck, 'Why y = vx works', 'For (x² + xy) dy = (x² + y²) dx the slope at (x, y) is (x² + y²)/(x² + xy). Look at the slope segments: what pattern do they show?', base, back,
          '<p>The right side (x² + y²)/(x² + xy) = (1 + v²)/(1 + v) with v = y/x depends <b>only on the ratio y/x</b>. So all points on the same ray from the origin have the <b>same slope</b> (parallel segments along each ray). Such an equation is <b>homogeneous</b>.</p>'
          '<p>Substitute <b>y = vx</b> (dy/dx = v + x dv/dx) and the variables separate: x dv/dx = (1 − v)/(1 + v). Solve, then put v = y/x (Ex 9.4 Q1: (x − y)² = C x e^(−y/x)).</p>',
          'Homogeneous equations: slope constant along rays; substitute y = vx',
          'Homogeneous ODE dy/dx = F(y/x): slope depends only on y/x, constant along rays from the origin; substitute y = vx, dy/dx = v + x dv/dx, then separate variables',
          vb=f'0 0 300 {h}', hint='Compare slopes on the same line through the origin.')


def growth_doubling(deck):
    P = Plane(-1, 27, -150, 4200, 300, 190, (30, 8, 10, 20))
    f = lambda t: 1000 * math.exp(t / 20)
    base = P.axes([(10, '10'), (20, '20')], [(1000, '1000'), (2000, '2000'), (4000, '4000')], grid=True, labels=False) + P.curve(f, 'c1', 0, 26, clip=(-150, 4200))
    back = (P.dot(0, 1000, 'd1s', 4.5, 'fx d2') + P.dot(20 * math.log(2), 2000, 'd2s', 5.5, 'fx d3') + P.line(0, 2000, 20 * math.log(2), 2000, 'guide fx d3') + P.line(20 * math.log(2), 0, 20 * math.log(2), 2000, 'guide fx d3')
            + P.text(20 * math.log(2), 0, '20 log 2 ≈ 13.9 yr', 't2 fx d4', dy=-6, dx=8) + P.text(1, 3800, 'P = 1000 e^(t/20)', 't1 fx d2'))
    mcard(deck, 'Example 9 · continuous growth', 'A bank adds interest continuously at 5% per year: dP/dt = P/20. In how many years does ₹1000 double?', base, back,
          '<p>Separate: dP/P = dt/20, so log P = t/20 + C and <b>P = 1000 e^(t/20)</b> (using P(0) = 1000).</p>'
          '<p>Doubling: 2000 = 1000 e^(t/20) gives <b>t = 20 log 2 ≈ 13.9 years</b>. General law: <b>dP/dt = kP ⇒ P = P₀ e^(kt)</b>; growth (k > 0), decay (k < 0). (Ex 9.3 Q20: r = 10 log 2 ≈ 6.93%; Q21: 1000 e^(0.5) ≈ ₹1648.)</p>',
          'Exponential growth: dP/dt = kP gives P = P₀ e^(kt)',
          'dP/dt = kP gives P = P0 e^(kt); 5% continuous interest: P = 1000 e^(t/20), doubling time 20 log 2 = 13.9 years; rate for doubling in 10 years is 10 log 2 = 6.93%',
          vb='0 0 300 190', hint='Separate the variables and integrate.')


# ================================================================ Maths 12 Ch 10 Vector algebra
def vector_addition_laws(deck):
    P, h = eqplane(-0.8, 6.4, -0.6, 4.4, pad=(10, 8, 8, 10))
    a, b = (3.6, 1.0), (1.6, 2.6)
    s = (a[0] + b[0], a[1] + b[1])
    base = P.axes(labels=False) + vec(P, 0, 0, a[0], a[1], 'c1') + P.text(a[0] / 2, a[1] / 2, 'a', 't1', dx=4, dy=14) + vec(P, 0, 0, b[0], b[1], 'c3') + P.text(b[0] / 2, b[1] / 2, 'b', 't3', dx=-12, dy=-2)
    back = (vec(P, a[0], a[1], s[0], s[1], 'c3', 'fx d2') + vec(P, 0, 0, s[0], s[1], 'c2', 'fx d3') + P.text(s[0] / 2, s[1] / 2, 'a + b', 't2 fx d3', dx=-6, dy=-10, anchor='end')
            + P.line(b[0], b[1], s[0], s[1], 'guide fx d4') + P.text(s[0], s[1], 'a + b = b + a', 't4 fx d4', dx=-4, dy=-8, anchor='end'))
    mcard(deck, 'Addition of vectors', 'Add the vectors a and b by the triangle law. What is the parallelogram law, and is a + b = b + a?', base, back,
          '<p><b>Triangle law:</b> place the tail of b at the head of a; the vector from the start of a to the end of b is <b>a + b</b>. <b>Parallelogram law:</b> if a and b are adjacent sides from a point, a + b is the diagonal from that point.</p>'
          '<p>Both routes reach the same point, so <b>a + b = b + a</b> (commutative), also associative: (a + b) + c = a + (b + c). In components: (a₁ + b₁, a₂ + b₂, a₃ + b₃). Subtraction: a − b = a + (−b).</p>',
          'Triangle and parallelogram laws of vector addition',
          'Triangle law: tail of b at head of a, a+b joins the start to the end; parallelogram law: diagonal of the parallelogram on a and b; vector addition is commutative and associative; componentwise addition',
          vb=f'0 0 300 {h}', hint='Place b at the head of a.')


def section_formula_line(deck):
    base = ('<line class="c0" x1="10" y1="90" x2="270" y2="90"></line>'
            '<circle class="d1s" cx="30" cy="90" r="5"></circle><circle class="d1s" cx="120" cy="90" r="5"></circle>'
            '<text class="lbl" x="30" y="112" text-anchor="middle">P (a)</text><text class="lbl" x="120" y="112" text-anchor="middle">Q (b)</text>')
    back = ('<circle class="d2s fx d2" cx="90" cy="90" r="5.5"></circle><text class="t2 fx d2" x="90" y="72" text-anchor="middle">R (2 : 1)</text>'
            '<text class="sm fx d2" x="140" y="140" text-anchor="middle">internal: R = (m b + n a)/(m + n) = (2b + a)/3</text>'
            '<circle class="d3s fx d4" cx="210" cy="90" r="5.5"></circle><text class="t3 fx d4" x="210" y="72" text-anchor="middle">R′ (external)</text>'
            '<text class="sm fx d4" x="140" y="158" text-anchor="middle">external: R′ = (m b − n a)/(m − n) = 2b − a</text>')
    mcard(deck, 'Section formula', 'P and Q have position vectors a and b. Find the position vector of the point R dividing PQ in the ratio 2 : 1 (i) internally (ii) externally.', base, back,
          '<p><b>Internally</b> m : n: <b>r = (m b + n a)/(m + n)</b>. For 2 : 1: (2b + a)/3. <b>Externally</b>: <b>r = (m b − n a)/(m − n)</b>, here 2b − a: R′ lies beyond Q with QR′ = PQ.</p>'
          '<p>Ex 10.2 Q15: a = î + 2ĵ − k̂, b = −î + ĵ + k̂: internal (−î + 4ĵ + k̂)/3, external −3î + 3k̂. The midpoint (m = n = 1) is (a + b)/2 (Q16: (3, 2, 1)).</p>',
          'Section formula for internal and external division',
          'Internal division m:n: (m b + n a)/(m+n); external: (m b - n a)/(m-n); midpoint (a+b)/2; Ex 10.2 Q15 gives (-i+4j+k)/3 and -3i+3k',
          vb='0 0 300 170', hint='Weight each end by the opposite part of the ratio.')


def dot_projection(deck):
    P, h = eqplane(-0.6, 6.4, -0.8, 4.4, pad=(10, 8, 8, 10))
    a, b = (4.0, 3.0), (5.5, 0.0)
    base = P.axes(labels=False) + vec(P, 0, 0, a[0], a[1], 'c1') + P.text(a[0], a[1], 'a', 't1', dx=6, dy=-2) + vec(P, 0, 0, b[0], b[1], 'c3') + P.text(b[0], 0, 'b', 't3', dx=4, dy=14)
    back = (P.line(a[0], a[1], a[0], 0, 'guide fx d2') + P.line(0, 0, a[0], 0, 'c2 fx d3') + P.dot(a[0], 0, 'd2s', 4.5, 'fx d3')
            + P.text(2.0, 0, '|a| cos θ = 4', 't2 fx d3', anchor='middle', dy=16) + P.text(0.7, 0.5, 'θ', 't4 fx d4', dx=4))
    mcard(deck, 'Scalar product as a projection', 'How is a · b related to the projection of a on b? Find the projection of a = 4î + 3ĵ on b = 5.5î.', base, back,
          '<p><b>a · b = |a||b| cos θ</b> = (projection of a on b) × |b|. Projection of a on b = <b>a · b / |b|</b> = |a| cos θ: the length of the shadow of a on the line of b.</p>'
          '<p>Here a · b = 22, |b| = 5.5, so the projection is 4. The dot product is 0 exactly when the vectors are perpendicular (Ex 10.3 Q3: (î − ĵ) on (î + ĵ) has projection 0). In components a · b = a₁b₁ + a₂b₂ + a₃b₃.</p>',
          'Dot product and projection',
          'a.b = |a||b|cos(theta); projection of a on b = a.b/|b|; a.b = 0 iff perpendicular; a.b = a1b1+a2b2+a3b3',
          vb=f'0 0 300 {h}', hint='Drop a perpendicular from the tip of a onto the line of b.')


def cross_parallelogram(deck):
    P, h = eqplane(-0.6, 6.6, -0.6, 4.2, pad=(10, 8, 8, 10))
    a, b = (4.0, 0.4), (1.4, 2.6)
    s = (a[0] + b[0], a[1] + b[1])
    base = P.axes(labels=False) + vec(P, 0, 0, a[0], a[1], 'c1') + vec(P, 0, 0, b[0], b[1], 'c3') + P.text(a[0], a[1], 'a', 't1', dx=6, dy=4) + P.text(b[0], b[1], 'b', 't3', dx=-10, dy=-4)
    back = (P.poly([(0, 0), a, s, b], 'f4 fx d2')
            + P.text(3.3, -0.3, 'area = |a × b| = |a||b| sin θ', 't4 fx d3', anchor='middle') )
    mcard(deck, 'Cross product', 'What does |a × b| measure, and what is the direction of a × b?', base, back,
          '<p><b>|a × b| = |a||b| sin θ</b> is the <b>area of the parallelogram</b> with adjacent sides a and b; the triangle has area ½|a × b|. The vector a × b is <b>perpendicular to both a and b</b>, with direction given by the right-hand rule (turn a into b).</p>'
          '<p>a × b = −(b × a) (not commutative); a × b = 0 iff a ∥ b. Example 25: a = 3î + ĵ + 4k̂, b = î − ĵ + k̂ gives a × b = 5î + ĵ − 4k̂, area √42.</p>',
          'Cross product: area of parallelogram and perpendicular direction',
          'a x b has magnitude |a||b|sin(theta) = area of parallelogram, direction perpendicular to a and b by the right-hand rule; a x b = -(b x a); zero iff parallel; area of triangle = half of |a x b|',
          vb=f'0 0 300 {h}', hint='Think of the parallelogram spanned by a and b.')


def unit_vector_plane(deck):
    P, h = eqplane(-1.5, 1.5, -1.3, 1.3, pad=(8, 8, 8, 8))
    ox, oy = P.X(0), P.Y(0)
    u = P.X(1) - ox
    base = P.axes(labels=False) + f'<circle class="ghost" cx="{ox:.1f}" cy="{oy:.1f}" r="{u:.1f}"></circle>' + vec(P, 0, 0, 1, 0, 'c0') + P.text(1, 0, 'î', 'lbi', dy=14, dx=2)
    t = math.radians(30)
    back = (vec(P, 0, 0, math.cos(t), math.sin(t), 'c2', 'fx d2') + P.line(math.cos(t), 0, math.cos(t), math.sin(t), 'guide fx d3') + P.line(0, 0, math.cos(t), 0, 'c1 fx d3') + P.line(math.cos(t), 0, math.cos(t), math.sin(t), 'c3 fx d3')
            + P.text(0.55, 0.55, 'r̂ = cos θ î + sin θ ĵ', 't2 fx d3', anchor='end', dx=-4, dy=-2) + P.text(0.85, 0.1, 'θ = 30°', 't4 fx d4', dx=2, dy=4))
    mcard(deck, 'Unit vectors in the XY-plane', 'Write every unit vector in the XY-plane. Which one makes 30° with the positive x-axis?', base, back,
          '<p>A unit vector r = xî + yĵ has x² + y² = 1, so x = cos θ, y = sin θ: <b>r = cos θ î + sin θ ĵ</b> with θ from 0 to 2π (the whole unit circle). Its direction cosines are (cos θ, sin θ).</p>'
          '<p>For θ = 30°: <b>(√3/2) î + ½ ĵ</b> (Misc Ex Q1). In 3-D the direction cosines l, m, n satisfy l² + m² + n² = 1.</p>',
          'Unit vectors in the XY-plane are cos θ î + sin θ ĵ',
          'Unit vectors in the xy-plane: cos(theta) i + sin(theta) j; 30 degrees gives (sqrt3/2) i + (1/2) j; direction cosines satisfy l^2+m^2+n^2 = 1',
          vb=f'0 0 300 {h}', hint='Points on the unit circle.')


# ================================================================ Maths 12 Ch 11 Three dimensional geometry
def direction_cosines_axes(deck):
    A = Axes3D(ox=100, oy=170, u=30)
    Pt = (2, 3, 4)
    n = math.sqrt(4 + 9 + 16)
    base = A.axes(3.6, 6.4, 5.4) + A.line((0, 0, 0), Pt, 'c1') + A.dot(Pt, 'd1s', 4.5) + A.text(Pt, 'line OP', 't1', dx=8, dy=-6)
    back = (A.box(Pt, 'guide fx d2') + '<text class="t2 fx d2" x="170" y="60">l = cos α = 2/√29</text><text class="t3 fx d3" x="170" y="80">m = cos β = 3/√29</text><text class="t4 fx d4" x="170" y="100">n = cos γ = 4/√29</text>')
    mcard(deck, 'Direction cosines', 'A line makes angles α, β, γ with the positive x, y, z axes. For the line through O and P(2, 3, 4) find its direction cosines and show l² + m² + n² = 1.', base, back,
          '<p><b>Direction cosines</b> l = cos α, m = cos β, n = cos γ. For OP: l = x/|OP| = 2/√29, m = 3/√29, n = 4/√29. They are the components of the unit vector along the line, so <b>l² + m² + n² = 1</b> (4 + 9 + 16 = 29).</p>'
          '<p><b>Direction ratios</b> a, b, c are any numbers proportional to (l, m, n): l = a/√(a² + b² + c²), etc. The axes have direction cosines (1, 0, 0), (0, 1, 0), (0, 0, 1) (Example 4). Reversing the direction changes all three signs.</p>',
          'Direction cosines and direction ratios of a line',
          'Direction cosines l,m,n = cosines of angles with the axes; l^2+m^2+n^2 = 1; direction ratios a,b,c proportional to l,m,n: l = a/sqrt(a^2+b^2+c^2); axes have (1,0,0),(0,1,0),(0,0,1)',
          vb='0 0 300 220', hint='Divide the coordinates of P by |OP|.')


def line_param_3d(deck):
    A = Axes3D(ox=90, oy=178, u=26)
    Pa = (0.5, 0.6, 0.5)
    b = (0.8, 2.0, 1.4)
    q = lambda t: (Pa[0] + t * b[0], Pa[1] + t * b[1], Pa[2] + t * b[2])
    base = A.axes(3.6, 6.0, 4.8) + A.dot(Pa, 'd1s', 5) + A.text(Pa, 'A (a)', 't1', dx=-8, dy=16, anchor='end') + A.line(Pa, q(0.8), 'c3') + A.text(q(0.8), 'b', 't3', dx=8, dy=-4)
    back = (A.line(q(-0.3), q(1.9), 'c1 fx d2') + A.dot(q(1.5), 'd2s', 5, 'fx d3') + A.text(q(1.5), 'P (r)', 't2 fx d3', dx=8, dy=-4)
            + A.line((0, 0, 0), Pa, 'guide fx d3') + A.line((0, 0, 0), q(1.5), 'guide fx d3') + '<text class="t4 fx d4" x="150" y="30">r = a + λ b</text>')
    mcard(deck, 'Equation of a line in space', 'Write the vector equation of the line through the point A (position vector a) parallel to the vector b. What is its Cartesian form?', base, back,
          '<p>A point P on the line satisfies AP = λb for some real λ, so <b>r = a + λ b</b> (λ ∈ R). If a = (x₁, y₁, z₁) and b = (a, b, c) then x = x₁ + λa, y = y₁ + λb, z = z₁ + λc; eliminating λ gives <b>(x − x₁)/a = (y − y₁)/b = (z − z₁)/c</b>.</p>'
          '<p>Through two points a, a′: direction b = a′ − a. If the direction cosines l, m, n are used, write l, m, n in place of a, b, c. (Example 6: through (5, 2, −4) parallel to 3î + 2ĵ − 8k̂.)</p>',
          'Vector and Cartesian equations of a line',
          'Line through a parallel to b: r = a + lambda b; Cartesian (x-x1)/a = (y-y1)/b = (z-z1)/c; through two points use b = a2 - a1',
          vb='0 0 300 220', hint='Move from A along b by any multiple λ.')


def skew_lines_distance(deck):
    A = Axes3D(ox=80, oy=190, u=26)
    base = (A.axes(3.6, 6.8, 4.6) + A.line((1, -0.4, 0), (1, 6.2, 0), 'c1') + A.text((1, 6.2, 0), 'l₁', 't1', dx=8, dy=4)
            + A.line((-0.4, 3, 2), (3.4, 3, 2), 'c3') + A.text((3.4, 3, 2), 'l₂', 't3', dx=-4, dy=14, anchor='end'))
    back = (A.line((1, 3, 0), (1, 3, 2), 'c2 fx d2') + A.dot((1, 3, 0), 'd2s', 4.5, 'fx d2') + A.dot((1, 3, 2), 'd2s', 4.5, 'fx d2')
            + A.text((1, 3, 1), 'd', 't2 fx d3', dx=8, dy=4))
    mcard(deck, 'Shortest distance between skew lines', 'Two lines are neither parallel nor intersecting (skew lines). What is the shortest distance between them?', base, back,
          '<p>The shortest distance is along the <b>common perpendicular</b>, which is parallel to <b>b₁ × b₂</b>. For l₁: r = a₁ + λb₁ and l₂: r = a₂ + μb₂: <b>d = |(a₂ − a₁) · (b₁ × b₂)| / |b₁ × b₂|</b> (the projection of a₂ − a₁ on the common perpendicular).</p>'
          '<p>If l₁ ∥ l₂ (b₁ ∥ b₂), the distance is instead <b>|b × (a₂ − a₁)|/|b|</b> (Example 10). d = 0 means the lines intersect (coplanar).</p>',
          'Shortest distance between two skew lines',
          'Skew lines: d = |(a2-a1).(b1 x b2)|/|b1 x b2|; parallel lines: |b x (a2-a1)|/|b|; d = 0 means the lines are coplanar/intersect; common perpendicular parallel to b1 x b2',
          vb='0 0 300 230', hint='Project a₂ − a₁ onto the direction perpendicular to both lines.')


def angle_between_lines(deck):
    P, h = eqplane(-0.4, 6.4, -0.4, 4.4, pad=(10, 8, 8, 10))
    d1, d2 = (4.0, 1.4), (1.6, 3.2)
    o = (0.0, 0.0)
    base = (P.axes(labels=False) + P.line(-0.3, -0.105, 5.8, 2.03, 'c1') + P.line(-0.15, -0.3, 2.5, 5.0, 'c3').replace('y2="', 'y2="') + P.text(5.6, 2.1, 'l₁ (direction b₁)', 't1', anchor='end', dy=-10) + P.text(2.4, 4.0, 'l₂ (b₂)', 't3', dx=6))
    back = (P.text(2.0, 0.55, 'θ', 't4 fx d2', dx=2) + vec(P, 0, 0, 3.4, 1.19, 'c2', 'fx d2') + vec(P, 0, 0, 1.35, 2.7, 'c2', 'fx d2') + P.text(2.7, 4.15, 'cos θ = |b₁·b₂|/(|b₁||b₂|)', 't2 fx d3'))
    mcard(deck, 'Angle between two lines', 'How do you find the angle between two lines from their direction ratios (a₁, b₁, c₁) and (a₂, b₂, c₂)?', base, back,
          '<p>The angle between two lines (even skew ones) is the angle between their <b>direction vectors</b>: <b>cos θ = |a₁a₂ + b₁b₂ + c₁c₂| / (√(a₁² + b₁² + c₁²) √(a₂² + b₂² + c₂²))</b>, with θ acute. With direction cosines: cos θ = |l₁l₂ + m₁m₂ + n₁n₂|.</p>'
          '<p><b>Perpendicular</b> ⇔ a₁a₂ + b₁b₂ + c₁c₂ = 0; <b>parallel</b> ⇔ a₁/a₂ = b₁/b₂ = c₁/c₂. (Ex 11.2 Q8(i): directions (3, 2, 6) and (1, 2, 2) give cos θ = 19/21.)</p>',
          'Angle between two lines from direction ratios',
          'cos(theta) = |a1a2+b1b2+c1c2| / (sqrt(a1^2+b1^2+c1^2) sqrt(a2^2+b2^2+c2^2)); perpendicular when the dot product is zero; parallel when ratios are proportional',
          vb=f'0 0 300 {h}', hint='Use the direction vectors of the lines.')


# ================================================================ Maths 12 Ch 12 Linear programming
def lp_corner_points(deck):
    P = Plane(-3, 26, -6, 70, 300, 190, (16, 8, 10, 18))
    poly = [(0, 0), (20, 0), (10, 50), (0, 60)]
    base = P.axes([(10, '10'), (20, '20')], [(20, '20'), (40, '40'), (60, '60')], grid=True, labels=False) + P.poly(poly, 'f1')
    base += P.line(-2, 100 + 10, 22, -20, 'c0') if False else ''
    back = ''
    for k, ((x, y), lab) in enumerate(zip(poly, ['O (0,0): 0', 'A (20,0): 5000', 'B (10,50): 6250', 'C (0,60): 4500'])):
        back += P.dot(x, y, 'd2s' if lab.startswith('B') else 'd1s', 5 if lab.startswith('B') else 4, f'fx d{k % 4 + 1}')
    back += (P.text(10, 50, 'B: 6250 (max)', 't2 fx d4', dx=8, dy=-4) + P.text(20, 0, 'A: 5000', 'sm fx d2', dx=4, dy=-8) + P.text(0, 60, 'C: 4500', 'sm fx d3', dx=6, dy=-6)
             + P.text(0, 0, 'O: 0', 'sm fx d1', dx=6, dy=-6))
    mcard(deck, 'Corner point method', 'Maximise Z = 250x + 75y subject to 5x + y ≤ 100, x + y ≤ 60, x, y ≥ 0. Where does the maximum occur?', base, back,
          '<p>The feasible region is the polygon OABC. <b>Theorem:</b> an optimal value of a linear objective over a convex polygon occurs at a <b>corner point</b>. So evaluate Z at O(0, 0), A(20, 0), B(10, 50), C(0, 60): 0, 5000, <b>6250</b>, 4500.</p>'
          '<p>The maximum profit ₹6250 is at B: buy <b>10 tables and 50 chairs</b>. B is the intersection of 5x + y = 100 and x + y = 60 (subtract: 4x = 40).</p>',
          'Corner point method: evaluate Z at the vertices',
          'Optimal value of Z = ax+by over a bounded feasible polygon occurs at a corner point; evaluate Z at each vertex; furniture dealer: max 250x+75y at (10,50) = 6250',
          vb='0 0 300 190', hint='Find the vertices of the feasible region and evaluate Z at each.')


def lp_iso_profit(deck):
    P = Plane(-0.6, 6.2, -0.6, 5.6, 300, 190, (16, 8, 10, 18))
    base = P.axes([(1, '1'), (2, '2'), (3, '3'), (4, '4')], [(1, '1'), (2, '2'), (3, '3'), (4, '4')], grid=False, labels=False) + P.poly([(0, 0), (4, 0), (0, 4)], 'f1') + P.text(2.0, 1.0, 'x + y ≤ 4', 'sm', anchor='middle')
    back = ''
    for k, c in enumerate([4, 8, 12, 16]):
        # 3x + 4y = c
        pts = [(0, c / 4), (c / 3, 0)]
        cls = 'guide' if c < 16 else 'c2'
        back += P.line(-0.2, (c + 0.6) / 4, (c + 0.8) / 3, -0.2, f'{cls} fx d{k + 1}')
        back += P.text(c / 3 if c < 16 else 0.15, 0 if c < 16 else c / 4, f'Z = {c}', ('sm' if c < 16 else 't2') + f' fx d{k + 1}', dx=(4 if c < 16 else 8), dy=(-6 if c < 16 else -8))
    back += P.dot(0, 4, 'd2s', 5.5, 'fx d4')
    mcard(deck, 'Iso-profit lines', 'Maximise Z = 3x + 4y subject to x + y ≤ 4, x, y ≥ 0. Slide the line 3x + 4y = c across the feasible region: where is it last touching?', base, back,
          '<p>Each line 3x + 4y = c is a set of points with the same Z. As c increases the line moves up and to the right; the largest c for which it still meets the feasible triangle is when it just touches a <b>corner</b>: here (0, 4) with <b>Z = 16</b>.</p>'
          '<p>Check with corner values: (0, 0) → 0, (4, 0) → 12, (0, 4) → 16 (Ex 12.1 Q1). Steeper or flatter objective lines would end at a different vertex.</p>',
          'Iso-profit line touches the last vertex',
          'Lines 3x+4y=c move across the region; maximum Z is at the last vertex touched, (0,4) with Z=16; corner values 0, 12, 16',
          vb='0 0 300 190', hint='Move the objective line parallel to itself.')


def lp_multiple_optima(deck):
    P = Plane(-3, 26, -3, 26, 300, 200, (16, 8, 10, 18))
    poly = [(0, 10), (5, 5), (15, 15), (0, 20)]
    base = P.axes([(10, '10'), (20, '20')], [(10, '10'), (20, '20')], grid=True, labels=False) + P.poly(poly, 'f1')
    for (x, y), lab in zip(poly, ['A (0,10)', 'B (5,5)', 'C (15,15)', 'D (0,20)']):
        base += P.dot(x, y, 'd0s', 3.6) + P.text(x, y, lab, 'sm', dx=6 if x else 8, dy=(14 if y < 10 else -6))
    back = P.line(-2, 20.7, 16.5, 14.5, 'c2 fx d2') + P.line(0, 20, 15, 15, 'c4 fx d2').replace('class="c4', 'class="c4') + P.text(13, 23.5, 'Z = 180 on all of CD', 't2 fx d3', anchor='middle') + P.dot(5, 5, 'd1s', 5, 'fx d3') + P.text(5, 5, 'min 60', 't1 fx d3', dx=8, dy=-6)
    mcard(deck, 'Example 3 · multiple optimal solutions', 'Minimise and maximise Z = 3x + 9y subject to x + 3y ≤ 60, x + y ≥ 10, x ≤ y, x, y ≥ 0. Why does the maximum occur at two corners?', base, back,
          '<p>Corner values: A(0, 10) → 90, B(5, 5) → 60, C(15, 15) → 180, D(0, 20) → 180. Minimum <b>60 at B</b>. Maximum <b>180 at both C and D</b>.</p>'
          '<p>The objective line 3x + 9y = 180 is the same line as the constraint x + 3y = 60, so it contains the whole edge CD. <b>Every point of segment CD</b> is optimal: infinitely many solutions.</p>',
          'Two corners with the same optimum ⇒ the whole edge is optimal',
          'If two corner points give the same optimal value, every point on the segment joining them is also optimal; Example 3: Z=3x+9y max 180 on segment CD (parallel to x+3y=60), min 60 at (5,5)',
          vb='0 0 300 200', hint='Compare the slope of the objective line with the edges.')


def lp_unbounded_check(deck):
    P = Plane(-0.6, 8.6, -0.6, 10.6, 300, 200, (16, 8, 10, 18))
    reg = [(0, 3), (1, 0), (6, 0), (8, 4 / 3), (8, 10), (2.5, 10), (0, 5)]
    base = P.axes([(2, '2'), (4, '4'), (6, '6')], [(2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10')], grid=True, labels=False) + P.poly(reg, 'f1')
    for (x, y), lab in zip([(0, 5), (0, 3), (1, 0), (6, 0)], ['(0,5): 100', '(0,3): 60', '(1,0): −50', '(6,0): −300']):
        base += P.dot(x, y, 'd0s', 3.8) + P.text(x, y, lab, 'sm', dx=6, dy=(12 if y == 0 else 0))
    back = (P.poly([(6, 0), (8, 5), (8, 4 / 3)], 'f2 fx d2') + P.line(6, 0, 8.2, 5.5, 'c2 fx d2') + P.text(4.3, 6.6, 'Z < −300 meets the region', 't2 fx d3', anchor='middle')
            + P.text(4.3, 8.4, 'so no minimum', 't4 fx d4', anchor='middle'))
    mcard(deck, 'Example 4 · unbounded region', 'Minimise Z = −50x + 20y over the unbounded region 2x − y ≥ −5, 3x + y ≥ 3, 2x − 3y ≤ 12, x, y ≥ 0. The smallest corner value is −300 at (6, 0). Is that the minimum?', base, back,
          '<p>For an <b>unbounded</b> region the smallest corner value m is the minimum <b>only if the open half-plane ax + by &lt; m has no point in common with the region</b>. Here −50x + 20y &lt; −300, i.e. −5x + 2y &lt; −30, does contain feasible points (the red wedge).</p>'
          '<p>So Z can be made smaller than −300: <b>Z has no minimum</b>. Similarly, to check the maximum 100 at (0, 5) test −50x + 20y &gt; 100: it also meets the region (large y), so no maximum either.</p>',
          'Unbounded feasible region: test the open half-plane',
          'For an unbounded region, corner minimum m is the true minimum iff the open half-plane ax+by<m has no common point with the feasible region; example -50x+20y has no minimum',
          vb='0 0 300 200', hint='Draw the half-plane Z < −300 and see whether it overlaps the region.')


def lp_infeasible(deck):
    P = Plane(-0.6, 9.6, -0.6, 9.6, 300, 190, (16, 8, 10, 18))
    upper = [(0, 8), (8, 0), (9.6, 0), (9.6, 9.6), (0, 9.6)]
    lower = [(0, 0), (5, 0), (0, 3)]
    base = P.axes([(2, '2'), (4, '4'), (6, '6'), (8, '8')], [(2, '2'), (4, '4'), (6, '6'), (8, '8')], grid=True, labels=False) + P.line(0, 8, 8, 0, 'c1') + P.line(0, 3, 5, 0, 'c2')
    back = P.poly(upper, 'f1 fx d2') + P.poly(lower, 'f2 fx d3') + P.text(5.5, 6.5, 'x + y ≥ 8', 't1 fx d2', anchor='middle') + P.text(1.6, 1.2, '3x + 5y ≤ 15', 't2 fx d3', anchor='middle') + P.text(4.8, 3.3, 'no overlap: infeasible', 't4 fx d4', anchor='middle')
    mcard(deck, 'Example 5 · no feasible region', 'Minimise Z = 3x + 2y subject to x + y ≥ 8, 3x + 5y ≤ 15, x, y ≥ 0. What can you say?', base, back,
          '<p>The half-plane x + y ≥ 8 lies on the far side of its line; 3x + 5y ≤ 15 is the small triangle near the origin. They have <b>no point in common</b> (even the largest x + y in the triangle is 5 &lt; 8), so the <b>feasible region is empty</b> and the problem has no solution.</p>'
          '<p>Same happens in Ex 12.1 Q10: x − y ≤ −1 means y ≥ x + 1 while −x + y ≤ 0 means y ≤ x. An LPP can therefore be <b>infeasible</b>, <b>unbounded</b> with or without an optimum, or have a <b>unique / multiple</b> optimum.</p>',
          'Infeasible LPP: empty feasible region',
          'If the constraints have no common point the feasible region is empty and the LPP has no solution; example x+y>=8 with 3x+5y<=15; Ex 12.1 Q10 also infeasible',
          vb='0 0 300 190', hint='Do the two shaded half-planes overlap anywhere?')


# ================================================================ Maths 12 Ch 13 Probability
def cond_prob_venn(deck):
    front = (f'<path class="f0" d="{_R}"></path><circle class="c0" cx="115" cy="100" r="58"></circle><circle class="c0" cx="185" cy="100" r="58"></circle>'
             '<text class="t1" x="88" y="66" text-anchor="middle">E</text><text class="t2" x="212" y="66" text-anchor="middle">F</text><text class="lbi" x="20" y="28">S</text>'
             '<text class="lbl" x="150" y="104" text-anchor="middle">0.2</text><text class="sm" x="82" y="106" text-anchor="middle">0.4</text><text class="sm" x="218" y="106" text-anchor="middle">0.1</text>')
    back = (f'<path class="ns2 fx d2" d="{_BMA}"></path><path class="ns4 fx d3" d="{_LENS}"></path>'
            '<text class="t2 fx d2" x="150" y="182" text-anchor="middle">F has occurred: F is the new sample space (0.3)</text>'
            '<text class="t4 fx d3" x="150" y="30" text-anchor="middle">P(E|F) = P(E ∩ F)/P(F) = 0.2/0.3 = 2/3</text>')
    mcard(deck, 'Conditional probability', 'P(E) = 0.6, P(F) = 0.3 and P(E ∩ F) = 0.2. Find P(E|F) and P(F|E). What does conditioning do to the sample space?', front, back,
          '<p><b>P(E|F) = P(E ∩ F)/P(F)</b> (P(F) ≠ 0): once F has occurred, F becomes the whole sample space, and we ask what fraction of it lies in E. Here 0.2/0.3 = <b>2/3</b>; and P(F|E) = 0.2/0.6 = <b>1/3</b> (Ex 13.1 Q1).</p>'
          '<p>Facts: 0 ≤ P(E|F) ≤ 1; P(E′|F) = 1 − P(E|F); P((E ∪ F)|G) = P(E|G) + P(F|G) − P((E ∩ F)|G). The conditional probability P(E|F) is generally different from P(F|E).</p>',
          'Conditional probability: F becomes the new sample space',
          'P(E|F) = P(E and F)/P(F); F becomes the reduced sample space; P(E|F) = 0.2/0.3 = 2/3 and P(F|E) = 1/3 for P(E)=0.6, P(F)=0.3, P(E and F)=0.2',
          vb='0 0 300 200', hint='Restrict attention to F.')


def dice_conditional(deck):
    x0, y0, s = 40, 22, 38
    cell = lambda a, b, cls: f'<rect class="{cls}" x="{x0 + (b - 1) * s}" y="{y0 + (a - 1) * s}" width="{s - 3}" height="{s - 3}" rx="4"></rect>'
    base = ''.join(cell(a, b, 'f0') for a in range(1, 7) for b in range(1, 7))
    base += ''.join(f'<text class="num" x="{x0 + (b - 1) * s + 17}" y="{y0 - 6}">{b}</text><text class="num" x="{x0 - 10}" y="{y0 + (b - 1) * s + 20}">{b}</text>' for b in range(1, 7))
    base += '<text class="sm" x="270" y="8" text-anchor="end">red die →</text><text class="sm" x="4" y="14">black</text>'
    back = ''.join(cell(5, b, 'f2 fx d2') for b in range(1, 7)) + cell(5, 5, 'f4 fx d3') + cell(5, 6, 'f4 fx d3')
    back += '<text class="t2 fx d2" x="20" y="268">black = 5: 6 outcomes (new space)</text><text class="t4 fx d3" x="20" y="286">sum &gt; 9: (5,5), (5,6): 2/6 = 1/3</text>'
    mcard(deck, 'Ex 13.1 Q10(a) · reduced sample space', 'A black and a red die are rolled. Find P(sum greater than 9 | the black die shows 5).', base, back,
          '<p>Given “black = 5”, only the <b>6 outcomes in that row</b> remain, equally likely. Sums greater than 9 occur for red = 5 and 6 (sums 10 and 11): <b>2 of 6 = 1/3</b>.</p>'
          '<p>Formula check: P(E ∩ F) = 2/36, P(F) = 6/36, so P(E|F) = 2/6. For (b), given red &lt; 4, the sum 8 needs (6, 2) or (5, 3): 2 of 18 outcomes, <b>1/9</b>.</p>',
          'Conditional probability by counting the reduced sample space',
          'Given black die 5, the sample space is the 6 outcomes with black=5; sum>9 happens for red=5,6 so probability 2/6 = 1/3; part (b): sum 8 given red<4 is 2/18 = 1/9',
          vb='0 0 300 296', hint='Only look at the row where the black die is 5.')


def independence_area(deck):
    base = ('<rect class="f0" x="30" y="30" width="240" height="120"></rect>'
            '<text class="lbl" x="150" y="20" text-anchor="middle">A: head (½)</text><text class="lbl" x="18" y="95" text-anchor="end">B</text>')
    back = ('<line class="c1 fx d2" x1="150" y1="30" x2="150" y2="150"></line><line class="c3 fx d2" x1="30" y1="130" x2="270" y2="130"></line>'
            '<rect class="f4 fx d3" x="30" y="130" width="120" height="20"></rect>'
            '<text class="t1 fx d2" x="90" y="80" text-anchor="middle">P(A) = 1/2</text><text class="t3 fx d2" x="210" y="145" text-anchor="middle">P(B) = 1/6</text>'
            '<text class="t4 fx d3" x="150" y="176" text-anchor="middle">P(A ∩ B) = 1/2 · 1/6 = 1/12 = P(A)P(B)</text>')
    mcard(deck, 'Independent events', 'A fair coin and a fair die are tossed. A: “head”, B: “3 on the die”. Are A and B independent?', base, back,
          '<p>Events are <b>independent</b> if <b>P(E ∩ F) = P(E) P(F)</b>, equivalently P(E|F) = P(E): learning that F happened does not change the chance of E. On the unit square, the overlap area equals the product of the two side lengths.</p>'
          '<p>Here P(A ∩ B) = 1/12 = (1/2)(1/6): independent (Ex 13.2 Q4). Independence is <b>not</b> the same as mutually exclusive: exclusive events with positive probabilities are dependent (P(A ∩ B) = 0 ≠ P(A)P(B)).</p>',
          'Independent events: P(E ∩ F) = P(E)P(F)',
          'E,F independent iff P(E and F) = P(E)P(F) iff P(E|F) = P(E); coin head and die 3 are independent (1/12 = 1/2 * 1/6); independent is different from mutually exclusive',
          vb='0 0 300 190', hint='Compare the overlap with the product of the two probabilities.')


def bayes_frequencies(deck):
    base = ('<rect class="f0" x="20" y="30" width="260" height="34" rx="4"></rect><text class="lbl" x="150" y="52" text-anchor="middle">100 000 people</text>')
    back = ('<rect class="f2 fx d2" x="20" y="90" width="12" height="34" rx="2"></rect><rect class="f1 fx d2" x="36" y="90" width="244" height="34" rx="2"></rect>'
            '<text class="t2 fx d2" x="26" y="82">100 diseased (0.1%)</text><text class="t1 fx d2" x="280" y="82" text-anchor="end">99 900 healthy</text>'
            '<rect class="f2 fx d3" x="20" y="150" width="12" height="30" rx="2"></rect><rect class="f4 fx d3" x="36" y="150" width="36" height="30" rx="2"></rect>'
            '<text class="t2 fx d3" x="20" y="146">99 test +</text><text class="t4 fx d3" x="80" y="172">≈ 500 false +</text>'
            '<text class="t3 fx d4" x="150" y="204" text-anchor="middle">P(disease | positive) = 99/(99 + 500) ≈ 22/133 ≈ 16.5%</text>')
    mcard(deck, 'Bayes\' theorem in natural frequencies', 'A test detects the disease 99% of the time, but gives a false positive for 0.5% of healthy people. If 0.1% of people have the disease, what is P(disease | test positive)?', base, back,
          '<p>Think of 100 000 people: 100 have the disease and 99 of them test positive; of the 99 900 healthy people about 0.5% ≈ 500 also test positive. Among ≈ 599 positives only 99 are ill: <b>99/599 ≈ 16.5%</b>. Exactly: 0.001·0.99/(0.001·0.99 + 0.999·0.005) = <b>22/133</b> (Ex 13.3 Q5).</p>'
          '<p><b>Bayes’ theorem:</b> P(Eᵢ|A) = P(Eᵢ)P(A|Eᵢ)/Σⱼ P(Eⱼ)P(A|Eⱼ). A rare disease means most positives are false alarms, even for a good test.</p>',
          'Bayes: why rare-disease tests give many false positives',
          'Bayes theorem P(Ei|A) = P(Ei)P(A|Ei)/sum P(Ej)P(A|Ej); with prevalence 0.1%, sensitivity 99% and false positive 0.5%, P(disease | +) = 22/133 = 16.5%',
          vb='0 0 300 216', hint='Imagine a population of 100 000 people.')


def total_probability_tree(deck):
    base = '<circle class="f0" cx="20" cy="100" r="7"></circle>'
    back = ('<line class="c0 fx d1" x1="26" y1="100" x2="100" y2="50"></line><line class="c0 fx d1" x1="26" y1="100" x2="100" y2="150"></line>'
            '<text class="lbl fx d1" x="46" y="66">A: 0.6</text><text class="lbl fx d1" x="46" y="146">B: 0.4</text>'
            '<line class="c2 fx d2" x1="106" y1="50" x2="200" y2="30"></line><line class="c0 fx d2" x1="106" y1="50" x2="200" y2="70"></line>'
            '<line class="c2 fx d2" x1="106" y1="150" x2="200" y2="130"></line><line class="c0 fx d2" x1="106" y1="150" x2="200" y2="170"></line>'
            '<text class="t2 fx d2" x="206" y="34">defective 0.012</text><text class="sm fx d2" x="206" y="74">good 0.588</text>'
            '<text class="t2 fx d2" x="206" y="134">defective 0.004</text><text class="sm fx d2" x="206" y="174">good 0.396</text>'
            '<text class="t4 fx d3" x="150" y="196" text-anchor="middle">P(B | defective) = 0.004/(0.012 + 0.004) = 1/4</text>')
    mcard(deck, 'Probability tree', 'Machine A makes 60% of the items (2% defective) and machine B makes 40% (1% defective). An item chosen at random is defective. What is the probability that it came from B?', base, back,
          '<p><b>Total probability:</b> P(defective) = 0.6 × 0.02 + 0.4 × 0.01 = 0.012 + 0.004 = 0.016 (multiply along a branch, add the branches that lead to “defective”).</p>'
          '<p><b>Bayes:</b> P(B | defective) = 0.004/0.016 = <b>1/4</b> (Ex 13.3 Q8). Reading a tree: the probability of a full path is the product of its branch probabilities; conditional probabilities are “branch ÷ total”.</p>',
          'Tree diagram: total probability and Bayes',
          'Total probability P(A) = sum P(Ei)P(A|Ei); Bayes P(Ei|A) = P(Ei)P(A|Ei)/P(A); machines A (60%,2%) and B (40%,1%): P(B|defective) = 1/4',
          vb='0 0 300 208', hint='Multiply along the branches, add the two defective paths.')
