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


def anim(deck, tag, q, svg_front, svg_back, note_html, term, definition, css='', hint='Think it through, then flip.', vb='0 0 300 200', front_only=''):
    """One blueprint card: same question on both faces; the back adds the animated layer and a note.
    `front_only` is SVG shown on the front but not the back (e.g. a static object that moves on the back)."""
    front = (f'<div class="w bp"><p class="tag">{tag}</p><h2>{q}</h2>'
             f'<svg viewBox="{vb}">{ARROW_DEFS}{svg_front}{front_only}</svg><p class="hint">{hint}</p></div>')
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


# ---------------------------------------------------------------- Ch 3 Motion in a plane
def projectile_shadows(deck):
    ox, oy, R, H, n, T = 40, 172, 220, 118, 30, 3.0
    fr = [i / n for i in range(n + 1)]
    css = (keyframes('pb', [(R * f, -4 * H * f * (1 - f)) for f in fr], T, 'linear', 0.4) +
           keyframes('px', [(R * f, 0) for f in fr], T, 'linear', 0.4) +
           keyframes('py', [(0, -4 * H * f * (1 - f)) for f in fr], T, 'linear', 0.4))
    path = ' '.join(f'{ox + R * f:.1f},{oy - 4 * H * f * (1 - f):.1f}' for f in fr)
    base = (f'<line class="ax" x1="{ox - 12}" y1="{oy}" x2="{ox + R + 25}" y2="{oy}" marker-end="url(#ah)"></line>'
            f'<line class="ax" x1="{ox - 12}" y1="{oy + 10}" x2="{ox - 12}" y2="30" marker-end="url(#ah)"></line>'
            f'<text class="lbl" x="{ox + R + 22}" y="{oy + 16}" text-anchor="end">x</text><text class="lbl" x="{ox - 4}" y="38">y</text>'
            f'<polyline class="guide" points="{path}"></polyline>')
    back = (f'<g transform="translate({ox},{oy})"><circle class="dot pb" cx="0" cy="0" r="7"></circle></g>'
            f'<g transform="translate({ox},{oy + 12})"><circle class="dot3 px" cx="0" cy="0" r="5"></circle></g>'
            f'<g transform="translate({ox - 12},{oy})"><circle class="dot2 py" cx="0" cy="0" r="5"></circle></g>'
            f'<text class="rd" x="{ox + 60}" y="{oy + 26}">x-shadow: steady pace</text>'
            f'<text class="gr" x="{ox + 2}" y="26">y-shadow: up, stop, down (free fall)</text>')
    anim(deck, 'Projectile · independence of motions',
         'Watch the shadows of a projectile on the two axes. What kind of motion does each shadow do?',
         base, back,
         '<p>Horizontal: <b>uniform velocity</b> (aₓ = 0, vₓ = u cos θ).</p>'
         '<p>Vertical: <b>free fall</b> (aᵧ = −g), exactly like a ball thrown straight up with u sin θ.</p>'
         '<p>Both shadows share only the <b>time</b>.</p>',
         'Projectile = uniform horizontal motion + vertical free fall',
         'x-shadow moves uniformly (ax = 0); y-shadow rises and falls like a vertical throw (ay = −g); they share only time',
         css, hint='Imagine a light above and a light to the side.', vb='0 0 300 200')


def circular_arrows(deck):
    cx, cy, r = 150, 104, 72
    css = (f'.bp .spinr{{transform-origin:{cx}px {cy}px;animation:spinr 4s linear infinite .3s}}'
           '@keyframes spinr{from{transform:rotate(0deg)}to{transform:rotate(-360deg)}}')
    base = (f'<circle class="ghost" cx="{cx}" cy="{cy}" r="{r}"></circle>'
            f'<circle class="dot" cx="{cx}" cy="{cy}" r="3"></circle>')
    still = f'<circle class="obj2" cx="{cx + r}" cy="{cy}" r="7"></circle>'
    back = (f'<g class="spinr"><line class="f-n" x1="{cx + r}" y1="{cy}" x2="{cx + r}" y2="{cy - 50}" marker-end="url(#an)"></line>'
            f'<line class="f-mg" x1="{cx + r}" y1="{cy}" x2="{cx + r - 40}" y2="{cy}" marker-end="url(#am)"></line>'
            f'<circle class="obj2" cx="{cx + r}" cy="{cy}" r="7"></circle></g>'
            '<text class="gr" x="8" y="20">v: tangent</text><text class="rd" x="8" y="36">a: to centre</text>')
    anim(deck, 'Uniform circular motion · intuition',
         'A ball goes round a circle at constant speed. Which way do its velocity and acceleration point, and is it accelerating at all?',
         base, back,
         '<p><b>v</b> is along the tangent; <b>a = v²/R</b> points to the centre, always ⟂ v.</p>'
         '<p>Speed is constant but the <b>direction</b> of v keeps turning, so the ball <b>is</b> accelerating. '
         'a has constant size but is <b>not a constant vector</b>.</p>',
         'Uniform circular motion: directions of v and a',
         'v tangent, a = v²/R towards the centre (perpendicular to v); acceleration exists because the direction of v changes',
         css, hint='Constant speed… so is a = 0?', vb='0 0 300 190', front_only=still)


