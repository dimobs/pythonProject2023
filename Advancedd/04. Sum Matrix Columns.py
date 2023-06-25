rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

sum = 0

for c in range(columns):
    for r in range(rows):
        sum += matrix[r][c]
    print(sum)
    sum = 0





