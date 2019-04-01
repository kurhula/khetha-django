#!/bin/sh -e

rm -r build/assets
mkdir -p build/assets

cp -anv node_modules/normalize.css/normalize.css -t build/assets

for package in card layout-grid ripple theme typography; do
    cp -anv "node_modules/@material/$package/dist/"*.min.* -t build/assets
done
