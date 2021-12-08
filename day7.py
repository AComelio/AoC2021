# https://adventofcode.com/2021/day/7

from utils import time_me, run_tests, tokenise_input_file

example_input = '16,1,2,0,4,2,7,1,2,14'
example_input = list(map(int, example_input.split(',')))

test_pairs_part1 = [
    (example_input.copy(), 37),
]
test_pairs_part2 = [
    (example_input.copy(), 168),
]

@time_me
def part1(postions):
    minx = min(postions)
    maxx = max(postions)
    pos_costs = dict()
    for potention_position in range(minx, maxx+1):
        total_dist = sum([abs(p - potention_position) for p in postions])
        pos_costs[potention_position] = total_dist
    return min(pos_costs.values())

@time_me
def part2(postions):
    minx = min(postions)
    maxx = max(postions)
    pos_costs = dict()
    for potention_position in range(minx, maxx+1):
        total_dist = sum([(abs(p - potention_position) * (abs(p - potention_position) + 1)) / 2 for p in postions])
        pos_costs[potention_position] = total_dist
    return min(pos_costs.values())

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day7_input.txt', seperator=',', func=int)
    print(f'Part 1 answer: {part1(vals.copy())}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals.copy())}')
