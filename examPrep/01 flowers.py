from collections import deque

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
            print(f"Found it {f}")
            break
    else:
        continue

    break

else:
    print("Connot found")






