def paperwork(n, m):
    '''Your classmates asked you to copy some paperwork for them.
    You know that there are 'n' classmates and the paperwork has 'm' pages.'''
    if n < 0:
        return 0
    elif m < 0:
        return 0
    else:
        return n * m

t = paperwork(5, 5)
print(t)
print('Hello there')
