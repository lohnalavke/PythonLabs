import os
import matplotlib.pyplot as plt

folder = 'Распределения'
if not os.path.exists(folder):
    print(f'Ошибка: папка "{folder}" не найдена.')
    exit()

os.chdir(folder)

# Настройка шрифта для поддержки кириллицы
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans']

# Обрабатываем все файлы с расширением .txt
for filename in os.listdir('.'):
    if not filename.endswith('.txt'):
        continue

    # Читаем данные из файла
    data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # пропускаем пустые строки
                data.append(float(line))

    # Определяем имя для сохранения графика (без расширения .txt)
    base_name = os.path.splitext(filename)[0]
    output_file = base_name + '.png'

    # Строим гистограмму
    plt.figure()
    plt.title(f'Распределение: {base_name}')
    plt.xlabel('Значение')
    plt.ylabel('Плотность вероятности')
    plt.hist(data, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig(output_file, dpi=150)
    plt.close()  # закрываем фигуру, чтобы не накладывались

    print(f'График сохранён: {output_file}')

print('Все гистограммы построены.')