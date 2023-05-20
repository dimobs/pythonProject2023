line = input().split(', ')
my_dict = {}

newLine = [(ord(x)) for x in line]

for key, value in enumerate(newLine):
    if not line[key] in my_dict.keys():
        my_dict[line[key]] = value

print(my_dict)