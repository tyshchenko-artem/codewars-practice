def rot13(message: str):
    "Функция принимает строку и возвращает эту строку закодированную с помощью кодировки rot13"
    dict_of_changing = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
                        'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
                        'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
                        'y': 'l', 'z': 'm',
                        'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U',
                        'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C',
                        'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K',
                        'Y': 'L', 'Z': 'M', '+': '+', '-': '-', '!': '!', '?': '?', ':': ':', ';': ';',
                        ',': ',', '$': '$', '(': '(', ')': ')', '0': '0', '1': '1', '2': '2', '3': '3',
                        '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', ' ': ' ', '.': '.'}
    final_list = []
    create_list_of_letters = []
    for element in message:
        create_list_of_letters.append(element)
    for let in create_list_of_letters:
        for item in dict_of_changing.items():
            if let == item[0]:
                final_list.append(item[1])
    solution = ''.join(final_list)
    return solution


# test
print(rot13('test'))
print(rot13('Tes1t'))
print(rot13('Test?'))
print(rot13('Nibvq fhpprff ng nyy pbfgf!'))