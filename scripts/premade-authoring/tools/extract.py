"""Extract a chapter's text (watermark removed), page by page: python extract.py <pdf> -> .work/<name>.txt"""
import sys, os
from _work import WORK
from clean_pdf import clean
pdf = sys.argv[1]
d, _ = clean(pdf)
name = os.path.splitext(os.path.basename(pdf))[0]
out = os.path.join(WORK, name + '.txt')
with open(out, 'w', encoding='utf8') as f:
    for i, p in enumerate(d):
        f.write(f'=== PAGE {i}\n{p.get_text()}\n')
print(out, len(d), 'pages')
