n = int(input())

matrix = []
primery_diagonal = []
secondary_diagonal = []

for i in range(n):
    matrix.append([int(x) for x in input().split(' ')])
    primery_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n - i - 1])

total = abs(sum(primery_diagonal) - sum(secondary_diagonal))

print(total)