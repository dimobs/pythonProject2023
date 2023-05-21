line = input()
phonebook = {}

def modify(name, phone):
        phonebook[name] = phone

while "-" in line:
    (name, phone) = line.split('-')
    modify(name, phone)
    line = input()

n = int(line)


for n in range(0, n):
    command = input()
    if command in phonebook:
        print(f"{command} -> {phonebook[command]}")
    else:
        print(f"Contact {command} does not exist.")



