def boolean_to_string(b:bool):
    '''Функция принимает булевое значение и возвращает строку "True", если b == True. Если b == False возвращается
    "False".'''
    if type(b) == bool:
        if b is True:
            return 'True'
        else:
            return 'False'
    else:
        return 'argument must be a boolean'



test1 = boolean_to_string(True)
test2 = boolean_to_string(False)
print(test1)
print(test2)