"""Apply exact-text replacements to a deck script and rebuild it.
Usage: python patchscript.py <decks/script.py> <patchfile>
Patch file: blocks of
    =====OLD
    text to find (must occur exactly once in the script)
    =====NEW
    replacement text
    =====END
Raw text, no escaping. Fails without writing if any block does not match exactly once."""
import sys, re, subprocess, os
script, patch = sys.argv[1], sys.argv[2]
src = open(script, encoding='utf8').read()
blocks = re.findall(r'=====OLD\n(.*?)\n=====NEW\n(.*?)\n=====END', open(patch, encoding='utf8').read(), re.S)
if not blocks:
    sys.exit('no blocks found')
for i, (old, new) in enumerate(blocks, 1):
    n = src.count(old)
    if n != 1:
        sys.exit(f'block {i}: {n} matches for: {old[:90]!r}')
    src = src.replace(old, new)
open(script, 'w', encoding='utf8').write(src)
print(len(blocks), 'replacements applied to', os.path.basename(script))
if '--nobuild' not in sys.argv:
    here = os.path.dirname(os.path.abspath(script))
    r = subprocess.run([sys.executable, script], capture_output=True, text=True, encoding='utf8')
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else '', r.stderr.strip()[-300:])
