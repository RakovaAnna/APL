import pymorphy2
import math

import nltk
from nltk.corpus import stopwords

russian_stop = set(stopwords.words('russian'))
morph = pymorphy2.MorphAnalyzer()


# Считываем тексты из файла.
def read_text():
    try:
        f = open("input.txt", "r")
        text = f.read()
        f.close()
    except FileNotFoundError:
        text = ''
    return text


# Убираем лишнюю пунктуацию.
def delete_punctuation(text):
    # Удаляем всю пунктуацию внутри предложений.
    for char in ',', ';', ':', '—', ')', '(', '"', '-':
        text = text.replace(char, '')
    # Знаки, разделяющие текст по предложениям, заменяем на точки
    for char in '.', '!', '?':
        text = text.replace(char, ' . ')
    return text


# Нормализуем все слова в тексте, сохраняя разделение на предложения
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


# Считываем тексты и переводим все слова в нижний регистр.
text = read_text()
text = text.lower()
# Убираем пунктуацию
text = delete_punctuation(text)

# Нормализовываем слова в тексте, сохраняя разделение на предложениия
normal_text = normalize_words(text.split())

print(normal_text)
