def digitize(n: int):
    '''Функция принимает на вход целое цисло и делит это число на список чисел в обратном порядке.'''
    create_str = str(n)
    sep_list = []
    rev_list = []

    for num in create_str:
        sep_list.append(int(num))

    for i in reversed(sep_list):
        rev_list.append(i)

    return rev_list

test = digitize(35231)
print(test)
