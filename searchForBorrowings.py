def read_text(file_name):
    try:
        f = open(file_name, "r")
        text = f.read()
        f.close
    except FileNotFoundError:
        text = ''
    return text

def get_word_combinations(words):
    word_combinations = []
    length = len(words)
    if length==1:
        return [words[0]]
    for i in range(length):
        if i<length-1:
            word_combinations.append(words[i]+' '+words[i+1])
    return list(set(word_combinations))

#среднее арифметическое соотношений частот
def determine_similarity_by_1way(set1, set2):
    similarity_list = []
    for key in set1:
        if key in set2:
            similarity_list.append(min(set1[key],set2[key])/max(set1[key],set2[key]))
    if len(similarity_list)==0:
        return 0
    return sum(similarity_list)/len(similarity_list)

#косинусное сходство
def determine_similarity_by_2way(set1, set2):
    summa = 0
    for key in set1:
        if key in set2:
            summa=summa+set1[key]*set2[key]
    return summa