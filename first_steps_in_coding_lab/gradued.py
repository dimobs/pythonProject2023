average_point = 0
name = input()
class_number = 0
sum = 0
negative_score = 0


while True:
    class_number += 1
    score = float(input())
    if score < 4:
        negative_score += 1
        if negative_score == 2:
            print(f'{name} has been excluded at {class_number - 1} grade')
            break
    else:
        sum += score

        if class_number == 12:
            average_point = sum / class_number
            print(f'{name} graduated. Average grade: {average_point:.2f}')
            break