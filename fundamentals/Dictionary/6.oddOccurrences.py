# Java C# PHP PHP JAVA C java

line = input().split(' ')
my_dict = {}
outPut = []
new_list = [(x.lower()) for x in line]
for word in new_list:
    if not word in my_dict.keys():
        my_dict[word] = 1
    else:
        my_dict[word] += 1

for key, value in my_dict.items():
    if value % 2 != 0:
        outPut.append(key)
output = " ".join(outPut)
print(output)