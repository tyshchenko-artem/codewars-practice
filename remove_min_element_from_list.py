def remove_smallest(numbers: list):
    '''Входной параметр функции - список. Функция находит минимальный элемент в списке, удаляет его и возвращает
    список уже без минимального числа. Если в списке есть несколько элементов с одинаковыми значениями, удаляется
    элемент с меньшим индексом.'''
    if len(numbers) == 0:
        return []
    else:
        copy_inp_list = numbers
        sort_list = sorted(copy_inp_list)
        find_the_lowest_num = sort_list[0]
        for el in copy_inp_list:
            if el == find_the_lowest_num:
                copy_inp_list.remove(el)
                return copy_inp_list


# test
print(remove_smallest([5, 3, 2, 1, 4]))  # [5, 3, 2, 4]
print(remove_smallest([2, 2, 1, 2, 1]))  # [2, 2, 2, 1]
print(remove_smallest([]))  # []
