"""Quick deck lint: python tools/lint.py <deck.json>
Flags \\text{}, KaTeX inside cloze / advanced HTML, unbalanced delimiters, empty fields, oversized HTML, duplicate questions."""
import sys, json, collections
OPEN, CLOSE = '\\(', '\\)'
d = json.load(open(sys.argv[1], encoding='utf8'))
bad = 0
seen = collections.Counter()


def flag(i, c, msg):
    global bad
    bad += 1
    print(f'#{i} [{c.get("noteType")}] {msg}: {(c.get("term") or c.get("text") or "")[:70]}')


for i, c in enumerate(d['cards']):
    blob = json.dumps(c, ensure_ascii=False)
    if '\\\\text{' in blob: flag(i, c, 'text{} used')
    nt = c.get('noteType')
    if nt == 'cloze':
        if OPEN in c['text']: flag(i, c, 'KaTeX in cloze')
        if '{{c' not in c['text']: flag(i, c, 'cloze without deletion')
    if nt == 'basic':
        for f in ('term', 'definition'):
            v = c.get(f, '')
            if not v.strip(): flag(i, c, f'empty {f}')
            if v.count(OPEN) != v.count(CLOSE): flag(i, c, f'unbalanced delimiters in {f}')
        seen[c['term']] += 1
    if nt == 'advanced-html':
        a = c['advancedHtml']
        for k in ('frontHtml', 'backHtml'):
            if OPEN in a[k]: flag(i, c, 'KaTeX in advanced HTML')
            if len(a[k]) > 30000: flag(i, c, f'{k} over 30000 chars')
            if 'style="' in a[k].replace('style="color:', 'X'): flag(i, c, 'inline style attr')
print('cards', len(d['cards']), 'issues', bad)
for t, n in seen.items():
    if n > 1: print('duplicate question:', t[:80])
