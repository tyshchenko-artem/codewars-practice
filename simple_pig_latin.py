def pig_latin(text: str):
    """Функция принимает на вход строку и превращает ее в строку на поросячьей латыне"""
    create_list = text.split()
    one_more_list = []
    for el in create_list:
        if el != '!' and el != '?':
            one_more_list.append(el[1:] + el[0] + 'ay')
        if el == '!':
            one_more_list.append(el)
        if el == '?':
            one_more_list.append(el)
    solution = ' '.join(one_more_list)
    return solution


# тесты

print(pig_latin('Pig latin is cool'))
print(pig_latin('This is my string'))
print(pig_latin('Hello world !'))
print(pig_latin('Quis custodiet ipsos custodes ?'))
