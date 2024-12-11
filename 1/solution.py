def calculate_total_distance(input_file_path):
    total_distance = 0
    left_values, right_values = [], []

    with open(input_file_path, 'r') as io:

        text = io.read().strip().split('\n')

        for row in text:
            pairs = row.split('   ')
            left_values.append(pairs[0])
            right_values.append(pairs[1])

        left_values.sort()
        right_values.sort()

        left_len, right_len = len(left_values), len(right_values)
        if left_len != right_len: raise Exception('Missing pairs')


        for i in range(left_len):
            left_value, right_value = int(left_values[i]), int(right_values[i])
            total_distance += abs(left_value - right_value)

        return total_distance

total_distance = calculate_total_distance('./puzzle-input.txt')
print(total_distance)
