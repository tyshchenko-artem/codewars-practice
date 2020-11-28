def reversewords(s: str):
    '''Функция принимает на вход строку и возвращает строку, в которой все слова находятся в обратном порядке.'''
    begin_from_list = s.split()
    make_reverse_list = []
    for el in begin_from_list[::-1]:
        make_reverse_list.append(el)
    return ' '.join(make_reverse_list)

#test
print(reversewords('hello world!'))