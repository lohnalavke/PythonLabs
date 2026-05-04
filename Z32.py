# Задание 32, вариант 2
def make_pairs(filename, done_pairs=None):
    # читаем все строки, убираем пробелы и пустые строки
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip() != '']

    if not lines:
        return []

    # первая строка — число мальчиков
    n_boys = int(lines[0])
    names = lines[1:]

    # мальчики — первые n_boys имён, девочки — остальные
    all_boys = names[:n_boys]
    all_girls = names[n_boys:]

    # если заданы уже составленные пары, удаляем их участников
    if done_pairs is None:
        done_pairs = []

    # собираем занятых мальчиков и девочек
    busy_boys = set()
    busy_girls = set()
    for boy, girl in done_pairs:
        busy_boys.add(boy)
        busy_girls.add(girl)

    # оставляем только свободных
    free_boys = [b for b in all_boys if b not in busy_boys]
    free_girls = [g for g in all_girls if g not in busy_girls]

    # составляем пары подряд
    pairs = []
    for b, g in zip(free_boys, free_girls):
        pairs.append((b, g))

    return pairs


if __name__ == '__main__':
    with open('dancers.txt', 'w', encoding='utf-8') as f:
        f.write('3\n')          # мальчиков
        f.write('Петя\n')
        f.write('Вася\n')
        f.write('Коля\n')
        f.write('Маша\n')
        f.write('Даша\n')
        f.write('Оля\n')
        f.write('Света\n')     # девочек больше

    print('1. Обычный вызов:')
    new = make_pairs('dancers.txt')
    print('Новые пары:', new)

    print('\n2. Два позиционных аргумента (уже есть одна пара Петя-Маша):')
    old_pairs = [('Петя', 'Маша')]
    new2 = make_pairs('dancers.txt', old_pairs)
    print('Новые пары:', new2)

    print('\n3. Именованный второй аргумент:')
    new3 = make_pairs('dancers.txt', done_pairs=[('Вася', 'Даша')])
    print('Новые пары:', new3)

    print('\n4. Все аргументы по именам (в любом порядке):')
    new4 = make_pairs(done_pairs=[('Коля', 'Оля')], filename='dancers.txt')
    print('Новые пары:', new4)

    # когда мальчиков и девочек поровну
    with open('equal.txt', 'w', encoding='utf-8') as f:
        f.write('2\n')
        f.write('Антон\n')
        f.write('Борис\n')
        f.write('Анна\n')
        f.write('Белла\n')
    print('\nПоровну:', make_pairs('equal.txt'))

    # когда один мальчик
    with open('one_boy.txt', 'w', encoding='utf-8') as f:
        f.write('1\n')
        f.write('Иван\n')
        f.write('Катя\n')
        f.write('Лена\n')
    print('Один мальчик:', make_pairs('one_boy.txt'))

    # когда нет девочек
    with open('no_girls.txt', 'w', encoding='utf-8') as f:
        f.write('2\n')
        f.write('Серёжа\n')
        f.write('Максим\n')
    print('Нет девочек:', make_pairs('no_girls.txt'))

    # когда вообще никого нет
    with open('empty.txt', 'w', encoding='utf-8') as f:
        f.write('0\n')
    print('Пустой файл:', make_pairs('empty.txt'))