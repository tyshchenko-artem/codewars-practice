def bool_to_word(boolean: bool):
    '''Функция преобразует булевые значения в строки. True преобразуется в "Yes" False - "No"'''
    if boolean == True:
        return 'Yes'
    elif boolean == False:
        return 'No'


# test
print(bool_to_word(True))
print(bool_to_word(False))
