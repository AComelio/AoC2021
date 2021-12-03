# https://adventofcode.com/2021/day/3

from utils import time_me, run_tests, tokenise_input_file

example_input = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
example_input = example_input.split('\n')

test_pairs_part1 = [
    (example_input, 198),
]
test_pairs_part2 = [
    (example_input, 230),
]

def get_counts(num_strs):
    counts = [0,] * len(num_strs[0])
    for num_str in num_strs:
        for i, c in enumerate(num_str):
            counts[i] += int(c)
    return counts

@time_me
def part1(num_strs):
    total_nums = len(num_strs)
    threshhold = total_nums / 2
    counts = get_counts(num_strs)
    gamma = ''
    epsilon = ''
    for count in counts:
        if count >= threshhold:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)
    return gamma * epsilon

@time_me
def part2(num_strs):
    oxygen_strs = num_strs.copy()
    co2_strs = num_strs.copy()
    i = 0
    while len(oxygen_strs) > 1:
        total_nums = len(oxygen_strs)
        threshhold = total_nums / 2
        counts = get_counts(oxygen_strs)
        if counts[i] >= threshhold:
            oxygen_strs = [s for s in oxygen_strs if s[i] == '1']
        else:
            oxygen_strs = [s for s in oxygen_strs if s[i] == '0']
        i += 1
    i = 0
    while len(co2_strs) > 1:
        total_nums = len(co2_strs)
        threshhold = total_nums / 2
        counts = get_counts(co2_strs)
        if counts[i] >= threshhold:
            co2_strs = [s for s in co2_strs if s[i] == '0']
        else:
            co2_strs = [s for s in co2_strs if s[i] == '1']
        i += 1
    return int(oxygen_strs[0], base=2) * int(co2_strs[0], base=2)

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day3_input.txt')
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
