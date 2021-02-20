from collections import OrderedDict

def my_languages(results:dict):
    '''Function returns the list of languages where
    your test score is at least 60, in descending order of the results.'''
    dict_sorted_by_value = OrderedDict(sorted(results.items(), key=lambda x: x[1], reverse=True))
    my_lang = []
    for language, score in dict_sorted_by_value.items():
        if score >= 60:
            my_lang.append(language)
    return my_lang


#test
print(my_languages({"Java": 10, "Ruby": 80, "Python": 65}))
print(my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}))