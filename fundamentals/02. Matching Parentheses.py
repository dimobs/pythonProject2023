from inspect import stack

line = input()
stack_parents = [];

for index in range(len(line)):
    if line[index] == "(":
        stack_parents.append(index)
    elif line[index] == ')':
        start_positions = stack_parents.pop()
        end_position = index + 1
        print(line[start_positions:end_position])