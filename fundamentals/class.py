class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if Class.__students_count > len(self.grades):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return float(f"{(sum(self.grades) / len(self.grades)):.2f}")

    def __repr__(self):
        list_students = ', '.join(self.students)
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {list_students}. Average grade: {average_grade}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)