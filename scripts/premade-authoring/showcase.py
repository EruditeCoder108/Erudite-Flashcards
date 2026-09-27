"""Richer advanced-HTML cards: themed layouts, inline SVG and CSS animation.

Each card still asks one question with one answer. Rules the sanitiser imposes:
no inline style attributes (style with classes in the CSS), no scripts, no
external URLs, SVG limited to shapes/text/markers. KaTeX does not render in
advanced HTML, so maths uses Unicode.
"""
import math
from deckkit import _strip

BASE = """
.w{box-sizing:border-box;min-height:470px;padding:18px 16px 16px;border-radius:18px;
  font:14px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif}
.w svg{display:block;width:100%;height:auto;overflow:visible}
.w h2{margin:4px 0 12px;font-size:19px;line-height:1.25;font-weight:700}
.w .tag{margin:0;font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.w .fx{opacity:0;animation:fade .5s ease forwards}
.w .d1{animation-delay:.25s}.w .d2{animation-delay:.6s}.w .d3{animation-delay:.95s}
.w .d4{animation-delay:1.3s}.w .d5{animation-delay:1.65s}.w .d6{animation-delay:2s}
.w .draw{stroke-dasharray:100;stroke-dashoffset:100;animation:draw 1.8s ease forwards .2s}
@keyframes fade{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
@keyframes draw{to{stroke-dashoffset:0}}
"""

# ---------------------------------------------------------------- themes
BLUEPRINT = BASE + """
.w.bp{color:#e7f0ff;background:
  linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px) 0 0/18px 18px,
  linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px) 0 0/18px 18px,#0e2a47}
.bp .tag{color:#7fb4ff}.bp h2{color:#fff}
.bp .ax{stroke:#9fc2ee;stroke-width:1.4;fill:none}
.bp .lbl{fill:#cfe0f7;font-size:11px}
.bp .hi{fill:#ffd166;font-size:12px;font-weight:700}
.bp .curve{stroke:#ffd166;stroke-width:3;fill:none;stroke-linecap:round;stroke-linejoin:round}
.bp .guide{stroke:#7fb4ff;stroke-width:1;stroke-dasharray:4 4;fill:none}
.bp .road{stroke:#cfe0f7;stroke-width:2.5;fill:none}
.bp .car{fill:#3aa0ff;stroke:#e7f0ff;stroke-width:1.2}
.bp .f-mg{stroke:#ff8a80;stroke-width:3}.bp .f-n{stroke:#80e8a8;stroke-width:3}.bp .f-f{stroke:#ffd166;stroke-width:3}
.bp .f-a{stroke:#c9a7ff;stroke-width:2;stroke-dasharray:5 4}
.bp .t-mg{fill:#ff8a80;font-weight:700;font-size:13px}.bp .t-n{fill:#80e8a8;font-weight:700;font-size:13px}
.bp .t-f{fill:#ffd166;font-weight:700;font-size:13px}.bp .t-a{fill:#c9a7ff;font-size:11px}
.bp .eq{margin-top:10px;padding:10px 12px;border:1px solid rgba(127,180,255,.45);border-radius:12px;
  background:rgba(8,24,44,.65);font-size:14px}
.bp .eq b{color:#ffd166;font-weight:650}.bp .eq p{margin:2px 0}
.bp .hint{margin-top:10px;color:#9fc2ee;font-size:12.5px}
"""

CHALK = BASE + """
.w.cb{color:#f1f5ee;background:radial-gradient(120% 90% at 30% 10%,#27503f 0,#1b3a2f 60%,#15302a 100%)}
.cb .tag{color:#b8dcc4}.cb h2{color:#fff;font-family:Georgia,"Times New Roman",serif}
.cb .ax{stroke:#dfe9e2;stroke-width:1.3;fill:none}
.cb .tick{fill:#dfe9e2;font-size:11px;font-family:Georgia,serif;font-style:italic}
.cb .sin{stroke:#ffe08a;stroke-width:3;fill:none;stroke-linecap:round}
.cb .cos{stroke:#8fe3ff;stroke-width:2.6;fill:none;stroke-dasharray:7 5}
.cb .pt{fill:#ffe08a}.cb .pt2{fill:#8fe3ff}
.cb .say{fill:#ffe08a;font-size:11px;font-family:Georgia,serif}
.cb .say2{fill:#8fe3ff;font-size:11px;font-family:Georgia,serif}
.cb .key{display:flex;gap:14px;margin:8px 0 0;font-size:13px}
.cb .key i{font-style:normal}.cb .k1{color:#ffe08a}.cb .k2{color:#8fe3ff}
.cb .box{margin-top:10px;padding:10px 12px;border:1px dashed rgba(241,245,238,.45);border-radius:12px;font-size:13.5px}
.cb .box b{color:#ffe08a}
.cb .qg{display:grid;grid-template-columns:1fr 1fr;margin:6px 0 10px;border-radius:14px;overflow:hidden}
.cb .qg div{min-height:112px;padding:12px;display:flex;flex-direction:column;justify-content:space-between;
  background:rgba(255,255,255,.05)}
.cb .qg div:nth-child(1){border-right:2px solid #dfe9e2;border-bottom:2px solid #dfe9e2}
.cb .qg div:nth-child(2){border-bottom:2px solid #dfe9e2}
.cb .qg div:nth-child(3){border-right:2px solid #dfe9e2}
.cb .qg small{color:#b8dcc4;font-size:11px;letter-spacing:.06em;text-transform:uppercase}
.cb .qg b{font-size:18px;color:#ffe08a;font-family:Georgia,serif}
.cb .qg b.q{color:rgba(241,245,238,.35);letter-spacing:.2em}
"""

