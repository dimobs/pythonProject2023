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
