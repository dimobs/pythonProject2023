def concatenate(*args, **kwargs):
    output = ''.join(args)

    for k, v in kwargs.items():
        if k in output:
            output = output.replace(k, v)
    return output

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))