PETRI = BASE + """
.w.pt{color:#1d2b24;background:linear-gradient(160deg,#f3fbf6 0,#e3f4ea 55%,#d7eee2 100%)}
.pt .tag{color:#3f7a5a}.pt h2{color:#123a27}
.pt .steps{position:relative;display:flex;flex-direction:column;gap:9px;margin-top:4px}
.pt .steps:before{content:"";position:absolute;left:31px;top:24px;bottom:24px;width:2px;background:#9fd3b5}
.pt .st{position:relative;display:flex;align-items:center;gap:12px;padding:8px 10px;border-radius:14px;
  background:rgba(255,255,255,.85);box-shadow:0 1px 0 rgba(18,58,39,.08)}
.pt .st svg{flex:none;width:44px;height:44px}
.pt .st b{display:block;font-size:14.5px;color:#123a27}
.pt .st span{font-size:12.5px;color:#43594d}
.pt .st .n{color:#b3471d;font-weight:700}
.pt .blank b{color:#9cb3a6;letter-spacing:.2em}
.pt .wall{fill:#fff;stroke:#3f7a5a;stroke-width:2}
.pt .nA{fill:#e2562b}.pt .nB{fill:#2b7de2}.pt .n2{fill:#7a3fe2}.pt .sp{fill:#f2c14e;stroke:#b3871d}
.pt .ring{fill:none;stroke:#3f7a5a;stroke-width:1.6;stroke-dasharray:3 3}
"""

TILES = BASE + """
.w.tl{color:#1f2430;background:#f6f4ef}
.tl .tag{color:#7a7466}.tl h2{color:#1f2430}
.tl .grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.tl .t{border-radius:14px;padding:10px 11px 11px;background:#fff;border:1px solid #e8e1d2;min-height:88px;
  display:flex;flex-direction:column;gap:6px}
.tl .t.wide{grid-column:1 / -1;min-height:70px}
.tl .t i{font-style:normal;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
  padding:3px 8px;border-radius:999px;align-self:flex-start;color:#fff}
.tl .t b{font-size:14px;font-weight:600;line-height:1.3}
.tl .t b.q{color:#c9c0ad;letter-spacing:.25em}
.tl .t b.no{color:#c93b3f}
.tl .c1 i{background:#8b5cf6}.tl .c2 i{background:#0891b2}.tl .c3 i{background:#d97706}
.tl .c4 i{background:#16a34a}.tl .c5 i{background:#dc2626}
.tl .t b.r{animation:fade .45s ease both}
.tl .c2 b.r{animation-delay:.08s}.tl .c3 b.r{animation-delay:.16s}.tl .c4 b.r{animation-delay:.24s}.tl .c5 b.r{animation-delay:.32s}
"""

LAB = BASE + """
.w.lb{color:#e8edf5;background:linear-gradient(170deg,#141b2d 0,#101626 100%)}
.lb .tag{color:#67e8f9}.lb h2{color:#fff}
.lb .row{display:grid;grid-template-columns:44px 1fr;align-items:center;gap:8px;margin:7px 0}
.lb .row em{font-style:normal;font-weight:700;color:#fff}
.lb .bar{position:relative;height:22px;border-radius:7px;background:rgba(255,255,255,.07);overflow:hidden}
.lb .bar .fill{position:absolute;left:0;top:0;bottom:0;border-radius:7px;text-decoration:none;
  animation:grow 1.1s cubic-bezier(.2,.8,.2,1) both}
.lb .bar u{position:absolute;right:8px;top:2px;text-decoration:none;font-size:12px;font-weight:700;color:#fff}
.lb .e .fill{background:linear-gradient(90deg,#f59e0b,#fbbf24)}.lb .l .fill{background:linear-gradient(90deg,#0e7490,#0891b2)}
.lb .sec{margin-top:10px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:#94a3b8}
.lb .w1{width:100%}.lb .w2{width:53%}.lb .w3{width:17%}.lb .v1{width:77%}.lb .v2{width:85%}.lb .v3{width:100%}
.lb .chips{display:flex;gap:6px;margin:6px 0 2px}
.lb .chips span{padding:4px 9px;border-radius:999px;background:rgba(103,232,249,.12);color:#a5f3fc;font-size:12px;font-weight:650}
.lb .rule{margin-top:12px;padding:10px 12px;border-radius:12px;background:rgba(245,158,11,.12);color:#fde68a;font-size:13.5px}
.lb .q{color:#64748b;letter-spacing:.2em;font-weight:700}
.lb .orb{fill:rgba(103,232,249,.22);stroke:#67e8f9;stroke-width:1.4}
.lb .orbs{fill:rgba(251,191,36,.25);stroke:#fbbf24;stroke-width:1.4}
.lb .hy{fill:rgba(167,139,250,.3);stroke:#c4b5fd;stroke-width:1.4}.lb .hy.back{opacity:.45}
.lb .lbl{fill:#cbd5e1;font-size:11px}.lb .big{fill:#fff;font-size:15px;font-weight:700}
.lb .spin{transform-box:fill-box;transform-origin:center;animation:spin 1.2s cubic-bezier(.2,.8,.2,1) both}
.lb .spin.d2{animation-delay:.3s}.lb .spin.d3{animation-delay:.55s}.lb .spin.d4{animation-delay:.8s}.lb .spin.d5{animation-delay:1.05s}
@keyframes grow{from{width:0}}
@keyframes spin{from{opacity:0;transform:scale(.4) rotate(-40deg)}to{opacity:1;transform:none}}
"""


