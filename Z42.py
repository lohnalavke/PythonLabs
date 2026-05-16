m = (4%5)+1
print(m, m+5, m+10)

# Задание 42, пункты 5, 10, 15
from string import punctuation
from functools import reduce
import os

# Создание тестового текстового файла (если его нет)
test_lines = [
    "Дом, который построил Джек.",
    "А это пшеница, которая в тёмном чулане хранится,",
    "в доме, который построил Джек.",
    "Весёлый дровосек.",
    "Синевато-беловатый туман.",
    "Самый длинный предлинный-предлинный."
    ]
with open('Текст.txt', 'w', encoding='utf-8') as f:
    for line in test_lines:
        f.write(line + '\n')

# Функция для удаления знаков пунктуации в начале и конце слова
def clean_word(word):
    if len(word) == 0:
        return word
    if word[0] in punctuation:
        return clean_word(word[1:])
    if word[-1] in punctuation:
        return clean_word(word[:-1])
    return word

#5
with open('Текст.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip() != '']

all_words = []
for line in lines:
    all_words.extend(line.split())

cleaned_words = list(map(clean_word, all_words))

# Фильтруем слова, начинающиеся на строчную «д»
words_with_d = list(filter(lambda w: w.startswith('д'), cleaned_words))

if words_with_d:
    # Ищем самое короткое слово
    shortest_d = reduce(lambda a, b: a if len(a) <= len(b) else b, words_with_d)
    print("5. Самое короткое слово, начинающееся на строчную 'д':", shortest_d)
else:
    print("5. Нет слов, начинающихся на строчную 'д'")

#10
words_with_iy = list(filter(lambda w: w.endswith('ый'), cleaned_words))

if words_with_iy:
    longest_iy = reduce(lambda a, b: a if len(a) >= len(b) else b, words_with_iy)
    print("10. Самое длинное слово с окончанием '-ый':", longest_iy)
else:
    print("10. Нет слов с окончанием '-ый'")

#15
longest_line = reduce(lambda a, b: a if len(a) >= len(b) else b, lines)
print("15. Самая длинная строка:", longest_line)
print("   Длина:", len(longest_line), "символов")