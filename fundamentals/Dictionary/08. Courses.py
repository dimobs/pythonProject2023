course_name = {}

line = input()

while ":" in line:
    key, value = line.split(" : ")
    if not key in course_name:
        course_name[key] = []
        course_name[key].append(value)
    else:
        course_name[key].append(value)
    line = input()

for word in course_name:
    print(f"{word}: {len(course_name[word])}")
    for i in range(len(course_name[word])):
        print(f"-- {course_name[word][i]}")
