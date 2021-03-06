def even_last(numbers):
    if len(numbers) == 0:
        return 0
    else:
        new_list = []
        for i in range(0, len(numbers), 2):
            new_list.append(numbers[i])
        return sum(new_list) * numbers[-1]

#testing
print(even_last([2, 3, 4, 5]))
print(even_last([]))