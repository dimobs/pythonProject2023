word = list('abs')

while len(word) < 15:
    word.extend(word)
print(word)