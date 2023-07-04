def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return 'Enter valid values'

    def area():
        return length * width

    def perimeter():
         return 2 * (length + width)

    return f'Reactangle area: {area()}\n' \
           f'Reactangle perimeter: {perimeter()}\n'

print(rectangle(2, 10))
print(rectangle('2', 10))