"""Which HTML tags do basic/cloze cards use, and which are stripped by the app's sanitizer? Also finds bare '<' that could be parsed as a tag.
Usage: python tagaudit.py"""
import os, json, glob, re, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
ALLOWED = {'b', 'strong', 'i', 'em', 'u', 'br', 'p', 'div', 'ul', 'ol', 'li', 'span', 'mark', 'code', 'pre', 'blockquote', 'hr'}
tags = collections.Counter()
bad_tags = collections.defaultdict(list)
bare = []
for f in sorted(glob.glob(os.path.join(ROOT, 'premade-cards', '*', '*', '*', 'deck.json'))):
    name = f.replace('\\', '/').split('/')[-2]
    for i, c in enumerate(json.load(open(f, encoding='utf8'))['cards']):
        if c['noteType'] not in ('basic', 'cloze'):
            continue
        for k in ('term', 'definition', 'text', 'extra'):
            t = c.get(k)
            if not isinstance(t, str):
                continue
            for m in re.finditer(r'<\s*/?\s*([a-zA-Z][a-zA-Z0-9]*)', t):
                tag = m.group(1).lower()
                tags[tag] += 1
                if tag not in ALLOWED:
                    bad_tags[tag].append(f'{name[:40]}#{i}[{k}] ' + t[max(0, m.start() - 30):m.start() + 50].replace('\n', ' '))
            for m in re.finditer(r'<(?![a-zA-Z/])', t):
                pass
print('tags used:', dict(tags))
for tag, rows in bad_tags.items():
    print(f'\nNOT allowed by sanitizer: <{tag}> x{len(rows)}')
    for r in rows[:6]:
        print('   ', r)
