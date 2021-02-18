def div_con(x: list):
    '''Given a mixed array of number and string representations of integers,
    add up the string integers and subtract this from the total of the non-string integers.
    Return as a number.'''
    list_of_int = []
    list_of_strings = []
    for el in x:
        if type(el) == int:
            list_of_int.append(el)
        else:
            list_of_strings.append(int(el))
    sum_of_integers1 = sum(list_of_int)
    sum_of_integers2 = sum(list_of_strings)
    return sum_of_integers1 - sum_of_integers2


# test
print(div_con([9, 3, '7', '3']))  # 2
