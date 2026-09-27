"""Shared helpers for writing premade deck.json files (colour code + card builders)."""
import json, html as _html

# Colour code (brief section 4): blue terms, green examples, red exceptions/"not", orange numbers.
# Mid-tone shades so they read on both the dark and the light theme.
BLUE, GREEN, RED, ORANGE = '#3b82f6', '#22a35a', '#e5484d', '#f08c00'

def _c(color, s): return f'<span style="color:{color}">{s}</span>'
def T(s): return _c(BLUE, s)      # term
def E(s): return _c(GREEN, s)     # example
def X(s): return _c(RED, s)       # exception / not
def N(s): return _c(ORANGE, s)    # number / value
def I(s): return f'<i>{s}</i>'    # genus / species names
def EI(s): return E(I(s))         # italic example organism

class Deck:
    def __init__(self, name, class_name, base_tags):
        self.name, self.class_name, self.base_tags = name, class_name, base_tags
        self.cards, self.section = [], None

    def sec(self, tag):
        self.section = tag
        return self

    def _tags(self, extra=()):
        return self.base_tags + ([self.section] if self.section else []) + list(extra)

    def basic(self, q, a, reverse=False, **kw):
        c = {'noteType': 'basic', 'term': q, 'definition': a, 'tags': self._tags()}
        if reverse: c['reverse'] = True
        c.update(kw); self.cards.append(c)

    def cloze(self, text, extra=''):
        c = {'noteType': 'cloze', 'text': text, 'tags': self._tags()}
        if extra: c['extra'] = extra
        self.cards.append(c)

    def occlusion(self, prompt, image, size, masks, guess='hide-all', extra='', printed=False):
        """masks: (answer, box) or (answer, box, printed). box is [x, y, w, h] in image
        pixels, rot(box, degrees) for a label printed on a slant, or poly([(x, y), ...])
        for an odd shape. `printed` means the diagram already shows this label under
        the mask, so the app skips its answer tag."""
        w, h = size
        def mask(m):
            answer, box = m[0], m[1]
            if isinstance(box, dict) and 'poly' in box:
                xs, ys = [p[0] for p in box['poly']], [p[1] for p in box['poly']]
                x0, y0 = min(xs), min(ys)
                bw, bh = max(1, max(xs) - x0), max(1, max(ys) - y0)
                item = {'shape': 'polygon', 'bboxPx': [x0, y0, bw, bh], 'answer': answer,
                        'points': [[round((px - x0) / bw, 4), round((py - y0) / bh, 4)] for px, py in box['poly']]}
            elif isinstance(box, dict):
                item = {'shape': 'rect', 'bboxPx': list(box['box']), 'rotate': box['rotate'], 'answer': answer}
            else:
                item = {'shape': 'rect', 'bboxPx': list(box), 'answer': answer}
            if (m[2] if len(m) > 2 else printed):
                item['labelInImage'] = True
            return item
        self.cards.append({
            'noteType': 'image-occlusion', 'term': prompt, 'definition': extra, 'image': image,
            'occlusion': {'mode': guess, 'guessMode': guess, 'units': 'px', 'imageWidth': w, 'imageHeight': h,
                          'masks': [mask(m) for m in masks]},
            'tags': self._tags()})

    def advanced(self, term, definition, front_html, back_html, css):
        self.cards.append({'noteType': 'advanced-html', 'term': term, 'definition': definition,
                           'advancedHtml': {'frontHtml': front_html, 'backHtml': back_html,
                                            'frontCss': css, 'backCss': css},
                           'tags': self._tags()})

    def write(self, path):
        with open(path, 'w', encoding='utf8') as f:
            json.dump({'version': 1, 'name': self.name, 'className': self.class_name,
                       **({'description': self.description} if getattr(self, 'description', '') else {}),
                       'cards': self.cards},
                      f, ensure_ascii=False, indent=2)
        return len(self.cards)

def rot(box, degrees):
    """A mask box turned about its centre, for labels printed on a diagonal."""
    return {'box': list(box), 'rotate': degrees}

def poly(points):
    """A polygon mask from image-pixel points, for labels that are not boxes."""
    return {'poly': [tuple(p) for p in points]}

def pad(box, p=6, size=None):
    x, y, w, h = box
    x, y, w, h = x - p, y - p, w + 2 * p, h + 2 * p
    if size:
        x, y = max(0, x), max(0, y)
        w, h = min(w, size[0] - x), min(h, size[1] - y)
    return [x, y, w, h]

