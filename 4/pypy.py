def make_vertical(t):
    rows = len(t)
    columns = len(t[0])
    return ["".join([t[i][j] for i in range(rows)]) for j in range(0, columns)]


def make_left_diagonal(t):
    left_diagonal = []
    rows = len(t)
    columns = len(t[0])
    for j in range(0, columns):
        diagonal = []
        for it in range(0, min(j, rows - 1) + 1):
            c = t[rows - 1 - it][j - it]
            diagonal.append(c)
        left_diagonal.append(diagonal)
    for i in range(0, rows - 1):
        diagonal = []
        for it in range(0, min(i, columns - 1) + 1):
            c = t[i - it][columns - 1 - it]
            diagonal.append(c)
        left_diagonal.append(diagonal)
    return ["".join(line) for line in left_diagonal]


def make_right_diagonal(t):
    right_diagonal = []
    rows = len(t)
    columns = len(t[0])
    for j in range(0, columns):
        diagonal = []
        for it in range(0, min(columns - j - 1, rows - 1) + 1):
            c = t[rows - 1 - it][j + it]
            diagonal.append(c)
        right_diagonal.append(diagonal)
    for i in range(0, rows - 1):
        diagonal = []
        for it in range(0, min(i, columns) + 1):
            c = t[i - it][it]
            diagonal.append(c)
        right_diagonal.append(diagonal)
    return ["".join(line) for line in right_diagonal]


def count_xmas_ocurrences(input_file_path):
    with open(input_file_path, "r") as io:
        text = [line.strip() for line in io.readlines()]
        ans = 0
        horizontal = text
        vertical = make_vertical(text)
        left_diagonal_text = make_left_diagonal(text)
        right_diagonal_text = make_right_diagonal(text)

        for t in [horizontal, vertical, left_diagonal_text, right_diagonal_text]:
            for line in t:
                ans += line.count("XMAS") + line.count("SAMX")
        return ans


ans = count_xmas_ocurrences("puzzle-input.txt")
print(ans)
