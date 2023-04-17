def is_even(num):
    result = num % 2 == 0
    return result

nums =[int(x) for x in input().split()]
filtered = list(filter(is_even, nums))
for num in filtered:
    print(num)