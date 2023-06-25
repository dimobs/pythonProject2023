
rows, columns = [int(x) for x in input().split(', ')] #3, 6

matrix = []
sum = 0

for _ in range(rows):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)

for row in range(rows):
    for col in range(columns):
        sum += matrix[row][col]

print(sum, matrix, sep='\n')