# ---- Advanced HTML: "reveal the hidden column" table card -------------------------------
# Paper-coloured card so it reads the same on the dark and light app themes.
TABLE_CSS = """
.k{box-sizing:border-box;min-height:470px;padding:20px 16px;background:#fbf8f1;color:#1f2430;
  font:14px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;border-radius:18px}
.k .eyebrow{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:#7a7466;margin:0 0 6px}
.k h2{font-size:19px;line-height:1.25;margin:0 0 14px;font-weight:700}
.k table{width:100%;border-collapse:separate;border-spacing:0 6px}
.k td{padding:9px 10px;vertical-align:top;background:#fff;border:1px solid #e8e1d2}
.k td:first-child{border-radius:10px 0 0 10px;font-weight:650;width:38%;border-right:0}
.k td:last-child{border-radius:0 10px 10px 0}
.k .q{color:#b8ae99;font-weight:700;letter-spacing:.2em}
.k .a{color:#1d5fd6;font-weight:600}
.k .a.no{color:#c93b3f}
.k .note{margin-top:12px;font-size:12px;color:#7a7466}
.k td.a{animation:pop .45s ease both}
.k tr:nth-child(2) td.a{animation-delay:.06s}.k tr:nth-child(3) td.a{animation-delay:.12s}
.k tr:nth-child(4) td.a{animation-delay:.18s}.k tr:nth-child(5) td.a{animation-delay:.24s}
@keyframes pop{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
"""

def table_card(deck, eyebrow, question, rows, note='', term=None):
    """rows: [(label, answer_html, is_negative)] -> front hides answers, back shows them."""
    def build(show):
        trs = ''.join(
            f'<tr><td>{lbl}</td>'
            + (f'<td class="a{" no" if neg else ""}">{ans}</td>' if show else '<td class="q">?</td>')
            + '</tr>' for lbl, ans, neg in rows)
        n = f'<p class="note">{note}</p>' if (note and show) else ''
        return f'<div class="k"><p class="eyebrow">{eyebrow}</p><h2>{question}</h2><table>{trs}</table>{n}</div>'
    plain = '; '.join(f'{_strip(l)}: {_strip(a)}' for l, a, _ in rows)
    deck.advanced(term or _strip(question), plain, build(False), build(True), TABLE_CSS)

def _strip(s):
    import re
    return _html.unescape(re.sub(r'<[^>]+>', '', s))

# ---- Advanced HTML: molecular-orbital ladder --------------------------------------------
MO_CSS = TABLE_CSS + """
.k .mo{display:flex;flex-direction:column;gap:5px;margin:4px 0 10px}
.k .lv{display:flex;align-items:center;gap:8px}
.k .lv .nm{width:74px;text-align:right;font-size:13px;color:#4a4538}
.k .lv .bx{display:flex;gap:6px}
.k .lv .o{width:40px;height:26px;border:1.5px solid #cfc5ae;border-radius:7px;background:#fff;
  display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:700;color:#1d5fd6;letter-spacing:-1px}
.k .lv.anti .o{border-color:#e7b8b9}
.k .lv.anti .nm{color:#b0474a}
.k .res{background:#fff;border:1px solid #e8e1d2;border-radius:12px;padding:10px 12px;font-size:14px}
.k .res b{color:#1d5fd6}.k .res .no{color:#c93b3f;font-weight:700}
.k .res .n{color:#c77700;font-weight:700}
.k .o.f{animation:pop .4s ease both}
"""

# Valence MO order (bottom -> top). KK (sigma1s, sigma*1s) omitted.
MO_ORDER_LIGHT = [('σ2s', 1, False), ('σ*2s', 1, True), ('π2p', 2, False), ('σ2p<sub>z</sub>', 1, False), ('π*2p', 2, True), ('σ*2p<sub>z</sub>', 1, True)]
MO_ORDER_HEAVY = [('σ2s', 1, False), ('σ*2s', 1, True), ('σ2p<sub>z</sub>', 1, False), ('π2p', 2, False), ('π*2p', 2, True), ('σ*2p<sub>z</sub>', 1, True)]

def _fill(order, n):
    """Aufbau + Hund over the ladder: returns per-level list of per-orbital electron counts."""
    out = []
    for _, k, _ in order:
        take = min(n, 2 * k); n -= take
        boxes = [0] * k
        for i in range(take):          # singly first (Hund), then pair
            boxes[i % k] += 1
        out.append(boxes)
    return out

