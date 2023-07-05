

def palindrome(*args):
    k, v = args
    if k == k[::-1]:
        return f"{k} is a palindrome"
    else:
        return f"{k} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))