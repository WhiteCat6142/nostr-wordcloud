import matplotlib.pyplot as plt
import japanize_matplotlib
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import MeCab
import re

class words:

    def __init__(self):
        self.word_list = []
        self.wc = None

    def get_words(self,text):
        mecab = MeCab.Tagger("-Osimple")
        parsed = mecab.parse(text)
        lines = parsed.split('\n')
        lines = lines[0:-2]
        tmpword=""
        for line in lines:
            tmp = re.split('\t|-', line)
            if (tmp[1] in ["名詞"]) and (tmp[2] in ["一般", "固有名詞"])  and (tmp[0]!="自分") and (tmp[0]!="人"):
                tmpword+=tmp[0]
            elif tmpword!="":
                self.word_list.append(tmpword)
                tmpword=""
         if tmpword!="":
                self.word_list.append(tmpword)
                tmpword=""

    @classmethod
    def read_file(cls,file):
        read_text = open(file, encoding="utf8").read()
        w=cls()
        w.get_words(read_text)

    def __str__(self):
        return " ".join(self.word_list)

    def cloud(self,font_path):
        wc = WordCloud(font_path=font_path,background_color='white')
        wc.generate(str(self))
        return wc

    def render(self,font_path):
        if self.wc is None:
            self.wc = self.cloud(font_path)
        plt.imshow(self.wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def save_file(self,file,font_path):
        if self.wc is None:
            self.wc = self.cloud(font_path)
        self.wc.to_file(file)
