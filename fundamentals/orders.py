orders = int(input())
total = 0

for _ in range(orders):
    priceCapules = float(input())
    days = int(input())
    capsulesPerDay = int(input())

    if priceCapules < 0.01 or priceCapules > 100:
        continue

    if days < 1 or days > 31:
        continue

    if capsulesPerDay < 1 or capsulesPerDay > 2000:
        continue

    order_price = days * capsulesPerDay * capsulesPerDay
    total += order_price
    print(f'The price for the coffee is: ${order_price:.2f}')
    print(f'Total: ${total:.2f}')

