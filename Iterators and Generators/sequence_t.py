class sequence_repeat:

   def __init__(self, sequence: str, number: int):
      self.sequence = sequence
      self.number = number
      self.i = -1

   def __iter__(self):
      return self

   def __next__(self):
      if self.i == self.number - 1:
         raise StopIteration

      self.i += 1

      return self.sequence[self.i % len(self.sequence)]







result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')