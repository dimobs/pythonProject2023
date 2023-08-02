from collections import deque
flower_found = ""

flowers = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil",
}

vowels = deque(input().split())
consonants = deque(input().split())

while vowels and consonants:
    v, c = vowels.popleft(), consonants.pop()

    for f in flowers:
        flowers[f] = flowers[f].replace(v, "")
        flowers[f] = flowers[f].replace(c, "")

        if not flowers[f]:
            print(f"Word found: {f}")
            break
    else:
        continue

    break

else:
    print(f"Cannot find any word!")


if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")











