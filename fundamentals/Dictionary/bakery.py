data = input().split(" ")
bakey = {}

for i in range(0, len(data), 2):
   key = data[i]
   value = data[i+1]
   bakey[key] = int(value)

print(bakey)



