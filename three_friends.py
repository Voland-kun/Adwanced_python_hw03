def three_friends():
    # Отдельные переменные чтобы проще под ввод с клавиатуры было переделать, который не доделал (-:
    # Ну тип расширение на любое количество друзей и всё такое.
    a = ("Иван", ("топор","палатка", "тушенка", "кружка"))
    b = ("Сергей", ("тушенка", "топор", "фонарь", "кружка"))
    c = ("Василий", ("фонарь", "лыжи", "акваланг","топор"))
    d = ("Эдуард", ("топор", "фонарь", "бобёр", "верёвка", "нож", "тушенка", "кружка"))
    fr_dict = {
        a[0]:a[1],
        b[0]:b[1],
        c[0]:c[1],
        d[0]:d[1]
    }

    key_list = list(fr_dict)
    value_list = [set(fr_dict[key]) for key in key_list]
    inter = set.intersection(*value_list)

    unique = all_but_one_and_unique(value_list, key_list, 1)
    all_but_one = all_but_one_and_unique(value_list, key_list, 0)

    print(f"Есть у каждого: {inter}")
    print(f"Есть у одного: {unique}")
    print(f"Есть у всех кроме одного: {all_but_one}")

def all_but_one_and_unique(list_of_sets, list_of_keys, flag):
    result_dict = {}
    for i in range(0, len(list_of_sets)):
        temp_list = list_of_sets[::]
        cur_elem = temp_list.pop(i)
        if flag: # ищет которые есть только у одного
            res = cur_elem.difference(*temp_list)
            if res:
                result_dict[list_of_keys[i]] = tuple(res)
        else: # ищет которые есть у всех кроме одного
            res = (set.intersection(*temp_list)).difference(cur_elem)
            if res:
                result_dict[list_of_keys[i]] = tuple(res)
    return result_dict


three_friends()

