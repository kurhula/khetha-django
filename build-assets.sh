#!/bin/sh -e

test -e build/assets && rm -r build/assets
mkdir -p build/assets

cp -av node_modules/normalize.css/normalize.css build/assets

for package in \
    button \
    card \
    floating-label \
    layout-grid \
    ripple \
    snackbar \
    textfield \
    theme \
    top-app-bar \
    typography \
; do
    cp -av "node_modules/@material/$package/dist/"*.min.* build/assets
done

cp -av node_modules/zepto/dist/zepto.min.js build/assets
