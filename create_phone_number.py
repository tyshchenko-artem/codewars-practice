def create_phone_number(n: list):
    """Функция принимает список чисел и возвращает строку в форме телефонного номера"""
    if len(n) == 10:
        create_list_of_strings = []
        for el in n:
            create_list_of_strings.append(str(el))
        create_list_of_first_three_numbers = create_list_of_strings[0:3]
        create_second_list = create_list_of_strings[3:6]
        create_last_list = create_list_of_strings[6:]
        create_first_part = '(' + ''.join(create_list_of_first_three_numbers) + ')'
        create_second_part = ''.join(create_second_list)
        create_third_part = ''.join(create_last_list)
        create_last_part = create_second_part + '-' + create_third_part
        return create_first_part + ' ' + create_last_part


# test
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
