#!/usr/bin/sh
nostrf=nostr-cloud-$(date +%Y%m%d%H%M).png
python3 ./main.py --noshow -o $nostrf
pngquant -ext -2.png 16 $nostrf
