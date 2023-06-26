rows = int(input())
    matrix = []
primary = []
secondary = []
primary_sum = 0
secondary_sum = 0

for i in range(rows): # 0, 1, 2
    matrix.append([int(x) for x in input().split(', ')])
    primary.append(matrix[i][i])
    primary_sum = sum(primary)
    secondary.append(matrix[i][rows - i - 1])
    secondary_sum = sum(secondary)

print(f"Primary diagonal: {', '.join(str(e) for e in primary)}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(str(e) for e in secondary)}. Sum: {secondary_sum}")
