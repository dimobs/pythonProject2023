longest_intersection = set()

for _ in range(int(input())):
    first_Data, second_Data = [el.split(",") for el in input().split('-')]

    first_range = set(range(int(first_Data[0]), int(first_Data[1]) + 1))
    second_range = set(range(int(second_Data[0]), int(second_Data[1]) + 1))

    intersection = first_range.intersection(second_range)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")