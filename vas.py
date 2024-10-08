def count_unique_characters(input_string):
    """Возвращает количество уникальных символов в строке."""
    # Приводим строку к нижнему регистру для учета без учета регистра
    input_string = input_string.lower()

    # Используем множество для хранения уникальных символов
    unique_characters = set()

    for char in input_string:
        if char.isalnum():  # Учитываем только буквы и цифры
            unique_characters.add(char)

    return len(unique_characters), unique_characters