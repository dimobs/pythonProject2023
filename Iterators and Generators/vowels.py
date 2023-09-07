class vowels:
    def __init__(self, text: str):
        self.text = text
        self.all_vowels = ["a", "i", "e", "u", "o", "y"]
        self.vowels = [ch for ch in self.text if ch.lower() in self.all_vowels]
        self.current_index = -1
        self.end_index = len(self.vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index > self.end_index:
            raise StopIteration()
        return self.vowels[self.current_index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)