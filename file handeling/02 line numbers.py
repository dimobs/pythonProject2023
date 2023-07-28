from string import punctuation

with open("files/01text.txt", "r") as f:
    text = f.readlines()

output_file = open("files/output.txt", "w")

for i in range(len(text)):

    letters, marks = 0, 0

    for symbol in text[i]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {i + 1}: {''.join(text[i])} ({letters})({marks})\n ")
output_file.close()