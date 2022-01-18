import wordProcessing

# Считываем тексты и переводим все слова в нижний регистр.
text = wordProcessing.read_text()
text = text.lower()
# Убираем пунктуацию
text = wordProcessing.delete_punctuation(text)

# Нормализовываем слова в тексте, сохраняя разделение на предложения
normal_text = wordProcessing.normalize_words(text.split())

print(normal_text)