def _card(deck, term, definition, css, front, back):
    deck.advanced(term, definition, front, back, css)


# ---------------------------------------------------------------- physics
ARROW_DEFS = ('<defs>'
              '<marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
              '<path d="M0 0 L8 4 L0 8 Z" fill="#cfe0f7"></path></marker>'
              '<marker id="am" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
              '<path d="M0 0 L8 4 L0 8 Z" fill="#ff8a80"></path></marker>'
              '<marker id="an" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
              '<path d="M0 0 L8 4 L0 8 Z" fill="#80e8a8"></path></marker>'
              '<marker id="af" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
              '<path d="M0 0 L8 4 L0 8 Z" fill="#ffd166"></path></marker>'
              '<marker id="aa" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
              '<path d="M0 0 L8 4 L0 8 Z" fill="#c9a7ff"></path></marker>'
              '</defs>')


def friction_graph(deck):
    axes = ('<line class="ax" x1="30" y1="180" x2="290" y2="180" marker-end="url(#ah)"></line>'
            '<line class="ax" x1="30" y1="180" x2="30" y2="15" marker-end="url(#ah)"></line>'
            '<text class="lbl" x="288" y="198" text-anchor="end">applied force F</text>'
            '<text class="lbl" x="36" y="22">friction f</text>')
    curve = ('<path class="curve draw" pathLength="100" d="M30 180 L150 55 L160 88 L285 88"></path>'
             '<line class="guide fx d3" x1="150" y1="55" x2="150" y2="180"></line>'
             '<text class="hi fx d3" x="150" y="46" text-anchor="middle">limiting fₛ,max = μₛN</text>'
             '<text class="lbl fx d2" x="102" y="128" text-anchor="middle" transform="rotate(-46 102 128)">static: f = F</text>'
             '<text class="hi fx d4" x="222" y="80" text-anchor="middle">kinetic fₖ = μₖN</text>'
             '<text class="lbl fx d4" x="104" y="172" text-anchor="middle">at rest</text>'
             '<text class="lbl fx d5" x="222" y="172" text-anchor="middle">sliding</text>')
    q = 'How does friction change as the applied force F grows from zero?'
    front = (f'<div class="w bp"><p class="tag">Friction · graph</p><h2>{q}</h2>'
             f'<svg viewBox="0 0 300 205">{ARROW_DEFS}{axes}</svg>'
             '<p class="hint">Sketch it, then flip.</p></div>')
    back = (f'<div class="w bp"><p class="tag">Friction · graph</p><h2>{q}</h2>'
            f'<svg viewBox="0 0 300 205">{ARROW_DEFS}{axes}{curve}</svg>'
            '<div class="eq fx d5"><p>Static friction <b>matches F</b> until it reaches μₛN.</p>'
            '<p>Then the block slides and friction <b>drops</b> to μₖN (μₖ &lt; μₛ).</p></div></div>')
    _card(deck, 'Friction vs applied force graph',
          'Static friction rises with F up to μₛN, then drops to kinetic μₖN once sliding starts', BLUEPRINT, front, back)


def banked_road(deck):
    road = ('<line class="road" x1="15" y1="205" x2="290" y2="92"></line>'
            '<line class="road" x1="15" y1="205" x2="290" y2="205"></line>'
            '<path class="ax" d="M65 205 A50 50 0 0 0 61.3 186"></path>'
            '<text class="lbl" x="72" y="198">θ</text>'
            '<g transform="rotate(-22.3 150 150)"><rect class="car" x="126" y="128" width="48" height="21" rx="6"></rect>'
            '<rect class="car" x="136" y="120" width="26" height="11" rx="4"></rect></g>')
    forces = ('<line class="f-mg fx d1" x1="150" y1="140" x2="150" y2="200" marker-end="url(#am)"></line>'
              '<text class="t-mg fx d1" x="157" y="198">mg</text>'
              '<line class="f-n fx d2" x1="150" y1="140" x2="116" y2="57" marker-end="url(#an)"></line>'
              '<text class="t-n fx d2" x="100" y="55">N</text>'
              '<line class="f-f fx d3" x1="150" y1="140" x2="100" y2="160" marker-end="url(#af)"></line>'
              '<text class="t-f fx d3" x="84" y="172">f</text>'
              '<line class="f-a fx d4" x1="232" y1="40" x2="176" y2="40" marker-end="url(#aa)"></line>'
              '<text class="t-a fx d4" x="236" y="44">to centre</text>')
    q = 'Car on a banked curve, faster than v₀. Which forces act, and what gives the centripetal force?'
    front = (f'<div class="w bp"><p class="tag">Circular motion · banked road</p><h2>{q}</h2>'
             f'<svg viewBox="0 0 300 215">{ARROW_DEFS}{road}</svg>'
             '<p class="hint">Draw the forces, then write the horizontal and vertical equations.</p></div>')
    back = (f'<div class="w bp"><p class="tag">Circular motion · banked road</p><h2>{q}</h2>'
            f'<svg viewBox="0 0 300 215">{ARROW_DEFS}{road}{forces}</svg>'
            '<div class="eq fx d5"><p>Horizontal: <b>N sin θ + f cos θ = mv²/R</b></p>'
            '<p>Vertical: <b>N cos θ = mg + f sin θ</b></p>'
            '<p>No friction needed at v₀ = √(Rg tan θ)</p></div></div>')
    _card(deck, 'Banked road: forces and equations',
          'mg, N and friction (down the slope); N sin θ + f cos θ = mv²/R, N cos θ = mg + f sin θ', BLUEPRINT, front, back)


