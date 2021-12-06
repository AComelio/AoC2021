# https://adventofcode.com/2021/day/5

from utils import time_me, run_tests, tokenise_input_file
from collections import defaultdict

def prep_input(lines_strs):
    lines = list()
    for l in lines_strs:
        p1, p2 = l.split(' -> ')
        x1, y1 = map(int, p1.split(','))
        x2, y2 = map(int, p2.split(','))
        lines.append(
            (
                (x1, y1),
                (x2, y2)
            )
        )
    return lines

example_input = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''
example_input = example_input.split('\n')

test_pairs_part1 = [
    (prep_input(example_input), 5),
]
test_pairs_part2 = [
    (prep_input(example_input), 12),
]

def remove_diagonals(lines):
    lines = [l for l in lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]
    return lines

@time_me
def part1(lines):
    lines = remove_diagonals(lines)
    counts = defaultdict(int)
    for l in lines:
        (x1, y1), (x2, y2) = l
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                counts[(x, y)] += 1
    return len([v for v in counts.values() if v > 1])

@time_me
def part2(lines):
    #lines = remove_diagonals(lines)
    counts = defaultdict(int)
    for l in lines:
        (x1, y1), (x2, y2) = l
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    counts[(x, y)] += 1
        else:
            dx = 0
            dy = 0
            if x1 < x2:
                xmod = 1
            else:
                xmod = -1
            if y1 < y2:
                ymod = 1
            else:
                ymod = -1
            while x1 + dx != x2:
                counts[(x1 + dx, y1 + dy)] += 1
                dx += xmod
                dy += ymod
            counts[(x2, y2)] += 1
    return len([v for v in counts.values() if v > 1])

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day5_input.txt')
    lines = prep_input(vals)
    print(f'Part 1 answer: {part1(lines)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(lines)}')

