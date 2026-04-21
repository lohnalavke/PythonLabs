import os
import numpy as np

# Количество генерируемых значений
N = 1000

folder = 'Распределения'
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f'Папка "{folder}" создана.')
else:
    print(f'Папка "{folder}" уже существует.')

os.chdir(folder)

# 2. Равномерное распределение на отрезке [0, 10)
uniform_data = np.random.uniform(0, 10, N)
with open('uniform.txt', 'w') as f:
    for value in uniform_data:
        f.write(f'{value}\n')
print('uniform.txt записан.')

# 3. Нормальное распределение с параметрами mu=0, sigma=1
normal_data = np.random.normal(0, 1, N)
with open('normal.txt', 'w') as f:
    for value in normal_data:
        f.write(f'{value}\n')
print('normal.txt записан.')

# 4. Распределение хи-квадрат с 5 степенями свободы
chisquare_data = np.random.chisquare(5, N)
with open('chisquare_5.txt', 'w') as f:
    for value in chisquare_data:
        f.write(f'{value}\n')
print('chisquare_5.txt записан.')

print('Все файлы успешно созданы.')