
lines = input().split(' ')
result = ""

for line in lines:
    result += line * len(line)

print(result)
