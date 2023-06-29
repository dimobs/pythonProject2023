import numpy as np

n = int(input())
active_cells= 0
sum = 0
def check_valid_index (row, col):
    if 0 <= row <= n and 0 <= col <= n and battle_field[row][col] != 0 and battle_field[row][col] > 0:
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
        battle_field[target_row][target_column] = 0
        damage_cells(target_row, target_column, detonation_power)

[print(*row, sep=" ") for row in battle_field]

asd = np.array(battle_field)
print(asd)



# sum = [sum(i for i in flattened if i % 2 == 0)]


# [print(*row, sep="") for row in matrix]