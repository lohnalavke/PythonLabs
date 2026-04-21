import numpy as np

#Создаём матрицу коэффициентов A и вектор свободных членов b
#система 3x3 с ненулевым определителем
A = np.array([
    [2, 3, 1],
    [-1, 5, -2],
    [3, -1, 4]
])
b = np.array([-7, 16, 10])

print('Матрица коэффициентов A:')
print(A)
print('Вектор свободных членов b:')
print(b)

# 2. Сохраняем A и b в текстовые файлы
np.savetxt('Matrix_A.txt', A, fmt='%d')
np.savetxt('Vector_b.txt', b, fmt='%d')
print("Файлы 'Matrix_A.txt' и 'Vector_b.txt' созданы.")

# 3. Читаем данные из файлов
M = np.loadtxt('Matrix_A.txt')
V = np.loadtxt('Vector_b.txt')
print('Прочитанные данные:')
print('M =\n', M)
print('V =', V)

# 4. Решаем систему линейных уравнений M * x = V
x = np.linalg.solve(M, V)
print('Решение системы (корни):')
print(x)

# 5. Записываем корни в новый текстовый файл
np.savetxt('Roots.txt', x, fmt='%.6f')
print("Корни записаны в файл 'Roots.txt'.")