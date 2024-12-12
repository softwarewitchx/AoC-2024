from re import findall

def add_all_muls(input_file_path):

    pattern = r'mul\(\d{1,3},\d{1,3}\)'

    with open(input_file_path, 'r') as io:
        text = io.read().strip()
        matches = findall(pattern, text)
        matches_pairs = list(map(lambda match: match.strip('mul()').split(','), matches))
        matches_results = list(map(lambda pair: int(pair[0]) * int(pair[1]), matches_pairs))
        return sum(matches_results)

muls_sum = add_all_muls('./puzzle-input.txt')
print(muls_sum)
