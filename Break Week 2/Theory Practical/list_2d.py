
# for inner_list in list_2d:
#     inner_list.sort(reverse=True)
#     print(inner_list)


# print(list_2d[1])

# list_2d[1][2] = 10

# print(list_2d)

# print(list_2d)
# for inner_list in list_2d:
#     for num in inner_list:
#         print(num, end=" ")
#     print()

from copy import deepcopy
list_2d = [[1,2,3], [4,5,6], [7,8,9]]

new_list = deepcopy(list_2d)
new_list[0][0] = 50
print(new_list)

list_2d[0] = [3,4,5]
print(list_2d)
