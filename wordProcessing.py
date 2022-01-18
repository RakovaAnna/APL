import pymorphy2
from consts import *


# Считывание текста
from nltk.corpus import stopwords


def read_text(name):
    try:
        file = open(name, encoding="utf8")
        text = file.read()
        file.close()
    except FileNotFoundError:
        text = ''
    return text


# Удаление пунктуации (кроме точек)
def delete_punctuation(text):
    # Удаляем всю пунктуацию внутри предложений.
    for char in punctuation_marks_all:
        text = text.replace(char, '')
    # Знаки, разделяющие текст по предложениям, заменяем на точки
    for char in punctuation_marks_sents:
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
def delete_stop(words, result_tf):
    russian_stop = set(stopwords.words('russian'))
    res = {}
    for word in words:
        if word not in russian_stop:
            res[word] = result_tf[word]
    return res
