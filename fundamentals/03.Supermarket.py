from collections import deque

people = deque()

while True:
    name = input()
    if name == "Paid":
        while people:
            print(people.popleft())
        continue
    elif name == "End":
        break

    people.append(name)

print(f"{len(people)} people remaining.")