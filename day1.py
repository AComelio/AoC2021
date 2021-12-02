# https://adventofcode.com/2021/day/1

from utils import time_me, run_tests, tokenise_input_file

example_input = '''199
200
208
210
200
207
240
269
260
263'''
example_input = tuple(map(int, example_input.split('\n')))

test_pairs_part1 = [
    (example_input, 7),
]
test_pairs_part2 = [
    (example_input, 5),
]

#@time_me
def part1(vals):
    pairs = zip(vals[:-1], vals[1:])
    return sum([a < b for a, b in pairs])

@time_me
def part2(vals):
    triples_sums = [sum(triple) for triple in zip(vals[:-2], vals[1:-1], vals[2:])]
    return part1(triples_sums)

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day1_input.txt', func=int)
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
