def alphabet_position(text: str):
    '''Функция заменяет все английские буквы в строке на позицию этой буквы
    в английском алфавите и возвращает результат в виде строки'''
    list_lower = text.lower()
    create_list_of_letters = []

    ignoring_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', ',', ':', ';', '\'', '"', '>',
                        '<', '=', ')', '(', '-', '_', '+', '#', '!', '?']

    dict_of_letters = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
        'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26
    }

    for letter in list_lower:
        if letter not in ignoring_symbols:
            create_list_of_letters.append(letter)
        else:
            continue

    result_list = []
    for el in create_list_of_letters:
        for letter, num in dict_of_letters.items():
            if el == letter:
                result_list.append(str(num))
    return ' '.join(result_list)


# test
print(alphabet_position("The sunset sets at twelve o' clock."))
