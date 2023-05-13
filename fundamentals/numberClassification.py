numbers = [int(x) for x in input().split(", ")]
# print(numbers)
# positeve_numbers = [x for x in numbers if x >= 0]
# print(f'Positive: {", ".join([str(x) for x in positeve_numbers])}')

pos = []
neg= []
even = []
odd = []

for num in numbers:
    if num >= 0:
        pos.append(num)

print(f'Positive: {", ".join([str(x) for x in pos])}')


