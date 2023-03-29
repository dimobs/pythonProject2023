divisorN = int(input())
bound = int(input())
maxMultiple = 0

for i in range(bound, 0, -1):
    if i % divisorN == 0:
        maxMultiple = i
        print(maxMultiple)
        break
