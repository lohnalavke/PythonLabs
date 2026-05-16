print((4%5)+1)

print("Пункт 5")
# Создание файла
data = [3, -5, 2, -8, 10, -1]
with open('numbers.txt', 'w') as f:
    for num in data:
        f.write(str(num) + '\n')

# Теперь основная программа
with open('numbers.txt', 'r') as f:
    numbers = list(map(float, f.readlines()))

mean_abs = sum(map(abs, numbers)) / len(numbers)
print('Числа:', numbers)
print('Средний модуль:', mean_abs)