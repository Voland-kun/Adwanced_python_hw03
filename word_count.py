import re


def dict_count(user_string):
    words_dict = {}
    user_string = user_string.title()
    # можно переводить в lower но разницы нет, зато в словаре имена собственные будут записаны с большой буквы
    spl = re.split(r'[^\w*\-]', user_string) # нижнее подчёркивание не обрабатывается, можно дополнительно
    # user_string = user_string.replace('_', ' ') # заменить _ в строке, но сделать в одной регулярке не смог
    # без того чтобы прописывать отдельно каждый символ который нужно обрабатывать.
    for i in spl:
        if i != '' and re.search(r'[\d*]', i) is None:
            if i not in words_dict:
                words_dict[i] = 1
            else:
                words_dict[i] += 1
    sort_tuple = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict(sort_tuple)
    number_of_results = 10
    count = 0
    for key, value in sorted_dict.items():
        if count < number_of_results:
            print(f'{key} : {value}')
            count += 1
    return sorted_dict

with open('War_and_Peace.txt') as f:
    test_str = f.read()

dict_count(test_str)
