type_movie = input()
rows, cols = int(input()), int(input())

income = 0
cinema_capacity = rows * cols

if type_movie == "Premiere":
    income = cinema_capacity * 12
elif type_movie == "Normal":
    income = cinema_capacity * 7.50
else:
    income = cinema_capacity * 5

print(f"{income:.2f} leva")
