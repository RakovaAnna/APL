from searchForKeyWords import *
from searchForBorrowings import *
import matplotlib.pyplot as plt

review_text_name = 'input.txt'
other_text_names_list = ['text1.txt','text2.txt','text3.txt']

def leave_only_keywords(text, keywords):
    tokens = get_lower_text_without_punctuation(text).split()
    new_tokens = []
    morph = pymorphy2.MorphAnalyzer()
    for t in tokens:
        normal = (morph.parse(t)[0]).normal_form
        if normal in keywords.keys():
            new_tokens.append(normal)
    return new_tokens

review_text_KWs = find_key_words(review_text_name)
rewiew_text_name_with_only_KWs = leave_only_keywords(review_text_name,review_text_KWs)

other_text_KWs_list = []
other_text_name_with_only_KWs = []
for i in range(len(other_text_names_list)):
    other_text_KWs_list.append(find_key_words(other_text_names_list[i]))
    other_text_name_with_only_KWs.append(leave_only_keywords(other_text_names_list[i],other_text_KWs_list[i]))

words1 = rewiew_text_name_with_only_KWs
w_combs1 = get_word_combinations(words1)

set1 = get_tf(w_combs1)
plt.plot(set1.keys(),set1.values())

for i in range(len(other_text_name_with_only_KWs)):
    fname = other_text_names_list[i]
    words2 = other_text_name_with_only_KWs[i]
    w_combs2 = get_word_combinations(words2)
    set2 = get_tf(w_combs2)
    general = list(set(words1) & set(words2))
    print('Слова, заимствованные из текста файла '+fname+':',general)

    print('Текст схож с текстом файла (1-ым способом) по словам ' + fname + ' на ' + str(
        '{:.4f}'.format(determine_similarity_by_1way(get_tf(words1), get_tf(words2)) * 100)) + '%')
    print('Текст схож с текстом файла (2-ым способом) по словам ' + fname + ' на ' + str(
        '{:.4f}'.format(determine_similarity_by_2way(get_tf(words1), get_tf(words2)) * 100)) + '%')
    print('Текст схож с текстом файла (1-ым способом) по словосочетаниям ' + fname + ' на ' + str(
        '{:.4f}'.format(determine_similarity_by_1way(set1, set2) * 100)) + '%')
    print('Текст схож с текстом файла (2-ым способом) по словосочетаниям ' + fname + ' на ' + str(
        '{:.4f}'.format(determine_similarity_by_2way(set1, set2) * 100)) + '%')

    plt.plot(list(set2.keys()),list(set2.values()))

plt.xticks(rotation=90)
plt.show()