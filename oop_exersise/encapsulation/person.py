class Person:
    def __init__(self, __name: str, __age: int):
        self.__name = __name
        self.__age = __age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

person = Person("Ivan", 22)
print(person.get_name())
print(person.get_age())
