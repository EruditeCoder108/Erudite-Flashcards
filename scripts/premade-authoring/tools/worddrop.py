"""For changed fields vs git HEAD, list the WORDS that disappeared (tags/markup ignored). Review these after a hand rewrite.
Usage: python worddrop.py"""
import os, re, json, subprocess, unicodedata, collections
root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
files = [l[3:].strip() for l in subprocess.check_output(['git', 'status', '--short', 'premade-cards'], cwd=root, text=True).splitlines()
         if l.endswith('deck.json')]


def words(t):
    t = (t or '').replace('[0.7em]', '')
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'\\\[|\\\]|\\\(|\\\)|\\[a-zA-Z]+', ' ', t)
    t = unicodedata.normalize('NFKD', t).lower()
    return re.findall(r'[a-z0-9]+', t)


n = 0
for f in files:
    old = json.loads(subprocess.check_output(['git', 'show', 'HEAD:' + f], cwd=root).decode('utf8'))['cards']
    new = json.load(open(os.path.join(root, f), encoding='utf8'))['cards']
    for a, b in zip(old, new):
        for k in ('term', 'definition', 'text', 'extra'):
            if a.get(k) != b.get(k):
                lost = collections.Counter(words(a.get(k))) - collections.Counter(words(b.get(k)))
                lost = {w: c for w, c in lost.items() if w not in ('and', 'or', 'the', 'a', 'is', 'so', 'it', 'of', 'to', 'in', 'then', 'that', 'this')}
                if lost:
                    n += 1
                    print(f.split('/')[-2][11:40], k, '| dropped:', ' '.join(sorted(lost)))
print(n, 'fields lost words')
