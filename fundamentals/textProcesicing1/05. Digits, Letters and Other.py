isdigit_ = input()
our_number = ""
our_alpha = ""
our_symbol = ""

for i in isdigit_:
    if i.isdigit():
        our_number += (i)
    elif i.isalpha():
        our_alpha += (i)
    else:
        our_symbol += (i)

print(int(our_number))
print(our_alpha)
print(our_symbol)

