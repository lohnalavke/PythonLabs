import os

# --------------------------------------------------------------
# Основная функция для составления пар
# --------------------------------------------------------------
def make_pairs(boys, girls, exclude=None):
        #exclude - список уже составленных пар (каждая пара - кортеж (девочка, мальчик))
    #Возвращает список новых пар.
    
    # Если exclude не задан, используем пустой список
    if exclude is None:
        exclude = []

    # Собираем множества занятых мальчиков и девочек из существующих пар
    busy_boys = set()
    busy_girls = set()
    for girl, boy in exclude:          # предполагаем, что пара хранится как (девочка, мальчик)
        busy_girls.add(girl)
        busy_boys.add(boy)

    #свободные мальчики и девочки
    free_boys = [b for b in boys if b not in busy_boys]
    free_girls = [g for g in girls if g not in busy_girls]

    # Составляем пары, беря первых по порядку
    pairs = []
    for i in range(min(len(free_girls), len(free_boys))):
        pairs.append((free_girls[i], free_boys[i]))
    return pairs

# Вариант 1: два файла (мальчики и девочки) по одному имени в строке
def read_variant1(boys_file, girls_file):
    """Читает имена из двух файлов, возвращает (boys, girls)"""
    with open(boys_file, 'r', encoding='utf-8') as f:
        boys = [line.strip() for line in f if line.strip() != '']
    with open(girls_file, 'r', encoding='utf-8') as f:
        girls = [line.strip() for line in f if line.strip() != '']
    return boys, girls

# Вариант 2: один файл, первая строка – число мальчиков, затем все мальчики, потом девочки
def read_variant2(filename):
    """Читает файл, возвращает (boys, girls)"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip() != '']
    # Первая строка – число мальчиков
    num_boys = int(lines[0])
    boys = lines[1:1+num_boys]
    girls = lines[1+num_boys:]
    return boys, girls

# Вариант 3: один файл, первая строка – число девочек, сначала мальчики, потом девочки
def read_variant3(filename):
    """Читает файл, возвращает (boys, girls)"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip() != '']
    num_girls = int(lines[0])
    # Всего строк = 1 (число) + мальчики + девочки
    total = len(lines)
    num_boys = total - 1 - num_girls
    boys = lines[1:1+num_boys]
    girls = lines[1+num_boys:]
    return boys, girls

# Вариант 4: один файл, два столбца через пробел: имя и буква (м/ж)
def read_variant4(filename):
    """Читает файл, возвращает (boys, girls)"""
    boys = []
    girls = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                continue  # пропускаем некорректные строки
            name, gender = parts
            if gender == 'м':
                boys.append(name)
            elif gender == 'ж':
                girls.append(name)
    return boys, girls

