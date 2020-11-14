def reverse_words(text: str):
    '''Функция принимает строку и возврашает все слова в этой строке в обратном порядке, при чем пробелы остаются
    на своих местах'''
    create_list_of_words = text.split()
    list_of_reverse_words = []
    for word in create_list_of_words:
        list_of_reverse_words.append(word[::-1])
    if '  ' in text:
        solution = '  '.join(list_of_reverse_words)
        return solution
    else:
        solution = ' '.join(list_of_reverse_words)
        return solution


# test
print(reverse_words('The quick brown fox jumps over the lazy dog.'))
print(reverse_words('apple'))
print(reverse_words('a b c d'))
print(reverse_words('double  spaced  words'))
