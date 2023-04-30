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
# result = [char for char in input() if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
# print("".join(result))

def valid_word(text):
    result = [char for char in text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
    return "".join(result)
text = input()
print(valid_word(text))

das