width_free_space = int(input())
length_free_space = int(input())
heigth_free_space = int(input())
fuill_space = 0

free_space = width_free_space * length_free_space * heigth_free_space

# dadas
while True:
    command_input = input()
    if command_input == "Done":
        if free_space > fuill_space:
            print(f'{free_space - fuill_space} Cubic meters left.')
            break

    command_input = int(command_input)
    fuill_space += int(command_input)

    if free_space < fuill_space:
        print(f"No more free space! You need {fuill_space - free_space} Cubic meters more.")
        break


