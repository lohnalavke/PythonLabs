print((5-1)%4+1)

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t_start = -10.0
t_end = 10.0
step = 0.05
t = np.arange(t_start, t_end + step, step)

y = 4 * np.sin(np.pi * t + np.pi / 8) -1
frequencies, psd = signal.periodogram(y, fs = 1/step, return_onesided = True)

# График сигнала во времени
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.plot(t, y)
plt.title("Сигнал во временной области")
plt.xlabel('t (c)')
plt.ylabel('y(t)')
plt.grid(True)

#Периодограмма(спектр мощности) в логарифмическом масштабе
plt.subplot(1, 2, 2)
plt.semilogy(frequencies, psd)
plt.title("Периодограмма")
plt.xlabel('Частота (Гц)')
plt.ylabel('Мощность')
plt.grid(True)

plt.tight_layout()
plt.show()

# Частота, на которой мощность максимальна
peak_index = np.argmax(psd)
peak_freq = frequencies[peak_index]
print(f"Частота с максимальной мощностью: {peak_freq:.3f} Гц")
