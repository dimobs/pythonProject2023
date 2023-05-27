
lines = input()

while lines != "end":
    result = ""

    for letter in reversed(lines):
        result += letter

    print(lines + " = " + result)
    lines = input()


