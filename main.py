import sys
import re

import argparse

import cloud
import fetch
import font

parser = argparse.ArgumentParser()
parser.add_argument("--noshow", action="store_true", help="without image viewer")
parser.add_argument("--font", type=str, default="NotoSansMonoCJK-VF", help="font file name")
parser.add_argument("--relay", type=str, default="wss://yabu.me", help="nostr relay")
parser.add_argument("--limit", type=int, default=350, help="number of events")
parser.add_argument("--pubkey", type=str, default=None, help="author pubkey (optinal)")
parser.add_argument("-o", type=str, default="wordcloud_nostr.png", help="output file")
args = parser.parse_args()

ban_list=["77911886971fe579fe3e4f90d9dc7e91fcd74850dc2853681fff17654b218091","a3c13ef4c9eccfde01bd9326a2ab08b2ad7dc57f3b77db77723f8e2ad7ba24d6","9f77d173dcd94cc4243d36883b157f8c3283051dc6bd237b1c5ac400fb90cecb","139b1ed03764c10e796b902d36b55d182016f963fadd4548c998c21872f66b28","53efc19ec1e2795adf40ffe8f23bb981aca01999b28b4beea67f07ec20123c98","e0ca1e9e2be7d0e7611881dc1f5e18b38e50a54bd9ce5bc6c75c9ef7e62f31ca"]

font_path=font.find_font(args.font)

w=cloud.words()
contents=fetch.fetch(args.relay, ban_list, args.limit, args.pubkey)
for content in contents:
    if len(content) > 200:
        continue
    lines=content.split()
    for line in lines:
        if re.match('[a-zA-z0-9!#$%&\'*+-\\\.^_`/|~:,]+',line):
            continue
        w.get_words(line)
if not(args.noshow):
    w.render(font_path)
w.save_file(args.o,font_path)