# ---------------------------------------------------------------- maths
def _wave(fn, x0=24, x1=288, cy=92, amp=58, steps=96):
    pts = []
    for i in range(steps + 1):
        t = 2 * math.pi * i / steps
        pts.append(f'{x0 + (x1 - x0) * i / steps:.1f},{cy - amp * fn(t):.1f}')
    return ' '.join(pts)


def sin_cos_graph(deck):
    X = lambda t: 24 + 264 * t / (2 * math.pi)
    axes = ('<line class="ax" x1="20" y1="92" x2="294" y2="92"></line>'
            '<line class="ax" x1="24" y1="20" x2="24" y2="164"></line>'
            '<text class="tick" x="14" y="38">1</text><text class="tick" x="9" y="154">−1</text>'
            + ''.join(f'<line class="ax" x1="{X(t):.1f}" y1="88" x2="{X(t):.1f}" y2="96"></line>'
                      f'<text class="tick" x="{X(t):.1f}" y="182" text-anchor="middle">{lbl}</text>'
                      f'<line class="ax" x1="{X(t):.1f}" y1="96" x2="{X(t):.1f}" y2="170" stroke-dasharray="2 4" opacity=".35"></line>'
                      for t, lbl in [(math.pi / 2, 'π/2'), (math.pi, 'π'), (3 * math.pi / 2, '3π/2'), (2 * math.pi, '2π')]))
    waves = (f'<polyline class="sin draw" pathLength="100" points="{_wave(math.sin)}"></polyline>'
             f'<polyline class="cos fx d3" points="{_wave(math.cos)}"></polyline>'
             f'<circle class="pt fx d2" cx="{X(math.pi/2):.1f}" cy="34" r="4"></circle>'
             f'<text class="say fx d2" x="{X(math.pi/2):.1f}" y="24" text-anchor="middle">max 1</text>'
             f'<circle class="pt fx d2" cx="{X(3*math.pi/2):.1f}" cy="150" r="4"></circle>'
             f'<text class="say fx d2" x="{X(3*math.pi/2) + 8:.1f}" y="160">min −1</text>'
             f'<circle class="pt2 fx d4" cx="{X(math.pi/4):.1f}" cy="{92-58*math.sin(math.pi/4):.1f}" r="3.5"></circle>'
             f'<circle class="pt2 fx d4" cx="{X(5*math.pi/4):.1f}" cy="{92-58*math.sin(5*math.pi/4):.1f}" r="3.5"></circle>')
    q = 'Sketch sin x and cos x on [0, 2π]. Where are the max and min of sin x, and where do the curves cross?'
    front = (f'<div class="w cb"><p class="tag">Graphs · sin and cos</p><h2>{q}</h2>'
             f'<svg viewBox="0 0 300 190">{axes}</svg></div>')
    back = (f'<div class="w cb"><p class="tag">Graphs · sin and cos</p><h2>{q}</h2>'
            f'<svg viewBox="0 0 300 190">{axes}{waves}</svg>'
            '<div class="key"><i class="k1">━ sin x</i><i class="k2">┅ cos x</i></div>'
            '<div class="box fx d5">sin x: <b>max at π/2</b>, <b>min at 3π/2</b>, zero at 0, π, 2π.<br>'
            'They cross at <b>π/4</b> and <b>5π/4</b>. cos x is sin x shifted left by π/2.</div></div>')
    _card(deck, 'Graphs of sin x and cos x on [0, 2π]',
          'sin: max 1 at π/2, min −1 at 3π/2; curves cross at π/4 and 5π/4', CHALK, front, back)


def astc(deck):
    cells = [('Quadrant II', 'sin, cosec'), ('Quadrant I', 'All'), ('Quadrant III', 'tan, cot'), ('Quadrant IV', 'cos, sec')]
    def grid(show):
        return '<div class="qg">' + ''.join(
            f'<div><small>{l}</small><b class="{"fx d" + str(i + 1) if show else "q"}">{a if show else "?"}</b></div>'
            for i, (l, a) in enumerate(cells)) + '</div>'
    q = 'Which functions are positive in each quadrant?'
    front = f'<div class="w cb"><p class="tag">Signs · ASTC</p><h2>{q}</h2>{grid(False)}</div>'
    back = (f'<div class="w cb"><p class="tag">Signs · ASTC</p><h2>{q}</h2>{grid(True)}'
            '<div class="box fx d5">Read I → IV: <b>A</b>ll <b>S</b>ilver <b>T</b>ea <b>C</b>ups</div></div>')
    _card(deck, 'Signs of trig functions (ASTC)', 'I: all; II: sin, cosec; III: tan, cot; IV: cos, sec', CHALK, front, back)


# ---------------------------------------------------------------- biology
def _cell(kind):
    if kind == 'two':
        return ('<svg viewBox="0 0 44 44"><circle class="wall" cx="14" cy="22" r="11"></circle><circle class="nA" cx="14" cy="22" r="4"></circle>'
                '<circle class="wall" cx="31" cy="22" r="11"></circle><circle class="nB" cx="31" cy="22" r="4"></circle></svg>')
    if kind == 'dikaryon':
        return ('<svg viewBox="0 0 44 44"><ellipse class="wall" cx="22" cy="22" rx="19" ry="13"></ellipse>'
                '<circle class="nA" cx="15" cy="22" r="4"></circle><circle class="nB" cx="29" cy="22" r="4"></circle></svg>')
    if kind == 'diploid':
        return ('<svg viewBox="0 0 44 44"><ellipse class="wall" cx="22" cy="22" rx="19" ry="13"></ellipse>'
                '<circle class="n2" cx="22" cy="22" r="6.5"></circle></svg>')
    return ('<svg viewBox="0 0 44 44"><circle class="ring" cx="22" cy="22" r="19"></circle>'
            '<circle class="sp" cx="15" cy="15" r="5"></circle><circle class="sp" cx="29" cy="15" r="5"></circle>'
            '<circle class="sp" cx="15" cy="29" r="5"></circle><circle class="sp" cx="29" cy="29" r="5"></circle></svg>')


