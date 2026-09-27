"""Shared paths for the authoring tools. Previews and contact sheets go to scripts/premade-authoring/.work/ (gitignored)."""
import os, sys
KIT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(KIT, '..', '..'))
WORK = os.path.join(KIT, '.work')
os.makedirs(WORK, exist_ok=True)
if KIT not in sys.path:
    sys.path.insert(0, KIT)
