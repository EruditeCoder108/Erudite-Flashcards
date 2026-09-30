"""Readability formatter for premade card text.

Applied automatically by Deck.write() and runnable over existing deck.json files:
    python fmt.py premade-cards/12th/Mathematics/class12-mathematics-ch03-matrices [--dry]

Rules (all idempotent, and skipped for cloze bodies / advanced HTML / text already holding KaTeX):
  1. [[a, b], [c, d]] text matrices -> KaTeX bmatrix on its own line (display math).
  2. (i)(ii)(iii) / (a)(b)(c) / (A)(B)(C) / 1. 2. 3. runs -> one item per line.
  3. Bold lead-ins: Trap: Correction: Update: Note: Mnemonic: Remember: Why:
  4. Long answers: sentence per line; a trailing ': <result>' goes on its own line.
"""
import re, json, sys, os

TRIG = {'sin', 'cos', 'tan', 'cot', 'sec', 'cosec', 'log', 'ln', 'det', 'adj'}
SUP = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', 'ⁿ': 'n', '⁻': '-'}
SUB = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
       'ᵢ': 'i', 'ⱼ': 'j', 'ₖ': 'k', 'ₙ': 'n', 'ₘ': 'm'}
GREEK = {'θ': r'\theta ', 'α': r'\alpha ', 'β': r'\beta ', 'γ': r'\gamma ', 'π': r'\pi ', 'ω': r'\omega ', 'λ': r'\lambda ', 'μ': r'\mu '}


def _script(m, table, mark):
    return mark + '{' + ''.join(table[c] for c in m.group(0)) + '}'


def to_tex(s):
    """Unicode maths -> LaTeX for one matrix entry. Returns None if it contains something we can't trust."""
    s = s.strip()
    words = re.findall(r'[A-Za-z]{3,}', s)
    if any(w not in TRIG for w in words):
        return None
    s = s.replace('−', '-').replace('×', r'\times ').replace('·', r'\cdot ').replace('′', "'")
    s = re.sub(r'√\(([^()]+)\)', r'\\sqrt{\1}', s)
    s = re.sub(r'√(\w+)', r'\\sqrt{\1}', s)
    s = re.sub(r'([₀-₉ᵢⱼₖₙₘ]+)', lambda m: _script(m, SUB, '_'), s)
    s = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ⁻]+)', lambda m: _script(m, SUP, '^'), s)
    for g, t in GREEK.items():
        s = s.replace(g, t)
    s = re.sub(r'\b(sin|cos|tan|cot|sec|log|ln|det|adj)\b', r'\\\1 ', s)
    s = re.sub(r'^(-?)(\d+|[a-zA-Z])/(\d+|[a-zA-Z])$', lambda m: m.group(1) + r'\dfrac{' + m.group(2) + '}{' + m.group(3) + '}', s)
    if re.search(r'[^\x00-\x7f]', s):
        return None
    return s.strip()


MAT = re.compile(r'\[\s*(\[[^\[\]]*\](?:\s*,\s*\[[^\[\]]*\])*)\s*\]')
ROW = re.compile(r'\[([^\[\]]*)\]')


def matrix_tex(m):
    rows = []
    for r in ROW.findall(m.group(1)):
        cells = [to_tex(c) for c in r.split(',')]
        if any(c is None or c == '' for c in cells):
            return None
        rows.append(cells)
    if len({len(r) for r in rows}) != 1:
        return None
    gap = r' \\[0.7em] ' if any('frac' in c for r in rows for c in r) else r' \\ '   # tall fractions need room between rows
    return r'\begin{bmatrix}' + gap.join(' & '.join(r) for r in rows) + r'\end{bmatrix}'


