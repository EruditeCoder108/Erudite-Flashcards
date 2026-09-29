"""Headless-Edge screenshot sheets of advanced-HTML cards (front+back), 4 faces per row.
Usage: python shot.py <deck.json> [filter|filter2] [page] [faces-per-page=8] [seconds into animation, default 10 = final state]
Writes .work/shot_<page>.png (final animation state: virtual time lets delays finish)."""
import sys, json, os, subprocess, html
from _work import WORK
deck = json.load(open(sys.argv[1], encoding='utf8'))
flt = (sys.argv[2] if len(sys.argv) > 2 else '').lower()
page = int(sys.argv[3]) if len(sys.argv) > 3 else 0
per = int(sys.argv[4]) if len(sys.argv) > 4 else 8
cards = [c for c in deck['cards'] if c.get('noteType') == 'advanced-html' and any(f in c['term'].lower() for f in flt.split('|'))]
faces = []
for c in cards:
    a = c['advancedHtml']
    for side in ('front', 'back'):
        faces.append((f"{c['term'][:48]} · {side}", a[side + 'Html'], a[side + 'Css']))
tsec = sys.argv[5] if len(sys.argv) > 5 else '10'
total = len(faces)
faces = faces[page * per:(page + 1) * per]
items = ''.join(f'<figure><figcaption>{html.escape(l)}</figcaption><div class=h data-i={i}></div></figure>' for i, (l, _, _) in enumerate(faces))
data = json.dumps([{'html': h, 'css': c} for _, h, c in faces])
doc = ('<!doctype html><meta charset=utf-8><style>body{margin:0;padding:10px;background:#222;font:12px system-ui;color:#ccc;display:flex;flex-wrap:wrap;gap:10px;width:1440px}'
       'figure{margin:0}figcaption{width:340px;margin-bottom:3px;white-space:nowrap;overflow:hidden}.h{width:340px;height:470px;overflow:hidden;border-radius:18px;background:#111}</style>'
       f'{items}<script>const T="{tsec}";const D={data};document.querySelectorAll(".h").forEach(e=>{{const it=D[e.dataset.i];const s=e.attachShadow({{mode:"open"}});'
       's.innerHTML="<style>*{box-sizing:border-box}*{animation-delay:-"+T+"s!important;animation-play-state:paused!important}"+it.css+"</style>"+it.html;});</script>')
src = os.path.join(WORK, 'shot.html')
open(src, 'w', encoding='utf8').write(doc)
out = os.path.join(WORK, f'shot_{page}.png')
rows = (len(faces) + 3) // 4
edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if os.path.exists(out): os.remove(out)
import time
for _ in range(4):
    subprocess.run([edge, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--window-size=1460,{rows * 505 + 30}',
                    '--virtual-time-budget=6000', f'--screenshot={out}', __import__('pathlib').Path(src).as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
    if os.path.exists(out): break
    time.sleep(2)
print(out, f'faces {page * per + 1}-{page * per + len(faces)} of {total}')
