def greet(name):
    '''Функция возвращает приветствия для пользователей.
    Если пользователя зовут "Johnny" возврашается строка "Hello, my love!"'''
    if name != "Johnny":
        return "Hello, {name}!".format(name=name)
    elif name == "Johnny":
        return "Hello, my love!"


print(greet('Alex'))
print(greet('Johnny'))
