import numpy as np
import matplotlib.pyplot as plt

a,b,c = 5,-4,1
x_min, x_max = -6,6
num_points = 100
num_realz = 5
noise_mean = 0
noise_std = 3

x = np.linspace(x_min, x_max, num_points)
y_true = a * x**2 + b * x + c

np.random.seed(42)
y_noisy = np.zeros((num_realz, num_points))
for i in range(num_realz):
    noise = np.random.normal(noise_mean, noise_std, size = num_points)
    y_noisy[i, :] = y_true + noise

y_mean = np.mean(y_noisy, axis = 0)
y_std = np.std(y_noisy, axis = 0, ddof = 1)
plt.figure(figsize=(10,6))
plt.errorbar(x, y_mean, yerr = y_std, fmt = 'o-', capsize = 3, label = 'Среднее с планками $\sigma$', color = 'blue', alpha = 0.7)
plt.plot(x, y_true, 'r--', linewidth = 2, label = 'истинная функция(без шума)')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Средние значения и планка погрешностей")
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.legend()
plt.show()

print(f"Среднее значение шума(оценка): {np.mean(noise):.3f}")
print(f"стандартное отклонение шума(оценка) {np.std(noise): .3f}")
