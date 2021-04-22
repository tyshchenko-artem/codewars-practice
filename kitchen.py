def gordon(a: str):
    '''Function turn words to Caps, Every word end with '!!!!',
    Any letter 'a' or 'A' become '@', Any other vowel should become '*'.'''
    caps = a.upper()
    split = caps.split()
    new_list = []
    for el in split:
        new_list.append(el.replace('A', '@') + '!!!')
    one_more_list = []
    for el in new_list:
        one_more_list.append(el.replace('E', '*'))
    lst = []
    for el in one_more_list:
        lst.append(el.replace('O', '*'))
    lst1 = []
    for el in lst:
        lst1.append(el.replace('I', '*'))
    lst2 = []
    for el in lst1:
        lst2.append(el.replace('U', '*'))
    
    return ' '.join(lst2)


check = gordon('i am a chef')
print(check)
