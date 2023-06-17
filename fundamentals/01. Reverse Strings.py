from inspect import stack

test = input()

stack_text = list(test)
print(stack_text)

while stack_text:
    removed_elements = stack_text.pop()
    print(removed_elements, end='')
