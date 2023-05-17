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
#      sender, resiver, content = data.split()
#      email = Email(sender, resiver, content)
#      emails.append(email)
#      data= input()
#
# indexes = [int(el) for el in input().split(', ')]
#
# for index, email in enumerate(emails):
#     if index in indexes:
#         emails[index].send()
#     print(f"{email.sender} says to {email.resive}: S ent: True")


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

# class Comment:
#     def __init__(self, username, content, likes = 0):
#         self.username = username
#         self.content = content
#         self.likes = likes
#
# comment = Comment("user1", "I like this book")
# print(comment.username)
# print(comment.content)
# print(comment.likes)

# class Party:
#     def __init__(self):
#         self.people = []
#
# party = Party()
# line = input()
# while line != "End":
#     party.people.append(line)
#     line = input()
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")

# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#             self.is_sent = True
#
#     def get_info(self):
#             return f"{self.sender} says to {self.receiver}: "\
#                     f"{self.content}. Sent: {self.is_sent}"
#
# emails = []
#
# line = input()
# while line != "Stop":
#     sender, receiver, content = line.split(" ")
#     email = Email(sender, receiver, content)
#     emails.append(email)
#     line = input()
#
# goSend = [int(el) for el in input().split(', ')]
#
# for x in goSend:
#     print(emails[0].content)
#     print(emails[x])
#
#
#     emails[x].send()
#
# for email in emails:
#     if email.is_sent == True:
#         print(email.get_info())

# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == 'mammal':
#            self.mammals.append(name)
#         elif species == 'fishes':
#             self.fishes.append(name)
#         elif species == 'birds':
#             self.birds.append(name)
#
#         Zoo._Zoo__animals += 1
#
#     def get_info(self, species):
#             outPut = ""
#             if species == 'mammal':
#                outPut = f"Mammals in {self.name}: {self.mammals}"
#             elif species == 'fishes':
#                outPut = f"Fishes in {self.name}: {self.fishes}"
#             elif species == 'birds':
#                 outPut = f"Birds in {self.name}: {self.birds}"
#
#             return f"{outPut}\nTotal animals: {Zoo._Zoo__animals}"
#
#
# name = input()
# numbersForAdded = int(input())
#
# zoo = Zoo(name)
# for i in range(1, numbersForAdded +1):
#     species, kind = input().split(" ")
#     zoo.add_animal(species, kind)
#
# sortBy = input()
#
# print(zoo.get_info(sortBy))


class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * self.radius * self.radius

    def calculate_area_of_sector(self, angle):
        return Circle.__pi * (angle/360) * self.radius * self.radius


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")


