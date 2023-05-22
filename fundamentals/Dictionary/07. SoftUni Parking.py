username = {}
license_plate = {}

n = int(input())

for i in range(0, n):
    line = [x for x in input().split()]
    if len(line) == 3:
        status = line[0]
        name = line[1]
        registration = line[2]
        if not name in license_plate:
            license_plate[name] = registration
            print(f"{name} registered {registration} successfully")
        else:
            print(f"ERROR: already registered with plate number {registration}")
    else:
        status = line[0]
        name = line[1]
        if name in license_plate:
            license_plate.pop(name)
            print(f"{line[1]} unregistered successfully")
        else:
            print(f"ERROR: user {line[1]} not found")

for i in license_plate:
    print(f"{i} => {license_plate[i]}")