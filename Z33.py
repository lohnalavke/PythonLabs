# Задание 33
import math
from functools import lru_cache

def my_range(mode, *args):
    # Разбор аргументов как у range
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        raise TypeError("Ожидается от 1 до 3 аргументов")

    # Вспомогательная функция для чисел Фибоначчи
    @lru_cache(maxsize=None)  # кешируем для скорости
    def fib(n):
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fib(n-1) + fib(n-2)

    result = []
    i = start
    while i < stop:
        if mode == 'square':
            val = i * i
        elif mode == 'cube':
            val = i ** 3
        elif mode == 'sqrt':
            val = math.sqrt(i) if i >= 0 else None
        elif mode == 'log':
            val = math.log(i) if i > 0 else None
        elif mode == 'fib':
            val = fib(i)
        else:
            raise ValueError("Неизвестный режим")
        result.append(val)
        i += step
    return result

# Демонстрация всех пунктов по порядку
if __name__ == '__main__':
    print("1. Квадраты чисел")
    print("  my_range('square', 5):", my_range('square', 5))
    print("  my_range('square', 2, 6):", my_range('square', 2, 6))
    print("  my_range('square', 2, 10, 2):", my_range('square', 2, 10, 2))

    print("\n2. Кубы чисел")
    print("  my_range('cube', 4):", my_range('cube', 4))
    print("  my_range('cube', 1, 5):", my_range('cube', 1, 5))
    print("  my_range('cube', 0, 10, 3):", my_range('cube', 0, 10, 3))

    print("\n3. Квадратные корни чисел")
    print("  my_range('sqrt', 5):", my_range('sqrt', 5))
    print("  my_range('sqrt', 1, 7):", my_range('sqrt', 1, 7))
    print("  my_range('sqrt', 0, 10, 2):", my_range('sqrt', 0, 10, 2))

    print("\n4. Логарифмы чисел")
    print("  my_range('log', 1, 6):", my_range('log', 1, 6))
    print("  my_range('log', 2, 8, 2):", my_range('log', 2, 8, 2))

    print("\n5. Числа Фибоначчи по номерам")
    print("  my_range('fib', 7):", my_range('fib', 7))
    print("  my_range('fib', 2, 8):", my_range('fib', 2, 8))
    print("  my_range('fib', 1, 10, 2):", my_range('fib', 1, 10, 2))