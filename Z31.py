print((4-1)%10+1)

import math

def cosh_series(x, eps=1e-10):
    result = 1.0
    # первый член ряда (n=1: x^2/2!)
    term = x * x / 2.0
    n = 1
    while abs(term) > eps:
        result += term
        n += 1
        # переход к следующему члену (n -> n+1)
        term = term * x * x / ((2*n - 1) * (2*n))
    return result

if __name__ == '__main__':
    x = float(input('Введите x: '))

    # 1. Вызов с одним позиционным параметром
    print('1. Результат с точностью по умолчанию:', cosh_series(x))

    # 2. Вызов с двумя позиционными параметрами
    print('2. Результат с точностью 1e-6:', cosh_series(x, 1e-6))

    # 3. Вызов с именованным параметром
    print('3. Результат при явной передаче точности:',
          cosh_series(x, eps=1e-12))

    # Проверка через math.cosh
    print('math.cosh(x) =', math.cosh(x))

    # Превращение функции в процедуру (печатает результат вместо return)
    def cosh_procedure(x, eps=1e-10):
        #Процедурный вариант: только печатает, ничего не возвращает
        res = cosh_series(x, eps)
        print(f'Процедура: ch({x}) = {res}')

    print('\nВызов процедуры:')
    cosh_procedure(x)