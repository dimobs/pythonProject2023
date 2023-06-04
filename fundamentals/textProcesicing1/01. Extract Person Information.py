from string import ascii_letters, digits

allowed_chars = ascii_letters + digits
n = int(input())
name = ""
age = ""

for _ in range(0, n):
    line = input().split(' ')
    for i in line:
        if i.startswith('@') and i.find('|') and len(i) >= 3:
            end_of = i.index('|')
            name = (i[1:end_of])

        elif i.startswith('#') and i.find('*') and len(i) >= 3:
            end_of = i.index('*')
            temp = (i[1:end_of])
            if isinstance(int(temp), int):
                age = temp

    if name and age:
        print(f"{name} is {int(age)} years old.")
        name = ""
        age = ""
    else:
        continue







