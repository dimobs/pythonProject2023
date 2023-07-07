n = int(input())

def checker_fn(r, c):
    if 0 <= r <= n and 0 <= c < n:
        return True
    else:
        print(f'Invalid coordinates')

matrix = [[int(i) for i in input().split()] for _ in range(n)]

command = input().split()

while command[0] != 'END':
    action, row, col, pow = command[0], int(command[1]), int(command[2]), int(command[3])
    if checker_fn(row, col):
        if action == 'Add':
            matrix[row][col] += pow
        elif action == 'Subtract':
            matrix[row][col] -= pow

    command = input().split()

[print(*r, sep=' | ') for r in matrix]