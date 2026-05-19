print("Пункт номер", (5-1)%10+1)

#логическое выражение 5
x = int(input())
y = int(input())
if x * y != 0 or y > x:
    print(True)
else:
    print(False)

#xyz 5 пункт
print("=" * 20)
print("X Y Z F")
for X in (0, 1):
    for Y in (0, 1):
        for Z in (0, 1):
            f = not (X and not Y or Z) and Y
            print(X, Y, Z, f)

#пункт 5 логическое выражение
print("=" * 20)
x = int(input())
y = int(input())
if (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
    print(True)
else:
    print(False)