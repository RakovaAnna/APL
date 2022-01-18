from wordProcessing import *
from wordCalculations import *

def get_lower_text_without_punctuation(file_name):
    # Считываем тексты и переводим все слова в нижний регистр
    text = read_text(file_name)
    text = text.lower()
    # Убираем пунктуацию
    text = delete_punctuation(text)
    return text

def find_key_words(file_name):
    text = get_lower_text_without_punctuation(file_name)

    # Нормализовываем слова в тексте, сохраняя разделение на предложения
    normal_text = normalize_words(text.split())

    # Разбиваем текст на отдельные слова и на отдельные предложения
    words = (normal_text.replace('.', '')).split()
    sentences = normal_text.split('. ')

    # Вычисляем TF для текстов
    result_tf = get_tf(words)

    # Удаляем стоп-слова для TF
    result_tf = delete_stop(words, result_tf)

    # Выделяем ключевые слова
    key_words = get_key_words(result_tf)
    return key_words