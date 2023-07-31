from collections import deque

workers = deque(int(x) for x in input().split(' '))
energy = [int(x) for x in input().split(' ')]
print(workers.rotate()) #10 16 13 25
print(energy)
