import os
import matplotlib.pyplot as

folder = "Распределения"
if not os.path.exists(folder):
    print(f"Папка '{folder}' не найдена. Сначала запустите первую программу.")
    
os.chdir(folder)
files = os.listdir(".")

txt_files = [f for f in files if f.endswith(".txt")]

if not txt_files:
    print("В папке нет текстовых файлов.")
    exit()

# Для каждого текстового файла строим гистограмму
for filename in txt_files:
    # Читаем числа из файла
    with open(filename, "r", encoding="utf-8") as f:
        # Преобразуем каждую строку в число, пропуская пустые строки
        data = []
        for line in f:
            line = line.strip()
            if line:
                try:
                    data.append(float(line))
                except ValueError:
                    print(f"Предупреждение: в файле {filename} некорректная строка: {line}")

    if not data:
        print(f"Файл {filename} не содержит чисел, пропускаем.")
        continue

    # Строим гистограмму
    plt.figure(figsize=(6, 4))
    plt.hist(data, bins=30, edgecolor='black', alpha=0.7, color='skyblue')
    plt.title(f"Гистограмма распределения\n{filename}")
    plt.xlabel("Значение")
    plt.ylabel("Частота")
    plt.grid(True, linestyle='--', alpha=0.5)

    # Формируем имя для сохранения (меняем расширение на .png)
    base = os.path.splitext(filename)[0]
    out_image = base + ".png"
    plt.savefig(out_image, dpi=150)
    plt.close() # закрываем фигуру, чтобы не занимать память
    print(f"Гистограмма для {filename} сохранена как {out_image}")

print("Готово.")
