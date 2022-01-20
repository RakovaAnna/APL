from searchForKeyWords import *
from searchForBorrowings import *
import matplotlib.pyplot as plt

review_text_name = 'input.txt'
other_text_names_list = ['text1.txt', 'text2.txt', 'text3.txt']
#input - это текстовая трансляция футбольного матча
#text1 - это текстовая трансляция футбольного матча (другая)
#text2 - это аналог input, измененного синонимизатором
#text3 - это "Алиса в стране чудес"

def sort_dicts(words1, words2):
    sorted_tuples = sorted(words1.items(), key=operator.itemgetter(1))
    sorted_dict1 = OrderedDict()
    sorted_dict2 = OrderedDict()
    for k, v in sorted_tuples:
        sorted_dict1[k] = v
        sorted_dict2[k] = words2[k]
    sorted_dict1 = dict(sorted_dict1)
    return sorted_dict1, dict(sorted_dict2)

# берем 1 текст нормализуем выделяем слова
# берем 2 текст нормализуем выделяем слова
# поскольку длина текстов разная, длина массивов словосочетаний тоже разная
# приводим массивы к одинаковой длине (берем первый квантиль):
#   берем наименьший текст и берем 5% самых популярных слов
#   берем наибольший текст, берем 5% самых популярных слов, но по количеству столько же сколько и в первом
# перебираем слова в текстах:
#   берем слова из первого текста
#   если оно есть во втором тексте то пишем % его вхождени
#   если его нет то пишем 0
# строим график
# если графики похожи то и тексты похожи

# Для слов
review_text_KWs = find_key_words(review_text_name)
i=2 #выбираем индекс сравниваемого текста
target_text_KWs = find_key_words(other_text_names_list[i])

print('Слова, заимствованные из другого текста :',list(set(review_text_KWs.keys()) & set(target_text_KWs.keys())))

for w in review_text_KWs:
    if w not in target_text_KWs:
        target_text_KWs[w]=0

for w in target_text_KWs:
    if w not in review_text_KWs:
        review_text_KWs[w]=0

target_text_KWs, review_text_KWs = sort_dicts(target_text_KWs, review_text_KWs)

plt.plot(list(target_text_KWs.keys()), list(target_text_KWs.values()), 'r', list(review_text_KWs.keys()), list(review_text_KWs.values()), 'b--')
plt.show()

print('Текст схож с другим текстом по среднему арифметическому соотношений частот на ' + str(
'{:.4f}'.format(determine_similarity_by_1way(target_text_KWs, review_text_KWs) * 100)) + '%')
print('Текст схож с другим текстом по косинусному сходству ' + str(
'{:.4f}'.format(determine_similarity_by_2way_simple(target_text_KWs, review_text_KWs))))

#РЕЗУЛЬТАТЫ

#1) Сравнение input и text1
#Текст схож с другим текстом по среднему арифметическому соотношений частот на 6.9484%
#Текст схож с другим текстом по косинусному сходству 0.4329

#2) Сравнение input и text2
#Текст схож с другим текстом по среднему арифметическому соотношений частот на 96.4057%
#Текст схож с другим текстом по косинусному сходству 0.9971

#3) Сравнение input и text3
#Текст схож с другим текстом по среднему арифметическому соотношений частот на 3.9754%
#Текст схож с другим текстом по косинусному сходству 0.1425