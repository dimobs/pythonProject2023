class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.count - 1:
            raise StopIteration

        self.counter += 1 #1, 2 , 3, 4, 5

        return self.counter * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)