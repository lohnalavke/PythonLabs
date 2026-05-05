#Зависимость погрешности от числа шагов
import math
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
from Z35 import bisection, newton

# Параметры точности (от 2^-2 до 2^-22)
powers = list(range(2, 23))
epsilons = [2.0 ** -p for p in powers]

# Отрезок поиска
a, b = 0.0, math.pi

#Уравнения и их истинные корни 
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
    (r"$\sin(x-\pi/6)-0.5=0$", eq1, math.pi/3),
    (r"$\cos(x)-0.5=0$",      eq2, math.pi/3),
    (r"$\tan(x)=1$",           eq3, math.pi/4),
    (r"$\arctan(x)=\pi/3$",    eq4, math.sqrt(3)),
    (r"$(x+4)(x-1)(x-20)(x+33)=0$", eq5, 1.0)
]

for name, f, xtrue in equations:
    # Списки для хранения результатов
    n_bisect = []
    err_bisect = []
    n_newton = []
    err_newton = []

    for eps in epsilons:
        # Метод бисекции (только если знаки разные)
        if f(a) * f(b) < 0:
            try:
                root_b, nb = bisection(a, b, eps, f)
                err = abs(root_b - xtrue)
                n_bisect.append(nb)
                err_bisect.append(err)
            except Exception:
                pass

        # Метод Ньютона 
        try:
            root_n, nn = newton(a, b, eps, f)
            err = abs(root_n - xtrue)
            n_newton.append(nn)
            err_newton.append(err)
        except Exception:
            pass

    # Сортируем по числу шагов, чтобы линии шли по порядку
    # (для бисекции n обычно растёт с уменьшением eps)
    bisect_points = sorted(zip(n_bisect, err_bisect))
    newton_points = sorted(zip(n_newton, err_newton))

    # Разделяем обратно на два списка
    if bisect_points:
        n_b, e_b = zip(*bisect_points)
    else:
        n_b, e_b = [], []
    if newton_points:
        n_n, e_n = zip(*newton_points)
    else:
        n_n, e_n = [], []

    # Построение графика
    plt.figure(figsize=(8, 5))
    plt.plot(n_b, e_b, 'o-', color='black', label='Метод бисекции')
    plt.plot(n_n, e_n, 's-', color='gray', label='Метод Ньютона')
    plt.xlabel('Число шагов $n$')
    plt.ylabel('$|x - x_{\\rm true}|$')
    plt.title(name)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    # Логарифмический масштаб по Y помогает разглядеть малые ошибки
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

print("Все графики построены.")