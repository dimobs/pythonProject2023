def fibonacci():
    n1, n2 = 0, 1

    while True:
        yield n1 #return 0(n1), 1(n2), 1(n1)

        n1, n2 = n2, n1 + n2

gen = fibonacci()
for i in range(5):
    print(next(gen))