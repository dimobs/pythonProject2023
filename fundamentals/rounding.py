# def is_even(num):
#     result = num % 2 == 0
#     return result
#
# nums =[int(x) for x in input().split()]
# filtered = list(filter(is_even, nums))
# for num in filtered:
#     print(num)

nums = [ "even" if num % 2 == 0 else 'odd' for num in range(1, 11) ]
print(nums)