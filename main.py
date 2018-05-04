# coding=utf-8

import re
# import synonyms
# import jieba.posseg as pseg



def Read():
    with open('./txt/aaaaa.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    title_list = re.findall('<title=(.*?)>', content)
    title = title_list[0] if len(title_list) != 0 else None
    article_list = re.findall('<neirong=([\s\S]*)>',(content.replace('\n','')).replace('<p>',''))
    article = article_list[0] if len(article_list) != 0 else None
    words_list = []
    list = article.split('</p>')

    print(words_list)


    return title


def words_change(words):
    words_tuple = pseg.lcut(words)
    word_list = []
    for word,flag in words_tuple:
        if flag == 'a' or flag=='ad' or flag=='v':  # 词性判断
            seg_list = (synonyms.nearby(word))[0]
            if len(seg_list) <= 1:
                word = word
            else:
                word = seg_list[1]
        word_list.append(word)
    return "".join(word_list)


if __name__ == '__main__':
    # wrods = '“北京遇上西雅图”中映射的美国房产问题'
    # words_change(wrods)
    Read()
