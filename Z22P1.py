import os
import random
import math

folder = "Распределения"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"{folder} создана")
else:
    print(f"{folder} уже существует")

n = 1000

uniform_data = [random.random() for _ in range(n)]
normal_data = [random.gauss(0,1) for _ in range(n)]

chi2_data = []
for _ in range(n):
    normals = [random.gauss(0,1) for _ in range(5)]

    chi2 = sum(x*x for x in normals)
    chi2_data.append(chi2)

with open(os.path.join(folder,"uniform.txt"), "w") as f:
    for val in uniform_data:
        f.write(f"{val}\n")

with open(os.path.join(folder, "normal.txt"), "w") as f:
    for val in normal_data:
        f.write(f"{val}\n")

with open(os.path.join(folder, "chisquare.txt"), "w") as f:
    for val in chi2_data:
        f.write(f"{val}\n")
print("Файлы созданы")
