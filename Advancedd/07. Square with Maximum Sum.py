r, c = [int(x) for x in input().split(', ')]

matrix = []
max_sum = float('-inf')

for _ in range(r):
    inner_list = [int(x) for x in input().split(',')]
    matrix.append(inner_list)
for h in range(r - 1):
    for v in range(c - 1):
        current_el = matrix[h][v]
        element_below = matrix[h + 1][v]
        next_element = matrix[h][v + 1]
        diagonal = matrix[h + 1][v + 1]
        sum_el = current_el + element_below + next_element + diagonal

        if max_sum < sum_el:
            max_sum = sum_el
            sub_matrix = [[current_el, next_element], [element_below, diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)


