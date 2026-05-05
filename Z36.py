# Задание 36 – все уравнения (без лямбда-функций)
import math
import sys
import os
import matplotlib as plt

# Подключаем модуль из папки modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
from nonlinear_solvers import bisection, newton

# Точности от 2^-2 до 2^-22
powers = list(range(2, 23))
epsilons = [2.0 ** -p for p in powers]

# Отрезок поиска
a, b = 0.0, math.pi

# ----- Определяем уравнения как обычные функции -----
def eq1(x):
    """sin(x - pi/6) - 0.5 = 0, корень pi/3"""
    return math.sin(x - math.pi/6) - 0.5

def eq2(x):
    """cos(x) - 0.5 = 0, корень pi/3"""
    return math.cos(x) - 0.5

def eq3(x):
    """tan(x) = 1, корень pi/4"""
    return math.tan(x) - 1.0

def eq4(x):
    """arctan(x) = pi/3, корень sqrt(3)"""
    return math.atan(x) - math.pi/3

def eq5(x):
    """(x+4)(x-1)(x-20)(x+33) = 0, корень 1"""
    return (x + 4) * (x - 1) * (x - 20) * (x + 33)

# Список: (название, функция)
equations = [
    ("$\\sin(x-\\pi/6)-0.5=0$", eq1),
    ("$\\cos(x)-0.5=0$", eq2),
    ("$\\tan(x)=1$", eq3),
    ("$\\arctan(x)=\\pi/3$", eq4),
    ("$(x+4)(x-1)(x-20)(x+33)=0$", eq5)
]

# Для каждого уравнения строим график
for name, f in equations:
    n_bisect = []
    n_newton = []
    valid_powers = []   # степени точности, для которых методы сработали

    for i, eps in enumerate(epsilons):
        p = powers[i]
        # --- Метод бисекции ---
        nb = None
        if f(a) * f(b) < 0:          # проверка знаков на концах
            try:
                _, nb = bisection(a, b, eps, f)
            except Exception:
                nb = None
        # --- Метод Ньютона ---
        nn = None
        try:
            _, nn = newton(a, b, eps, f)
        except Exception:
            nn = None

        # Добавляем точку в график, только если оба метода дали результат
        # или хотя бы один – чтобы графики были сравнимы,
        # будем добавлять только когда есть оба значения (как в примерах книги)
        if nb is not None and nn is not None:
            n_bisect.append(nb)
            n_newton.append(nn)
            valid_powers.append(p)

    # Строим график
    plt.figure(figsize=(8, 5))
    plt.plot(valid_powers, n_bisect, 'o-', color='black', label='Метод бисекции')
    plt.plot(valid_powers, n_newton, 's-', color='gray', label='Метод Ньютона')
    plt.xlabel('Показатель степени точности $k$  ($\\varepsilon = 2^{-k}$)')
    plt.ylabel('Число шагов $n$')
    plt.title(f'Уравнение: {name}')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

print("Все графики построены.")