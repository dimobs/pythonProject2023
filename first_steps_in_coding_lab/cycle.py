# for num in range(-3, 4, 2):
#     print(num)

# a = int(input())
#
# for a in range(a + 1):
#     if a % 2 == 0:
#         print(2 ** a)

# word = input('Enter word: ')
#
# for ch in word:
#     print(ch)

# repeat = int(input())
# total = 0
#
# for _ in range(repeat):
#     current_num = int(input())
#     total += current_num
#
# print(total)

import sys
repeat = int(input())

max_numb = -sys.maxsize
min_numb = sys.maxsize

for num in range(repeat):
    current_numb = int(input())

    if current_numb > max_numb:
        # 3 > -9999
        max_numb = current_numb

    if current_numb < min_numb:
        # 3 < 99999
        min_numb = current_numb


print(max_numb)
print(min_numb)