"""Retire an older premade deck in favour of a rebuilt one, then repackage.

Usage: python scripts/premade-authoring/replace_deck.py <subject folder> <old zip name> [new deck id]
e.g.   python scripts/premade-authoring/replace_deck.py premade-cards/11th/Biology erudite_chapter_3_plant_kingdom_revised.zip class11-biology-ch03-plant-kingdom

Removes the old zip and its manifest entry, runs `npm run zip:premade`, copies the
new deck's description into the manifest, and keeps the manifest in chapter order.
"""
import json, os, re, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
subject = os.path.join(ROOT, sys.argv[1])
old_zip = sys.argv[2]
new_id = sys.argv[3] if len(sys.argv) > 3 else None
manifest_path = os.path.join(subject, 'manifest.json')


def load():
    with open(manifest_path, encoding='utf8') as f:
        return json.load(f)


def save(items):
    with open(manifest_path, 'w', encoding='utf8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


old_path = os.path.join(subject, old_zip)
if os.path.exists(old_path):
    subprocess.run(['git', 'rm', '-q', old_path], cwd=ROOT, check=False)
    if os.path.exists(old_path):
        os.remove(old_path)
old_id = old_zip[:-4] if old_zip.endswith('.zip') else old_zip
save([i for i in load() if i.get('id') != old_id and (i.get('fileName') or '') != old_zip])

subprocess.run('npm run zip:premade', cwd=ROOT, shell=True, check=True, stdout=subprocess.DEVNULL)

items = load()
if new_id:
    with open(os.path.join(subject, new_id, 'deck.json'), encoding='utf8') as f:
        deck = json.load(f)
    for item in items:
        if item.get('id') == new_id:
            if deck.get('description'):
                item['description'] = deck['description']
            item['tags'] = [t for t in deck['cards'][0].get('tags', [])[:2]] + ['neet'] if deck.get('cards') else item.get('tags', [])
            item['estimatedTime'] = f"{max(10, round(item.get('cardCount', 0) * 0.2))} minutes"
            print(item)


def chapter(item):
    match = re.search(r'chapter[\s_:-]*(\d+)', item.get('name', ''), re.I) or re.search(r'ch[\s_-]*0*(\d+)', item.get('id', ''), re.I)
    return int(match.group(1)) if match else 999


items.sort(key=chapter)
save(items)
print([i['name'][:28] for i in items])
