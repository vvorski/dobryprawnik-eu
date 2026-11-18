#!/usr/bin/env bash
# Usage: ./set-base.sh /dobryprawnik-eu   (GitHub Pages project URL)
#        ./set-base.sh /                  (own domain at root)
set -euo pipefail
cd "$(dirname "$0")"
new="${1%/}"
cur=$(cat .base 2>/dev/null || echo "")
js=$(ls assets/index-*.js)
for f in index.html "$js"; do
  sed -i "s#\"$cur/assets/#\"$new/assets/#g" "$f"
done
sed -i "s#href:\"$cur/#href:\"$new/#g" "$js"
sed -i "s#basename:e=\"${cur:-/}\"#basename:e=\"${new:-/}\"#" "$js"
echo -n "$new" > .base
cp index.html 404.html
echo "base set to '${new:-/}'"
