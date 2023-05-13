from math import ceil

numbers = [int(x) for x in input().split(", ")]

low_bound = 1
high_bound = 10

groups_count = ceil((max(numbers) / 10))
print(groups_count)

for i in range(1, groups_count + 1):
    grouped_number = [x for x in numbers if low_bound <= x <= high_bound]
    print(f"Group of { 10 * i}'s: {grouped_number}")

    low_bound += 10
    high_bound += 10

