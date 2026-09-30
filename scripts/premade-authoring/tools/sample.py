"""Random sample of answers that are still one unformatted block. Usage: python sample.py <path-fragment> [n] [minlen]"""
import sys, os, json, glob, re, random
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
frag = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
minlen = int(sys.argv[3]) if len(sys.argv) > 3 else 90
random.seed(3)
rows = []
for f in glob.glob(os.path.join(ROOT, 'premade-cards', '*', '*', '*', 'deck.json')):
    if frag not in f.replace('\\', '/'):
        continue
    for c in json.load(open(f, encoding='utf8'))['cards']:
        if c['noteType'] == 'basic':
            a = c['definition']
            v = re.sub(r'<[^>]+>', '', a)
            if len(v) > minlen and '\n' not in a and '\\[' not in a:
                rows.append((f.replace('\\', '/').split('/')[-2], c['term'][:80], v[:300]))
print(len(rows), 'unformatted long answers')
for r in random.sample(rows, min(n, len(rows))):
    print(r[0][:38], '|', r[1], '\n    ', r[2])
