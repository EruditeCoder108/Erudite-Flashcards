"""Animated physics cards (Physics 11 and 12), built on the showcase.py blueprint theme.

Same sanitiser rules as showcase.py: no inline style attributes, no scripts, no SMIL
(<animate> is stripped), no gradients. Motion is done with CSS keyframes on classes;
inside an SVG, CSS px = SVG user units, so translate(40px, 0) moves 40 viewBox units.
Keep text >= 10.5 units in a 300-wide viewBox so it reads on a phone.
"""
from showcase import BLUEPRINT, ARROW_DEFS, _card

PHY = BLUEPRINT + """
.bp .obj{fill:#3aa0ff;stroke:#e7f0ff;stroke-width:1.2}
.bp .obj2{fill:#ffd166;stroke:#fff3c4;stroke-width:1.2}
.bp .obj3{fill:#80e8a8;stroke:#e7fff0;stroke-width:1.2}
.bp .ghost{fill:none;stroke:#9fc2ee;stroke-width:1;stroke-dasharray:3 3;opacity:.7}
.bp .tk{stroke:#cfe0f7;stroke-width:1}.bp .tkb{stroke:#fff;stroke-width:1.6}
.bp .num{fill:#e7f0ff;font-size:11px;text-anchor:middle}
.bp .sm{fill:#9fc2ee;font-size:10.5px}
.bp .yl{fill:#ffd166;font-size:12px;font-weight:700}.bp .gr{fill:#80e8a8;font-size:12px;font-weight:700}
.bp .rd{fill:#ff8a80;font-size:12px;font-weight:700}.bp .pu{fill:#c9a7ff;font-size:12px;font-weight:700}
.bp .c2{stroke:#80e8a8;stroke-width:3;fill:none;stroke-linecap:round;stroke-linejoin:round}
.bp .c3{stroke:#ff8a80;stroke-width:3;fill:none;stroke-linecap:round;stroke-linejoin:round}
.bp .c4{stroke:#c9a7ff;stroke-width:2.6;fill:none;stroke-linecap:round;stroke-linejoin:round}
.bp .zone{fill:rgba(255,209,102,.16);stroke:#ffd166;stroke-width:1.2}
.bp .zone2{fill:rgba(128,232,168,.14);stroke:#80e8a8;stroke-width:1.2}
.bp .lens{fill:rgba(14,42,71,.92);stroke:#ffd166;stroke-width:2}
.bp .dot{fill:#ffd166}.bp .dot2{fill:#80e8a8}.bp .dot3{fill:#ff8a80}
.bp .grid{stroke:rgba(159,194,238,.25);stroke-width:1}
.bp .chips{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 0}
.bp .chips span{padding:4px 9px;border-radius:999px;background:rgba(255,209,102,.14);color:#ffe7a3;font-size:12px;font-weight:650}
.bp .loop{animation-iteration-count:infinite}
.bp .slide{animation:slide 1.4s cubic-bezier(.2,.8,.2,1) both .2s}
@keyframes slide{from{transform:translateX(-150px);opacity:.2}to{transform:none;opacity:1}}
"""


def anim(deck, tag, q, svg_front, svg_back, note_html, term, definition, css='', hint='Think it through, then flip.', vb='0 0 300 200'):
    """One blueprint card: same question on both faces; the back adds the animated layer and a note."""
    front = (f'<div class="w bp"><p class="tag">{tag}</p><h2>{q}</h2>'
             f'<svg viewBox="{vb}">{ARROW_DEFS}{svg_front}</svg><p class="hint">{hint}</p></div>')
    back = (f'<div class="w bp"><p class="tag">{tag}</p><h2>{q}</h2>'
            f'<svg viewBox="{vb}">{ARROW_DEFS}{svg_front}{svg_back}</svg>'
            f'<div class="eq fx d5">{note_html}</div></div>')
    _card(deck, term, definition, PHY + css, front, back)


def keyframes(name, pts, dur, extra='linear', delay=0.2, loop=True):
    """CSS for a class `name` that walks through (x, y) points in equal time steps."""
    n = len(pts) - 1
    frames = ''.join(f'{100 * i / n:.2f}%{{transform:translate({x:.1f}px,{y:.1f}px)}}' for i, (x, y) in enumerate(pts))
    it = 'infinite' if loop else '1'
    return (f'.bp .{name}{{animation:{name} {dur}s {extra} {delay}s {it} both}}'
            f'@keyframes {name}{{{frames}}}')


