def even_numbers(function):

    def wrapper(numbers):
        return [n for n in numbers if n % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print((' ').join([str(x) for x in get_numbers([1, 2, 3, 4, 5, 6, 7, 8])]))