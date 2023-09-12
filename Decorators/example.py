from time import time


def measure_time(fn):
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(end - start)

        return result
    return wrapper


@measure_time
def sum_number_to(to_number):
    result = 0
    for n in range(to_number):
        result += n
    return result

sum_number_to(1000000)