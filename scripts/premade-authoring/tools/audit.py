"""Audit basic/cloze cards for defects. Usage: python audit.py [fragment] [category-to-list]"""
import sys, os, json, glob, re, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
frag = sys.argv[1] if len(sys.argv) > 1 else ''
show = sys.argv[2] if len(sys.argv) > 2 else ''
vis = lambda t: re.sub(r'<[^>]+>', '', t or '')
cats = collections.defaultdict(list)


def check(where, field, t, noteType):
    if not t or not isinstance(t, str):
        return
    v = vis(t)
    tag = f'{where} [{field}]'
    if re.search(r'[a-z][.!?][A-Z][a-z]', v.replace('e.g.', '').replace('i.e.', '')) and not re.search(r'\bNa\.|\bpH\.', v):
        cats['run-together sentence'].append((tag, v[:160]))
    if re.search(r'[a-z]{2}[A-Z][a-z]{3}', v) and '<i>' not in t:
        cats['camel-case join'].append((tag, v[:160]))
    if '  ' in v.replace('\n', ' ') and '\\[' not in t:
        cats['double space'].append((tag, v[:160]))
    if re.search(r'\[\[|\]\]', t):
        cats['leftover [[ ]] text matrix'].append((tag, v[:160]))
    if '\\text{' in t:
        cats['\\text{} in formula'].append((tag, v[:160]))
    if re.search(r'&(amp|lt|gt|nbsp);|&#\d+;', t):
        cats['html entity'].append((tag, v[:160]))
    if t.count('<span') != t.count('</span>') or t.count('<b>') != t.count('</b>') or t.count('<i>') != t.count('</i>'):
        cats['unbalanced tag'].append((tag, t[:160]))
    if re.search(r'\s[,;:.]\s|\s[,;.](?=\s|$)', v) and '\\[' not in t:
        cats['space before punctuation'].append((tag, v[:160]))
    if re.search(r'\(\s|\s\)', v):
        cats['space inside parentheses'].append((tag, v[:160]))
    if re.search(r'(\b\w+\b) \1\b', v, re.I) and not re.search(r'\b(that that|had had|is is|\d+ \d+)\b', v, re.I):
        cats['repeated word'].append((tag, v[:160]))
    if v.count('(') != v.count(')') and '\\[' not in t and '{{' not in t and not re.search(r'\(\w\)|\d\)', v):
        cats['unbalanced parentheses'].append((tag, v[:160]))
    if re.search(r'\bTODO\b|\bXXX\b|\?\?|lorem', v, re.I):
        cats['placeholder'].append((tag, v[:160]))
    if noteType == 'cloze' and field == 'text' and not re.search(r'\{\{c\d+::', t):
        cats['cloze without blank'].append((tag, v[:160]))
    if noteType == 'cloze' and re.search(r'\{\{c\d+::\s*\}\}', t):
        cats['empty cloze'].append((tag, v[:160]))
    if re.search(r'\{\{c\d+::[^}]*\\[\[(]', t):
        cats['math inside cloze'].append((tag, v[:160]))
    if len(v.strip()) < 2:
        cats['empty field'].append((tag, repr(t)[:80]))


seen = collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(ROOT, 'premade-cards', '*', '*', '*', 'deck.json'))):
    if frag not in f.replace('\\', '/'):
        continue
    name = f.replace('\\', '/').split('/')[-2]
    d = json.load(open(f, encoding='utf8'))
    for i, c in enumerate(d['cards']):
        nt = c['noteType']
        where = f'{name[:44]}#{i}'
        if nt == 'basic':
            check(where, 'Q', c.get('term'), nt); check(where, 'A', c.get('definition'), nt)
            seen[vis(c.get('term')).strip().lower()].append(where)
        elif nt == 'cloze':
            check(where, 'text', c.get('text'), nt); check(where, 'extra', c.get('extra'), nt)
            seen[vis(c.get('text')).strip().lower()].append(where)
for q, w in seen.items():
    if len(w) > 1 and len(q) > 25:
        cats['duplicate question (same deck or across)'].append((', '.join(w[:3]), q[:120]))
for k in sorted(cats, key=lambda k: -len(cats[k])):
    print(f'{len(cats[k]):5d}  {k}')
if show:
    for k in cats:
        if show in k:
            print('\n' + k)
            for w, t in cats[k][:25]:
                print('  ', w, '|', t)
