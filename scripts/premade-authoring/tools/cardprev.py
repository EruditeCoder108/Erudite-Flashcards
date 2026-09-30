"""Preview basic/cloze cards the way the app's study screen draws them (real app CSS + KaTeX).
Usage: python cardprev.py <deck.json> [start=0] [count=8] [--fmt]     -> .work/prev_<start>.png
--fmt runs fmt.py on the cards first (without saving) to preview the change."""
import sys, os, re, json, copy, subprocess, pathlib, time, html
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from _work import WORK
import fmt
ROOT = pathlib.Path(__file__).resolve().parents[3]
args = [a for a in sys.argv[1:] if not a.startswith('--')]
deck = json.load(open(args[0], encoding='utf8'))
start = int(args[1]) if len(args) > 1 else 0
count = int(args[2]) if len(args) > 2 else 8
cards = [c for c in deck['cards'] if c.get('noteType') in ('basic', 'cloze')]
if '--fmt' in sys.argv:
    cards = [fmt.format_card(copy.deepcopy(c), fmt.subject_of(args[0])) for c in cards]
idx = next((a[6:] for a in sys.argv if a.startswith('--idx=')), '')
cards = [cards[int(i)] for i in idx.split(',')] if idx else cards[start:start + count]

def faces(c):
    if c['noteType'] == 'basic':
        return c['term'], c['definition']
    t = re.sub(r'\{\{c\d::(.*?)(::.*?)?\}\}', r'<mark class="cloze-blank">[…]</mark>', c['text'])
    a = re.sub(r'\{\{c\d::(.*?)(::.*?)?\}\}', r'<mark class="cloze-answer">\1</mark>', c['text'])
    return t, a + (('\n' + c['extra']) if c.get('extra') else '')

figs = ''
for c in cards:
    t, a = faces(c)
    for label, body in (('Q', t), ('A', a)):
        figs += (f'<figure><div class="card-face"><div class="lbl">{label}</div>'
                 f'<div class="card-text medium-content"><div class="card-text-inline">{body}</div></div></div></figure>')
css = ''.join((ROOT / 'www' / 'mobile' / 'css' / n).read_text(encoding='utf8') for n in ('tokens.css', 'mobile-study.css'))
doc = f'''<!doctype html><meta charset=utf-8><link rel=stylesheet href="{(ROOT/'www'/'vendor'/'katex'/'katex.min.css').as_uri()}">
<style>{css}
html,body{{background:#e9e6df}}body{{margin:0;padding:10px;display:flex;flex-wrap:wrap;gap:10px;width:1660px;font-family:system-ui}}
figure{{margin:0}}.card-face{{position:relative!important;width:390px;height:420px;background:#fff;border-radius:22px;padding:34px 18px 18px;box-sizing:border-box;display:flex;overflow:hidden;transform:none!important;opacity:1!important;backface-visibility:visible!important;--card-text-align:center}}
.lbl{{position:absolute;left:18px;top:12px;font:700 12px system-ui;color:#888;letter-spacing:.1em}}
.card-text{{color:#1f2430}}</style>
<body class="theme-light">{figs}
<script src="{(ROOT/'www'/'vendor'/'katex'/'katex.min.js').as_uri()}"></script>
<script src="{(ROOT/'www'/'vendor'/'katex'/'auto-render.min.js').as_uri()}"></script>
<script src="{(ROOT/'js'/'core'/'math-render.js').as_uri()}"></script>
<script>document.querySelectorAll('.card-text').forEach(e=>EruditeMath.renderMath(e))</script>'''
src = os.path.join(WORK, 'prev.html')
open(src, 'w', encoding='utf8').write(doc)
out = os.path.join(WORK, f'prev_{start}.png')
rows = (len(cards) * 2 + 3) // 4
edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if os.path.exists(out): os.remove(out)
for _ in range(4):
    subprocess.run([edge, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--window-size=1680,{rows * 440 + 30}',
                    '--virtual-time-budget=4000', f'--screenshot={out}', pathlib.Path(src).as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
    if os.path.exists(out): break
    time.sleep(2)
print(out)
