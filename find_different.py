def iq_test(numbers: str):
    '''Функция находит отличающийся элемент(единственный четный или нечетный) в строке и возвращает его индекс.'''
    list_of_strings = numbers.split()
    list_of_numbers = []
    list_of_even = []
    list_of_odd = []
    for string in list_of_strings:
        list_of_numbers.append(int(string))
    for num in list_of_numbers:
        if num % 2 == 0:
            list_of_even.append(num)
        else:
            list_of_odd.append(num)
    result = []
    if len(list_of_even) < len(list_of_odd):
        result.append(list_of_even[0])
    elif len(list_of_even) > len(list_of_odd):
        result.append(list_of_odd[0])
    find_this_element_in_result_string = str(result[0])
    i = 0
    for el in list_of_strings:
        i += 1
        if el == find_this_element_in_result_string:
            break
    return i

# test
print(iq_test('45 25 23 1 33 37 19 36 21 47 49 15 37 17 9 27 33 49 35'))  # 8
print(iq_test("2 4 7 8 10"))  # 3
print(iq_test("1 2 2"))  # 1
