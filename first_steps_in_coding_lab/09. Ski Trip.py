from datetime import date

days = int(input())
place, rate = input(), input()

discount = 1
nights = days - 1
place = place.lower()
rate = rate.lower()
rfoa = 18.00 * nights
app = 25.00 * nights
# prezidentApp = 35.00 * nights
positive = 0.25
negative = 0.90

if place == 'apartament':
    if days < 10:
        discount = app * 0.70
    elif 10 <= days <= 15:
        discount = app * 0.65
    else:
        discount = app * 0.50
else:
    discount = rfoa * discount

if rate == 'positive':
    total = discount + (positive * discount)
else:
    total = (negative * discount)

print(f"{total:.2f}")
#
# 2
# apartament
# positive