from collections import deque
import operator
from colorama import Fore


def print_board():
    [print(f" {', '.join(row)}") for row in board]


def place_circle():
    row = 0

    while row != ROWS and board[row][player_col] == "0":
        row += 1

    board[row - 1][player_col] = player_symbol

    return row - 1


def get_circle_count(row, col, dx, dy, operator_function):
    current_count = 0

    for i in range(1, 4):
        new_row = operator_function(row, dx * i)
        new_col = operator_function(col, dy * i)

        if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
            break

        if board[new_row][new_col] != player_symbol:
            break

        current_count += 1

    return current_count


def check_for_win(row, col):
    for x, y in direction:
        count = get_circle_count(row, col, x, y, operator.add) + get_circle_count(row, col, x, y, operator.sub) + 1

        if count >= 4:
            return True

    if counter_for_row == ROWS * COLS:
        print_board()
        print("Draw!")
        raise SystemExit

    return False


ROWS, COLS = 6, 7

counter_for_row = 0

board = [["0"] * COLS for x in range(ROWS)]

player_one_symbol = Fore.YELLOW + "1" + Fore.RESET
player_two_symbol = Fore.RED + "2" + Fore.RESET

turns = deque([[1, player_one_symbol], [2, player_two_symbol]])
print(turns)
win = False

direction = (
    (-1, 0),  # top
    (0, -1),  # left
    (-1, -1),  # top-left
    (-1, 1),  # top-right
)

while not win:
    # print_board()

    player_number, player_symbol = turns[0]

    try:
        player_col = int(input(f'Player {player_number}, please choose a column: ')) - 1
    except ValueError:
        print(Fore.RED + f"Select a valid number in the range (1-{COLS})" + Fore.RESET)
        continue

    if not 0 <= player_col < COLS:
        print(Fore.RED + f"Select a valid number in the range (1-{COLS})" + Fore.RESET)
        continue

    if board[0][player_col] != "0":
        print(Fore.RED + "No empty spaces on that column, choose another one!" + Fore.RESET)
        continue

    row = place_circle()
    counter_for_row += 1
    win = check_for_win(row, player_col)

    turns.rotate()

    print_board()
print(f"Player {turns[1][0]} wins!")
