def def_print(a, b):
    print(b)
    print(a)

    if a > abs(b):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")

nums = [int(x) for x in input().split()]
positive = sum(x for x in nums if x >= 0)
negative = sum(x for x in nums if x < 0)

def_print(positive, negative)







