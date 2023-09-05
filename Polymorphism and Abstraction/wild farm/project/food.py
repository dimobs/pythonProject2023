from abc import ABC, abstractmethod


class Food(ABC): #Food - the class should be abstract

    @abstractmethod
    def __init__(self, quantity: int): #should receive quantity (int) upon initialization
        self.quantity = quantity


class Vegetable(Food): #should inherit from the Food class

    def __init__(self, quantity: int):
        super().__init__(quantity)


class Fruit(Food):

    def __init__(self, quantity: int):
        super().__init__(quantity)


class Meat(Food):

    def __init__(self, quantity: int):
        super().__init__(quantity)


class Seed(Food):

    def __init__(self, quantity: int):
        super().__init__(quantity)