print((5-1)%15+1)

import numpy as np
import matplotlib.pyplot as plt

N = 10000
a = np.random.uniform(1, 10, N)
x = np.random.uniform(-a, 2*a)

plt.figure(figsize=(10,6))
plt.hist(x, bins=50, density=True, edgecolor='black', alpha=0.7,  color='skyblue')
plt.title("Гистограмма случайного процесса: равномерный шум с параметрами (-a, 2a)\n где а ~ Uniform[1, 10]")
plt.xlabel('x')
plt.ylabel('плотность вероятности')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

print(f"Среднее выборки: {np.mean(x): .4f}")
print(f"Стандартное отклонение от выборки: {np.std(x):.4f}")
print(f"Минимум {np.min(x): .4f}, Максимум: {np.max(x): .4f}")
