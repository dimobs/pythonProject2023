# nums_arr = [2, 4, 5, 6, 7, 8, 9]
#
# nums = map(lambda x:x + 2, nums_arr)
# for el in nums:
#     print(el)

def repeat(word, times):
    return word * times

text = input()
n = int(input())

result = repeat(text, n)
print(result)

# result = lambda word, times: word * times
# print(result(text, n))