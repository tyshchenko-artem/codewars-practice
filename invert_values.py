def invert(lst: list):
    '''Функция принимает принимает список чисел. И возвращает список чисел,
    в котором все числа заменены на противоположные.'''
    if len(lst) == 0:
        return []
    new_lst = []
    for el in lst:
        if el > 0:
            el = el - el * 2
            new_lst.append(el)
        else:
            el = abs(el)
            new_lst.append(el)

    return new_lst

# test
print(invert([1, -2, 3, -4, 5]))
print(invert([]))
