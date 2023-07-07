my_list = [x.split() for x in input().split('|')]
print(*[' '.join(x) for x in my_list[::-1] if x])


