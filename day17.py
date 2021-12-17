# https://adventofcode.com/2021/day/16

from utils import time_me, run_tests
from math import ceil
from itertools import product

test_pairs_part1 = [
    (((20, 30), (-10, -5)), 45),
]
test_pairs_part2 = [
    (((20, 30), (-10, -5)), 112),
]

def sum_natural_numbers(n):
    return (n * (n+1)) // 2

@time_me
def part1(area):
    y_range = area[1]
    ymin = min(y_range)
    return sum_natural_numbers(abs(ymin)-1)

def quad_formula(a, b, c):
    plus   = (-b + (b ** 2 - 4 * a * c) ** 0.5)
    minus  = (-b - (b ** 2 - 4 * a * c) ** 0.5)
    plus  /= (2 * a)
    minus /= (2 * a)
    return (plus, minus)

@time_me
def part2(area):
    xmax = max(area[0])
    ymax = abs(min(area[1]))
    y_range = (-1*ymax, ymax)
    xmin = ceil(max(quad_formula(1, 1, -1 * (min(area[0]) * 2))))
    x_range = (xmin, xmax)
    max_steps = (ymax*2) + 1
    valid_pairs = set()
    target_x = set(range(area[0][0], area[0][1]+1))
    target_y = set(range(area[1][0], area[1][1]+1))
    target_pairs = set(product(target_x, target_y))
    for x in range(x_range[0], x_range[1]+1):
        for y in range(y_range[0], y_range[1]+1):
            x_loc = 0
            y_loc = 0
            x_vel = x
            y_vel = y
            for _ in range(max_steps):
                x_loc += x_vel
                y_loc += y_vel
                if (x_loc, y_loc) in target_pairs:
                    valid_pairs.add((x, y))
                    break
                if x_vel > 0:
                    x_vel -= 1
                y_vel -= 1
    return len(valid_pairs)

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = ((48, 70), (-189, -148))
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
