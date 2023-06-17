from collections import deque

people = deque(input().split(' '))

rotation_num = int(input()) - 1

while len(people) > 1:
    people.rotate(-rotation_num)
    exited_name = people.popleft()
    print(f"Removed {exited_name}")

print(f"Last is {people.popleft()}")



