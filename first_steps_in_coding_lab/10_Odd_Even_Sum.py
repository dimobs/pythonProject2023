import sys
n_numb = int(input())
even = 0
odd = 0

for i in range(1, n_numb + 1):
    current_numb = int(input())

    if (i % 2) == 0:
        even += current_numb
    if (i % 2) == 1:
        odd += current_numb

if even == odd:
    total = even
    print(f"Yes\nSum = {total}")
else:
    total = abs(even - odd)

    print(f"No\nDiff = {total}")