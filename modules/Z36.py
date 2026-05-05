import math
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
from Z35 import bisection, newton

# Параметры точности
powers = list(range(2, 23))          # степени двойки от 2 до 22
epsilons = [2.0 ** -p for p in powers]

a, b = 0.0, math.pi                 # отрезок поиска

# Уравнения (обычные функции) 
def eq1(x):
    return math.sin(x - math.pi/6) - 0.5

def eq2(x):
    return math.cos(x) - 0.5

def eq3(x):
    return math.tan(x) - 1.0

def eq4(x):
    return math.atan(x) - math.pi/3

def eq5(x):
    return (x + 4) * (x - 1) * (x - 20) * (x + 33)

equations = [
    (r"$\sin(x-\pi/6)-0.5=0$", eq1),
    (r"$\cos(x)-0.5=0$", eq2),
    (r"$\tan(x)=1$", eq3),
    (r"$\arctan(x)=\pi/3$", eq4),
    (r"$(x+4)(x-1)(x-20)(x+33)=0$", eq5)
]

for name, f in equations:
    n_bisect = []
    n_newton = []
    valid_powers = []

    for i, eps in enumerate(epsilons):
        p = powers[i]
        nb = None
        nn = None

        # Бисекция возможна только если функция меняет знак
        if f(a) * f(b) < 0:
            try:
                _, nb = bisection(a, b, eps, f)
            except Exception:
                pass

        # Метод Ньютона пробуем всегда
        try:
            _, nn = newton(a, b, eps, f)
        except Exception:
            pass

        # Включаем точку только если оба метода дали результат
        if nb is not None and nn is not None:
            n_bisect.append(nb)
            n_newton.append(nn)
            valid_powers.append(p)

    # Построение графика
    plt.figure(figsize=(8, 5))
    plt.plot(valid_powers, n_bisect, 'o-', color='black', label='Бисекция')
    plt.plot(valid_powers, n_newton, 's-', color='gray', label='Ньютон')
    plt.xlabel('k  ($\\varepsilon = 2^{-k}$)')
    plt.ylabel('Число шагов n')
    plt.title(name)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

print("Все графики построены.")