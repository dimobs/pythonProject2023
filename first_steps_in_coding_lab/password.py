username = input()
userpassword = input()
data = input()

while userpassword != data:
    data = input()

print(f"Welcome, {username}")
