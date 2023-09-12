def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper
    return decorator

@repeat(4) #zakacha se na decorator
def say_hi(): #tova se poddava na wrapper
    print('Hello')

say_hi()