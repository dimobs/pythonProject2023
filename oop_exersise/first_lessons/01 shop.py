class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
billa = Shop("Billa", ["Apples", "Bananas", "Cuc"])
print(billa.items)
print(billa.get_items_count())
