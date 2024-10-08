def find_duplicate_words(input_string):
    """Возвращает список дублирующихся слов в строке без учета регистра."""
    # Приводим строку к нижнему регистру и разбиваем на слова
    words = input_string.lower().split()
    # Используем словарь для подсчета слов
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    # Извлекаем дублирующиеся слова
    duplicates = [word for word, count in word_count.items() if count > 1]
    
    return duplicates
