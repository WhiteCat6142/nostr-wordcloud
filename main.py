import sys
import re

import cloud
import fetch

file='wordcloud_nostr.png' if len(sys.argv) == 1 else sys.argv[1]

font_path="/usr/share/fonts/google-noto-sans-mono-cjk-vf-fonts/NotoSansMonoCJK-VF.ttc"

ban_list=["77911886971fe579fe3e4f90d9dc7e91fcd74850dc2853681fff17654b218091","a3c13ef4c9eccfde01bd9326a2ab08b2ad7dc57f3b77db77723f8e2ad7ba24d6","9f77d173dcd94cc4243d36883b157f8c3283051dc6bd237b1c5ac400fb90cecb","139b1ed03764c10e796b902d36b55d182016f963fadd4548c998c21872f66b28"]
relay="wss://yabu.me"
limit=300

w=cloud.words()
contents=fetch.fetch(relay,ban_list,limit)
for content in contents:
    lines=content.split()
    for line in lines:
        if re.match('[a-zA-z0-9!#$%&\'*+-\\\.^_`/|~:,]+',line):
            continue
        w.get_words(line)
w.render(font_path)
w.save_file(file,font_path)

