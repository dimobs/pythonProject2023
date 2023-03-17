easterBreadSum = int(input())
topRanking = 0
easterBakerName = ""
easterBakerNameTopCHef = ""
command = ""
pointSum = 0
points = 0
pointsMax = 0

for i in range(0, easterBreadSum):
    easterBakerName = input()
    command = input()
    pointSum = 0
    while command != "Stop":
        points = int(command)
        pointSum += points
        command = input()

    print(f'{easterBakerName} has {pointSum} points.')
    if pointSum > pointsMax:
     pointsMax = pointSum
     easterBakerNameTopCHef = easterBakerName;
     print(f'{easterBakerName} is the new number 1!')

print(f'{easterBakerNameTopCHef} won competition with {pointsMax} points!')

