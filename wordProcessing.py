import pymorphy2


# Считывание текста
from nltk.corpus import stopwords


def read_text():
    try:
        f = open("input.txt", "r")
        text = f.read()
        f.close()
    except FileNotFoundError:
        text = ''
    return text


# Удаление пунктуации (кроме точек)
def delete_punctuation(text):
    # Удаляем всю пунктуацию внутри предложений.
    for char in ',', ';', ':', '—', ')', '(', '"', '-':
        text = text.replace(char, '')
    # Знаки, разделяющие текст по предложениям, заменяем на точки
    for char in '.', '!', '?':
        text = text.replace(char, ' . ')
    return text


# Нормализация слов в текста
def normalize_words(words):
    morph = pymorphy2.MorphAnalyzer()
    text = ''
    for i in range(len(words)):
        if words[i] == '.':
            text = text + ' ' + '.'
        else:
            normal = morph.parse(words[i])[0]
            text = text + ' ' + normal.normal_form
    return text


# Удаляем стоп-слова.
def del_stop(words, result_tf):
    russian_stop = set(stopwords.words('russian'))
    res = {}
    for word in words:
        if word not in russian_stop:
            res[word] = result_tf[word]
    return res
