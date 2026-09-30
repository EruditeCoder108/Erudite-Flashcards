"""Find pseudo-LaTeX left in plain text (x_g, T^{3/2}, ^2 ...) outside real math blocks. Usage: python rawmath.py [n_examples]"""
import os, sys, json, glob, re, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
KEEP = re.compile(r'(\\\[.*?\\\]|\\\(.*?\\\)|<[^>]+>)', re.S)
pats = {'subscript _': re.compile(r'[A-Za-zα-ωΔ)\]]_\{?[A-Za-z0-9,+\-−]+\}?'), 'superscript ^': re.compile(r'\^\{?[A-Za-z0-9+\-−/.]+\}?')}
cnt = collections.Counter(); ex = collections.defaultdict(list)
for f in glob.glob(os.path.join(ROOT, 'premade-cards', '*', '*', '*', 'deck.json')):
    name = f.replace('\\', '/').split('/')[-2]
    for i, c in enumerate(json.load(open(f, encoding='utf8'))['cards']):
        if c['noteType'] not in ('basic', 'cloze'):
            continue
        for k in ('term', 'definition', 'text', 'extra'):
            t = c.get(k)
            if not isinstance(t, str):
                continue
            parts = KEEP.split(t)
            plain = ''.join(parts[j] for j in range(0, len(parts), 2))
            for label, p in pats.items():
                for m in p.finditer(plain):
                    cnt[label] += 1
                    if len(ex[label]) < int(sys.argv[1] if len(sys.argv) > 1 else 6):
                        ex[label].append(f'{name[:34]}#{i}: ...{plain[max(0, m.start() - 25):m.end() + 15]}...'.replace('\n', ' '))
print(dict(cnt))
for label, rows in ex.items():
    print('\n' + label)
    for r in rows:
        print('  ', r)
