from collections import deque

names = deque(input().split())

rotation_num = int(input()) -1

while len(names) > 1:
    names.rotate(-rotation_num)
    winner = names.popleft()
    print(f"Removed {winner}")

print(f"Last is {names.popleft()}")

