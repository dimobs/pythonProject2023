nums = tuple([float(x) for x in input().split()])

occ = {}

for el in nums:
    occ[el] = nums.count(el)

for key, value in occ.items():
    print(f"{key} - {value} times")

