# class Email:
#     def __init__(self, sender, resiver, content): #parameter fun in class is method
#         self.sender = sender #atributes
#         self.resiver = resiver #atributes
#         self.content = content #atributes
#         self.is_sent = False #atributes
#
#         def send(self):
#             self.is_sent = True
#
#         def get_info(self):
#             return f"{self.sender} says: {self.resive}: "\
#                    f"{self.content}. Sent: {self.is_sent}"
# emails = []
# data = input()
# while data != "Stop":
#      sender = resiver, content = data.split()
#      email = Email(sender, resiver, content)
#      emails.append(email)
#      data= input()
#
# indexes = [int(el) for el in input().split(', ')]
#
# for index, email in enumerate(emails):
#     if index in indexes:
#         emails[index].send()
#     print(f"{email.sender} says to {email.resive}: S ent: True)
#

# class Zoo:
#     __animails = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birts = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "fish":
#             self.birts.append(name)
#
#         Zoo._Zoo__animails += 1
#
#     def get_info(self, species):
#         info = ""
#         if species == "mammal":
#             info = f"Mammals in {self.name}: {', '.join(self.mammals)}"
#         elif species == "fish":
#             info = f"Mammals in {self.name}: {', '.join(self.fishes)}"
#         elif species == "bird":
#             info = f"Mammals in {self.name}: {', '.join(self.birts)}"
#
#         return f"{info}\nTotal animals: {Zoo._Zoo__animails}"
#
#
# name = input()
# rows = int(input())
#
# zoo = Zoo(name)
#
# for _ in range(rows):
#     species, name = input().split()
#     zoo.add_animal(species, name)
#
# species = input()
# print(zoo.get_info(species))

class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes

comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)