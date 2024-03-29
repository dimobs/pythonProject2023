# rows, cols = [int(x) for x in input().split(' ')]
#
# matrix = []
# max_sum = float('-inf')
# output = ''
#
# for i in range(rows): #0 1 2 3 4
#     matrix.append([int(x) for x in input().split(' ')])
#
# for i in range(rows - 2): #4 - 0 1
#     for x in range(cols - 2):
#         x00 = matrix[i][x]
#         x01 = matrix[i][x + 1]
#         x02 = matrix[i][x + 2]
#         x10 = matrix[i + 1][x]
#         x11 = matrix[i + 1][x + 1]
#         x12 = matrix[i + 1][x + 2]
#         x20 = matrix[i + 2][x]
#         x21 = matrix[i + 2][x + 1]
#         x22 = matrix[i + 2][x + 2]
#
#         current_sum = x00 + x01 + x02 + x10 + x11 + x12 + x20 + x21 + x22
#         if max_sum < current_sum:
#             max_sum = current_sum
#             output = f"Sum = {max_sum}\n"
#             output += f"{x00} {x01} {x02}\n"
#             output += f"{x10} {x11} {x12}\n"
#             output += f"{x20} {x21} {x22}"
#
# print(output)

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_sum = float("-inf")
biggest_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]

        currnet_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if currnet_sum > max_sum:
            max_sum = currnet_sum
            biggest_sum = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in biggest_matrix]




