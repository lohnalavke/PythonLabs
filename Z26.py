# Парабола y = 5x^2 - 4x + 1 на отрезке [-6; 6]
# 5 реализаций нормального шума (mu=0, sigma=3)

import numpy as np
import matplotlib.pyplot as plt

#Генерация данных
x = np.arange(-6, 6.1, 0.2)                # отрезок [-6; 6] с шагом 0.2
y_true = 5 * x**2 - 4 * x + 1               # истинная парабола

#5 зашумлённых рядов
n_realizations = 5
data = np.zeros((len(x), n_realizations))
for i in range(n_realizations):
    noise = np.random.normal(0, 3, len(x))   # нормальный шум
    data[:, i] = y_true + noise

# Вычисляем средние и стандартные отклонения по столбцам (axis=1)
y_mean = data.mean(axis=1)
y_std = data.std(axis=1)

# Построение графика с планками погрешностей
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans']
plt.figure(figsize=(8, 5))
plt.errorbar(x, y_mean, yerr=y_std, fmt='o', color='black',
             ecolor='gray', capsize=3, markersize=4, label='Среднее ± σ')
plt.plot(x, y_true, color='red', linewidth=1.5, alpha=0.7, label='Истинная парабола')
plt.title('Среднее по 5 реализациям с планками погрешностей (вариант 4)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('task26_var4_errorbar.png', dpi=150)
plt.show()