def fungal_sexual_cycle(deck):
    steps = [('two', 'Two hyphae meet', 'compatible mating types, each <span class="n">n</span>'),
             ('dikaryon', 'Plasmogamy', 'protoplasms fuse → <span class="n">n + n</span> dikaryon (asco-, basidiomycetes)'),
             ('diploid', 'Karyogamy', 'the two nuclei fuse → <span class="n">2n</span> zygote'),
             ('spores', 'Meiosis', 'in the fruiting body → haploid <span class="n">n</span> spores')]
    q = 'Sexual cycle of fungi: what happens, in order?'
    front = (f'<div class="w pt"><p class="tag">Kingdom Fungi</p><h2>{q}</h2><div class="steps">'
             + ''.join(f'<div class="st blank">{_cell(k) if i == 0 else _cell("two").replace("nA", "wall").replace("nB", "wall")}'
                       f'<div><b>{"Two hyphae meet" if i == 0 else "? ? ?"}</b></div></div>' for i, (k, _, _) in enumerate(steps))
             + '</div></div>')
    back = (f'<div class="w pt"><p class="tag">Kingdom Fungi</p><h2>{q}</h2><div class="steps">'
            + ''.join(f'<div class="st fx d{i + 1}">{_cell(k)}<div><b>{t}</b><span>{s}</span></div></div>'
                      for i, (k, t, s) in enumerate(steps))
            + '</div></div>')
    _card(deck, 'Fungal sexual cycle in order', 'Plasmogamy (n + n) → karyogamy (2n) → meiosis → haploid spores', PETRI, front, back)


KINGDOMS = ['Monera', 'Protista', 'Fungi', 'Plantae', 'Animalia']


def kingdom_tiles(deck, question, answers, term, eyebrow='Table 2.1 · Five kingdoms'):
    """answers: list of 5 (text, negative) in kingdom order."""
    def build(show):
        tiles = ''
        for i, (k, (a, neg)) in enumerate(zip(KINGDOMS, answers)):
            cls = 'r' + (' no' if neg else '') if show else 'q'
            tiles += (f'<div class="t c{i + 1}{" wide" if i == 4 else ""}"><i>{k}</i>'
                      f'<b class="{cls}">{a if show else "?"}</b></div>')
        return f'<div class="w tl"><p class="tag">{eyebrow}</p><h2>{question}</h2><div class="grid">{tiles}</div></div>'
    _card(deck, term, '; '.join(f'{k}: {_strip(a)}' for k, (a, _) in zip(KINGDOMS, answers)), TILES, build(False), build(True))


HERBARIUM = BASE + """
.w.hb{color:#2d2a22;background:#f4ecd8;border:1px solid #e2d5b5;
  font-family:Georgia,"Times New Roman",serif}
.hb .tag{color:#8a6d3b;font-family:system-ui,sans-serif}.hb h2{color:#2d2a22}
.hb .sheet{position:relative;margin-top:6px;padding:12px 12px 10px;border-radius:12px;background:#fbf6ea;
  border:1px solid #e6d9ba;box-shadow:0 1px 0 rgba(90,70,30,.08)}
.hb .label{position:absolute;right:10px;top:-12px;padding:4px 10px;border:1.5px solid #6b5a33;border-radius:4px;
  background:#fffdf6;font-size:12px;color:#4a3f26;transform:rotate(2deg)}
.hb .label b{display:block;font-size:14px}
.hb .rung{display:grid;grid-template-columns:96px 1fr;align-items:center;gap:8px;padding:6px 0;
  border-bottom:1px dashed #d8c89f}
.hb .rung:last-child{border-bottom:0}
.hb .rung small{font-family:system-ui,sans-serif;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:#8a6d3b}
.hb .rung b{font-size:16px;font-weight:600;color:#2d2a22}
.hb .rung b.q{color:#c9b98f;letter-spacing:.25em}
.hb .rung i{font-size:16px}
.hb .up{display:flex;align-items:center;gap:8px;margin-top:10px;font-family:system-ui,sans-serif;font-size:12.5px;color:#6b5a33}
.hb .up svg{width:22px;height:48px;flex:none}
.hb .stem{stroke:#8a6d3b;stroke-width:2;fill:none}
.hb .r1{animation:fade .45s ease both 1.5s}.hb .r2{animation:fade .45s ease both 1.25s}.hb .r3{animation:fade .45s ease both 1s}
.hb .r4{animation:fade .45s ease both .75s}.hb .r5{animation:fade .45s ease both .5s}.hb .r6{animation:fade .45s ease both .25s}
.hb .r7{animation:fade .45s ease both 0s}
.hb .name{margin:18px 0 6px;text-align:center;font-size:30px;line-height:1.2}
.hb .name span{display:inline-block;padding:0 4px}
.hb .name .g{color:#1f5f3f}.hb .name .s{color:#7a3b12}.hb .name .a{color:#555;font-size:22px}
.hb .parts{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:14px;font-family:system-ui,sans-serif}
.hb .parts div{padding:9px 8px;border-radius:10px;background:#fffdf6;border:1px solid #e6d9ba;font-size:12.5px;line-height:1.35}
.hb .parts b{display:block;margin-bottom:3px;font-size:13.5px}
.hb .parts .g b{color:#1f5f3f}.hb .parts .s b{color:#7a3b12}.hb .parts .a b{color:#555}
.hb .rules{margin-top:12px;padding:10px 12px;border-radius:10px;background:#efe3c4;font-family:system-ui,sans-serif;font-size:13px}
"""

