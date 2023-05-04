array = input()
x = array.split("|")
inputData = input()

while "Go Shopping!":
    command = inputData.split(" ")
    a = command[0]
    b = command[1]
    c = command[2]
    if a == "Unnecessary":
        if b in x:
            x.remove(b)
    if a == "Urgemt":
        if b not in x:
            x.append(b)
    if a == "Correct":
        if b in x:
          for i in range(len(x)):
              if x[i] == b:
                  x[i] = c
    if a == "Reaggange":
        i = x.index(b)
        del x[i]
        x = x + [b]

print(x)






