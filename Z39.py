print((5-1)%5+1)

from functools import reduce

lists = [
    [2, 3, 4],
    [5, -1, 2, 3],
    [10],               
    [0, 100, 200],
    [-2, -2, -2, -2]   
]
products = list(map(lambda sublist: reduce(lambda a, b: a * b, sublist, 1), lists))

print("Исходные списки:", lists)
print("Произведения:", products)