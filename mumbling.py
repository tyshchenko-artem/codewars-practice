def accum(s):
    """Функция принимает на вход строку и возвращает разделенную дефисами строку,
    в которой каждый элемент умножается на свой индекс"""
    index = 0
    new_list = []
    for el in s:
        index += 1
        new_list.append(el * index)
    final_list = []
    for old_string in new_list:
        final_list.append(old_string.capitalize())
    solution = '-'.join(final_list)
    return solution


print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))
