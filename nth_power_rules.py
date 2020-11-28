def modified_sum(a:list, n:int):
    '''Функция принимает на вход список чисел и одно целое число. Находит сумму чисел в списке возведенных в степень
    n, находит сумму чисел в списке и в итоге вычитает из суммы ступеней сумму списковых чисел.'''
    create_list_of_power_of_numbers = []
    for el in a:
        create_list_of_power_of_numbers.append(el ** n)
    first_sum = sum(create_list_of_power_of_numbers)
    second_sum = sum(a)
    return first_sum - second_sum

#test
print(modified_sum([1, 2, 3], 3))