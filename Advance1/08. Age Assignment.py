
def age_assignment(*args, **kwargs):
    output = []
    for k, age in kwargs.items():
        for name in args:
            if name.startswith(k):
                output.append(f"{name} is {age} years old.")

    return '\n'.join(sorted(output))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))