def complementary_ranges(deck):
    import math
    ox, oy, L = 24, 178, 250          # L = u²/g in px
    cols = {15: 'curve', 75: 'curve', 30: 'c2', 60: 'c2', 45: 'c3'}
    delays = {45: .2, 30: .9, 60: 1.3, 15: 1.9, 75: 2.3}
    paths, css = '', ''
    for th in (45, 30, 60, 15, 75):
        t = math.radians(th); R = L * math.sin(2 * t)
        pts = ' '.join(f'{ox + x:.1f},{oy - (x * math.tan(t) - x * x / (2 * L * math.cos(t) ** 2)):.1f}'
                       for x in [R * i / 60 for i in range(61)])
        cls = f'r{th}'
        css += f'.bp .{cls}{{stroke-dasharray:100;stroke-dashoffset:100;animation:draw 1.2s ease forwards {delays[th]}s}}'
        paths += f'<polyline class="{cols[th]} {cls}" pathLength="100" points="{pts}"></polyline>'
    labels = ('<text class="yl fx d6" x="150" y="40" text-anchor="middle">15° &amp; 75°</text>'
              '<text class="gr fx d6" x="150" y="56" text-anchor="middle">30° &amp; 60°</text>'
              '<text class="rd fx d6" x="150" y="72" text-anchor="middle">45° (max R)</text>')
    base = f'<line class="road" x1="{ox - 6}" y1="{oy}" x2="{ox + L + 14}" y2="{oy}"></line>'
    anim(deck, 'Projectile · complementary angles',
         'Same launch speed at 15°, 30°, 45°, 60°, 75°. Which angles land at the same spot, and which goes farthest?',
         base, paths + labels,
         '<p>R = u² sin 2θ / g, and sin 2θ = sin(180° − 2θ), so <b>θ and 90° − θ give equal range</b>.</p>'
         '<p><b>45°</b> gives the maximum R = u²/g. The steeper twin goes higher and stays up longer.</p>',
         'Equal ranges for complementary angles; maximum at 45°',
         'R = u² sin 2θ / g: θ and 90° − θ give the same range; 45° gives the maximum u²/g', css, vb='0 0 300 190')


