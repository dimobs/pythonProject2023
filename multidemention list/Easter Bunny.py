from turtle import position

size = int(input())

matrix = []
bunny_pos = []
best_path = []

best_direction = None
max_collected_egg = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]

for direction, position in directions.items():
    row, col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]
    ]

    path = []
    collected_egg = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'X':
            break

        collected_egg += int(matrix[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

        if collected_egg >= max_collected_egg:
            max_collected_egg = collected_egg
            best_direction = direction
            best_path = path

print(best_direction)
print(best_path)
print(*best_path, sep='\n')
print(max_collected_egg)