RANKS = ['Kingdom', 'Phylum / Division', 'Class', 'Order', 'Family', 'Genus', 'Species']


def taxon_ladder(deck, common, values, italic=(), eyebrow='Table 1.1 · Taxonomic categories'):
    """values: 7 strings from Kingdom down to Species; italic: ranks (by index) to italicise."""
    q = f'Place the {common.lower()} in the taxonomic hierarchy.'
    def build(show):
        rungs = ''
        for i, (rank, value) in enumerate(zip(RANKS, values)):
            shown = f'<i>{value}</i>' if i in italic else value
            cell = f'<b>{shown}</b>' if show else '<b class="q">?</b>'
            rungs += f'<div class="rung{f" r{i + 1}" if show else ""}"><small>{rank}</small>{cell}</div>'
        arrow = ('<div class="up"><svg viewBox="0 0 22 48"><path class="stem" d="M11 46V6M4 13l7-8 7 8"></path></svg>'
                 '<span>Going up: <b>fewer</b> shared characters in each taxon.</span></div>') if show else ''
        return (f'<div class="w hb"><p class="tag">{eyebrow}</p><h2>{q}</h2><div class="sheet">'
                f'<div class="label">Specimen<b>{common}</b></div>{rungs}</div>{arrow}</div>')
    definition = '; '.join(f'{r}: {v}' for r, v in zip(RANKS, values))
    _card(deck, f'Classification of {common.lower()}', definition, HERBARIUM, build(False), build(True))


def binomial_anatomy(deck):
    q = 'Name each part of this scientific name and the rule it follows.'
    name = '<p class="name"><span class="g"><i>Mangifera</i></span> <span class="s"><i>indica</i></span> <span class="a">Linn.</span></p>'
    front = (f'<div class="w hb"><p class="tag">1.1 · Binomial nomenclature</p><h2>{q}</h2>{name}'
             '<div class="parts"><div class="g"><b>1 · ?</b></div><div class="s"><b>2 · ?</b></div><div class="a"><b>3 · ?</b></div></div></div>')
    back = (f'<div class="w hb"><p class="tag">1.1 · Binomial nomenclature</p><h2>{q}</h2>{name}'
            '<div class="parts"><div class="g fx d1"><b>Genus</b>Starts with a capital letter</div>'
            '<div class="s fx d2"><b>Specific epithet</b>Starts with a small letter</div>'
            '<div class="a fx d3"><b>Author</b>Abbreviated, at the end: first described by Linnaeus</div></div>'
            '<div class="rules fx d4">Latin, in <b>italics</b> when printed; each word <b>underlined separately</b> when handwritten.</div></div>')
    _card(deck, 'Parts of <i>Mangifera indica</i> Linn.',
          'Mangifera = genus (capital letter); indica = specific epithet (small letter); Linn. = author (abbreviated). Italics in print, each word underlined separately in handwriting.',
          HERBARIUM, front, back)


SEA = BASE + """
.w.sea{color:#e6f4f1;background:linear-gradient(180deg,#0f3d4a 0,#0b2e3a 55%,#08222c 100%)}
.sea .tag{color:#7fe0d0}.sea h2{color:#fff}
.sea .cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:7px;margin-top:6px}
.sea .al{border-radius:14px;padding:10px 9px 12px;min-height:250px;display:flex;flex-direction:column;gap:8px;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1)}
.sea .al em{font-style:normal;font-size:11px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
  padding:4px 7px;border-radius:999px;align-self:flex-start;color:#08222c}
.sea .g em{background:#7ddc8a}.sea .br em{background:#d9a85b}.sea .rd em{background:#f2837b}
.sea .al small{color:#9fc9c1;font-size:10.5px;overflow-wrap:anywhere}
.sea .al b{font-size:13.5px;line-height:1.35;font-weight:600;overflow-wrap:anywhere}
.sea .al b.q{color:rgba(230,244,241,.3);letter-spacing:.25em}
.sea .g{box-shadow:inset 0 3px 0 #7ddc8a}.sea .br{box-shadow:inset 0 3px 0 #d9a85b}.sea .rd{box-shadow:inset 0 3px 0 #f2837b}
.sea .al b.r{animation:fade .45s ease both}.sea .br b.r{animation-delay:.12s}.sea .rd b.r{animation-delay:.24s}
.sea .gm{display:grid;grid-template-columns:128px 1fr;align-items:center;gap:10px;padding:9px 10px;margin-top:8px;
  border-radius:14px;background:rgba(255,255,255,.06)}
.sea .gm svg{width:128px;height:46px}
.sea .gm b{display:block;font-size:15px;color:#fff}.sea .gm span{font-size:12.5px;color:#9fc9c1}
.sea .gm b.q{color:rgba(230,244,241,.3);letter-spacing:.25em}
.sea .cell{fill:#7ddc8a;stroke:#e6f4f1;stroke-width:1.2}.sea .egg{fill:#f2c14e;stroke:#e6f4f1;stroke-width:1.2}
.sea .fl{fill:none;stroke:#e6f4f1;stroke-width:1.2;stroke-linecap:round}
.sea .ml{animation:swimL 1.4s cubic-bezier(.3,.7,.3,1) both}
.sea .mr{animation:swimR 1.4s cubic-bezier(.3,.7,.3,1) both}
.sea .gm:nth-child(4) g{animation-delay:.15s}.sea .gm:nth-child(5) g{animation-delay:.3s}.sea .gm:nth-child(6) g{animation-delay:.45s}
@keyframes swimL{from{transform:translateX(-26px)}to{transform:none}}
@keyframes swimR{from{transform:translateX(26px)}to{transform:none}}
"""


