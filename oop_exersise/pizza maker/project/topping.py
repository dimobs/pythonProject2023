class Topping:
    def __init__(self, topping_type: str, weight: float) -> None:
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self) -> str:
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value: str) -> None:
        if not value:
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type = value

    def get_weight(self):
        return self.__weight

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, value: float) -> None:
        if value <= 0:
            raise ValueError ("The weight cannot be less or equal to zero")
        self.__weight = value