# ---------------------------------------------------------------- Ch 5 Work, energy and power
def spring_energy_bars(deck):
    import math
    T, A, n, rest = 3.0, 55, 24, 150          # period, amplitude, frames, block centre at rest
    xs = [A * math.cos(2 * math.pi * i / n) for i in range(n + 1)]
    def frames(name, fn):
        body = ''.join(f'{100 * i / n:.2f}%{{transform:{fn(x)}}}' for i, x in enumerate(xs))
        return f'@keyframes {name}{{{body}}}'
    sl = rest - 18 - 20                         # spring length at rest (wall x = 20, block half-width 18)
    css = ('.bp .blk{animation:blk 3s linear infinite .3s}'
           f'.bp .spr{{transform-origin:20px 0;animation:spr 3s linear infinite .3s}}'
           '.bp .pe,.bp .ke{transform-box:fill-box;transform-origin:50% 100%}'
           '.bp .pe{animation:pe 3s linear infinite .3s}.bp .ke{animation:ke 3s linear infinite .3s}'
           '.bp .pef{fill:#3aa0ff}.bp .kef{fill:#80e8a8}.bp .ef{fill:none;stroke:#ffd166;stroke-width:1.5;stroke-dasharray:4 3}'
           + frames('blk', lambda x: f'translateX({x:.1f}px)')
           + frames('spr', lambda x: f'scaleX({(sl + x) / sl:.3f})')
           + frames('pe', lambda x: f'scaleY({max(0.02, (x / A) ** 2):.3f})')
           + frames('ke', lambda x: f'scaleY({max(0.02, 1 - (x / A) ** 2):.3f})'))
    zig = ' '.join(f'{20 + sl * i / 12:.1f},{60 + (0 if i in (0, 12) else (-9 if i % 2 else 9))}' for i in range(13))
    base = ('<line class="road" x1="20" y1="20" x2="20" y2="80"></line><line class="road" x1="20" y1="80" x2="290" y2="80"></line>'
            f'<line class="guide" x1="{rest}" y1="28" x2="{rest}" y2="86"></line><text class="sm" x="{rest}" y="98" text-anchor="middle">x = 0</text>'
            f'<text class="sm" x="{rest - A}" y="98" text-anchor="middle">−A</text><text class="sm" x="{rest + A}" y="98" text-anchor="middle">+A</text>'
            '<line class="ax" x1="80" y1="190" x2="260" y2="190"></line>')
    still = (f'<polyline class="curve" points="{zig}" transform="translate(0,0)"></polyline>'
             f'<rect class="obj" x="{rest - 18}" y="44" width="36" height="34" rx="4"></rect>')
    back = (f'<g class="spr"><polyline class="curve" points="{zig}"></polyline></g>'
            f'<g class="blk"><rect class="obj" x="{rest - 18}" y="44" width="36" height="34" rx="4"></rect></g>'
            '<rect class="ef" x="96" y="112" width="36" height="78"></rect><rect class="ef" x="166" y="112" width="36" height="78"></rect>'
            '<rect class="pef pe" x="96" y="112" width="36" height="78"></rect><rect class="kef ke" x="166" y="112" width="36" height="78"></rect>'
            '<text class="lbl" x="114" y="204" text-anchor="middle">PE ½kx²</text><text class="lbl" x="184" y="204" text-anchor="middle">KE ½mv²</text>'
            '<text class="yl" x="214" y="120">total E</text><text class="yl" x="214" y="134">constant</text>')
    anim(deck, 'Spring · energy exchange',
         'A block on a smooth floor oscillates on a spring between −A and +A. How do its KE and PE change, and where is it fastest?',
         base, back,
         '<p>At ±A: all <b>PE</b> (½kA²), v = 0. At x = 0: all <b>KE</b>, speed maximum v = A√(k/m).</p>'
         '<p>K + V = ½kA² stays constant: the two parabolas of Fig. 5.8 are mirror images.</p>',
         'Spring–block: KE and PE exchange, total constant',
         'At the ends all PE and v = 0; at x = 0 all KE and v max = A√(k/m); K + V = ½kA² constant',
         css, hint='Picture two bars, KE and PE.', vb='0 0 300 210', front_only=still)


def collision_1d(deck):
    css = ('.bp .ea{animation:ea 4s linear infinite .3s}.bp .eb{animation:eb 4s linear infinite .3s}'
           '.bp .ia{animation:ia 4s linear infinite .3s}.bp .ib{animation:ib 4s linear infinite .3s}'
           '@keyframes ib{0%,40%{transform:translateX(0)}80%{transform:translateX(55px)}100%{transform:translateX(55px)}}'
           '@keyframes ea{0%{transform:translateX(0)}40%{transform:translateX(110px)}100%{transform:translateX(110px)}}'
           '@keyframes eb{0%,40%{transform:translateX(0)}80%{transform:translateX(110px)}100%{transform:translateX(110px)}}'
           '@keyframes ia{0%{transform:translateX(0)}40%{transform:translateX(110px)}80%{transform:translateX(165px)}100%{transform:translateX(165px)}}')
    base = ('<text class="sm" x="10" y="18">Elastic, equal masses</text><line class="road" x1="10" y1="62" x2="290" y2="62"></line>'
            '<text class="sm" x="10" y="108">Completely inelastic, equal masses</text><line class="road" x1="10" y1="152" x2="290" y2="152"></line>')
    still = ('<circle class="obj" cx="30" cy="50" r="11"></circle><circle class="obj2" cx="162" cy="50" r="11"></circle>'
             '<circle class="obj" cx="30" cy="140" r="11"></circle><circle class="obj2" cx="162" cy="140" r="11"></circle>'
             '<text class="lbl" x="30" y="84" text-anchor="middle">v →</text><text class="lbl" x="162" y="84" text-anchor="middle">at rest</text>')
    back = ('<g class="ea"><circle class="obj" cx="30" cy="50" r="11"></circle></g><g class="eb"><circle class="obj2" cx="162" cy="50" r="11"></circle></g>'
            '<g class="ia"><circle class="obj" cx="30" cy="140" r="11"></circle></g>'
            '<g class="ib"><circle class="obj2" cx="162" cy="140" r="11"></circle></g>'
            '<text class="gr" x="290" y="80" text-anchor="end">A stops, B leaves with v</text>'
            '<text class="yl" x="290" y="170" text-anchor="end">stick together at v/2</text>')
    anim(deck, 'Collisions · 1D',
         'Ball A (speed v) hits an identical ball B at rest. What happens if the collision is elastic? If they stick together?',
         base, back,
         '<p><b>Elastic</b>: velocities exchange — A stops, B moves off with v. KE and momentum both conserved.</p>'
         '<p><b>Completely inelastic</b>: common velocity v/2 (momentum mv = 2m·v/2); half the KE is lost as heat and sound.</p>',
         'Equal masses: elastic exchange vs sticking together',
         'Elastic: A stops, B moves at v. Completely inelastic: both at v/2, half the KE lost', css,
         hint='Momentum is conserved in both.', vb='0 0 300 180', front_only=still)


