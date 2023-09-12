def uppercase(fn):
    def upper():
        return fn().upper()

    return upper

@uppercase
def say_hi():
    return "hello there"

say_hi = uppercase(say_hi)
print(say_hi())

