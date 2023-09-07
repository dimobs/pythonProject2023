def solution():
    def integers():  # generator because yield
        num = 1
        while True:
            yield num
            num += 1

    def halves():  # generator because yield
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return (take, halves, integers)


take = solution()[0]  # take
halves = solution()[1]  # halves
print(take(5, halves()))
