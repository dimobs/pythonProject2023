
rows, columns = [int(x) for x in input().split(' ')]

matrix = []
count = 0
for i in range(rows):
    matrix.append([x for x in input().split(' ')])

for i in range(rows - 1):
    for j in range(columns - 1):
        left_el = matrix[i][j]
        right_el = matrix[i][j + 1]
        left_dw = matrix[i + 1][j]
        right_dw = matrix[i + 1][j + 1]


        if left_el == right_el == left_dw == right_dw:
            count += 1

print(count)

