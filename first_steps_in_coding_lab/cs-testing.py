numbers_and_symbols = {'zero': 0,
                       'one': 1,
                       'two': 2,
                       'three': 3,
                       'four': 4,
                       'five': 5,
                       'six': 6,
                       'seven': 7,
                       'eight': 8,
                       'nine': 9,
                       'plus': '+',
                       'minus': '-',
                       }

nums_and_symbols = []

s = 'onezeropluseight'
# s = 'foursixminustwotwoplusonezero'
# s = 'oneminusoneone'
int_numbers = []

while s != '':
    for text, value in numbers_and_symbols.items():
        if s.startswith(text):
            s = s[len(text):]
            int_numbers.append(value)
            break

digit_and_symbol = []
find_current_num = ''
length = len(int_numbers) - 1
for i in range(len(int_numbers)):
    if isinstance(int_numbers[i], int):
        if i == length:
            find_current_num += str(int_numbers[i])
            digit_and_symbol.append(int(find_current_num))
            break
        else:
            find_current_num += str(int_numbers[i])
    else:
        digit_and_symbol.append(int(find_current_num))
        find_current_num = ''
        digit_and_symbol.append(int_numbers[i])

result = 0

for i in range(len(digit_and_symbol)):
    if i % 2 != 0:
        if i == 1:
            if digit_and_symbol[i] == '+':
                result += (digit_and_symbol[i - 1] + digit_and_symbol[i + 1])
            else:
                result += (digit_and_symbol[i - 1] - digit_and_symbol[i + 1])
        else:
            if digit_and_symbol[i] == '+':
                result += digit_and_symbol[i + 1]
            else:
                result -= digit_and_symbol[i + 1]

if result < 0:
    print('negative')
else:
    last_text = ''
    for digit in str(result):
        for key, value in numbers_and_symbols.items():
            if int(digit) == value:
                last_text += key
                break

    print(last_text)