# Считаем частоту всех слов
import operator
from collections import OrderedDict


def get_tf(words):
    num_words = len(words)
    unique = set(words)
    frequencies = {}
    for word in unique:
        frequencies[word] = float('{:.4f}'.format(words.count(word) / num_words))
    return frequencies


# Выделяем ключевые слова
def get_key_words(words):
    sorted_tuples = sorted(words.items(), key=operator.itemgetter(1))
    sorted_dict = OrderedDict()
    for k, v in sorted_tuples:
        sorted_dict[k] = v
    sorted_dict = dict(sorted_dict)
    words_values = list(sorted_dict.items())
    # выделяем слова с плотностью вхождения 5%
    threshold_value = words_values[(len(words_values) // 100 * 95)][1]
    key_words = {word: words[word] for word in words if words[word] >= threshold_value}
    return key_words
