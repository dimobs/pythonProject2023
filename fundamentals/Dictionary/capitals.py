countries = [x for x in input().split(',')]
towns = [x for x in input().split(',')]
dict = {}

for i in range(0, len(countries)):
   dict[countries[i]] = towns[i]
   print(f"{dict[countries[i]]} -> {towns[i]}")


