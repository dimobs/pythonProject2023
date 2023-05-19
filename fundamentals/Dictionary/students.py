data = input()

courses = {}

while ":" in data:
    student_name, student_id, student_course = data.split(':')
    if student_course not in courses:
        courses[student_course] = {student_id: student_name}
    else:
        courses[student_course][student_id] = student_name
    data = input()

students = courses[data]

for student_id, name in students.items():
    print(f"{name} - {student_id}")




