class Customer:
    id = 1 #class attribute id / starting from 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id: int = Customer.id #which will keep the value of the id for the upcoming customer
        Customer.id += 1 #autoincremented,

    @staticmethod
    def get_next_id() -> int:
        return Customer.id

    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; " \
               f"Address: {self.address}; " \
               f"Email: {self.email}"

