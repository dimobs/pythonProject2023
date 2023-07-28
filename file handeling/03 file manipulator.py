import os
while True:
    command, *info = input().split('-')

    if command == 'Create':
        with open(f"files/{info[0]}", "w") as f:
            pass
    if command == 'Add':
        with open(f"files/{info[0]}", 'a') as f:
            f.write(f"files/{info[1]}\n")
    if command == 'Replace':
        try:
            with open(f"files/{info[0]}", "r+") as f:
                text = f.read()
                text = text.replace(info[1], info[2])
                f.seek(0)
                f.write(text)

        except FileNotFoundError:
            print(f"An error occurred")

    if command == 'Delete':
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print(f"An error occurred")

    if command == 'End':
        break