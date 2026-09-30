"""Apply a patch file (same block format as patchscript.py) across several deck scripts: each block goes to the one script
that contains its OLD text exactly once. Fails without writing if any block matches nowhere or in more than one script.
Usage: python patchmulti.py <patchfile> <decks/script1.py> <decks/script2.py> ..."""
import sys, re, os, subprocess
patch, scripts = sys.argv[1], sys.argv[2:]
srcs = {s: open(s, encoding='utf8').read() for s in scripts}
blocks = re.findall(r'=====OLD\n(.*?)\n=====NEW\n(.*?)\n=====END', open(patch, encoding='utf8').read(), re.S)
if not blocks:
    sys.exit('no blocks found')
touched = set()
for i, (old, new) in enumerate(blocks, 1):
    hits = [(s, t.count(old)) for s, t in srcs.items() if old in t]
    if len(hits) != 1 or hits[0][1] != 1:
        sys.exit(f'block {i}: matches {[(os.path.basename(s), n) for s, n in hits]} for: {old[:90]!r}')
    s = hits[0][0]
    srcs[s] = srcs[s].replace(old, new)
    touched.add(s)
for s in touched:
    open(s, 'w', encoding='utf8').write(srcs[s])
print(len(blocks), 'replacements in', len(touched), 'scripts')
for s in sorted(touched):
    r = subprocess.run([sys.executable, s], capture_output=True, text=True, encoding='utf8')
    print(os.path.basename(s), (r.stdout.strip().splitlines() or [''])[-1], r.stderr.strip()[-200:])
