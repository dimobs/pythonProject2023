def fill_the_box(*args):
    sum = 1
    cube = 3
    if "Finish" in args:
        end_of_the_index = args.index("Finish")
    for i in args[0:end_of_the_index]:
        if cube - 1 >= 0:
            cube -=1
            sum *= i
        else:
            sum -= i
    if sum <= 0:
        return f"No more free space! You have {abs(sum)} more cubes."
    else:
        return f"There is free space in the box. You could put {sum} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))