# ---------------------------------------------------------------- Ch 6 Systems of particles and rotation
def rolling_wheel(deck):
    import math
    R, x0, cy = 28, 40, 132
    D = 2 * math.pi * R                      # one revolution = distance rolled (no slipping)
    css = (f'.bp .roll{{animation:roll 3.2s linear infinite .3s}}'
           f'@keyframes roll{{from{{transform:translateX(0)}}to{{transform:translateX({D:.1f}px)}}}}'
           '.bp .spin6{transform-box:fill-box;transform-origin:center;animation:spin6 3.2s linear infinite .3s}'
           '@keyframes spin6{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}'
           '.bp .rim{fill:rgba(58,160,255,.18);stroke:#cfe0f7;stroke-width:2}.bp .spk{stroke:#9fc2ee;stroke-width:1.4}')
    cyc = ' '.join(f'{x0 + R * (t - math.sin(t)):.1f},{cy + R - R * (1 - math.cos(t)):.1f}' for t in [2 * math.pi * i / 40 for i in range(41)])
    wheel = (f'<g class="spin6"><circle class="rim" cx="{x0}" cy="{cy}" r="{R}"></circle>'
             + ''.join(f'<line class="spk" x1="{x0}" y1="{cy}" x2="{x0 + R * math.cos(a):.1f}" y2="{cy + R * math.sin(a):.1f}"></line>' for a in [k * math.pi / 3 for k in range(6)])
             + f'<circle class="dot3" cx="{x0}" cy="{cy + R}" r="4.5"></circle></g>')
    arrows = (f'<line class="f-mg" x1="{x0}" y1="{cy - R}" x2="{x0 + 64}" y2="{cy - R}" marker-end="url(#am)"></line>'
              f'<line class="f-n" x1="{x0}" y1="{cy}" x2="{x0 + 32}" y2="{cy}" marker-end="url(#an)"></line>')
    base = (f'<line class="road" x1="10" y1="{cy + R}" x2="290" y2="{cy + R}"></line>')
    still = (f'<circle class="rim" cx="{x0}" cy="{cy}" r="{R}"></circle><circle class="dot3" cx="{x0}" cy="{cy + R}" r="4.5"></circle>')
    back = (f'<polyline class="guide" points="{cyc}"></polyline>'
            f'<g class="roll">{wheel}{arrows}</g>'
            '<text class="rd" x="150" y="40">top: 2v</text><text class="gr" x="150" y="56">centre: v</text>'
            '<text class="yl" x="150" y="72">contact point: 0</text>')
    anim(deck, 'Rolling motion · intuition',
         'A wheel rolls without slipping at speed v. How fast do its top, centre and contact point move? What path does a rim point trace?',
         base, back,
         '<p>Rolling = translation (v) + rotation (Rω = v). Top: v + v = <b>2v</b>; centre: <b>v</b>; contact: v − v = <b>0</b>.</p>'
         '<p>A rim point traces a <b>cycloid</b> (dashed) and touches the ground at rest each turn.</p>',
         'Rolling without slipping: speeds of top, centre and contact point',
         'Top moves at 2v, centre at v, contact point at 0 (v = Rω); a rim point traces a cycloid',
         css, hint='Rolling = sliding + spinning.', vb='0 0 300 180', front_only=still)


