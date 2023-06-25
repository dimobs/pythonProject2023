rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = list(input())
    matrix.append(inner_list)

serched_symbol = input()
position = None

for r in range(rows):
    if position:
        break
    for c in range(rows):
        if matrix[r][c] == serched_symbol:
            position = (r, c)
            break

if position:
    print(position)
else:
    print(f'{serched_symbol} does not occur in the matrix')
