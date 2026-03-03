import os
from array import array

print("=== Пункт 1: выделение отведения из Rat.wdq ===")

channel = int(input("Введите номер отведения (1–4): "))
if channel < 1 or channel > 4:
    print("Номер должен быть от 1 до 4.")
    exit()

# Имя исходного файла
input_file = "Rat.wdq"

if not os.path.exists(input_file):
    print(f"Файл {input_file} не найден. Для демонстрации создадим тестовый файл.")
    # Создадим тестовый файл с 1000 чисел на канал (всего 4000 чисел)
    # Для простоты заполним числами от 0 до 3999
    test_data = list(range(4000))
    with open(input_file, 'wb') as f:
        # array('h') автоматически упакует числа в 2-байтные знаковые
        arr = array('h', test_data)
        arr.tofile(f)
    print("Тестовый файл создан.")

# Открываем файл и читаем все числа как signed short
with open(input_file, 'rb') as f:
    # Создаем пустой массив типа 'h'
    data = array('h')
    # Читаем все байты из файла и добавляем в массив
    data.fromfile(f, os.path.getsize(input_file) // 2)  # //2 потому что 2 байта на число

# Общее количество чисел
total_numbers = len(data)
print(f"Всего чисел в файле: {total_numbers}")

# Проверяем, что число кратно 4
if total_numbers % 4 != 0:
    print("Предупреждение: количество чисел не кратно 4, возможно файл повреждён.")
    # Но мы всё равно попробуем обработать
    measurements_per_channel = total_numbers // 4
else:
    measurements_per_channel = total_numbers // 4

print(f"Измерений на один канал: {measurements_per_channel}")

# Индекс начала нужного канала (нумерация каналов с 1)
start_index = (channel - 1) * measurements_per_channel
# Берём первые 100 чисел из этого канала (если их меньше 100, берём сколько есть)
end_index = min(start_index + 100, start_index + measurements_per_channel)
channel_data = data[start_index:end_index]

# Формируем имя выходного файла
base = os.path.splitext(input_file)[0]  # "Rat"
output_file = f"{base}{channel}.txt"

# Записываем в текстовый файл
with open(output_file, 'w', encoding='utf-8') as f:
    for value in channel_data:
        f.write(str(value) + '\n')

print(f"Первые {len(channel_data)} значений отведения {channel} сохранены в {output_file}")
print()