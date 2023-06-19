# name_count = int(input())
# names = set()
# list_ = [1,2,3,4,5]
# for _ in range(name_count):
#     names.add(input())
#
# print(*names, sep='\n')
# print(names)
# print(list_)
# print(*list_)


print(*{input() for _ in range(int(input()) + 1)}, sep='\n')
