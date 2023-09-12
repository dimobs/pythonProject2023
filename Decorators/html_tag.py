def tags(tag): #p
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper
    return decorator


@tags('p')
def htmlTag(*args):
    return "".join(args)

print(htmlTag('This is a html tag', ' second html tag'))

