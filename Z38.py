m = (4%5)+1
print(m, m+5, m+10)

import math
import matplotlib.pyplot as plt

# Общие настройки графиков
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans']
plt.rcParams['font.size'] = 12

# № 5 
dt = 0.1
# Создаём список t с помощью map
t5 = list(map(lambda i: 1.0 + i * dt, range(91)))
# Вычисляем значения функции
y5 = list(map(lambda t: (1.0 / t) * math.cos(2 * math.pi * t), t5))

plt.figure(figsize=(8, 5))
plt.plot(t5, y5, color='black')
plt.title(r'$f(t) = \frac{1}{t} \cos(2\pi t)$')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# №10
dx = 0.1
# Генерируем x от -4 до 4
x10 = list(map(lambda i: -4.0 + i * dx, range(81)))
# Исключаем ноль
x10_filtered = list(filter(lambda x: x != 0.0, x10))
# Вычисляем логарифм
y10 = list(map(lambda x: math.log2(abs(x)), x10_filtered))

plt.figure(figsize=(8, 5))
plt.plot(x10_filtered, y10, color='black')
plt.title(r'$f(x) = \log_2(|x|)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# №15
dx = 0.1
x15 = list(map(lambda i: 1.0 + i * dx, range(311)))  # (32-1)/0.1 = 310 шагов → 311 точек
y15 = list(map(math.sqrt, x15))

plt.figure(figsize=(8, 5))
plt.plot(x15, y15, color='black')
plt.title(r'$f(x) = \sqrt{x}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()