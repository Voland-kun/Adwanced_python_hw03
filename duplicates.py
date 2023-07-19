def dup_list(user_list):
    dup = []
    for i in user_list:
        if user_list.count(i) > 1 and i not in dup:
            dup.append(i)
    # либо переводить в сет, а потом обратно в список
    # for i in user_list:
    #     if user_list.count(i) > 1:
    #         dup.append(i)
    # dup = list(set(dup))
    return dup

test = [1,1,1,2,1,3,3,4,5,6,7,7,2,8,9]
print(dup_list(test))