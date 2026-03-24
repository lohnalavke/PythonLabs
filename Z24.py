import numpy as np
import os

matrix_file = "matrix.txt"
b_file = "b.txt"
roots_file = "roots.txt"

if not os.path.exists(matrix_file):
    print(f"Файл {matrix_file} не найден. Создаём матрицу 3x3.")
    example_matrix = np.array([[2, 1, -1],
                               [-3, -1, 2],
                               [-2, 1, 2]])
    with open(matrix_file, 'w', encoding='utf-8') as f:
        for row in example_matrix:
            f.write(' '.join(str(num) for num in row) + '\n')
    print(f"Файл {matrix_file} создан.")

if not os.path.exists(b_file):
    print(f"Файл {b_file} не найден. Создаём пример столбца свободных членов.")
    example_b = np.array([8, -11, -3])
    with open(b_file, 'w', encoding='utf-8') as f:
        for val in example_b:
            f.write(str(val) + '\n')
    print(f"Файл {b_file} создан.")

# Чтение матрицы коэффициентов
matrix = []
with open(matrix_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            row = list(map(float, line.split()))
            matrix.append(row)

# Чтение столбца свободных членов
b = []
with open(b_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            b.append(float(line))

# Преобразование в массивы NumPy
A = np.array(matrix)
b = np.array(b)

# Проверка размерностей
if A.shape[0] != A.shape[1]:
    print("Матрица не квадратная, систему решить нельзя.")
    exit()
if A.shape[0] != b.shape[0]:
    print("Количество уравнений не совпадает с количеством неизвестных.")
    exit()

# Решение системы
try:
    x = np.linalg.solve(A, b)
    print("Решение системы:", x)
except np.linalg.LinAlgError:
    print("Матрица вырождена, система не имеет единственного решения.")
    exit()

# Запись корней в файл
with open(roots_file, 'w', encoding='utf-8') as f:
    for i, val in enumerate(x, start=1):
        f.write(f"x{i} = {val}\n")

print(f"Корни сохранены в файл {roots_file}")