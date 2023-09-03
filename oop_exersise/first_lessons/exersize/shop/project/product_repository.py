from typing import List
from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> str:
        product = [p for p in self.products if p.name == product_name][0]
        if product:
            return product

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        self.products.pop(product)

    def __repr__(self) -> None:
        res = ""
        for p in self.products:
            res += f"{p.name}: {p.quantity}\n"
        return res