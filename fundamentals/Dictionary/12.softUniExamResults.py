line = input()
students = {}
flag = False
engines = {}

while line != "exam finished":
    if line.endswith('banned'):
        name, command = line.split('-')
        students[name][2] = True
    else:
        (username, language, (points)) = line.split("-")
        points = int(points)

        if not language in engines:
            engines[language] = 1
        else:
            engines[language] += 1

        if not username in students:
            students[username] = []
            students[username].append(language)
            students[username].append(points)
            students[username].append(flag)

        else:
            if points > students[username][1]:
                students[username][1] = points
    line = input()

print(f"Results:")
for name in students:
    if students[name][2] == False:
        print(f"{name} | {students[name][1]}")
print("Submissions:")
for name in engines:
    print(f"{name} - {engines[name]}")
