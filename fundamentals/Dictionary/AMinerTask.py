key = input()
obj = {}

while key != "stop":
    value = input()
    if not key in obj:
       obj[key] = int(value)
    else:
       obj[key] += int(value)
    key = input()

for i in obj:
    print(f"{i} -> {obj[i]}")


