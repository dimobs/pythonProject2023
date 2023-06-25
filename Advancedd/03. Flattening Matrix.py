rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(',')])
    flat = [j for row in matrix for j in row]

print(flat)

