"""Survey remaining structure problems in basic/cloze cards. Usage: python survey.py [fragment]"""
import sys, os, json, glob, re, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
frag = sys.argv[1] if len(sys.argv) > 1 else ''
vis = lambda t: re.sub(r'<[^>]+>', '', t or '')
cats = collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(ROOT, 'premade-cards', '*', '*', '*', 'deck.json'))):
    if frag not in f:
        continue
    subj = f.replace('\\', '/').split('/')[-3]
    for c in json.load(open(f, encoding='utf8'))['cards']:
        if c['noteType'] == 'basic':
            texts = [('Q', c['term']), ('A', c['definition'])]
        elif c['noteType'] == 'cloze':
            texts = [('C', c['text']), ('E', c.get('extra', ''))]
        else:
            continue
        for side, t in texts:
            v = vis(t)
            if not v:
                continue
            key = subj
            if len(v) > 150 and '\n' not in v and '<br' not in t:
                cats['long-unbroken ' + key].append(v)
            if v.count(';') >= 2 and '\n' not in v:
                cats['semicolon-list ' + key].append(v)
            if re.search(r'\bStep \d|\bFirst\b.*\bthen\b|→.*→', v):
                cats['steps/chain ' + key].append(v)
            if len(re.findall(r'[=≠≈≤≥]', v)) >= 3 and '\\[' not in t:
                cats['equation-dense ' + key].append(v)
            if re.search(r'(?:^|\W)(?:Advantages|Disadvantages|Types|Features|Characteristics|Properties|Differences?)\b[^.]*:', v) and '\n' not in v:
                cats['labelled-list ' + key].append(v)
for k in sorted(cats):
    print(f'{k}: {len(cats[k])}')
if len(sys.argv) > 2:
    for k in sorted(cats):
        if sys.argv[2] in k:
            for v in cats[k][:6]:
                print('  -', v[:230].replace('\n', ' / '))
