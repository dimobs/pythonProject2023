data = input().split(" ")
listProducts = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i+1]

    if not key in listProducts:
        listProducts[key] = value

criteria = input().split()

for product in criteria:
    if product in listProducts:
        quantity = listProducts[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
