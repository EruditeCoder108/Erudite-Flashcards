"""Print the deck-script source lines behind card indices. Usage: python srcfor.py <decks/script.py> <deck.json> 3,5,9"""
import sys, json, re
src = open(sys.argv[1], encoding='utf8').read().split('\n')
cs = [c for c in json.load(open(sys.argv[2], encoding='utf8'))['cards'] if c['noteType'] in ('basic', 'cloze')]
for i in sys.argv[3].split(','):
    c = cs[int(i)]
    t = c['term'] if c['noteType'] == 'basic' else c['text']
    key = re.sub(r'<[^>]+>', '', t.split('\n')[0].split('\\[')[0])[:28]
    hits = [n for n, l in enumerate(src) if key and key in l]
    if not hits:
        print(f'#{i}: NOT FOUND for {key!r}')
    for n in hits[:2]:
        print(f'#{i} L{n + 1}: {src[n][:1100]}')
        k = n
        while src[k].rstrip().endswith(',') and k + 1 < len(src) and k - n < 4:   # call continues on the next line
            k += 1
            print(f'      L{k + 1}: {src[k][:1100]}')
