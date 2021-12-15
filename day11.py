# https://adventofcode.com/2021/day/11

from utils import time_me, run_tests, tokenise_input_file, get_adjacent_coords
from collections import deque

def input_2_grid(str_input):
    grid = dict()
    for j, l in enumerate(str_input):
        for i, v in enumerate(l):
            grid[(i, j)] = int(v)
    return grid

example_input = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''
example_input = example_input.split('\n')
example_grid = input_2_grid(example_input)

test_pairs_part1 = [
    (example_grid.copy(), 1656),
]
test_pairs_part2 = [
    (example_grid.copy(), 195),
]

@time_me
def part1(grid):
    flashes = 0
    time_steps = 100
    for _ in range(time_steps):
        flashed = set()
        stack = deque()
        for coord in grid:
            grid[coord] += 1
            if grid[coord] > 9:
                stack.append(coord)
                flashed.add(coord)
        while stack:
            coord = stack.pop()
            adj = [c for c in get_adjacent_coords(coord) if c in grid]
            for c in adj:
                grid[c] += 1
                if grid[c] > 9 and c not in flashed:
                    stack.append(c)
                    flashed.add(c)
        for c in flashed:
            grid[c] = 0
        flashes += len(flashed)
    return flashes

@time_me
def part2(grid):
    all_flashed = False
    time_steps = 0
    while not all_flashed:
        time_steps += 1
        flashed = set()
        stack = deque()
        for coord in grid:
            grid[coord] += 1
            if grid[coord] > 9:
                stack.append(coord)
                flashed.add(coord)
        while stack:
            coord = stack.pop()
            adj = [c for c in get_adjacent_coords(coord) if c in grid]
            for c in adj:
                grid[c] += 1
                if grid[c] > 9 and c not in flashed:
                    stack.append(c)
                    flashed.add(c)
        for c in flashed:
            grid[c] = 0
        all_flashed = len(flashed) == len(grid)
    return time_steps

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day11_input.txt')
    grid = input_2_grid(vals)
    print(f'Part 1 answer: {part1(grid.copy())}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(grid.copy())}')