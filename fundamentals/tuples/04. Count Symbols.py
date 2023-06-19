# occurrences = {}
#
# for letter in input():
#     occurrences[letter] = occurrences.get(letter, 0) + 1
#
# for key, value in sorted(occurrences.items()):
#     print(f"{key}: {value} time/s")

text = input()

for letter in sorted(set(text)):
    print(f"{letter}: {text.count(letter)} time/s")