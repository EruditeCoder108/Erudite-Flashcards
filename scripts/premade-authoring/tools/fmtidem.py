"""Find cards where a second fmt pass changes text again (idempotency check). Usage: python fmtidem.py [fragment]"""
import sys, os, json, glob, copy
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import fmt
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
frag = sys.argv[1] if len(sys.argv) > 1 else ''
n = shown = 0
for f in sorted(glob.glob(os.path.join(ROOT, 'premade-cards', '*', '*', '*', 'deck.json'))):
    if frag not in f:
        continue
    for c in json.load(open(f, encoding='utf8'))['cards']:
        if c['noteType'] not in ('basic', 'cloze'):
            continue
        c2 = copy.deepcopy(c)
        fmt.format_card(c2, fmt.subject_of(f))
        if c2 != c:
            n += 1
            if shown < 6:
                shown += 1
                for k in ('term', 'definition', 'text', 'extra'):
                    if c.get(k) != c2.get(k):
                        print(k, '\n  BEFORE', repr(c[k])[:260], '\n  AFTER ', repr(c2[k])[:260])
print(n, 'cards still changing')
