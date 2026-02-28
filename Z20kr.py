import math
import os

print("=== №1 ===")
with open('numbers.txt', 'w') as f:
    for i in range(1,101):
        square = i ** 2
        cube = i ** 3
        f.write(f"{i}\t{square}\t{cube}\n")
print("Файл создан")

print("===  №2 ===")
step = math.pi / 24
with open("trig.txt", "w") as f:
    x = 0
    while x <= 2 * math.pi:
        sin_x = math.sin(x)
        cos_x = math.cos(x)
        f.write(f":{x:.06f}\t{sin_x:.6f}\t {cos_x:.6f}\n")
        x += step
print("Файл trig.txt создан")

print("=== №3 ===")
num_stud = int(input("количесво учеников: "))
with open("зачёт.txt", "w") as f:
    for _ in range(num_stud):
        print(f"\nВведите данные ученика: ")
        surname = input("Фамилия: ")
        name = input("Имя: ")
        otch = input("Отчество: ")
        birth = input("Дата рождения(например 01.01.2001): ")
        grade = input("Оценка: ")
        
        f.write(f"{surname}\t{name}\t{otch}\t{birth}\t{grade}\n")
print("Файл зачёт.txt записан")

print("=== Пункт 4 ===")
search_surname = input("Введите фамилию учащегося для поиска оценки: ")

found = False
with open('Зачёт.txt', 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) < 5:
            continue  
        surname = parts[0]
        if surname == search_surname:
            grade = parts[4]  # оценка — пятый столбец
            print(f"Оценка учащегося {surname}: {grade}")
            found = True
            break
if not found:
    print("Учащийся с такой фамилией не найден.")
print()