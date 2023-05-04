import math

students = int(input())
lectures = int(input())
bonus = int(input())
currentStudent = 0
maxBonus = 0
maxAttended = 0

for i in range(0, students):
    atendance = int(input())
    total = (atendance / lectures ) * (5 + bonus)
    if (maxBonus <= total):
        maxBonus = total
        maxAttended = atendance
print("Max Bonus:", math.ceil(maxBonus), ".")
print("Max Attended:", maxAttended, "lectures.")
