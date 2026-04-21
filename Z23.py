import numpy as np

# 1. Создаём матрицу
n = 3  # размер матрицы
A = np.zeros((n, n))
for i in range(n):
    A[i, :i] = -1
    A[i, i+1:] = 1
print('Сгенерированная матрица:')
print(A)

# 2. Сохраняем матрицу в текстовый файл
np.savetxt('Matrix_23.txt', A, fmt='%d')
print("Матрица сохранена в файл 'Matrix_23.txt'")

# 3. Читаем матрицу из файла
M = np.loadtxt('Matrix_23.txt')
print('Матрица, прочитанная из файла:')
print(M)

# 4. Вычисляем определитель
det = np.linalg.det(M)
print(f'Определитель матрицы = {det}')