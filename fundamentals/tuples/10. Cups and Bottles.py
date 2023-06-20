from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

wasted_litters_of_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup <= current_bottle:
        wasted_litters_of_water += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)

if cups:
    print(f"Cups: {' '.join(str(c) for c in cups)}")
else:
    print(f"Bottles: {' '.join(str(b) for b in bottles)}")

print(f'Wasted litters of water: {wasted_litters_of_water}')