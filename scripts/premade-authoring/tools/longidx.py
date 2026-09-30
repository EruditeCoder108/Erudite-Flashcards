"""Indices (among basic/cloze cards) whose answer is still one long block. Usage: python longidx.py <deck.json> [minlen]"""
import sys, json, re
d = json.load(open(sys.argv[1], encoding='utf8'))['cards']
m = int(sys.argv[2]) if len(sys.argv) > 2 else 110
cs = [c for c in d if c['noteType'] in ('basic', 'cloze')]
out = []
for i, c in enumerate(cs):
    a = c.get('definition') if c['noteType'] == 'basic' else c.get('extra', '')
    v = re.sub(r'<[^>]+>', '', a or '')
    if len(v) > m and '\n' not in a and '<br' not in a and '\[' not in a:
        out.append(str(i))
print(','.join(out), '|', len(out), 'of', len(cs))
