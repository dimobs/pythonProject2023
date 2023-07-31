def drow_upper_parts(n):
    for row in range(1, n + 1): #1 - 7
        for num in range(1, row + 1): #1 - 7
            print(num, end=' ')
        print()

def drow_bottom(n):
    for row in range(n - 1, 0, -1):
        for num in range(1, row + 1):
            print(num, end=' ')
        print()

def drow_numbers_triangle(n):
    drow_upper_parts(n)
    drow_bottom(n)


