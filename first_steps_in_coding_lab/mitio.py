text = 'foursixminustwotwoplusonezeroplusfour'
new_text = ""

num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
            "nine": "9", "zero": "0", "plus": "+", "minus": "-"}

for k, v in num_dict.items():
    new_text = text.replace(k, v)
    text = new_text

splited_text = new_text.split("+")
expresion = []
for sub_text in splited_text:
    if "-" in sub_text:
        sub_text = sub_text.split("-")
        expresion.append(sub_text[0])
        expresion.append(f"-{sub_text[1]}")
    else:
        expresion.append(sub_text)

expresion = [int(num) for num in expresion]
total_sum = sum(expresion)
total_sum_as_string = str(total_sum)

result = ""
for k, v in num_dict.items():
    result = total_sum_as_string.replace(v, k)
    total_sum_as_string = result

if "minus" in result:
    print(result.replace("minus", "negative"))
else:
    print(result)