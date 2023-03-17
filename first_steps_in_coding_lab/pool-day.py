import math

people = int(input())
ticket = float(input())
tools = float(input())
umbrella_price = float(input())
need_for_personal = 75

entrance = people * ticket
capacity_bed = math.ceil(people * (need_for_personal / 100))
personals_price = tools * capacity_bed
umbrela_taken_price = math.ceil(people / 2) * umbrella_price
total = entrance + personals_price + umbrela_taken_price

print(f'{total:.2f} lv.')
