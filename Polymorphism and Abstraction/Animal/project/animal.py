from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self) -> str:
        pass

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a " \
               f"{self.age} year old {self.gender} {self.__class__.__name__}"