def spinning_arms(deck):
    def body(cx, arm, cls):
        return (f'<g class="{cls}"><line class="road" x1="{cx - arm}" y1="100" x2="{cx + arm}" y2="100"></line>'
                f'<circle class="obj2" cx="{cx - arm}" cy="100" r="7"></circle><circle class="obj2" cx="{cx + arm}" cy="100" r="7"></circle>'
                f'<circle class="obj" cx="{cx}" cy="100" r="16"></circle><circle class="dot3" cx="{cx}" cy="88" r="3"></circle></g>')
    css = ('.bp .slow{transform-box:fill-box;transform-origin:center;animation:sp 6s linear infinite .3s}'
           '.bp .fast{transform-box:fill-box;transform-origin:center;animation:sp 1.5s linear infinite .3s}'
           '@keyframes sp{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}')
    base = ('<circle class="ghost" cx="75" cy="100" r="64"></circle><circle class="ghost" cx="225" cy="100" r="64"></circle>'
            '<text class="lbl" x="75" y="186" text-anchor="middle">arms out</text><text class="lbl" x="225" y="186" text-anchor="middle">arms tucked in</text>')
    still = body(75, 58, '') + body(225, 22, '')
    back = (body(75, 58, 'slow') + body(225, 22, 'fast') +
            '<text class="yl" x="75" y="22" text-anchor="middle">I large → ω small</text>'
            '<text class="gr" x="225" y="22" text-anchor="middle">I small → ω large</text>')
    anim(deck, 'Conservation of angular momentum',
         'A person spins on a frictionless swivel chair holding two weights. What happens when the arms are pulled in?',
         base, back,
         '<p>No external torque → <b>L = Iω = constant</b>. Pulling the mass inward cuts I, so ω rises.</p>'
         '<p>Skaters, divers and dancers doing a pirouette use this. Rotational KE = L²/2I <b>increases</b>: the muscles do work pulling the arms in.</p>',
         'Arms in, spin faster: Iω = constant',
         'No external torque so Iω is constant; pulling arms in reduces I and increases ω (KE rises by the work of the muscles)',
         css, hint='What stays constant?', vb='0 0 300 195', front_only=still)


def explosion_cm(deck):
    ox, oy, Rg, H, n = 34, 170, 220, 118, 30
    fr = [i / n for i in range(n + 1)]
    cm = lambda f: (Rg * f, -4 * H * f * (1 - f))
    sep = lambda f: 150 * max(0.0, f - 0.5)
    css = (keyframes('cm', [cm(f) for f in fr], 3.4, 'linear', 0.3) +
           keyframes('f1', [(cm(f)[0] + sep(f), cm(f)[1]) for f in fr], 3.4, 'linear', 0.3) +
           keyframes('f2', [(cm(f)[0] - sep(f), cm(f)[1]) for f in fr], 3.4, 'linear', 0.3))
    path = ' '.join(f'{ox + cm(f)[0]:.1f},{oy + cm(f)[1]:.1f}' for f in fr)
    base = (f'<line class="road" x1="10" y1="{oy}" x2="290" y2="{oy}"></line><polyline class="guide" points="{path}"></polyline>'
            f'<text class="sm" x="{ox + Rg / 2}" y="{oy - H - 8}" text-anchor="middle">explodes at the top</text>')
    back = (f'<g transform="translate({ox},{oy})"><circle class="obj f1" cx="0" cy="0" r="6"></circle>'
            f'<circle class="obj3 f2" cx="0" cy="0" r="6"></circle>'
            f'<g class="cm"><line class="f-mg" x1="-6" y1="-6" x2="6" y2="6"></line><line class="f-mg" x1="-6" y1="6" x2="6" y2="-6"></line></g></g>'
            '<text class="rd" x="290" y="30" text-anchor="end">✕ = centre of mass</text>')
    anim(deck, 'Centre of mass · explosion',
         'A shell explodes into two equal pieces at the top of its path. What path does the centre of mass follow?',
         base, back,
         '<p>The explosion forces are <b>internal</b>; the only external force is still gravity (Mg).</p>'
         '<p>So Ma<sub>cm</sub> = Mg: the CM continues on the <b>same parabola</b> as if nothing happened.</p>',
         'Exploding projectile: path of the centre of mass',
         'Internal explosion forces do not affect the CM; with gravity alone acting, the CM continues on the original parabola',
         css, hint='Which forces are external?', vb='0 0 300 185')