# Вариант 5: один файл, первая строка – заголовок "мальчики девочки" (порядок неизвестен),
# затем имена в два столбца, один может быть длиннее (пустые места обозначены пробелом)
def read_variant5(filename):
    """Читает файл, возвращает (boys, girls)"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Убираем пустые строки в конце, но сохраняем пробелы в начале
    lines = [line.rstrip('\n') for line in lines if line.strip() != '' or line.startswith(' ')]
    if not lines:
        return [], []

    # Первая строка – заголовок
    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Неверный заголовок")
    col1_name, col2_name = header[0], header[1]

    # Определяем, какой столбец мальчики, какой девочки
    if col1_name == 'мальчики' and col2_name == 'девочки':
        boys_col = 1
        girls_col = 2
    elif col1_name == 'девочки' and col2_name == 'мальчики':
        boys_col = 2
        girls_col = 1
    else:
        raise ValueError("Заголовок должен содержать 'мальчики' и 'девочки'")

    # Собираем имена из столбцов
    col1 = []  # первый столбец
    col2 = []  # второй столбец

    for line in lines[1:]:
        # Если строка начинается с пробела – значит заполнен только второй столбец
        if line.startswith(' '):
            # убираем ведущий пробел и добавляем во второй столбец
            name = line.strip()
            if name:
                col2.append(name)
        else:
            # иначе пробуем разделить по пробелу
            parts = line.split()
            if len(parts) == 1:
                # только первый столбец
                col1.append(parts[0])
            elif len(parts) == 2:
                # оба столбца
                col1.append(parts[0])
                col2.append(parts[1])
            # если больше двух – игнорируем (маловероятно)

    # Теперь распределяем по полу
    if boys_col == 1:
        boys = col1
        girls = col2
    else:
        boys = col2
        girls = col1

    return boys, girls


# --------------------------------------------------------------
# Демонстрация работы на разных примерах для каждого варианта
# --------------------------------------------------------------
def demo_variant1():
    print("=== Вариант 1: два файла ===")
    # Создадим тестовые файлы
    with open('boys1.txt', 'w', encoding='utf-8') as f:
        f.write("Антон\nБорис\n")
    with open('girls1.txt', 'w', encoding='utf-8') as f:
        f.write("Аня\nКатя\nДаша\n")

    boys, girls = read_variant1('boys1.txt', 'girls1.txt')
    print("Мальчики:", boys)
    print("Девочки:", girls)

    # Разные случаи
    print("Пары (поровну):", make_pairs(boys, girls))
    # Добавим ещё мальчика
    boys.append("Виктор")
    print("Пары (мальчиков больше):", make_pairs(boys, girls))
    # Удалим одного мальчика, чтобы девочек стало больше
    boys.pop()
    boys.pop()
    print("Пары (девочек больше):", make_pairs(boys, girls))
    # Один мальчик
    boys = ["Иван"]
    girls = ["Маша", "Оля"]
    print("Один мальчик:", make_pairs(boys, girls))
    # Нет девочек
    boys = ["Петя", "Коля"]
    girls = []
    print("Нет девочек:", make_pairs(boys, girls))
    print()

def demo_variant2():
    print("=== Вариант 2: один файл, число мальчиков в начале ===")
    # Создадим файл: 2 мальчика, затем девочки
    with open('data2.txt', 'w', encoding='utf-8') as f:
        f.write("2\nАнтон\nБорис\nАня\nКатя\n")
    boys, girls = read_variant2('data2.txt')
    print("Мальчики:", boys)
    print("Девочки:", girls)
    print("Пары:", make_pairs(boys, girls))
    print()

def demo_variant3():
    print("=== Вариант 3: один файл, число девочек в начале ===")
    # Создадим файл: 2 девочки, сначала мальчики потом девочки
    with open('data3.txt', 'w', encoding='utf-8') as f:
        f.write("2\nАнтон\nБорис\nАня\nКатя\n")
    boys, girls = read_variant3('data3.txt')
    print("Мальчики:", boys)
    print("Девочки:", girls)
    print("Пары:", make_pairs(boys, girls))
    print()

def demo_variant4():
    print("=== Вариант 4: два столбца с буквой ===")
    with open('data4.txt', 'w', encoding='utf-8') as f:
        f.write("Антон м\nАня ж\nБорис м\nКатя ж\n")
    boys, girls = read_variant4('data4.txt')
    print("Мальчики:", boys)
    print("Девочки:", girls)
    print("Пары:", make_pairs(boys, girls))
    print()

def demo_variant5():
    print("=== Вариант 5: два столбца с заголовком, возможны пропуски ===")
    # Пример: первый столбец мальчики (длиннее), второй девочки
    with open('data5.txt', 'w', encoding='utf-8') as f:
        f.write("мальчики девочки\n")
        f.write("Антон Аня\n")
        f.write("Борис Катя\n")
        f.write("Виктор\n")          # только мальчик
        f.write("Григорий\n")         # только мальчик
    boys, girls = read_variant5('data5.txt')
    print("Мальчики:", boys)
    print("Девочки:", girls)
    print("Пары:", make_pairs(boys, girls))

    # Пример: второй столбец девочки длиннее
    with open('data5b.txt', 'w', encoding='utf-8') as f:
        f.write("девочки мальчики\n")
        f.write("Аня Антон\n")
        f.write("Катя Борис\n")
        f.write(" Даша\n")           # пробел перед именем – только девочка
        f.write(" Лена\n")           # только девочка
    boys, girls = read_variant5('data5b.txt')
    print("\nДругой порядок столбцов:")
    print("Мальчики:", boys)
    print("Девочки:", girls)
    print("Пары:", make_pairs(boys, girls))
    print()

# --------------------------------------------------------------
# Демонстрация работы с параметром exclude
# --------------------------------------------------------------
def demo_exclude():
    print("=== Демонстрация работы exclude ===")
    boys = ["Антон", "Борис", "Виктор"]
    girls = ["Аня", "Катя", "Даша"]

    # 1. Без exclude
    pairs1 = make_pairs(boys, girls)
    print("Без exclude:", pairs1)

    # 2. С одним позиционным параметром (исключаем одну пару)
    exclude = [("Аня", "Антон")]
    pairs2 = make_pairs(boys, girls, exclude)
    print("С exclude (позиционно):", pairs2)

    # 3. Передаём exclude по имени
    pairs3 = make_pairs(boys, girls, exclude=exclude)
    print("С exclude по имени:", pairs3)

    # 4. Все аргументы по имени в произвольном порядке
    pairs4 = make_pairs(girls=girls, boys=boys, exclude=exclude)
    print("Все по имени:", pairs4)
    print()


# --------------------------------------------------------------
# Запуск всех демонстраций
# --------------------------------------------------------------
if __name__ == "__main__":
    demo_variant1()
    demo_variant2()
    demo_variant3()
    demo_variant4()
    demo_variant5()
    demo_exclude()