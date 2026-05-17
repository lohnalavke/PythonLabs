m = (5-1)%5 +1
print(m, m+5, m+10)

print("Пункт 5")
m = int(input('m: '))
n = int(input('n: '))

if m % n == 0:
    print(m // n)
else:
    print('m на n нацело не делится')

print("Пункт 10")
# Задание 5, пункт 10
a = float(input('Введите сторону a: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону c: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Такого треугольника не существует')
else:
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')

    if (a**2 + b**2 == c**2) or (a**2+c**2 == b**2) or (b**2+c**2 == a**2):
        print('Треугольник прямоугольный')

print("Пункт 15")
month = int(input('Введите номер месяца: '))

if month == 12 or month == 1 or month == 2:
    print('Зима')
elif 3 <= month <= 5:
    print('Весна')
elif 6 <= month <= 8:
    print('Лето')
elif 9 <= month <= 11:
    print('Осень')