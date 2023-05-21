line = input()
obj = {}

for ch in line:
    if ch == ' ':
        continue
    if ch not in obj:
        obj[ch] = 1
    else:
        obj[ch] += 1

for i in obj:
    print(f"{i} -> {obj[i]}")
