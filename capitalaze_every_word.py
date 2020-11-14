def to_jaden_case(string: str):
    """Функция принимает строку и возвращает строку, в которой все слова начинаются с большой буквы"""
    create_list = string.split()
    lst = []
    for el in create_list:
        lst.append(el.capitalize())
    solution = ' '.join(lst)
    return solution


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
