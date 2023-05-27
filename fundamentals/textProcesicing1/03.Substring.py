
lines = input()
substrings = input()

while lines in substrings:
    substrings = substrings.replace(lines, "")

print(substrings)