# ---------------------------------------------------------------- Ch 7 Gravitation
def kepler_second_law(deck):
    import math
    a, e, cx, cy, n = 112, 0.6, 142, 96, 60
    b, c = a * math.sqrt(1 - e * e), a * e
    def pos(M):
        E = M
        for _ in range(30):
            E -= (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        return cx + a * math.cos(E), cy + b * math.sin(E)
    sx, sy = cx + c, cy                           # Sun at the right focus; perihelion is the right end
    p0 = pos(0)
    pts = [(x - p0[0], y - p0[1]) for x, y in (pos(2 * math.pi * i / n) for i in range(n + 1))]
    css = keyframes('kp', pts, 6.0, 'linear', 0.3)
    orbit = ' '.join(f'{cx + a * math.cos(t):.1f},{cy + b * math.sin(t):.1f}' for t in [2 * math.pi * i / 80 for i in range(81)])
    def wedge(m0, m1):
        arc = [pos(m0 + (m1 - m0) * k / 12) for k in range(13)]
        return f'{sx:.1f},{sy:.1f} ' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in arc)
    base = (f'<polyline class="guide" points="{orbit}"></polyline>'
            f'<circle class="dot" cx="{sx:.1f}" cy="{sy:.1f}" r="7"></circle><text class="yl" x="{sx:.1f}" y="{sy + 22:.1f}" text-anchor="middle">Sun</text>')
    still = f'<circle class="obj" cx="{p0[0]:.1f}" cy="{p0[1]:.1f}" r="6"></circle>'
    back = (f'<polygon class="zone" points="{wedge(-0.45, 0.45)}"></polygon>'
            f'<polygon class="zone2" points="{wedge(math.pi - 0.45, math.pi + 0.45)}"></polygon>'
            f'<g transform="translate({p0[0]:.1f},{p0[1]:.1f})"><circle class="obj kp" cx="0" cy="0" r="6"></circle></g>'
            '<text class="yl" x="292" y="30" text-anchor="end">near Sun: fast</text>'
            '<text class="gr" x="8" y="30">far: slow</text>')
    anim(deck, 'Kepler’s second law · intuition',
         'Why does a planet move fastest at perihelion and slowest at aphelion?',
         base, back,
         '<p>The two shaded wedges are swept in <b>equal times</b> and have <b>equal areas</b>: short and wide near the Sun, long and thin far away.</p>'
         '<p>Gravity is a central force, so <b>L = m r v⊥ is conserved</b>: small r → large v.</p>',
         'Law of areas: fast at perihelion, slow at aphelion',
         'Equal areas in equal times because L = mr v⊥ is conserved (central force); small r gives large speed',
         css, hint='Watch the speed, then think about angular momentum.', vb='0 0 300 190', front_only=still)


