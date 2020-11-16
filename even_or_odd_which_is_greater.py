def even_or_odd(s:str):
    '''На вход принимается строка. Функция подсчитывает сумму четных и нечетных чисел в этой строке
    и возвращает такие значения: "Even is greater than Odd", если сумма четных больше; "Odd is greater than Even",
    если сумма нечетных больше; "Even and Odd are the same", если значения равны.'''
    create_list_of_numbers = []
    create_list_of_even = []
    create_list_of_odd = []
    for el in s:
        create_list_of_numbers.append(int(el))
    for num in create_list_of_numbers:
        if num % 2 == 0:
            create_list_of_even.append(num)
        else:
            create_list_of_odd.append(num)
    find_sum_of_even_list = sum(create_list_of_even)
    find_sum_of_odd_list = sum(create_list_of_odd)
    if find_sum_of_even_list > find_sum_of_odd_list:
        return 'Even is greater than Odd'
    elif find_sum_of_even_list < find_sum_of_odd_list:
        return 'Odd is greater than Even'
    else:
        return 'Even and Odd are the same'

#test
print(even_or_odd('12'))
print(even_or_odd('123'))
print(even_or_odd('112'))