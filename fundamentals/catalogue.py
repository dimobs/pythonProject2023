class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        return [w for w in self.products if w.startswith(letter)]

    def __repr__(self):
        self.products.sort()
        outPut = ""
        outPut += f"Items in the {self.name} catalogue:\n"
        for i in self.products:
            outPut += f"{i}\n"

        return outPut.rstrip()

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
