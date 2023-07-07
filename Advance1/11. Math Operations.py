def fill_the_box(*args):
    sum = 1
    over_container = 0
    flag = False
    for i in range(3):
        sum *= int(args[i])
    for j in args[3:]:
        if j == 'Finish':
            break
        if (sum - j) >= 0:
            sum -= j
            if sum == 0:
                flag = True
        else:
            over_container -= j
            flag = True
    if flag and over_container <= 0:
        over_container = abs(over_container)
        return f"No more free space! You have {over_container} more cubes."
    else:

        return f"There is free space in the box. You could put {sum} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))