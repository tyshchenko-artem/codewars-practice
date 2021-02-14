def max_redigit(num:int):
    '''Function takes one positive three digit integer and rearranges its digits to get maximum possible number.
    Assume that argument is integer. Return None if argument is not valid.'''
    try:
        string = str(num)
        if len(string) < 3:
            return None
        elif len(string) > 3:
            return None
        create_list_of_int = []
        create_list_of_strings = []
        for letter in string:
            create_list_of_int.append(int(letter))
        reverse = sorted(create_list_of_int, reverse=True)
        for i in reverse:
            create_list_of_strings.append(str(i))
        create_string = ''.join(create_list_of_strings)
        return int(create_string)
    except ValueError:
        return None


#test
print(max_redigit(321))
print(max_redigit('-'))
print(max_redigit(0))
print(max_redigit(99))
print(max_redigit(1000))
print(max_redigit(1))
