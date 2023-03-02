import math

W = 2000
F = 1200
SF = 720


tournaments = int(input())
starting_point = int(input())
final_point = 0
average_score = 0
wins = 0
precent_wins = 0

final_point = starting_point
for _ in range(1, tournaments + 1):
    tournament = input()
    if tournament == 'F':
        final_point += F

    elif tournament == 'SF':
        final_point += SF

    elif tournament == 'W':
        wins += 1
        final_point += W

final_point = math.floor(final_point)
average_score = math.floor((final_point - starting_point) / tournaments)
precent_wins = math.floor((wins / tournaments) * 100)

print(f"Final points: {final_point:.0f}\nAverage points: {average_score} {precent_wins:.2f}%")