def mo_card(deck, species, valence_e, heavy, question, result_html, term, definition):
    order = MO_ORDER_HEAVY if heavy else MO_ORDER_LIGHT
    fill = _fill(order, valence_e)
    def ladder(show):
        rows = []
        for (nm, k, anti), boxes in reversed(list(zip(order, fill))):
            cells = ''.join(f'<span class="o{" f" if show and b else ""}">{("↑↓" if b == 2 else "↑" if b == 1 else "") if show else ""}</span>' for b in boxes)
            rows.append(f'<div class="lv{" anti" if anti else ""}"><span class="nm">{nm}</span><span class="bx">{cells}</span></div>')
        return '<div class="mo">' + ''.join(rows) + '</div>'
    head = f'<p class="eyebrow">MO theory · {species}</p><h2>{question}</h2>'
    front = f'<div class="k">{head}{ladder(False)}<p class="note">KK (σ1s, σ*1s) filled. Fill {valence_e} valence electrons.</p></div>'
    back = f'<div class="k">{head}{ladder(True)}<div class="res">{result_html}</div></div>'
    deck.advanced(term, definition, front, back, MO_CSS)

# ---- Advanced HTML: worked example with one step hidden ---------------------------------
STEPS_CSS = TABLE_CSS + """
.k .prob{background:#fff;border:1px solid #e8e1d2;border-radius:12px;padding:10px 12px;font-size:13.5px;margin:0 0 10px}
.k ol{margin:0;padding:0;list-style:none;counter-reset:s}
.k li{counter-increment:s;display:flex;gap:10px;align-items:flex-start;padding:7px 0;border-bottom:1px dashed #e3dac6;font-size:14px}
.k li:before{content:counter(s);flex:none;width:22px;height:22px;border-radius:50%;background:#efe7d6;color:#7a7466;
  font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center}
.k li.h{color:#b8ae99;font-weight:700;letter-spacing:.15em}
.k li.h:before,.k li.r:before{background:#1d5fd6;color:#fff}
.k li.r{color:#1d5fd6;font-weight:650;animation:pop .45s ease both}
"""

def steps_card(deck, eyebrow, question, problem, steps, hide, term, definition):
    """steps: list of html strings; `hide` = index of the step the student must supply."""
    def build(show):
        lis = ''.join(
            (f'<li class="r">{s}</li>' if show else '<li class="h">?</li>') if i == hide else f'<li>{s}</li>'
            for i, s in enumerate(steps))
        return f'<div class="k"><p class="eyebrow">{eyebrow}</p><h2>{question}</h2><div class="prob">{problem}</div><ol>{lis}</ol></div>'
    deck.advanced(term, definition, build(False), build(True), STEPS_CSS)

# ---- Advanced HTML: 2x2 quadrant grid -----------------------------------------------------
QUAD_CSS = TABLE_CSS + """
.k .qg{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:0;margin:8px 0 12px;
  border-radius:14px;overflow:hidden;border:1px solid #e8e1d2}
.k .qg div{background:#fff;min-height:118px;padding:12px;display:flex;flex-direction:column;justify-content:space-between}
.k .qg div:nth-child(1){border-right:2px solid #1f2430;border-bottom:2px solid #1f2430}
.k .qg div:nth-child(2){border-bottom:2px solid #1f2430}
.k .qg div:nth-child(3){border-right:2px solid #1f2430}
.k .qg small{color:#7a7466;font-size:11px;letter-spacing:.06em;text-transform:uppercase}
.k .qg b{font-size:17px;color:#1d5fd6}.k .qg b.q{color:#b8ae99;letter-spacing:.2em}
.k .qg b.r{animation:pop .45s ease both}
"""

def quadrant_card(deck, eyebrow, question, cells, note, term, definition):
    """cells in visual order: [QII, QI, QIII, QIV] -> (label, answer)."""
    def build(show):
        g = ''.join(f'<div><small>{lbl}</small><b class="{"r" if show else "q"}">{ans if show else "?"}</b></div>' for lbl, ans in cells)
        n = f'<p class="note">{note}</p>' if show and note else ''
        return f'<div class="k"><p class="eyebrow">{eyebrow}</p><h2>{question}</h2><div class="qg">{g}</div>{n}</div>'
    deck.advanced(term, definition, build(False), build(True), QUAD_CSS)