def algae_tiles(deck, question, answers, term, eyebrow='Table 3.1 · Divisions of algae'):
    """answers: (green, brown, red) texts."""
    classes = [('g', 'Chlorophyceae', 'Green'), ('br', 'Phaeophyceae', 'Brown'), ('rd', 'Rhodophyceae', 'Red')]
    def build(show):
        cols = ''.join(f'<div class="al {c}"><em>{common}</em><small>{name}</small>'
                       f'<b class="{"r" if show else "q"}">{a if show else "?"}</b></div>'
                       for (c, name, common), a in zip(classes, answers))
        return f'<div class="w sea"><p class="tag">{eyebrow}</p><h2>{question}</h2><div class="cols">{cols}</div></div>'
    _card(deck, term, '; '.join(f'{n}: {_strip(a)}' for (_, n, _c), a in zip(classes, answers)), SEA, build(False), build(True))


def _gamete(x, r, cls, flagella, side):
    """A round gamete centred at x (y 23); flagella trail away from the partner."""
    body = f'<circle class="{cls}" cx="{x}" cy="23" r="{r}"></circle>'
    if not flagella:
        return body
    d = -1 if side == 'l' else 1
    tail = ''.join(f'<path class="fl" d="M{x + d * r} {23 + dy} q{d * 8} {dy * 2 - 4} {d * 16} {dy * 2}"></path>' for dy in (-3, 3))
    return body + tail


def gamete_fusion(deck):
    rows = [  # (r, cls, flagellated) left, right, name, example
        ((9, 'cell', True), (9, 'cell', True), 'Isogamy', 'Flagellated, similar size · <i>Ulothrix</i>'),
        ((9, 'cell', False), (9, 'cell', False), 'Isogamy', 'Non-flagellated, similar size · <i>Spirogyra</i>'),
        ((12, 'cell', True), (6, 'cell', True), 'Anisogamy', 'Dissimilar in size · <i>Eudorina</i>'),
        ((16, 'egg', False), (5, 'cell', True), 'Oogamy', 'Large static egg + small motile male · <i>Volvox</i>, <i>Fucus</i>')]
    q = 'Name each kind of sexual reproduction in algae, with the NCERT example.'
    def build(show):
        out = ''
        for l, r, name, ex in rows:
            if show:
                gl = f'<g class="ml">{_gamete(52, l[0], l[1], l[2], "l")}</g>'
                gr = f'<g class="mr">{_gamete(52 + l[0] + r[0] + 1, r[0], r[1], r[2], "r")}</g>'
                text = f'<div><b>{name}</b><span>{ex}</span></div>'
            else:
                gl = _gamete(36, l[0], l[1], l[2], 'l')
                gr = _gamete(92, r[0], r[1], r[2], 'r')
                text = '<div><b class="q">?</b></div>'
            out += f'<div class="gm"><svg viewBox="0 0 128 46">{gl}{gr}</svg>{text}</div>'
        return f'<div class="w sea"><p class="tag">3.1 · Algae</p><h2>{q}</h2>{out}</div>'
    _card(deck, 'Isogamy, anisogamy and oogamy in algae',
          'Isogamy: similar gametes, flagellated (Ulothrix) or non-flagellated (Spirogyra). Anisogamy: dissimilar in size (Eudorina). '
          'Oogamy: large non-motile egg + small motile male (Volvox, Fucus).', SEA, build(False), build(True))


GROVE = BASE + """
.w.gv{color:#1e2a1c;background:linear-gradient(170deg,#f3f7ea 0,#e6efd6 100%)}
.gv .tag{color:#5b7a3a}.gv h2{color:#1e2a1c;font-size:17.5px}
.gv .grp{margin-top:8px;padding:8px 10px 9px;border-radius:14px;background:#fff;border:1px solid #d9e4c4}
.gv .grp h3{margin:0 0 4px;font-size:14px;color:#2f4a1f}
.gv .gen{display:grid;grid-template-columns:34px 1fr;gap:2px 8px;align-items:center;margin:5px 0 0}
.gv .gen i{grid-row:span 2;font-style:normal;font-size:11px;font-weight:700;text-align:center;padding:3px 0;border-radius:7px;color:#fff}
.gv .n i{background:#7cb342}.gv .d i{background:#2f6fa3}
.gv .gen span{font-size:12.5px;color:#2f3a2a;font-weight:600}
.gv .bar{height:5px;border-radius:3px;background:#eef3e2;overflow:hidden}
.gv .bar u{display:block;height:100%;border-radius:3px;animation:grow 1.1s cubic-bezier(.2,.8,.2,1) both}
.gv .n u{background:#7cb342}.gv .d u{background:#2f6fa3}
.gv .s1{width:100%}.gv .s2{width:34%}.gv .s3{width:12%}
.gv .q{color:#b7c4a3;letter-spacing:.25em}
.gv .grp:nth-child(4) u{animation-delay:.2s}.gv .grp:nth-child(5) u{animation-delay:.4s}
@keyframes grow{from{width:0}}
"""


