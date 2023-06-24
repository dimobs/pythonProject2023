matrix = []
rows, cols =[int(x) for x in input().split(', ')]
sum = 0

for i in range(rows):
    lines = [int(n) for n in input().split(',')]
    matrix.append(lines)

for row in range(rows):
    for col in range(cols):
        sum += matrix[row][col]


print(sum)
print(matrix)