# def is_even(num):
#     result = num % 2 == 0
#     return result
#
# nums =[int(x) for x in input().split()]
# filtered = list(filter(is_even, nums))
# for num in filtered:
#     print(num)

# nums = [ "even" if num % 2 == 0 else 'odd' for num in range(1, 11) ]
# print(nums)

# text = input()
# result = []
#
# for char in text:
#     if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         result.append(char)
# print(result)

# text = input()
# result = [char for char in text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
# print("".join(result))

# entries = [['man', 'thats'],['right', 'awesome']]
#
# element = [x for i in
# for x in i]
# print(element)

nums = [1, 2, 30, -4, 5]

print(nums)
new_ = sorted(nums, key=lambda x: -x)
print(nums)
print(new_)