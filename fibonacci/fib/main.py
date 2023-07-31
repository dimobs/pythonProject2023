def create_seq(count):
    nums = []

    if count == 1:
        nums.append(0)
    if count == 2:
        nums.append([0, 1])
    else:
        nums = [0, 1]
        for num in range(2, count):
            next_num = nums[-1] + nums[-2]
            nums.append(next_num)

    return nums

def locate_num(num, seq):
    try:
        index = seq.index(num)
        return f"The number - {num} is at index {index}"
    except ValueError:
        return "The number {num} is not in the sequence"
