from collections import deque
from functools import reduce
from math import floor

# my_collections = deque(input().split())

# idx = 0

# while idx < len(my_collections):
#     el = my_collections[idx]
#
#     if el == '*':
#         for _ in range(idx - 1):
#             my_collections.appendleft(int(my_collections.popleft() * int(my_collections.popleft())))
#     if el == '/':
#         for _ in range(idx - 1):
#             my_collections.appendleft(int(my_collections.popleft() / int(my_collections.popleft())))
#     if el == '+':
#         for _ in range(idx - 1):
#             my_collections.appendleft(int(my_collections.popleft() + int(my_collections.popleft())))
#     if el == '-':
#         for _ in range(idx - 1):
#             my_collections.appendleft(int(my_collections.popleft()) - int(my_collections.popleft()))
#     if el in '*/=-':
#         del my_collections[1]
#         idx = 1
#
#     idx += 1
#
# print(floor(int(my_collections[0])))

my_collection = input().split()

idx = 0

my_funk = {
    '*': lambda i: reduce(lambda a, b: a * b, map(int, my_collection[:i])), #i = my_collection[i:] - my_collection[:i]
    '/': lambda i: reduce(lambda a, b: a / b, map(int, my_collection[:i])),
    '+': lambda i: reduce(lambda a, b: a + b, map(int, my_collection[:i])),
    '-': lambda i: reduce(lambda a, b: a - b, map(int, my_collection[:i])),
}

while idx < len(my_collection):
    element = my_collection[idx]

    if element in '*/+-':
        my_collection[0] = my_funk[element](idx)
        [my_collection.pop(1) for i in range(idx)]
        idx = 1

    idx += 1

print(floor(int(my_collection[0])))