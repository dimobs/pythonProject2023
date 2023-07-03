n = int(input())
active_cells= 0
sum = 0
def check_valid_index (row, col):
    if 0 <= row <= n - 1 and 0 <= col <= n - 1 and battle_field[row][col] != 0 and battle_field[row][col] > 0:
        return True

direction = [[-1, 0],[1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]]

def damage_cells (r, c, d):
    for i in range(len(direction)):
        row_target, col_target = direction[i]
        new_r = row_target + r
        new_c = col_target + c
        if check_valid_index(new_r, new_c):
           battle_field[new_r][new_c] -= d

battle_field = [[int(x) for x in input().split()]for _ in range(n)]

coordiantes = [[int(i) for i in x.split(',')] for x in input().split(' ')]
sum_active_cells = 0

for target in coordiantes:
    target_row, target_column = target
    if check_valid_index(target_row, target_column):
        detonation_power = battle_field[target_row][target_column]
        damage_cells(target_row, target_column, detonation_power)
        battle_field[target_row][target_column] = 0

for r in range(len(battle_field)):
    for c in range(len(battle_field[r])):
        if battle_field[r][c] > 0:
            sum += battle_field[r][c]
            active_cells += 1


print(f'Alive cells: {active_cells}')
print(f'Sum: {sum}')
[print(*row, sep=" ") for row in battle_field]


