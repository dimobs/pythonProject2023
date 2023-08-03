SIZE = 6
mars = []
rover_pos = []

deposits = {
    "W": ["Water", 0],
    "M": ["Metal", 0],
    "C": ["Concrete", 0]
}

direction = {
    "left": lambda r, c: [r, (c - 1) % SIZE],
    "right": lambda r, c: [r, (c + 1) % SIZE],
    "up": lambda r, c: [(r - 1) % SIZE, c],
    "down": lambda r, c: [(r + 1) % SIZE, c],
}

for row in range(SIZE):
    current_row = input().split()

    if "E" in current_row:
        rover_pos = [row, current_row.index("E")]

    mars.append(current_row)

commands = input().split(", ")

for command in commands:
    rover_pos = direction[command](*rover_pos)
    position = mars[rover_pos[0]][rover_pos[1]]


    if position in deposits:
        print(f"{deposits[position][0]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        deposits[position][1] += 1

    elif position == "R":
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if all([deposits["W"][1], deposits["M"][1], deposits["C"][1]]):
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")