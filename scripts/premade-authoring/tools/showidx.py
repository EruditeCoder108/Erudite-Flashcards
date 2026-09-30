"""Print Q/A (tags stripped, newlines shown) for card indices. Usage: python showidx.py <deck.json> 3,5,9"""
import sys, json, re
cs = [c for c in json.load(open(sys.argv[1], encoding='utf8'))['cards'] if c['noteType'] in ('basic', 'cloze')]
for i in sys.argv[2].split(','):
    c = cs[int(i)]
    f = lambda t: re.sub(r'<br\s*/?>', ' / ', re.sub(r'</?(span|b|i|small)[^>]*>', '', t or '')).replace('\n', ' / ')
    if c['noteType'] == 'basic':
        print(f'#{i} Q: {f(c["term"])}\n     A: {f(c["definition"])}')
    else:
        print(f'#{i} C: {f(c["text"])}' + (f'\n     X: {f(c.get("extra"))}' if c.get('extra') else ''))
