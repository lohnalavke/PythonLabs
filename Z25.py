# Парабола y = 5x^2 - 4x + 1 на отрезке [-6; 6]
# с нормальным шумом (mu=0, sigma=3)
import numpy as np
import matplotlib.pyplot as plt

#Генерация данных
x = np.arange(-6, 6.1, 0.2)               # отрезок [-6; 6] с шагом 0.2
y_true = 5 * x**2 - 4 * x + 1              # истинная парабола
noise = np.random.normal(0, 3, len(x))     # нормальный шум с sigma=3
z = y_true + noise                          # зашумлённые данные

#Построение матрицы для полинома второй степени
A = np.ones((len(x), 3))   # три столбца: свободный член, x, x^2
A[:, 1] = x
A[:, 2] = x**2

#Аппроксимация методом наименьших квадратов
result = np.linalg.lstsq(A, z, rcond=None)
coeffs = result[0]                         # коэффициенты модели
z_fit = A @ coeffs                         # аппроксимированные значения

#Оценка ошибки (среднеквадратичная ошибка)
mse = result[1][0] / len(x) if len(result[1]) > 0 else np.mean((z - z_fit)**2)
print('Коэффициенты аппроксимации:')
print(f'a0 = {coeffs[0]:.4f}')
print(f'a1 = {coeffs[1]:.4f}')
print(f'a2 = {coeffs[2]:.4f}')
print(f'Среднеквадратичная ошибка = {mse:.4f}')

# Построение графика
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans']  # для кириллицы
plt.figure(figsize=(8, 5))
plt.plot(x, z, 'o', color='gray', markersize=4, alpha=0.7, label='Данные с шумом')
plt.plot(x, z_fit, color='black', linewidth=2, label='Аппроксимация')
plt.title('Аппроксимация параболой (вариант 4)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('task25_var4.png', dpi=150)
plt.show()
