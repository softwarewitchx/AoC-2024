def is_valid(numbers):
    if len(numbers) != 2:
        return False
    for number in numbers:
        if not number.isdigit():
            return False
        if len(number) > 3:
            return False
    return True


def add_all_muls(input_file_path):
    with open(input_file_path, "r") as io:
        text = io.read().strip()
        pos = -1
        s = 0
        while True:
            start_pos = text.find("mul(", pos + 1)
            if start_pos == -1:
                break
            end_pos = text.find(")", start_pos + 1)
            pos = start_pos
            expression = text[start_pos : end_pos + 1]
            numbers = expression.replace("mul(", "").replace(")", "").split(",")
            if is_valid(numbers):
                s += int(numbers[0]) * int(numbers[1])
        return s


muls_sum = add_all_muls("puzzle-input.txt")
print(muls_sum)