TAG = re.compile(r'(<[^>]+>)')
# A run of matrices joined by operators, with an optional short leading coefficient.
SEP = r'(?:\s*(?:\+|−|-|=|≠|×|·)?\s*)'
COEF = r'(?:(?:\d+|[a-zA-Z]|(?:sin|cos|tan)\s?[θαβ]|\([^()\[\]]{1,14}\))\s*)?'
RUN = re.compile(r'(?<![A-Za-z0-9])' + COEF + MAT.pattern + r'(?:' + SEP + COEF + MAT.pattern + r')*')


def _run_tex(run):
    out, last = [], 0
    for m in MAT.finditer(run):
        t = matrix_tex(m)
        if t is None:
            return None
        pre = run[last:m.start()]
        pre = pre.strip()
        pre_t = ''
        if pre:
            # coefficient / operator between matrices
            pre_t = to_tex(pre.replace('≠', r'\neq ')) if not pre.endswith('≠') else None
            if pre_t is None and pre in ('≠',):
                pre_t = r'\neq'
            if pre_t is None:
                return None
        out.append((pre_t + ' ' if pre_t else '') + t)
        last = m.end()
    return ' '.join(out)


def matrices(text):
    """Replace matrix runs in the text nodes of an HTML fragment. Tags stay put; a run inside a span is fine."""
    if 'bmatrix' in text:   # already converted: matrix fractions use \dfrac (\frac was tiny inside matrices)
        text = text.replace('\\frac{', '\\dfrac{')
        if 'dfrac' in text and '[0.7em]' not in text:
            text = text.replace(' \\\\ ', ' \\\\[0.7em] ')
        return text
    if '\\(' in text or '\\[' in text or '{{' in text:
        return text
    parts = TAG.split(text)
    for i, p in enumerate(parts):
        if i % 2 or '[[' not in p:
            continue
        def rep(m):
            tex = _run_tex(m.group(0))
            return m.group(0) if tex is None else '\\[' + tex + '\\]'
        parts[i] = RUN.sub(rep, p)
    return ''.join(parts)


# -------------------------------------------------------------------- enumerations
ROMAN = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii']
LOWER = list('abcdefgh')
UPPER = list('ABCDEFGH')


PH = re.compile(r'\x00\d+\x00')


def _blank(lead):
    return not PH.sub('', lead).strip()


def _break_before(text, marks):
    """Insert a newline before each marker position (text-only positions), trimming the joining space/comma/'and'."""
    out, last = [], 0
    for pos in marks:
        lead = text[last:pos]
        if _blank(text[:pos]) or PH.sub('', text[:pos]).endswith('\n') or re.search(r'\n[ ]*$', lead):
            out.append(lead)
        else:
            lead = re.sub(r'(?:[ ,;]| and| or)+$', '', lead)
            out.append(lead)
            out.append('\n')
        last = pos
    out.append(text[last:])
    return ''.join(out)


def _enum(text, seq, pat):
    """Break before each (x) marker when at least two consecutive markers exist."""
    ms = list(re.finditer(pat, text))
    found = [m.group(1) for m in ms]
    if not any(found[i] == seq[0] and i + 1 < len(found) and found[i + 1] == seq[1] for i in range(len(found))):
        return text
    marks, prev_end = [], None
    for m in ms:
        # "(b) (c) simply have..." refers to labels; a marker with no content since the last one is not a list item
        gap = text[prev_end:m.start()] if prev_end is not None else 'x'
        if m.group(1) in seq and re.search(r'[A-Za-z0-9]', PH.sub('', gap)):
            marks.append(m.start())
        prev_end = m.end()
    return _break_before(text, marks)


