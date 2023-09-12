def store_result(func): #decorator
    _FILE_NAME = 'result.txt'

    def wrapper(*args):
        with open(_FILE_NAME, 'a') as f:
            f.write(f"Function {func.__name__} was called. Result: {func(*args)}\n")
    return wrapper

class store_results:
    _FILE_NAME = 'result.txt' #atributes

    def __init__(self, func): #decorator
        self.func = func

    def __call__(self, *args, **kwargs):
        with open(store_results._FILE_NAME, "a") as f:
            f.write(f"Function {self.func.__name__} was called. Result: {self.func(*args)}\n")


class store_results_with_params:
    _FILE_NAME = 'result.txt'

    def __init__(self, param): #decorator
        self.param = param

    def __call__(self, func): #wrapper
        def wrapper(*args):
            with open(store_results._FILE_NAME, "a") as f:
                f.write(f"Function {func.__name__} was called. Result: {func(*args)}. With param {self.param}\n")

        return wrapper


@store_results_with_params(2)
def add(a, b): #wrapper
    return a + b


@store_results_with_params(3)
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)