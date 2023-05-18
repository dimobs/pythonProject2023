class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = int(price)
        self.owmer = None

    def buy(self, money, owner):
        if int(money) >= self.price and owner != None:
            self.owmer = owner
            money_left = f"{money -self.price:.2f}"
            return f"Successfully bought a {self.type}. Change: {money_left}"
        elif int(money) <= self.price:
            return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.owmer != None:
            self.owmer = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owmer != None:
            return f"{self.model} {self.type} is owned by: {self.owmer} "
        else:
            return f"{self.model} {self.model} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
