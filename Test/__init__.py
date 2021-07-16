# listBoss = [1, 2, 3, 4]
#
# listBoss.insert(int(len(listBoss) / 2), 5)
#
# print(len(listBoss))
# listBoss.sort(reverse=True)
# print(listBoss)

# numbers = list(range(1, 1_000_000))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# get list's mid 3 num or 2 num
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5]
lists = (list1, list2)

for list in lists:
    if len(list) % 2 == 0:
        print(list[int(len(list) / 2) - 1:
                   int(len(list) / 2) + 1])
    else:
        print(list[int(len(list) / 2) - 1:
                   int(len(list) / 2) + 2])

print(1 not in list1)
# # try the pinyin plug
# 列表 = (1, 2)
# # 'tuple' object does not support item assignment
# # 列表[0] = 1
# print(列表)
