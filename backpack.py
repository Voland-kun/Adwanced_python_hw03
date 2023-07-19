# Довольно костыльное решение с полным перебором, причём двухкратным если исходное целевое значение недостижимо, но
# динамическое программирование, которым как я понимаю подобные задачи решаются нормально, пока выглядит чем-то
# непонятным. Но вроде работает.
def sum_exist(nums, target):
    flag = False
    super_list = []
    sum_max = 0
    key_list = list(nums)
    for x in range(1, 2 ** len(nums)):
        elemlist = []
        current_sum = 0
        for i in range(len(nums)):
            if x & (2 ** i):
                current_sum += nums[key_list[i]]
                elemlist.append(str(f'{key_list[i]}: {nums[key_list[i]]}'))
                if target > current_sum > sum_max:
                    sum_max = current_sum

        if target == current_sum:
            super_list.append(elemlist)
            flag = True
    if flag:
        return super_list, str(f"Максимально возможный вес {target}")
    else:
        return sum_exist(nums, sum_max)


backpack = {"чашка": 6,
            "палатка": 9,
            "верёвка": 7,
            "топор": 8,
            "фонарь": 6,
            "бобёр": 7,
            }
target = 25

# backpack = {"чашка": 16,
#             "палатка": 9,
#             "верёвка": 7,
#             "топор": 6,
#             "фонарь": 5,
#             "бобёр": 4,
#             "спички": 2
#             }
# target = 17


# nums2 = [6, 9, 7, 8, 6, 7]
# target2 = 25
# nums1 = [16, 9, 7, 6, 5, 3, 2]
# target1 = 17

print(sum_exist(backpack, target))
