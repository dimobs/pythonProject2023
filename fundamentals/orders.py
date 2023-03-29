orders = int(input())
total = 0

for _ in range(orders):
    priceCapules = float(input())
    days = int(input())
    capsulesPerDay = int(input())

    order_price = days * capsulesPerDay * capsulesPerDay
    total += order_price
    print(f'The price for the coffee is: ${order_price:.2f}')
    print(f'Total: ${total:.2f}')

