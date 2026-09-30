"""Dry-run fmt.py over every deck: counts changes, checks no visible text is lost, dumps formulas for KaTeX validation.
Usage: python fmtcheck.py [glob-fragment]"""
import sys, os, json, glob, copy, re, collections
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import fmt
from _work import WORK
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
frag = sys.argv[1] if len(sys.argv) > 1 else ''
tot = ch = 0
bad, forms = [], []
per = collections.Counter()
norm = lambda x: re.sub(r'\\n|\s+|<[^>]+>|[,;.]|\band\b|\bor\b', '', x)
for f in sorted(glob.glob(os.path.join(ROOT, 'premade-cards', '*', '*', '*', 'deck.json'))):
    if frag not in f:
        continue
    d = json.load(open(f, encoding='utf8'))
    for c in d['cards']:
        if c['noteType'] not in ('basic', 'cloze'):
            continue
        tot += 1
        c2 = copy.deepcopy(c)
        fmt.format_card(c2, fmt.subject_of(f))
        if c2 == c:
            continue
        ch += 1
        per[f.replace('\\', '/').split('/')[-3]] += 1
        b = json.dumps(c2, ensure_ascii=False)
        a = json.dumps(c, ensure_ascii=False)
        for m in re.finditer(r'\\\\\[(.*?)\\\\\]', b):
            forms.append(json.loads('"' + m.group(1) + '"'))
        if '\\\\[' not in b and norm(a) != norm(b):
            bad.append((a[:200], b[:200]))
print(tot, 'cards;', ch, 'changed;', len(forms), 'formulas;', len(bad), 'visible-text diffs')
print(per.most_common(10))
for x in bad[:8]:
    print(x)
json.dump(forms, open(os.path.join(WORK, 'forms.json'), 'w'))