# ---------------------------------------------------------------- Ch 1 Units and measurement
def ruler_sig_figs(deck):
    x0, s = 20, 50  # 1 cm = 50 units
    ticks = ''
    for mm in range(0, 51):
        x = x0 + mm * s / 10
        h = 16 if mm % 10 == 0 else (11 if mm % 5 == 0 else 7)
        ticks += f'<line class="{"tkb" if mm % 10 == 0 else "tk"}" x1="{x:.1f}" y1="110" x2="{x:.1f}" y2="{110 + h}"></line>'
        if mm % 10 == 0:
            ticks += f'<text class="num" x="{x:.1f}" y="140">{mm // 10}</text>'
    base = ('<rect class="ghost" x="14" y="104" width="262" height="44" rx="4"></rect>' + ticks +
            '<text class="sm" x="268" y="160" text-anchor="end">cm (least count 1 mm)</text>'
            f'<rect class="obj slide" x="{x0}" y="80" width="{2.87 * s:.1f}" height="24" rx="3"></rect>')
    end = x0 + 2.87 * s
    back = (f'<line class="guide fx d2" x1="{end:.1f}" y1="70" x2="{end:.1f}" y2="130"></line>'
            f'<rect class="zone fx d2" x="{x0 + 2.8 * s:.1f}" y="106" width="{0.1 * s:.1f}" height="22"></rect>'
            '<text class="gr fx d3" x="60" y="40">2 . 8 → read off marks</text>'
            '<text class="gr fx d3" x="60" y="56">(certain)</text>'
            f'<text class="yl fx d4" x="{end + 6:.1f}" y="72">7 ← guessed</text>'
            '<text class="yl fx d4" x="196" y="88">(first uncertain)</text>')
    anim(deck, 'Significant figures · intuition',
         'A ruler has mm marks. The rod ends between 2.8 and 2.9 cm. How should you report it, and how many significant figures?',
         base, back,
         '<p>Report <b>2.87 cm</b>: the reliable digits (2, 8) plus <b>one</b> estimated digit (7) → <b>3 significant figures</b>.</p>'
         '<p>Writing 2.8734 cm would claim precision the ruler does not have.</p>',
         'Significant figures: reliable digits + first uncertain digit',
         'Report 2.87 cm: certain digits 2, 8 plus one estimated digit 7, so 3 significant figures')


# ---------------------------------------------------------------- Ch 2 Motion in a straight line
def _varrow(length, cls, marker):
    """Vertical arrow from (0, 0) upward by `length` (negative = downward), drawn in local coordinates."""
    return f'<line class="{cls}" x1="0" y1="0" x2="0" y2="{-length}" marker-end="url(#{marker})"></line>'


def vertical_throw(deck):
    T, H, n = 3.2, 140, 24          # flight time (s of animation), max rise in units, frames
    pts = [(0, -H * 4 * (i / n) * (1 - i / n)) for i in range(n + 1)]   # y = parabola in time
    css = (keyframes('mv', pts, T, 'linear', 0.3) +
           '.bp .vel{transform-origin:0 0;animation:vel ' + str(T) + 's linear .3s infinite both}'
           '@keyframes vel{from{transform:scaleY(1)}to{transform:scaleY(-1)}}'
           '.bp .ball{fill:#ffd166;stroke:#fff3c4;stroke-width:1.5}')
    ground = ('<line class="road" x1="20" y1="196" x2="280" y2="196"></line>'
              '<line class="guide" x1="110" y1="46" x2="190" y2="46"></line>'
              '<text class="sm" x="196" y="50">top</text>')
    static_ball = '<g transform="translate(150,186)"><circle class="ball" cx="0" cy="0" r="9"></circle></g>'
    moving = ('<g transform="translate(150,186)"><g class="mv">'
              f'<g class="vel">{_varrow(52, "f-n", "an")}</g>'
              '<line class="f-mg" x1="16" y1="0" x2="16" y2="34" marker-end="url(#am)"></line>'
              '<circle class="ball" cx="0" cy="0" r="9"></circle></g></g>'
              '<text class="gr" x="22" y="80">v (green): shrinks,</text><text class="gr" x="22" y="96">0 at top, then flips</text>'
              '<text class="rd" x="196" y="120">a = g (red):</text><text class="rd" x="196" y="136">never changes</text>')
    q = 'A ball is thrown straight up. At the top, its velocity is zero. Is its acceleration zero there too?'
    front = (f'<div class="w bp"><p class="tag">Free fall · intuition</p><h2>{q}</h2>'
             f'<svg viewBox="0 0 300 205">{ARROW_DEFS}{ground}{static_ball}</svg><p class="hint">Picture the velocity arrow on the way up and down.</p></div>')
    back = (f'<div class="w bp"><p class="tag">Free fall · intuition</p><h2>{q}</h2>'
            f'<svg viewBox="0 0 300 205">{ARROW_DEFS}{ground}{moving}</svg>'
            '<div class="eq fx d3"><p><b>No.</b> a = g downward at every instant, including the top.</p>'
            '<p>If a were 0 at the top, v would stay 0 and the ball would hang in the air. '
            'Zero velocity ≠ zero acceleration.</p></div></div>')
    _card(deck, 'Ball thrown up: velocity and acceleration at the top',
          'At the top v = 0 but a = g downward; velocity shrinks, passes through zero and reverses while a stays constant', PHY + css, front, back)


