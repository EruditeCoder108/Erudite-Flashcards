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
