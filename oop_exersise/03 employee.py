class Employee:
    def __init__(self, employee_id: int, fname: str, lname: str, salary: float):
        self.id = employee_id
        self.first_name = fname
        self.last_name = lname
        self.salary = salary

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def raise_salary(self, new_salary: float) -> float:
         self.salary += new_salary

         return self.salary

    def get_annual_salary(self) -> float:
        return self.salary * 12

employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())