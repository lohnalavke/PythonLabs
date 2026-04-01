print((5-1)%8+1)
import random

arr = [0] * 4 + [1] * 4 + [2] * 4
print("Исходный массив")
print(arr)
print()

random.shuffle(arr)
print("Перемешанный массив")
print(arr)
