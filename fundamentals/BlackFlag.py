plunder = int(input())

dalys = int(input())
expected = int(input())

total = 0

for i in range(1, plunder + 1):
    total += dalys

    if i % 5 == 0:
        total = total - ((total * 30)/100)

    if i % 3 == 0:
         total = total + (dalys / 2)


if expected < total:
    print(f'Ahoy! {total:.2f}')
else:
    total = (1 - (expected - total)/(expected)) * 100
    print(f'Collected only {total:.2f}% of the plunder.')