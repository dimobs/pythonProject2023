prices = {}
quantitys = {}

while True:
    line = input()
    if line == 'buy':
        break

    command = line.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product in prices:
        prices[product] = price
        quantitys[product] += quantity
    else:
        prices[product] = price
        quantitys[product] = quantity

for product in prices:
    price = prices[product]
    quantity = quantitys[product]
    total = price * quantity
    print(f"{product} -> {total:.2f}")


