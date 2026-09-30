"""Have rebuilds changed cards other than basic/cloze (advanced HTML, occlusion, media refs) since a git revision?
Usage: python otherdrift.py <rev>   e.g. 4c95b7e"""
import sys, json, subprocess, os
rev = sys.argv[1]
root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
names = subprocess.check_output(['git', 'diff', '--name-only', rev, '--', 'premade-cards'], cwd=root, text=True).split()
drift = 0
for f in names:
    if not f.endswith('deck.json'):
        continue
    old = json.loads(subprocess.check_output(['git', 'show', f'{rev}:{f}'], cwd=root).decode('utf8'))
    new = json.load(open(os.path.join(root, f), encoding='utf8'))
    if len(old['cards']) != len(new['cards']):
        print('COUNT CHANGED', f, len(old['cards']), len(new['cards']))
        drift += 1
    for i, (a, b) in enumerate(zip(old['cards'], new['cards'])):
        if a['noteType'] != b['noteType']:
            print('TYPE CHANGED', f.split('/')[-2], i); drift += 1; continue
        if a['noteType'] in ('basic', 'cloze'):
            for k in a:
                if k not in ('term', 'definition', 'text', 'extra') and a[k] != b.get(k):
                    print('FIELD', k, 'changed', f.split('/')[-2], i); drift += 1
            continue
        if a != b:
            print('OTHER CARD CHANGED', f.split('/')[-2][:45], i, a['noteType'], (a.get('term') or '')[:50]); drift += 1
    for k in ('name', 'className', 'description'):
        if old.get(k) != new.get(k):
            print('DECK', k, 'changed', f.split('/')[-2]); drift += 1
print(drift, 'unexpected changes across', len(names), 'files')
