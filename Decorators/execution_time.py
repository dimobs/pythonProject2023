from time import time


def exec_time(func):
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()

        return end - start
    return wrapper


@exec_time
def fn(string):
    result = ""
    for s in string:
        result += s
    return result

print(fn(['a' for i in range(1000000)]))

