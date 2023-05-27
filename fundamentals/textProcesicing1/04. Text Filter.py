
baneded_word = input().split(", ")

text = input()

for word in baneded_word:
    while word in text:
        text = text.replace(word, "*" * len(word))

print(text)