def enumerations(text):
    if '{{' in text:
        return text
    tags = []
    def hold(m):
        tags.append(m.group(0)); return '\x00%d\x00' % (len(tags) - 1)
    p = TAG.sub(hold, text)
    tail = r'(?=\s(?!(?:and|or|to)\b))'   # "(a) and (b)" is a reference to labels, not a list
    head = r'(?<![\w(])(?<!and )(?<!or )(?<!to )'
    for seq, pat in ((ROMAN, head + r'\(([ivx]+)\)' + tail), (LOWER, head + r'\(([a-h])\)' + tail),
                     (UPPER, head + r'\(([A-H])\)' + tail)):
        p = _enum(p, seq, pat)
    nums = [(m.start(), m.group(1)) for m in re.finditer(r'(?:(?<=\s)|^)(\d)\.(?=\s)', p)]
    if [k for _, k in nums][:2] == ['1', '2']:
        p = _break_before(p, [pos for pos, _k in nums])
    return re.sub(r'\x00(\d+)\x00', lambda m: tags[int(m.group(1))], p)


# -------------------------------------------------------------------- lead-ins and long answers
LEAD = re.compile(r'(^|\n|(?<=[.!?] ))(Trap|Correction|Update|Note|Mnemonic|Remember|Why|Careful|Tip|Beyond the textbook)(:)(?! ?</b>)')


def leadins(text):
    if '{{' in text:
        return text
    return LEAD.sub(lambda m: m.group(1) + '<b>' + m.group(2) + ':</b>', text)


ABBR = r'(?<!e\.g)(?<!i\.e)(?<!vs)(?<!Ex)(?<!Fig)(?<!No)(?<!Eq)(?<!etc)(?<!approx)'
SENT = re.compile(ABBR + r'(?<=[a-z0-9\)\]²³₀-₉′%])\. (?=[A-Z])')
RESULT = re.compile(r':\s+(<span style="color:#f08c00">(?:(?!</span>).)*</span>\.?)$')


def plain_len(t):
    t = re.sub(r'\\\[.*?\\\]|\\\(.*?\\\)', 'M', t)   # converted math counts as one char, so later passes never newly fire
    return len(re.sub(r'<[^>]+>', '', t))


def long_answer(text):
    if '\n' in text or '{{' in text or plain_len(text) < 110:
        return text
    t = SENT.sub('.\n', text)
    if plain_len(t) >= 70:
        t = RESULT.sub(lambda m: ':\n' + m.group(1), t)
    return t


def tidy_display(t):
    """Display math is a block: drop the punctuation/space/newline hugging it so no stray '.' or blank line shows."""
    t = re.sub(r'(\\](?:</span>)?)[.;,]?[ \n]+', r'\1', t)
    t = re.sub(r'(\\](?:</span>)?)\.$', r'\1', t)
    return re.sub(r'[ \n]+((?:<span[^>]*>)?\\\[)', r'\1', t)



# -------------------------------------------------------------------- lists, chains, result equations
def _holdtags(text):
    tags = []
    def hold(m):
        tags.append(m.group(0)); return '\x00%d\x00' % (len(tags) - 1)
    return TAG.sub(hold, text), tags


def _release(p, tags):
    return re.sub(r'\x00(\d+)\x00', lambda m: tags[int(m.group(1))], p)


def numbered_paren(text):
    """1) do this 2) do that  ->  one step per line (same idea as '1. 2.')."""
    if '{{' in text:
        return text
    p, tags = _holdtags(text)
    nums = [(m.start(), m.group(1)) for m in re.finditer(r'(?:(?<=\s)|^)(\d)\)(?=\s)', p)]
    if [k for _, k in nums][:2] == ['1', '2']:
        p = _break_before(p, [pos for pos, _k in nums])
    return _release(p, tags)


def semicolon_lists(text):
    """a; b; c (3+ items, none inside brackets)  ->  one per line."""
    if '\n' in text or '<br' in text or plain_len(text) < 60:
        return text
    p, tags = _holdtags(text)     # cloze braces {{c1::..}} raise the depth, so only outer semicolons split
    depth, cuts = 0, []
    for i, ch in enumerate(p):
        if ch in '({[':
            depth += 1
        elif ch in ')}]':
            depth = max(0, depth - 1)
        elif ch == ';' and depth == 0 and p[i + 1:i + 2] == ' ':
            cuts.append(i)
    if len(cuts) < 2:
        return text
    items, last = [], 0
    for i in cuts:
        items.append(p[last:i]); last = i + 2
    items.append(p[last:])
    if any(len(PH.sub('', it).strip()) < 4 or len(PH.sub('', it)) > 110 for it in items):
        return text
    return _release('\n'.join(items), tags)