def newtons_cannon(deck):
    import math
    S, cx, cy, Re = 58, 150, 118, 0.86          # px per unit, centre, Earth radius (launch at r = 1)
    def path(v, tmax):
        x, y, vx, vy, dt, t, out = 0.0, 1.0, v, 0.0, 0.002, 0.0, [(0.0, 1.0)]
        while t < tmax:
            r3 = (x * x + y * y) ** 1.5
            vx -= x / r3 * dt; vy -= y / r3 * dt
            x += vx * dt; y += vy * dt; t += dt
            if int(t / dt) % 25 == 0:
                out.append((x, y))
            if x * x + y * y < Re * Re or abs(x) > 2.5 or y > 1.9 or y < -1.9:
                break
        return out
    runs = [('c3', 'dot3', 0.62, 'falls back', 3.0), ('curve', 'dot', 1.0, 'orbit: v = √(gR)', 6.3), ('c2', 'dot2', math.sqrt(2), 'escapes: √2 × orbit speed', 3.2)]
    base = (f'<circle class="obj" cx="{cx}" cy="{cy}" r="{Re * S:.1f}"></circle>'
            f'<polygon class="road" points="{cx - 8},{cy - Re * S + 2:.1f} {cx},{cy - S:.1f} {cx + 8},{cy - Re * S + 2:.1f}"></polygon>'
            '<text class="lbl" x="150" y="122" text-anchor="middle">Earth</text>')
    css, back, legend = '', '', ''
    for k, (cls, dcls, v, label, dur) in enumerate(runs):
        pts = path(v, 12.0)
        poly = ' '.join(f'{cx + S * x:.1f},{cy - S * y:.1f}' for x, y in pts)
        back += f'<polyline class="{cls}" points="{poly}" opacity=".55"></polyline>'
        rel = [(S * x, -S * (y - 1)) for x, y in pts]
        step = max(1, len(rel) // 50)
        rel = rel[::step] + [rel[-1]]
        css += keyframes(f'nc{k}', rel, dur, 'linear', 0.3)
        back += f'<g transform="translate({cx},{cy - S})"><circle class="{dcls} nc{k}" cx="0" cy="0" r="4.5"></circle></g>'
        legend += f'<text class="{["rd", "yl", "gr"][k]}" x="8" y="{186 + 0 * k}"></text>'
    back += ('<text class="rd" x="8" y="20">slow: falls back</text><text class="yl" x="8" y="36">√(gR) ≈ 7.9 km/s: orbits</text>'
             '<text class="gr" x="8" y="52">√(2gR) ≈ 11.2 km/s: escapes</text>')
    anim(deck, 'Orbits · Newton’s cannon',
         'A cannon on a very tall mountain fires horizontally, faster each time. What happens to the ball?',
         base, back,
         '<p>Too slow: it falls back. At <b>v₀ = √(gR) ≈ 7.9 km/s</b> it keeps "falling around" the Earth: a circular orbit.</p>'
         '<p>At <b>vₑ = √(2gR) = √2 v₀ ≈ 11.2 km/s</b> its total energy is zero and it escapes.</p>',
         'Newton’s cannon: orbital speed vs escape speed',
         'Slow: falls back; v0 = √(gR) ≈ 7.9 km/s: circular orbit; ve = √(2gR) ≈ 11.2 km/s = √2 v0: escapes',
         css, hint='Faster and faster…', vb='0 0 300 195')


# ---------------------------------------------------------------- Ch 8 Mechanical properties of solids
def stress_strain_story(deck):
    axes = ('<line class="ax" x1="30" y1="175" x2="292" y2="175" marker-end="url(#ah)"></line>'
            '<line class="ax" x1="30" y1="175" x2="30" y2="14" marker-end="url(#ah)"></line>'
            '<text class="lbl" x="290" y="192" text-anchor="end">strain</text><text class="lbl" x="36" y="22">stress</text>')
    curve = ('<path class="curve draw" pathLength="100" d="M30 175 L58 70 C62 58 66 56 72 58 C110 66 150 40 200 30 C220 27 236 36 252 60"></path>'
             '<circle class="dot fx d1" cx="58" cy="70" r="4"></circle><text class="hi fx d1" x="46" y="66" text-anchor="end">A</text>'
             '<circle class="dot fx d2" cx="70" cy="57" r="4"></circle><text class="hi fx d2" x="70" y="48" text-anchor="middle">B</text>'
             '<circle class="dot fx d3" cx="200" cy="30" r="4"></circle><text class="hi fx d3" x="200" y="22" text-anchor="middle">D</text>'
             '<circle class="dot3 fx d4" cx="252" cy="60" r="4"></circle><text class="rd fx d4" x="258" y="64">E</text>'
             '<line class="guide fx d4" x1="120" y1="56" x2="148" y2="175"></line>'
             '<text class="sm fx d4" x="152" y="170">permanent set</text>'
             '<text class="lbl fx d1" x="62" y="130">Hooke’s law</text><text class="lbl fx d1" x="62" y="143">(elastic, linear)</text>'
             '<text class="lbl fx d3" x="150" y="90">plastic region</text>')
    anim(deck, 'Stress–strain curve · the story of a stretched wire',
         'A metal wire is loaded more and more until it snaps. Sketch stress vs strain and name the key points.',
         axes, curve,
         '<p><b>O–A</b>: linear, Hooke’s law (A = proportional limit). <b>B</b>: yield point / elastic limit (σᵧ).</p>'
         '<p>Beyond B, unloading leaves a <b>permanent set</b>. <b>D</b>: ultimate tensile strength (σᵤ). <b>E</b>: fracture. '
         'D and E far apart → <b>ductile</b>; close → <b>brittle</b>.</p>',
         'Stress–strain curve of a metal: O, A, B, D, E',
         'O–A linear (Hooke); B yield point/elastic limit; beyond B permanent set; D ultimate strength; E fracture; ductile if D, E far apart',
         hint='Label the points as you go.', vb='0 0 300 200')


# ---------------------------------------------------------------- Ch 9 Mechanical properties of fluids
def venturi_flow(deck):
    cy = 128
    def h(x):                                   # half-height of the pipe
        if x <= 100 or x >= 200:
            return 30.0
        import math
        return 30 - 18 * (1 - math.cos(2 * math.pi * (x - 100) / 100)) / 2
    top = ' '.join(f'{x},{cy - h(x):.1f}' for x in range(16, 285, 4))
    bot = ' '.join(f'{x},{cy + h(x):.1f}' for x in range(16, 285, 4))
    # time to travel: dt = dx / v, v ∝ 30 / h
    xs, ts, t = list(range(16, 285, 4)), [], 0.0
    for x in xs:
        ts.append(t); t += 4 * h(x) / 30
    T = 3.2
    css = ''
    dots = ''
    for li, lane in enumerate((-0.6, 0.0, 0.6)):
        for k in range(3):
            name = f'vf{li}{k}'
            # resample to equal time steps
            n, pts, j = 40, [], 0
            for i in range(n + 1):
                tt = ts[-1] * i / n
                while j < len(ts) - 2 and ts[j + 1] < tt:
                    j += 1
                f = (tt - ts[j]) / (ts[j + 1] - ts[j])
                x = xs[j] + 4 * f
                pts.append((x - 16, lane * h(x)))
            css += keyframes(name, pts, T, 'linear', -T * k / 3).replace('1 both', 'infinite both')
            dots += f'<g transform="translate(16,{cy})"><circle class="dot {name}" cx="0" cy="0" r="3.2"></circle></g>'
    tubes = ''
    for x, hh, cls in ((58, 58, 'zone2'), (150, 22, 'zone'), (242, 58, 'zone2')):
        base_y = cy - h(x)
        tubes += (f'<rect class="ghost" x="{x - 6}" y="{base_y - 70 - (30 - h(x)):.1f}" width="12" height="{70 + 30 - h(x):.1f}"></rect>'
                  f'<rect class="{cls} fx d3" x="{x - 6}" y="{base_y - hh - (30 - h(x)):.1f}" width="12" height="{hh + 30 - h(x):.1f}"></rect>')
    base = (f'<polyline class="road" points="{top}"></polyline><polyline class="road" points="{bot}"></polyline>'
            f'<text class="sm" x="58" y="{cy + 50}" text-anchor="middle">wide</text><text class="sm" x="150" y="{cy + 50}" text-anchor="middle">narrow</text>')
    back = (dots + tubes +
            '<text class="gr" x="58" y="18" text-anchor="middle">slow, high P</text>'
            '<text class="yl" x="150" y="18" text-anchor="middle">fast, low P</text>')
    anim(deck, 'Continuity + Bernoulli · venturi',
         'Water flows steadily through a pipe with a narrow section. Where is it fastest, and where is the pressure lowest?',
         base, back,
         '<p><b>Continuity</b>: Av = constant, so the fluid speeds up in the narrow part.</p>'
         '<p><b>Bernoulli</b> (same height): P + ½ρv² = constant, so faster flow means <b>lower pressure</b>: the column above the constriction is shortest.</p>',
         'Flow through a constriction: speed and pressure',
         'Av = constant so v is largest in the narrow part; P + ½ρv² = constant so pressure is lowest there',
         css, hint='Mass in = mass out.', vb='0 0 300 190')


def terminal_velocity(deck):
    import math
    n, T = 30, 3.6
    # v(t) = vt (1 − e^(−t/τ)); position y(t) = vt (t − τ(1 − e^(−t/τ)))
    tau, tmax = 0.8, 4.0
    ys = [60 * (t - tau * (1 - math.exp(-t / tau))) for t in [tmax * i / n for i in range(n + 1)]]
    scale = 128 / ys[-1]
    css = keyframes('tv', [(0, y * scale) for y in ys], T, 'linear', 0.3)
    css += ('.bp .oil{fill:rgba(255,209,102,.10);stroke:#9fc2ee;stroke-width:1.2}'
            '.bp .tvarr{transform-origin:0 0;animation:tvarr ' + str(T) + 's linear .3s infinite both}'
            '@keyframes tvarr{' + ''.join(f'{100 * i / 10:.0f}%{{transform:scaleY({max(0.02, 1 - math.exp(-tmax * i / 10 / tau)):.3f})}}' for i in range(11)) + '}')
    vt_curve = ' '.join(f'{170 + 115 * t / tmax:.1f},{160 - 100 * (1 - math.exp(-t / tau)):.1f}' for t in [tmax * i / 40 for i in range(41)])
    base = ('<rect class="oil" x="30" y="20" width="90" height="165" rx="6"></rect>'
            '<line class="ax" x1="170" y1="160" x2="292" y2="160" marker-end="url(#ah)"></line>'
            '<line class="ax" x1="170" y1="160" x2="170" y2="40" marker-end="url(#ah)"></line>'
            '<text class="lbl" x="290" y="176" text-anchor="end">t</text><text class="lbl" x="176" y="46">v</text>')
    still = '<circle class="obj2" cx="75" cy="36" r="8"></circle>'
    back = ('<g transform="translate(75,36)"><g class="tv"><circle class="obj2" cx="0" cy="0" r="8"></circle>'
            '<g class="tvarr"><line class="f-mg" x1="0" y1="10" x2="0" y2="42" marker-end="url(#am)"></line></g></g></g>'
            f'<polyline class="curve draw" pathLength="100" points="{vt_curve}"></polyline>'
            '<line class="guide fx d4" x1="170" y1="60" x2="290" y2="60"></line><text class="hi fx d4" x="288" y="54" text-anchor="end">v_t</text>'.replace('v_t', 'vₜ'))
    anim(deck, 'Viscosity · terminal velocity',
         'A small metal ball is dropped into a tall jar of oil. How does its speed change with time?',
         base, back,
         '<p>Speed rises, but the Stokes drag <b>6πηav</b> grows with it. When drag + buoyancy = weight, acceleration is zero: '
         '<b>vₜ = 2a²(ρ − σ)g / 9η</b>.</p><p>vₜ ∝ a²: bigger drops fall faster; more viscous oil → slower.</p>',
         'Ball in oil: approach to terminal velocity',
         'Speed rises to a constant terminal value when 6πηav + buoyancy = weight; vt = 2a²(ρ−σ)g/9η',
         css, hint='What force grows with speed?', vb='0 0 300 190', front_only=still)
