def shop_stats(data1, data2=None, param='total'):
    #Приводим данные к единому виду: словарь
    purchases = {}

    if isinstance(data1, dict):                    # словарь
        purchases = data1
    elif isinstance(data1, list) and data2 is None:  # список кортежей
        for name, amount in data1:
            purchases.setdefault(name, []).append(amount)
    elif isinstance(data1, list) and isinstance(data2, list):  # два списка
        for name, amount in zip(data1, data2):
            purchases.setdefault(name, []).append(amount)
    else:
        raise ValueError('Неверный формат данных')

    #Вычисляем нужный параметр для каждого покупателя 
    result = {}
    for name, amounts in purchases.items():
        if param == 'count':                 # число покупок
            val = len(amounts)
        elif param == 'average':             # средняя сумма
            val = sum(amounts) / len(amounts)
        elif param == 'max':                 # максимальная сумма
            val = max(amounts)
        elif param == 'min':                 # минимальная сумма
            val = min(amounts)
        elif param == 'total':               # общая сумма
            val = sum(amounts)
        else:
            raise ValueError("Неизвестный параметр")
        result[name] = val

    return result

if __name__ == '__main__':
    names = ['Аня', 'Боря', 'Аня', 'Вера', 'Боря', 'Аня']
    amounts = [120.5, 340.0, 50.0, 100.0, 90.0, 200.0]

    list_of_tuples = list(zip(names, amounts))

    dict_of_lists = {
        'Аня': [120.5, 50.0, 200.0],
        'Боря': [340.0, 90.0],
        'Вера': [100.0]
    }

    print('ПАРАМЕТРЫ:')
    params = ['count', 'average', 'max', 'min', 'total']
    titles = ['Число покупок', 'Средняя сумма', 'Максимальная сумма',
              'Минимальная сумма', 'Общая сумма']

    for param, title in zip(params, titles):
        print(f'\n=== {title} ===')
        # два списка
        res1 = shop_stats(names, amounts, param)
        # список кортежей
        res2 = shop_stats(list_of_tuples, param=param)
        # словарь
        res3 = shop_stats(dict_of_lists, param=param)

        print('  Два списка:', res1)
        print('  Список кортежей:', res2)
        print('  Словарь:', res3)