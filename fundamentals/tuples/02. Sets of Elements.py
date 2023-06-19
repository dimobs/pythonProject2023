first, second = [int(x) for x in input().split()]
my_sets_first = set()
my_sets_second = set()

for i in range(first):
    my_sets_first.add(int(input()))

for i in range(second):
    numb = int(input())
    my_sets_second.add(numb)


print(*my_sets_first.intersection(my_sets_second), sep='\n')
print(my_sets_first & my_sets_second)
print(my_sets_first | my_sets_second)
print(my_sets_first - my_sets_second)
print(my_sets_first ^ my_sets_second)



