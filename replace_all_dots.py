import re
def replace_dots(str):
    '''The code provided is supposed replace all the dots . in the specified String str with dashes -'''
    a = str.find('.')
    if a == -1:
        return str
    return re.sub(r"\.", "-", str)

print(replace_dots(""))
print(replace_dots("no dots"))
print(replace_dots("one.two.three"))
print(replace_dots(".........."))