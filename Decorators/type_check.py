def type_check(type_input):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_input):
                    return "Bad Type"
            return func(*args)
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))