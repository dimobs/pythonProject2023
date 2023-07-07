from turtle import position

n = int(input())

matrix = [list(input()) for _ in range(n)]
positions = (  # създаваме тюпъл с всички посоки на коня
    (-2, -1),  # горе 2 и ляво 1
    (-2, 1),  # горе 2 и дясно 1
    (-1, -2),  # горе 1 и ляво 2
    (-1, 2),  # горе 1 и дясно 2
    (2, 1),  # долу 2 и дясно 1
    (2, -1),  # долу 2 и ляво 1
    (1, 2),  # долу  1 и дясно 2
    (1, -2)  # долу 1 и ляво 2
)

removed_kings = 0

while True:
    max_attacks = 0
    knight_with_most_attacs_pos = []

    for row in range(n):
        if matrix[row][col] == 'K':
            attacks = 0

            for pos in position:
                pos_row = row + pos[0]
                pos_col = row + pos[1]

        if 0 <= pos_row < n and 0 <= pos_col < n:  # проверяваме дали позицията е валидна
            if matrix[pos_row][pos_col] == "K":  # проверяваме дали имаме кон на дадената позиция
                attacks += 1  # увеличаваме атаките
        if attacks > max_attacks:  # проверяваме дали това е коня с най-много атаки
            knight_with_most_attacks_pos = [row, col]  # запазваме координатите на коня
            max_attacks = attacks  # обновяваме максималните атаки за тази итерация на дъската

        if knight_with_most_attacks_pos:  # проверяваме дали имаме кон за махане
            r, c = knight_with_most_attacks_pos  # взимаме позицията на коня
            matrix[r][c] = "0"  # заменяме коня с 0
            removed_knights += 1  # увеличаваме броя на махнатите коне
        else:  # в противен случай, прекратяваме цикъла
            break

        print(removed_knights)  # принтираме броя на махнатите