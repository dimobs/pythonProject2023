import math
import tkinter as tk

root = tk.Tk()

root.title("Calculator")

display_var = tk.StringVar()
display = tk.Label(root, bg="white", font=("Roboto", 25), textvariable=display_var, width=18, anchor="e")
display.grid(row=0, column=0, columnspan=4, sticky="nswe")

operand_1 = ""
operator = ""
operand_2 = ""
memory = 0
is_equal = False


def factorial(number):
    if number == 1:
        return 1

    return number * factorial(number - 1)


def click(x):
    global operand_1, operand_2, operator, is_equal, memory

    operations = {
        "CA": lambda x: x.operator == operator
    }

    if x == "CA":
        operand_1 = ""
        operand_2 = ""
        operator = ""
        display_var.set("")

    elif x == "CE":
        result = display_var.get()

        if operand_1 == result:
            operand_1 = ""
        elif operand_2 == result:
            operand_2 = ""
        else:
            operator = ""

        display_var.set("")

    elif x == "mc":
        memory = 0
        display_var.set("")
    elif x == "mr":
        display_var.set(str(memory))
    elif x == "m+":
        if operand_2:
            memory += float(operand_2)
        elif operand_1:
            memory += float(operand_1)
    elif x == "m-":
        if operand_2:
            memory -= float(operand_2)
        elif operand_1:
            memory -= float(operand_1)

    elif x == "fac":
        if not operator:
            operand_1 = str(factorial(int(operand_1)))
            display_var.set(operand_1)
        else:
            operand_2 = str(factorial(int(operand_2)))
            display_var.set(operand_2)

        if len(display_var.get()) > 19:
            display_var.set("overflow")

    elif x == "sqrt":
        result = math.sqrt(float(display_var.get()))
        result = int(result) if result.is_integer() else result

        if not operator:
            operand_1 = str(result)
            display_var.set(operand_1)
        else:
            operand_2 = str(result)
            display_var.set(operand_2)

    elif x == "+/-":
        if operand_1 and operand_2:
            result = float(operand_2) * (-1)
            result = int(result) if result.is_integer() else result
            operand_2 = str(result)
            display_var.set(operand_2)
        elif operand_1:
            result = float(operand_1) * (-1)
            result = int(result) if result.is_integer() else result
            operand_1 = str(result)
            display_var.set(operand_1)

    elif x in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
        if x == "." and display_var.get() == "":
            x = "0."
        if not operator:
            operand_1 += x
            display_var.set(operand_1)
        elif operator and not is_equal:
            operand_2 += x
            display_var.set(operand_2)

    elif x in ["*", "/", "+", "-"] and operand_1:
        if operator in ["*", "/", "+", "-"]:
            x = "="

        else:
            operator = x
            is_equal = False
            display_var.set(operator)

    if x == "=":
        result = 0
        if operator == "+":
            result = float(operand_1) + float(operand_2)
        elif operator == "-":
            result = float(operand_1) - float(operand_2)
        elif operator == "*":
            result = float(operand_1) * float(operand_2)
        elif operator == "/":
            try:
                result = float(operand_1) / float(operand_2)
            except ZeroDivisionError:
                result = 0

        if result.is_integer():
            result = int(result)

        operand_1 = str(result)
        operand_2 = ""
        operator = "="
        is_equal = True
        display_var.set(operand_1)


button_mc = tk.Button(root, text="mc", font=("Roboto", 11), command=lambda x="mc": click(x))
button_mc.grid(row=1, column=0, sticky="nswe")

button_m_add = tk.Button(root, text="m+", font=("Roboto", 11), command=lambda x="m+": click(x))
button_m_add.grid(row=1, column=1, sticky="nswe")

button_m_subtract = tk.Button(root, text="m-", font=("Roboto", 11), command=lambda x="m-": click(x))
button_m_subtract.grid(row=1, column=2, sticky="nswe")

button_mr = tk.Button(root, text="mr", font=("Roboto", 11), command=lambda x="mr": click(x))
button_mr.grid(row=1, column=3, sticky="nswe")

buttonCE = tk.Button(root, text="CE", font=("Roboto", 17), command=lambda x="CE": click(x))
buttonCE.grid(row=2, column=0, sticky="nswe")

buttonCA = tk.Button(root, text="CA", font=("Roboto", 17), command=lambda x="CA": click(x))
buttonCA.grid(row=2, column=1, sticky="nswe")

button_sqrt = tk.Button(root, text="sqrt", font=("Roboto", 17), command=lambda x="sqrt": click(x))
button_sqrt.grid(row=2, column=2, sticky="nswe")

button_fac = tk.Button(root, text="fac", font=("Roboto", 17), command=lambda x="fac": click(x))
button_fac.grid(row=2, column=3, sticky="nswe")

button_multiplication = tk.Button(root, text="*", font=("Roboto", 25), command=lambda x="*": click(x))
button_multiplication.grid(row=3, column=0, sticky="nswe")

button_division = tk.Button(root, text="/", font=("Roboto", 25), command=lambda x="/": click(x))
button_division.grid(row=3, column=1, sticky="nswe")

button_add = tk.Button(root, text="+", font=("Roboto", 25), command=lambda x="+": click(x))
button_add.grid(row=3, column=2, sticky="nswe")

button_subtract = tk.Button(root, text="-", font=("Roboto", 25), command=lambda x="-": click(x))
button_subtract.grid(row=3, column=3, sticky="nswe")

button7 = tk.Button(root, text="7", font=("Roboto", 25), command=lambda x="7": click(x))
button7.grid(row=4, column=0, sticky="nswe")

button8 = tk.Button(root, text="8", font=("Roboto", 25), command=lambda x="8": click(x))
button8.grid(row=4, column=1, sticky="nswe")

button9 = tk.Button(root, text="9", font=("Roboto", 25), command=lambda x="9": click(x))
button9.grid(row=4, column=2, sticky="nswe")

button4 = tk.Button(root, text="4", font=("Roboto", 25), command=lambda x="4": click(x))
button4.grid(row=5, column=0, sticky="nswe")

button5 = tk.Button(root, text="5", font=("Roboto", 25), command=lambda x="5": click(x))
button5.grid(row=5, column=1, sticky="nswe")

button6 = tk.Button(root, text="6", font=("Roboto", 25), command=lambda x="6": click(x))
button6.grid(row=5, column=2, sticky="nswe")

button1 = tk.Button(root, text="1", font=("Roboto", 25), command=lambda x="1": click(x))
button1.grid(row=6, column=0, sticky="nswe")

button2 = tk.Button(root, text="2", font=("Roboto", 25), command=lambda x="2": click(x))
button2.grid(row=6, column=1, sticky="nswe")

button3 = tk.Button(root, text="3", font=("Roboto", 25), command=lambda x="3": click(x))
button3.grid(row=6, column=2, sticky="nswe")

button_equal = tk.Button(root, text="=", font=("Roboto", 25), bg="orange", command=lambda x="=": click(x))
button_equal.grid(row=4, column=3, rowspan=4, sticky="nswe")

button_sign = tk.Button(root, text="+/-", font=("Roboto", 15), command=lambda x="+/-": click(x))
button_sign.grid(row=7, column=0, sticky="nswe")

button0 = tk.Button(root, text="0", font=("Roboto", 25), command=lambda x="0": click(x))
button0.grid(row=7, column=1, sticky="nswe")

button_decimal = tk.Button(root, text=".", font=("Roboto", 15), command=lambda x=".": click(x))
button_decimal.grid(row=7, column=2, sticky="nswe")

root.mainloop()
