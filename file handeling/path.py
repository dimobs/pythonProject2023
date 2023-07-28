import os

file_names = "numbers.txt" 

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, file_names)

try:
    file = open(file_path, 'r')
    content_lines = file.read().split('\n')
    number = [int(x) for x in content_lines if x]

    print(sum(number))
except FileNotFoundError:
    print("File not found")

