import math

def print_sh(x, eps=10**(-10)):
    x = float(x)               # преобразую аргумент к вещественному типу
    term = x                    # первое слагаемое (n=0)
    total = 0.0                  # начальное значение суммы
    n = 0                        # счётчик членов (номер текущего слагаемого)

    while True:
        # Сохраняем сумму до добавления текущего члена
        prev_total = total
        total += term
        if abs(total - prev_total) < eps:
            break

        n += 1
        term *= x * x / ((2 * n) * (2 * n + 1))

    print(f"sh({x}) = {total} (вычислено)")
    print(f"Точное значение (math.sinh): {math.sinh(x)}")
    print(f"Разница: {abs(total - math.sinh(x))}\n")

if __name__ == "__main__":
    print_sh(1.0)
    print_sh(2.0, 1e-8)
    print_sh(0.5, eps=1e-12)