def derivation_chains(text):
    """Steps of a derivation joined by ' → ' where every step is an equation: one step per line, arrow leads the line."""
    if '\n' in text or '{{' in text or '<br' in text or plain_len(text) < 60:
        return text
    p, tags = _holdtags(text)
    segs = p.split(' → ')
    if len(segs) < 3 or ';' in PH.sub('', p):
        return text
    if not all(re.search(r'[=≠≈≤≥<>]', PH.sub('', s)) for s in segs[:-1]):
        return text
    if any(re.search(r'[0-9a-z)]\. [A-Za-z]', PH.sub('', s)) for s in segs):
        return text   # more than one derivation in the card
    return _release('\n→ '.join(segs), tags)


UNI = {'−': '-', '×': r'\times ', '·': r'\cdot ', '÷': r'\div ', '≤': r'\le ', '≥': r'\ge ', '≠': r'\ne ', '≈': r'\approx ',
       '∈': r'\in ', '∉': r'\notin ', '⊂': r'\subset ', '⊆': r'\subseteq ', '∪': r'\cup ', '∩': r'\cap ', '⇒': r'\Rightarrow ',
       '⇔': r'\Leftrightarrow ', '∞': r'\infty ', 'Σ': r'\sum ', '∑': r'\sum ', '∫': r'\int ', '°': r'^{\circ}', '′': "'",
       '∴': r'\therefore ', '±': r'\pm ', '∠': r'\angle ', '⊥': r'\perp ', '∥': r'\parallel ', 'Δ': r'\Delta ', 'φ': r'\phi ',
       'ϕ': r'\phi ', 'ε': r'\varepsilon ', 'δ': r'\delta ', 'σ': r'\sigma ', 'ρ': r'\rho ', 'τ': r'\tau ', 'ω': r'\omega ',
       'Ω': r'\Omega ', '∂': r'\partial ', '→': r'\to ', '≡': r'\equiv ', '∼': r'\sim ', '…': r'\ldots ', '⋯': r'\cdots ',
       '½': r'\tfrac{1}{2}', '¼': r'\tfrac{1}{4}', '¾': r'\tfrac{3}{4}'}
SUB2 = {**SUB, 'ₐ': 'a', 'ₑ': 'e', 'ₒ': 'o', 'ₓ': 'x', 'ᵣ': 'r', 'ₚ': 'p', 'ₛ': 's', 'ₜ': 't', 'ₗ': 'l', '₊': '+', '₋': '-'}
SUP2 = {**SUP, '⁺': '+', 'ᵀ': 'T', 'ᵐ': 'm', 'ˣ': 'x', 'ʸ': 'y', 'ᵃ': 'a', 'ᵇ': 'b'}
WORDS = TRIG | {'lim', 'max', 'min', 'sup', 'inf', 'mod', 'gcd', 'exp'}


