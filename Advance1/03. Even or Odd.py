

def even_odd(*args):
    command = args[-1]

    if command == 'even':
        return [e for e in args[:-1] if int(e) % 2 == 0]
    else:
        return [o for o in args[:-1] if int(o) % 2 != 0]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))