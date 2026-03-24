import numpy as np
import os

# Имя файла с матрицей
filename = "matrix.txt"

if not os.path.exists(filename):
    print(f"Файл {filename} не найден. Создаём матрицу 3x3.")
    example_matrix = np.array([[1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]])
    with open(filename, 'w', encoding='utf-8') as f:
        for row in example_matrix:
            line = ' '.join(str(num) for num in row)
            f.write(line + '\n')
    print(f"Файл {filename} создан с матрицей:\n{example_matrix}")

# Чтение матрицы из файла
matrix = []
with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:  # если строка не пустая
            # Разбиваем строку по пробелам и преобразуем в числа
            row = list(map(float, line.split()))
            matrix.append(row)

matrix_np = np.array(matrix)

if matrix_np.shape[0] != matrix_np.shape[1]:
    print("Матрица не квадратная, определитель не существует.")
else:
    det = np.linalg.det(matrix_np)
    print(f"Матрица:\n{matrix_np}")
    print(f"Определитель матрицы: {det}")