#!/usr/bin/env bash
# chap.sh <script-stem e.g. math12_ch04> <deck dir glob fragment e.g. 12th/Mathematics/class12-mathematics-ch04> [minlen]
cd "$(dirname "$0")/.." || exit 1
export PYTHONIOENCODING=utf8 PYTHONWARNINGS=ignore
D=$(ls -d ../../premade-cards/$2*/ | head -1)deck.json
I=$(python tools/longidx.py "$D" ${3:-110} | cut -d'|' -f1)
echo "== $1: $I"
[ -n "$I" ] && python tools/srcfor.py "decks/$1.py" "$D" "$I" | cut -c1-900
