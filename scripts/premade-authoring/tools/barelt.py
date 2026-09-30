"""Find '<' directly followed by a letter that is not an allowed tag (the browser would treat it as a tag and swallow text)."""
import os, json, glob, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
ok = {'b', 'i', 'u', 'br', 'span', 'small', 'ul', 'ol', 'li', 'p', 'div', 'mark', 'code', 'pre', 'sub', 'sup', 'em', 'strong', 'blockquote', 'hr'}
n = 0
for f in glob.glob(os.path.join(ROOT, 'premade-cards', '*', '*', '*', 'deck.json')):
    name = f.replace('\\', '/').split('/')[-2]
    for i, c in enumerate(json.load(open(f, encoding='utf8'))['cards']):
        if c['noteType'] not in ('basic', 'cloze'):
            continue
        for k in ('term', 'definition', 'text', 'extra'):
            t = c.get(k)
            if not isinstance(t, str):
                continue
            for m in re.finditer(r'<(/?)([A-Za-z][A-Za-z0-9]*)', t):
                if m.group(2).lower() not in ok:
                    n += 1
                    print(name[:40], i, k, t[max(0, m.start() - 25):m.start() + 40].replace('\n', ' '))
print(n, 'bare < problems')
