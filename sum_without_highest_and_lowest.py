def sum_array(arr: list):
    '''Функция находит сумму элементов в списке без самого наибольшего и наименьшего числа.
    Если список пустой, None или там всего один элемент возврашает 0'''
    if arr is None:
        return 0
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        sort_arr = sorted(arr)
        remove_first = sort_arr[1:]
        remove_last = remove_first[:-1]
        return sum(remove_last)


# test
print(sum_array([None]))
print(sum_array([1]))
print(sum_array([6, 2, 3, 4, 5]))
print(sum_array([1, 34, 123, 4143]))
print(sum_array([3, 5]))
print(sum_array([-3, -5]))
