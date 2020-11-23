def stray(arr: list):
    '''Функция возвращает уникальный элемент из списка'''
    make_sort = sorted(arr)
    if make_sort[0] != make_sort[1]:
        return make_sort[0]
    else:
        return make_sort[-1]


print(stray([1, 1, 1, 1, 1, 1, 2]))
