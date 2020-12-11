def sep(string: str):
    '''Функция принимает строку со словами и цифрами и возвращает два списка со словами и цифрами.'''
    sep = string.split()
    list_of_search = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    list_of_transform = []
    list_of_other_elements = []
    list_of_let_1 = []
    list_of_num_1 = []
    list_of_let_2 = []
    list_of_num_2 = []

    for el in sep:
        if el[0] not in list_of_search and el[-1] in list_of_search:
            list_of_transform.append(el)
        else:
            list_of_other_elements.append(el)

    for e in ''.join(list_of_transform[0]):
        if e not in list_of_search:
            list_of_let_1.append(e)
        else:
            list_of_num_1.append(e)

    create_first_part = [''.join(list_of_let_1), ''.join(list_of_num_1)]

    for e in ''.join(list_of_transform[1]):
        if e not in list_of_search:
            list_of_let_2.append(e)
        else:
            list_of_num_2.append(e)

    create_second_part = [''.join(list_of_let_2), ''.join(list_of_num_2)]

    connect_first_part_of_solution = create_first_part + create_second_part

    connect_all = connect_first_part_of_solution + list_of_other_elements

    separate_int = []
    separate_letters_and_words = []

    for el in connect_all:
        try:
            separate_int.append(int(el))
        except ValueError:
            separate_letters_and_words.append(el)

    solution = (separate_int, separate_letters_and_words)

    return solution

# test
print(sep("abc83 cde7 1 b 24"))
