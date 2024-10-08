import bos
import gos
import vas
a = input("Введите текст")
b = input("Выберите метод:""(1) выводит кол-во уникальных символов в строке" "(2) выводит кол-во уникальных слов" "(3) Выводит дублирующиеся слова")
if b=="1":
 count, unique_chars = vas.count_unique_characters(a)
 print(f"Количество уникальных символов: {count}")
 print(f"Уникальные символы: {', '.join(unique_chars)}")
elif b=="2":
 unique_count = gos.count_unique_words(a)
 print(f"Количество уникальных слов: {unique_count}")
elif b=="3":
 duplicates = bos.find_duplicate_words(a)
 if duplicates:
  print("Дублирующиеся слова:", ", ".join(duplicates))
 else:
  print("Дублирующихся слов не найдено.")