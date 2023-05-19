command = input()
listProduct = {}
outPuts = ""

while command != "statistics":
    key, value = command.split(": ")
    if not key in listProduct:
        listProduct[key] = int(value)
    else:
        listProduct[key] += int(value)

    command = input()

print(f"Product in stock:")

for (key, value) in listProduct.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(listProduct.keys())}")
print(f"Total Quantity: {sum(listProduct.values())}")








