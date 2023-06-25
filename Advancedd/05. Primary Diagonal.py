rows = int(input())

matrix = []
sum = 0

for i in range(rows):
    matrix.append([int(x) for x in input().split()])
    sum += matrix[i][i]

print(sum)
