def min_max(lst):
    """Функция принимает список целых чисел и возвращает наибольшее и наименьшее целое число. Функция всегда
    возвращает два числа, если в исходном списке одно число, функция возвращает исходное число и его копию."""
    if len(lst) > 1:
        make_sort = sorted(lst)
        final_list = []
        final_list.append(make_sort[0])
        final_list.append(make_sort[-1])
        return final_list
    if len(lst) == 1:
        lst.append(lst[0])
        return lst


print(min_max([1, 2, 3, 4, 5]))
print(min_max([2334454, 5]))
print(min_max([1]))
