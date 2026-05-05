import math
import matplotlib.pyplot as plt

def derivative(x, func, dx=1e-10):
    #Приближённое вычисление производной (центральная разность)
    return (func(x + dx) - func(x - dx)) / (2 * dx)

def bisection(a, b, eps, func):
    #Метод деления отрезка пополам. Возвращает корень и число шагов
    n = 0
    while (b - a) > eps:
        n += 1
        c = (a + b) / 2.0
        f_a = func(a)
        f_c = func(c)
        if f_a * f_c > 0:
            a = c
        else:
            b = c
    return (a + b) / 2.0, n

def newton(a, b, eps, func):
    #Метод Ньютона. Возвращает корень и число шагов
    x0 = (a + b) / 2.0
    delta = func(x0) / derivative(x0, func)
    n = 0
    while abs(delta) > eps:
        n += 1
        delta = func(x0) / derivative(x0, func)
        x0 = x0 - delta
    return x0, n

# Тестирование точности при запуске модуля как программы
if __name__ == '__main__':
    def test_func(x):
        return x**2 - 4   # корень на [0, 10] равен 2

    powers = range(2, 23)       # от 2^-2 до 2^-22
    eps_vals = [2.0 ** -p for p in powers]
    n_bisect = []
    n_newton = []

    for eps in eps_vals:
        _, nb = bisection(0.0, 10.0, eps, test_func)
        _, nn = newton(0.0, 10.0, eps, test_func)
        n_bisect.append(nb)
        n_newton.append(nn)

    plt.plot(powers, n_bisect, 'o-', color='black', label='Метод бисекции')
    plt.plot(powers, n_newton, 's-', color='gray', label='Метод Ньютона')
    plt.xlabel('Показатель степени k  ($\\varepsilon = 2^{-k}$)')
    plt.ylabel('Число шагов n')
    plt.title('Зависимость числа шагов от точности (x² – 4 = 0)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()