def dominant_generation(deck):
    groups = [('Bryophytes', ('s1', 'Dominant, free-living, photosynthetic'), ('s2', 'Attached, depends on it')),
              ('Pteridophytes', ('s3', 'Prothallus: small, free-living'), ('s1', 'Dominant: true root, stem, leaves')),
              ('Gymnosperms', ('s3', 'Reduced, inside sporangia'), ('s1', 'Dominant: the plant itself'))]
    q = 'Gametophyte (n) or sporophyte (2n): which is dominant in each group?'
    def build(show):
        out = ''
        for name, gam, spo in groups:
            rows = ''
            for kind, label, (width, note) in (('n', 'n', gam), ('d', '2n', spo)):
                if show:
                    rows += f'<div class="gen {kind}"><i>{label}</i><span>{note}</span><div class="bar"><u class="{width}"></u></div></div>'
                else:
                    rows += f'<div class="gen {kind}"><i>{label}</i><span class="q">?</span><div class="bar"></div></div>'
            out += f'<div class="grp"><h3>{name}</h3>{rows}</div>'
        return f'<div class="w gv"><p class="tag">3.2 – 3.4 · Life cycles</p><h2>{q}</h2>{out}</div>'
    _card(deck, 'Dominant generation: bryophytes, pteridophytes, gymnosperms',
          'Bryophytes: gametophyte dominant, sporophyte dependent on it. Pteridophytes: sporophyte dominant; gametophyte (prothallus) small, free-living. '
          'Gymnosperms: sporophyte dominant; gametophytes reduced, not free-living.', GROVE, build(False), build(True))


# ---------------------------------------------------------------- chemistry
def bond_order_bars(deck):
    def rows(kind, show):
        data = [('N₂', 'w1', '945 kJ', 'v1', '110 pm'), ('O₂', 'w2', '498 kJ', 'v2', '121 pm'), ('F₂', 'w3', '159 kJ', 'v3', '143 pm')]
        out = ''
        for m, we, e, wl, l in data:
            width, val = (we, e) if kind == 'e' else (wl, l)
            bar = f'<span class="fill {width}"></span><u>{val}</u>' if show else '<u class="q">?</u>'
            out += f'<div class="row"><em>{m}</em><div class="bar {kind}">{bar}</div></div>'
        return out
    q = 'Rank N₂, O₂ and F₂ by bond enthalpy and bond length.'
    def build(show):
        chips = '<div class="chips"><span>N₂ · B.O. 3</span><span>O₂ · B.O. 2</span><span>F₂ · B.O. 1</span></div>' if show else ''
        rule = '<div class="rule fx d4">Higher bond order → <b>stronger</b> and <b>shorter</b> bond.</div>' if show else ''
        return (f'<div class="w lb"><p class="tag">Bond order · Fig. 4.21</p><h2>{q}</h2>{chips}'
                f'<p class="sec">Bond enthalpy</p>{rows("e", show)}<p class="sec">Bond length</p>{rows("l", show)}{rule}</div>')
    _card(deck, 'N2, O2, F2: bond enthalpy and length',
          'Enthalpy N₂ 945 > O₂ 498 > F₂ 159 kJ/mol; length N₂ 110 < O₂ 121 < F₂ 143 pm (bond order 3, 2, 1)', LAB, build(False), build(True))


def _lobe(angle, cx, cy, cls, length=46):
    return (f'<g transform="translate({cx} {cy}) rotate({angle})">'
            f'<path class="{cls}" d="M0 0 C 10 -12 {length - 8} -16 {length} 0 C {length - 8} 16 10 12 0 0 Z"></path></g>')


def sp3_mixer(deck):
    s = '<circle class="orbs" cx="24" cy="70" r="15"></circle><text class="lbl" x="24" y="104" text-anchor="middle">s</text>'
    p = ''.join(f'<g transform="translate({x} 70)">'
                f'<ellipse class="orb" cx="0" cy="-15" rx="8" ry="14"></ellipse><ellipse class="orb" cx="0" cy="15" rx="8" ry="14"></ellipse></g>'
                f'<text class="lbl" x="{x}" y="112" text-anchor="middle">p<tspan dy="3" font-size="8">{n}</tspan></text>'
                for x, n in [(80, 'x'), (110, 'y'), (140, 'z')])
    plus = '<text class="big" x="54" y="75" text-anchor="middle">+</text><text class="big" x="170" y="75" text-anchor="middle">→</text>'
    hyb = ''.join(f'<g class="spin fx d{i + 2}">{_lobe(a, 240, 70, "hy" + (" back" if a == 90 else ""), 44)}</g>'
                  for i, a in enumerate([-90, 28, 152, 90]))
    q = 'sp³ hybridisation of carbon: what mixes, how many hybrids, what angle?'
    front = (f'<div class="w lb"><p class="tag">Hybridisation</p><h2>{q}</h2>'
             f'<svg viewBox="0 0 300 130">{s}{p}{plus}<text class="big" x="240" y="78" text-anchor="middle">?</text></svg></div>')
    back = (f'<div class="w lb"><p class="tag">Hybridisation</p><h2>{q}</h2>'
            f'<svg viewBox="0 0 300 130">{s}{p}{plus}{hyb}<circle class="orbs" cx="240" cy="70" r="4"></circle></svg>'
            '<div class="chips fx d5"><span>1 s + 3 p</span><span>4 sp³</span><span>25% s</span><span>109.5°</span></div>'
            '<div class="rule fx d6">Four equivalent hybrids point to the corners of a <b>tetrahedron</b> (e.g. CH₄).</div></div>')
    _card(deck, 'sp3 hybridisation: orbitals, number, angle',
          '1 s + 3 p → 4 equivalent sp³ hybrids, 25% s-character, 109.5°, tetrahedral', LAB, front, back)
