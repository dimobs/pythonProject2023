from fib import main

data = input()
seq = []

while data !="Stop":
    split_data = data.split()
    if split_data[0] == "Create":
        n = int(split_data[-1])
        seq = main.create_seq(n)
    elif split_data[0] == "Locate":
        num = int(split_data[-1])
        print(main.locate_num(num, seq))
    data = input()