def calculate(num1, operation, num2):
    '''Функция представляет собой простой калькулятор'''
    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        return None
    else:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                return None
            else:
                return num1 / num2


# test
print(calculate(-3, "/", 0))
print(calculate(-3, "w", 0))
print(calculate(3.2, "*", 8))
