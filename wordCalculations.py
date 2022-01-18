# Считаем частоту всех слов
def TF(words):
    num_words = len(words)
    unique = set(words)
    frequencies = {}
    for word in unique:
        frequencies[word] = float('{:.4f}'.format(words.count(word) / num_words))
    return frequencies
