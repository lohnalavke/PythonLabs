print((4%6)+1)

print("Пункт 5")
# список слов из строки документации pow()
words = pow.__doc__.split()

sorted_words = sorted(words, key=len, reverse=True)

print(sorted_words)