# from math import pi
#
# radians = float(input())
# degrees = radians * 180 / pi
#
# print(degrees)


# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

# depozit = float(input())
# month_depozit = int(input())
# year_procent = float(input())
# lihva = depozit * year_procent/100
# moth_lihva = lihva / 12
# total = depozit + month_depozit * moth_lihva
# print (lihva)
# print(moth_lihva)
# print(total)

from math import floor

page_count = int(input())
page_per_hr = int(input())
day_count = int(input())

total_reading = page_count / page_per_hr
result = total_reading / day_count

# print(total_reading)
print(floor(result))



print(floor(result))
