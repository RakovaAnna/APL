from searchForKeyWords import *
from searchForBorrowings import *
import matplotlib.pyplot as plt

review_text_name = 'input.txt'
other_text_names_list = ['text1.txt', 'text2.txt', 'text3.txt']


def sort_dicts(words1, words2):
    sorted_tuples = sorted(words1.items(), key=operator.itemgetter(1))
    sorted_dict1 = OrderedDict()
    sorted_dict2 = OrderedDict()
    for k, v in sorted_tuples:
        sorted_dict1[k] = v
        sorted_dict2[k] = words2[k]
    sorted_dict1 = dict(sorted_dict1)
    return sorted_dict1, dict(sorted_dict2)

# def leave_only_keywords(text, keywords):
#     tokens = get_lower_text_without_punctuation(text).split()
#     new_tokens = []
#     morph = pymorphy2.MorphAnalyzer()
#     for t in tokens:
#         normal = (morph.parse(t)[0]).normal_form
#         if normal in keywords.keys():
#             new_tokens.append(normal)
#     return new_tokens


# review_text_KWs = find_key_words(review_text_name)
# review_text_name_with_only_KWs = leave_only_keywords(review_text_name, review_text_KWs)

# other_text_KWs_list = []
# other_text_name_with_only_KWs = []
# for i in range(len(other_text_names_list)):
#     other_text_KWs_list.append(find_key_words(other_text_names_list[i]))
#     other_text_name_with_only_KWs.append(leave_only_keywords(other_text_names_list[i],other_text_KWs_list[i]))
#
# words1 = rewiew_text_name_with_only_KWs
# w_combs1 = get_word_combinations(words1)
#
# set1 = get_tf(w_combs1)
# plt.plot(set1.keys(),set1.values())
#
# for i in range(len(other_text_name_with_only_KWs)):
#     fname = other_text_names_list[i]
#     words2 = other_text_name_with_only_KWs[i]
#     w_combs2 = get_word_combinations(words2)
#     set2 = get_tf(w_combs2)
#     general = list(set(words1) & set(words2))
#     print('Слова, заимствованные из текста файла '+fname+':',general)
#
#     print('Текст схож с текстом файла (1-ым способом) по словам ' + fname + ' на ' + str(
#         '{:.4f}'.format(determine_similarity_by_1way(get_tf(words1), get_tf(words2)) * 100)) + '%')
#     print('Текст схож с текстом файла (2-ым способом) по словам ' + fname + ' на ' + str(
#         '{:.4f}'.format(determine_similarity_by_2way(get_tf(words1), get_tf(words2)) * 100)) + '%')
#     print('Текст схож с текстом файла (1-ым способом) по словосочетаниям ' + fname + ' на ' + str(
#         '{:.4f}'.format(determine_similarity_by_1way(set1, set2) * 100)) + '%')
#     print('Текст схож с текстом файла (2-ым способом) по словосочетаниям ' + fname + ' на ' + str(
#         '{:.4f}'.format(determine_similarity_by_2way(set1, set2) * 100)) + '%')
#
#     plt.plot(list(set2.keys()),list(set2.values()))
#
# plt.xticks(rotation=90)
# plt.show()


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
target_text_KWs = find_key_words(other_text_names_list[1])

# Для словосочетаний
# key_words_1 = find_key_words(review_text_name)
# key_words_2 = find_key_words(other_text_names_list[1])
#
# _review_text_KWs = get_tf(get_word_combinations(list(key_words_1.keys())))
# _target_text_KWs = get_tf(get_word_combinations(list(key_words_2.keys())))
#
# review_text_KWs = get_key_words(_review_text_KWs)
# target_text_KWs = get_key_words(_target_text_KWs)



bigger = review_text_KWs if len(review_text_KWs) > len(target_text_KWs) else target_text_KWs
smaller = target_text_KWs if len(review_text_KWs) > len(target_text_KWs) else review_text_KWs

diff = len(bigger) - len(smaller)
keys = list(bigger.keys())

for i in range(diff):
    del bigger[keys[i]]

words1 = {}
words2 = {}
bigger_items = list(bigger.items())
smaller_items = list(smaller.items())
smaller_keys = list(smaller.keys())
for i in range(len(bigger)):
    words1[str(i)] = list(bigger.items())[i][1]
    words2[str(i)] = smaller_items[i][1] if bigger_items[i][0] in smaller_keys else 0

words1, words2 = sort_dicts(words1, words2)
print(words1.keys())
print(words2.keys())

plt.plot(list(words1.keys()), list(words1.values()), 'r', list(words2.keys()), list(words2.values()), 'b--')
plt.show()
