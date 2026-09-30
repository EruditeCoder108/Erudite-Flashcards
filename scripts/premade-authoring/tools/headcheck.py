"""Compare every changed deck against git HEAD: no letters or digits may be lost or added (whitespace, tags, punctuation
joins and math markup are ignored; the check compares the sorted ASCII letters/digits of each changed field).
Usage: python headcheck.py"""
import os, re, json, subprocess, unicodedata, collections
LOSS_ONLY = '--loss' in __import__('sys').argv   # allow additions (rewritten cards), report only lost characters
root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
files = [l[3:].strip() for l in subprocess.check_output(['git', 'status', '--short', 'premade-cards'], cwd=root, text=True).splitlines()
         if l.endswith('deck.json')]


def core(t):
    t = (t or '').replace('[0.7em]', '')   # row spacing in fraction matrices
    t = re.sub(r'\\\[|\\\]|\\\(|\\\)', '', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'\\(sin|cos|tan|cot|sec|log|ln|det|adj|lim|max|min)\b', r'\1', t)   # function names are words in the old text
    t = re.sub(r'\\[a-zA-Z]+', '', t)                   # LaTeX commands (\begin, \frac, \sqrt ...)
    t = unicodedata.normalize('NFKD', t)                   # x² -> x2, aₙ -> an, so they compare with ^{2} / _{n}
    t = re.sub(r'\band\b|\bor\b', '', t)                   # joiners dropped when a list is split
    return sorted(re.findall(r'[a-z0-9]', t.lower()))


bad = n = 0
for f in files:
    old = json.loads(subprocess.check_output(['git', 'show', 'HEAD:' + f], cwd=root).decode('utf8'))['cards']
    new = json.load(open(os.path.join(root, f), encoding='utf8'))['cards']
    assert len(old) == len(new), f
    for a, b in zip(old, new):
        for k in ('term', 'definition', 'text', 'extra'):
            if a.get(k) != b.get(k):
                n += 1
                ca, cb = core(a.get(k)), core(b.get(k))
                if (LOSS_ONLY and collections.Counter(ca) - collections.Counter(cb)) or (not LOSS_ONLY and ca != cb):
                    bad += 1
                    if bad <= 8:
                        print(f.split('/')[-2], '|', repr(a.get(k))[:220], '\n    ->', repr(b.get(k))[:220])
print(n, 'fields changed;', bad, 'differ in letters/digits')
