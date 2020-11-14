def abbrev_name(name: str):
    '''Функция получает строку, в которой указаны имя и фамилия человека'''
    create_list = name.split()
    final_list = []
    for el in create_list:
        final_list.append(el[0].capitalize() + '.')
    solution = ''.join(final_list)
    return solution[:-1]

# test
print(abbrev_name('Sam Harris'))
