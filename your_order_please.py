def order(sentence:str):
    list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    split = sentence.split()
    new_list = []
    for el in split:
        if list_of_numbers[0] in el:
            new_list.append(el)
    for el in split:
        if list_of_numbers[1] in el:
            new_list.append(el)
    for el in split:
        if list_of_numbers[2] in el:
            new_list.append(el)
    for el in split:
        if list_of_numbers[3] in el:
            new_list.append(el)
    for el in split:
        if list_of_numbers[4] in el:
            new_list.append(el)
    for el in split:
        if list_of_numbers[5] in el:
            new_list.append(el)
    for el in split:
        if list_of_numbers[6] in el:
            new_list.append(el)
    for el in split:
        if list_of_numbers[7] in el:
            new_list.append(el)
    for el in split:
        if list_of_numbers[8] in el:
            new_list.append(el)

    return ' '.join(new_list)


print(order('Thi1s is2 3a T4est'))
print(order(''))
print(order('4of Fo1r pe6ople g3ood th5e the2'))
