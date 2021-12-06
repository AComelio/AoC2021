# https://adventofcode.com/2021/day/6

from utils import time_me, run_tests, tokenise_input_file
from collections import defaultdict

example_input = '3,4,3,1,2'
example_input = list(map(int, example_input.split(',')))

test_pairs_part1 = [
    (example_input.copy(), 5934),
]
test_pairs_part2 = [
    (example_input.copy(), 26984457539),
]

@time_me
def part1(fish):
    for _ in range(80):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
    return len(fish)

@time_me
def part2(fish):
    counts = defaultdict(int)
    for i in range(9):
        counts[i] = fish.count(i)
    for _ in range(256):
        new_counts = defaultdict(int)
        for age, num in counts.items():
            if age > 0:
                new_counts[age-1] += num
            else:
                new_counts[6] += num
                new_counts[8] += num
        counts = new_counts
    return sum(counts.values())

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day6_input.txt', seperator=',', func=int)
    print(f'Part 1 answer: {part1(vals.copy())}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals.copy())}')