def odd_numbers_strobe(deck):
    unit = 6.2
    dots, braces = '', ''
    for k in range(6):
        y = 22 + unit * k * k
        dots += f'<circle class="dot fx d{k + 1}" cx="90" cy="{y:.1f}" r="7"></circle>'
        dots += f'<text class="sm fx d{k + 1}" x="62" y="{y + 4:.1f}" text-anchor="end">{k}τ</text>'
        if k:
            y0 = 22 + unit * (k - 1) ** 2
            braces += (f'<line class="guide fx d{k + 1}" x1="112" y1="{y0:.1f}" x2="112" y2="{y:.1f}"></line>'
                       f'<text class="yl fx d{k + 1}" x="124" y="{(y0 + y) / 2 + 4:.1f}">{2 * k - 1} units</text>')
    q = 'A stone falls from rest. Distances covered in successive equal time intervals are in what ratio?'
    front = (f'<div class="w bp"><p class="tag">Galileo’s law of odd numbers</p><h2>{q}</h2>'
             '<svg viewBox="0 0 300 180"><circle class="dot" cx="90" cy="22" r="7"></circle>'
             '<line class="road" x1="40" y1="178" x2="260" y2="178"></line></svg><p class="hint">Flash a strobe every τ seconds.</p></div>')
    back = (f'<div class="w bp"><p class="tag">Galileo’s law of odd numbers</p><h2>{q}</h2>'
            f'<svg viewBox="0 0 300 180">{dots}{braces}<line class="road" x1="40" y1="178" x2="260" y2="178"></line></svg>'
            '<div class="eq fx d6"><p><b>1 : 3 : 5 : 7 : 9 …</b></p>'
            '<p>Positions after τ, 2τ, 3τ… are ∝ 1, 4, 9, 16 (y = ½gt²); the gaps are the differences: 1, 3, 5, 7.</p></div></div>')
    _card(deck, "Galileo's law of odd numbers (free fall)",
          'Distances in successive equal intervals from rest are 1 : 3 : 5 : 7…, because total distance ∝ t² (1, 4, 9, 16…)', PHY, front, back)


def relative_velocity_1d(deck):
    css = ('.bp .road2{stroke:#9fc2ee;stroke-width:1.2;stroke-dasharray:10 10}'
           '.bp .ca{animation:ca 3s linear infinite}.bp .cb{animation:cb 3s linear infinite}'
           '.bp .rb{animation:rb 3s linear infinite}.bp .dash{animation:dash 3s linear infinite}'
           '@keyframes ca{from{transform:translateX(0)}to{transform:translateX(200px)}}'
           '@keyframes cb{from{transform:translateX(40px)}to{transform:translateX(190px)}}'
           '@keyframes rb{from{transform:translateX(40px)}to{transform:translateX(-10px)}}'
           '@keyframes dash{from{stroke-dashoffset:0}to{stroke-dashoffset:200}}')
    def car(cls, x, y, body, label):
        return (f'<g class="{cls}"><rect class="{body}" x="{x}" y="{y}" width="38" height="16" rx="5"></rect>'
                f'<text class="num" x="{x + 19}" y="{y + 12}">{label}</text></g>')
    top = ('<text class="sm" x="10" y="16">Seen from the ground</text>'
           '<line class="road" x1="10" y1="62" x2="290" y2="62"></line>' +
           car('ca', 10, 44, 'obj', 'A') + car('cb', 10, 24, 'obj2', 'B') +
           '<text class="lbl" x="290" y="80" text-anchor="end">A: 20 m/s   B: 15 m/s →</text>')
    bot = ('<text class="sm" x="10" y="112">Seen from car A</text>'
           '<line class="road2 dash" x1="10" y1="158" x2="290" y2="158"></line>' +
           car('', 130, 140, 'obj', 'A') + car('rb', 130, 120, 'obj2', 'B') +
           '<text class="lbl" x="290" y="176" text-anchor="end">A still; B drifts back at 5 m/s</text>')
    q = 'Car A moves at 20 m/s and car B at 15 m/s, same direction. What is the velocity of B relative to A?'
    front = (f'<div class="w bp"><p class="tag">Relative velocity · 1D</p><h2>{q}</h2>'
             f'<svg viewBox="0 0 300 185">{top}</svg><p class="hint">Imagine sitting in car A.</p></div>')
    back = (f'<div class="w bp"><p class="tag">Relative velocity · 1D</p><h2>{q}</h2>'
            f'<svg viewBox="0 0 300 185">{top}{bot}</svg>'
            '<div class="eq fx d3"><p><b>v<sub>BA</sub> = v<sub>B</sub> − v<sub>A</sub> = 15 − 20 = −5 m/s</b></p>'
            '<p>From A, B appears to move backward at 5 m/s (and the road rushes back at 20 m/s).</p></div></div>')
    _card(deck, 'Relative velocity of B with respect to A (same direction)',
          'v_BA = v_B − v_A = 15 − 20 = −5 m/s: B appears to move backward at 5 m/s as seen from A', PHY + css, front, back)
