import math
from statistics import mean

numb_students = int(input())

names = {}



for i in range(numb_students):
    name, grade = input().split(" ")
    if name not in names:
        names[name] = []
    grade = float(grade)
    names[name].append(grade)

for name, grades in names.items():

    avg = mean(grades)

    print(f"{name} -> {' '.join([str(f'{x:.2f}') for x in grades])} (avg: {avg:.2f})")