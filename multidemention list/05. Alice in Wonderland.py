size = int(input())

matrix = []
player = []
tea = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        player = [row, matrix[row].index('A')]

matrix[player[0]][player[1]] = "*"

while tea < 10:
    command = input()

    row, col = [
        player[0] + directions[command][0],
        player[1] + directions[command][1]
    ]

    if 0 <= row < size and 0 <= col < size:
        current_position = matrix[row][col]
        matrix[row][col] = "*"

        if current_position == 'R':
            print(f"Alice didn't make it to the tea party.")
            [print(*row) for row in matrix]
            raise SystemExit
        if current_position.isdigit():
            tea += int(current_position)
    else:
        print(f"Alice didn't make it to the tea party.")
        [print(*row) for row in matrix]
        raise SystemExit

    player[0] = row
    player[1] = col

print('She did it! She went to the party.')
# [print(*row) for row in matrix]
print(*[' '.join(row) for row in matrix], sep='\n')