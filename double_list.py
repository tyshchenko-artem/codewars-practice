def maps(a:list):
    '''На вход функция принимает список чисел, а возвращать список с удвоенными числами'''
    final_solution = []
    for num in a:
        if num == 1:
            final_solution.append(num + 1)
        else:
            final_solution.append(num * 2)
    return final_solution


#test
print(maps([1, 2, 3]))