def eq_tex(s):
    """Whole-equation Unicode -> LaTeX, or None if anything is unsure. Only meaning-preserving substitutions."""
    s = s.strip().rstrip('.')
    if not 10 <= len(s) <= 28 or not re.search(r'[=≠≈≤≥]', s) or re.search(r'[&#_^\$~<>]', s):
        return None   # display math cannot wrap, so only short equations become blocks
    for w in re.findall(r'[A-Za-z]{2,}', s):
        if w not in WORDS and not (w.isupper() and len(w) <= 4):
            return None
    if re.search(r'\d\s+[A-Za-z]\b', s):   # "2.23 m": a unit, not a variable
        return None
    s = re.sub(r'(∈|∉|⊂|⊆)\s*([NZQRC])\b', lambda m: m.group(1) + r' \mathbb{' + m.group(2) + '}', s)
    s = s.replace('{', r'\{').replace('}', r'\}').replace('%', r'\%')
    s = re.sub(r'√\(([^()]+)\)', lambda m: '\\sqrt{' + m.group(1) + '}', s)
    s = re.sub(r'√(\w+)', lambda m: '\\sqrt{' + m.group(1) + '}', s)
    s = re.sub(r'([₀-₉ᵢⱼₖₙₘₐₑₒₓᵣₚₛₜₗ₊₋]+)', lambda m: _script(m, SUB2, '_'), s)
    s = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ⁻⁺ᵀᵐˣʸᵃᵇ]+)', lambda m: _script(m, SUP2, '^'), s)
    for k, v in UNI.items():
        s = s.replace(k, v)
    for g, t in GREEK.items():
        s = s.replace(g, t)
    s = re.sub(r'\b(sin|cos|tan|cot|sec|log|ln|det|adj|lim|max|min)\b', lambda m: '\\' + m.group(1) + ' ', s)
    if re.search(r'[^\x00-\x7f]', s):
        return None
    return s.strip()


FINAL_SPAN = re.compile(r'(<span style="color:#[0-9a-f]{6}">)([^<>]+)(</span>)(\.?)$')


def result_equations(text):
    """A coloured result/formula that ends the text and is a clean equation -> display block (tinted box)."""
    if '\\(' in text or '\\[' in text or '{{' in text or '<br' in text:
        return text
    m = FINAL_SPAN.search(text)
    if not m:
        return text
    before = re.sub(r'<[^>]+>', '', text[:m.start()]).rstrip()
    if before and not before.endswith(':'):   # the equation must begin at the span, e.g. "Result:" then the formula
        return text
    tex = eq_tex(m.group(2))
    if tex is None:
        return text
    return text[:m.start()] + m.group(1) + '\\[' + tex + '\\]' + m.group(3)


def format_text(text, cloze=False, answer=False, subject=None):
    if not text or not isinstance(text, str):
        return text
    t = text
    if not cloze:
        t = matrices(t)
    elif '\n' not in t:
        t = semicolon_lists(t)
    t = enumerations(t)
    t = numbered_paren(t)
    t = re.sub(r'<br\s*/?>\n|\n<br\s*/?>', '<br>', t)
    t = leadins(t)
    if answer and not cloze:
        t = derivation_chains(t)
        t = semicolon_lists(t)
        t = long_answer(t)
        if subject == 'mathematics':
            t = result_equations(t)
    return tidy_display(t) if '\\[' in t else t


def format_card(c, subject=None):
    """Format a card dict in place (basic and cloze only; other types untouched)."""
    nt = c.get('noteType')
    if nt == 'basic':
        c['term'] = format_text(c.get('term'))
        c['definition'] = format_text(c.get('definition'), answer=True, subject=subject)
    elif nt == 'cloze':
        c['text'] = format_text(c.get('text'), cloze=True)
        if c.get('extra'):
            c['extra'] = format_text(c['extra'], answer=True, subject=subject)
    return c


def subject_of(path):
    return 'mathematics' if 'Mathematics' in path.replace('\\', '/') else None


def format_deck_file(path, dry=False):
    d = json.load(open(path, encoding='utf8'))
    before = json.dumps(d['cards'], ensure_ascii=False)
    sub = subject_of(path)
    for c in d['cards']:
        format_card(c, sub)
    changed = json.dumps(d['cards'], ensure_ascii=False) != before
    if changed and not dry:
        with open(path, 'w', encoding='utf8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
    return changed


if __name__ == '__main__':
    dry = '--dry' in sys.argv
    for a in [x for x in sys.argv[1:] if not x.startswith('--')]:
        p = os.path.join(a, 'deck.json') if os.path.isdir(a) else a
        print(p, 'changed' if format_deck_file(p, dry) else 'same')
