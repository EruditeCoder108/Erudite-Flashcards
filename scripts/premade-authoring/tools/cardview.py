"""Render every advanced-HTML card of a deck.json (front + back, 340x470, shadow DOM) into cards.html.
Usage: python cardview.py <deck.json> [filter-substring]"""
import sys, json, os, html
from _work import WORK, ROOT
HERE = WORK
deck = json.load(open(sys.argv[1], encoding='utf8'))
flt = sys.argv[2].lower() if len(sys.argv) > 2 else ''
cards = [c for c in deck['cards'] if c.get('noteType') == 'advanced-html' and flt in c['term'].lower()]
items = []
for i, c in enumerate(cards):
    a = c['advancedHtml']
    for side in ('front', 'back'):
        items.append({'id': f'c{i}{side[0]}', 'label': f"{c['term']} · {side}",
                      'html': a[side + 'Html'], 'css': a[side + 'Css']})
page = """<!doctype html><meta charset=utf-8><title>cards</title>
<style>body{margin:0;padding:16px;background:#222;font:12px system-ui;color:#ccc;display:flex;flex-wrap:wrap;gap:14px}
figure{margin:0}figcaption{max-width:340px;margin-bottom:4px}.h{width:340px;height:470px;overflow:auto;border-radius:18px;background:#111}</style>
<div id=root></div><script>
const items=%s;
for(const it of items){const f=document.createElement('figure');f.innerHTML='<figcaption></figcaption><div class=h></div>';
f.querySelector('figcaption').textContent=it.label;document.body.appendChild(f);
const s=f.querySelector('.h').attachShadow({mode:'open'});s.innerHTML='<style>*{box-sizing:border-box}'+it.css+'</style>'+it.html;}
</script>""" % json.dumps(items)
open(os.path.join(HERE, 'cards.html'), 'w', encoding='utf8').write(page)
print(len(cards), 'cards ->', os.path.join(HERE, 'cards.html'))
