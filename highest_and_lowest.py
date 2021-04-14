def high_and_low(numbers:str):
    '''given a string of space separated numbers, and function return the highest and lowest number.'''
    l = numbers.split()
    if len(l) == 1:
        return numbers
    else:
        list_num = []
        for s in l:
            list_num.append(int(s))
        mx = max(list_num)
        mn = min(list_num)
        return str(mx) + ' ' + str(mn)


t = high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
t1 = high_and_low("1 -1")
t2 = high_and_low("1 1")
t3 = high_and_low("1 -1 0")
t4 = high_and_low("42")
print(t)
print(t1)
print(t2)
print(t3)
print(t4)