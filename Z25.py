import numpy as np
import matplotlib.pyplot as plt

print( (5-1)%8, "пункт")

a_true = 5.0
b_true = -4.0
c_true = 1.0
x_min = -6
x_max = 6
num_points = 200
noise_mean = 0
noise_std = 3

x = np.linspace(x_min, x_max, num_points)
y_true = a_true * x**2 + b_true * x + c_true

np.random.seed(42)
noise = np.random.normal(noise_mean, noise_std, size = num_points)
y_noisy = y_true + noise

coeffs = np.polyfit(x, y_noisy, 2)
a_fit, b_fit, c_fit = coeffs
print(f"Истинные коэффициенты: a={a_true}, b = {b_true}, c = {c_true}")
print(f"Полученные коэффициенты: a = {a_fit: .3f}, b = {b_fit: .3f}, c = {c_fit: .3f}")

y_fit = np.polyval(coeffs, x)

mse = np.mean((y_noisy - y_fit)**2)
print(f"Среднеквадратичная ошибка (MSE) аппроксимации: {mse: .3f}")

error_vs_true = np.mean((y_true - y_fit)**2)
print(f"Среднеквадратичная ошибка относительно истиной функции: {error_vs_true: .3f}")

plt.figure(figsize=(10,6))
plt.plot(x, y_true, 'g-', label = 'Истиная функция', linewidth = 2)
plt.plot(x, y_fit, 'r--', label = 'Аппроксимация полином 2-й степени', linewidth = 2)
plt.scatter(x, y_noisy, s =10, color = 'blue', alpha = 0.5, label = 'Зашумленные данные')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
