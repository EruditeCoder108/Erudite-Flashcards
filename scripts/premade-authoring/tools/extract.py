"""Extract a chapter's text (watermark removed), page by page: python extract.py <pdf> -> .work/<name>.txt"""
import sys, os, re
from _work import WORK
from clean_pdf import clean
pdf = sys.argv[1]
d, _ = clean(pdf)
name = os.path.splitext(os.path.basename(pdf))[0]
out = os.path.join(WORK, name + '.txt')
with open(out, 'w', encoding='utf8') as f:
    for i, p in enumerate(d):
        t = p.get_text()
        t = re.sub(r'([^\n]+\n)(\1)+', r'\1', t)      # bold headings are printed several times over
        t = re.sub(r'\nl\n', '\n• ', t).replace('Reprint 2026-27\n', '')
        f.write(f'=== PAGE {i}\n{t}\n')
print(out, len(d), 'pages')
