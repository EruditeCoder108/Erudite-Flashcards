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
