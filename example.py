import matplotlib.pyplot as plt
from wordcloud import WordCloud
import MeCab
from texts import text


def wakati(text):
    tagger = MeCab.Tagger('')
    tagger.parse('')
    node = tagger.parseToNode(text)
    word_list = []

    while node:
        pos = node.feature.split(",")[0]
        # 品詞を選択
        if pos in ["形容詞", "動詞", "名詞", "副詞"]:
            word = node.surface
            word_list.append(word)
        node = node.next

    return word_list


def create_wordcloud(text):

    # ストップワードの設定
    stop_words = [u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
                  u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した', u'思う', \
                  u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て', u'に', u'を', u'は', u'の', u'が', u'と', u'た', u'し', u'で', \
                  u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'']

    wordcloud = WordCloud(background_color="white",
                          width=900,
                          height=500,
                          font_path='ipaexm.ttf',
                          stopwords=set(stop_words)).generate(text)

    plt.figure(figsize=(15, 12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


wordlist = wakati(text)
create_wordcloud(" ".join(wordlist))
