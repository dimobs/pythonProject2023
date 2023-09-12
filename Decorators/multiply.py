def multiply(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * times
        return wrapper
    return decorator


@multiply(3)
def add_ten(num):
    # def wrapper(*args, **kwargs):
    #     return func(*args, **kwargs) * times
    return num + 10


print(add_ten(3))
