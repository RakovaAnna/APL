import wordProcessing


# Считываем тексты и переводим все слова в нижний регистр.
from wordCalculations import *

text = wordProcessing.read_text()
text = text.lower()
# Убираем пунктуацию
text = wordProcessing.delete_punctuation(text)

# Нормализовываем слова в тексте, сохраняя разделение на предложения
normal_text = wordProcessing.normalize_words(text.split())

# Разбиваем текст на отдельные слова и на отдельные предложения
words = (normal_text.replace('.', '')).split()
sentences = normal_text.split('. ')

# Вычисляем TF для текстов
result_tf = TF(words)

# Удаляем стоп-слова для TF
result_tf = wordProcessing.del_stop(words, result_tf)
print(normal_text)
print(result_tf)
