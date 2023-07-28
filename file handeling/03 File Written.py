import os


root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, "My_first_file.txt")

print(root_dir, file_path)
with open(file_path, "a") as file:
    file.write('I Just created my first file!\n')
