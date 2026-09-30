"""List indices (among basic/cloze cards) changed vs git HEAD in a deck, to feed cardprev --idx. Usage: python changedidx.py <deck.json> [max]"""
import sys, os, json, subprocess
p = os.path.abspath(sys.argv[1])
root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=os.path.dirname(p), text=True).strip()
rel = os.path.relpath(p, root).replace('\\', '/')
old = json.loads(subprocess.check_output(['git', 'show', 'HEAD:' + rel], cwd=root).decode('utf8'))['cards']
new = json.load(open(p, encoding='utf8'))['cards']
keep = lambda cs: [c for c in cs if c['noteType'] in ('basic', 'cloze')]
old, new = keep(old), keep(new)
idx = [str(i) for i, (a, b) in enumerate(zip(old, new)) if a != b]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
step = max(1, len(idx) // n)
print(','.join(idx[::step][:n]), '| total changed', len(idx))
