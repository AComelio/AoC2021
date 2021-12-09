# https://adventofcode.com/2021/day/9

from utils import time_me, run_tests, tokenise_input_file
from collections import deque
import math

example_input = '''2199943210
3987894921
9856789892
8767896789
9899965678'''
example_input = example_input.split('\n')
example_grid = dict()
for y, l in enumerate(example_input):
    for x, height in enumerate(l):
        example_grid[(x,y)] = int(height)

test_pairs_part1 = [
    (example_grid.copy(), 15),
]
test_pairs_part2 = [
    (example_grid.copy(), 1134),
]

@time_me
def part1(grid):
    risk_total = 0
    sorted_locs = [loc for loc in sorted(grid, key=lambda n: grid[n])]
    i = 0
    while i < len(sorted_locs):
        x, y = sorted_locs[i]
        adj_coords = {
            (x+1, y),
            (x, y+1),
            (x-1, y),
            (x, y-1)
        }
        adj_coords = {adj for adj in adj_coords if adj in grid}
        if all(grid[(x,y)] < grid[adj] for adj in adj_coords):
            risk_total += 1 + grid[(x,y)]
            for adj in adj_coords:
                sorted_locs.remove(adj)
        i += 1
    return risk_total

@time_me
def part2(grid):
    basin_sizes = list()
    sorted_locs = [loc for loc in sorted(grid, key=lambda n: grid[n])]
    i = 0
    while i < len(sorted_locs):
        x, y = sorted_locs[i]
        adj_coords = {
            (x+1, y),
            (x, y+1),
            (x-1, y),
            (x, y-1)
        }
        adj_coords = {adj for adj in adj_coords if adj in grid}
        if all(grid[(x,y)] < grid[adj] for adj in adj_coords):
            basin = {(x,y),}
            to_check = deque()
            for adj in adj_coords:
                sorted_locs.remove(adj)
                if grid[adj] != 9:
                    to_check.append(adj)
            while len(to_check) > 0:
                l = to_check.pop()
                basin.add(l)
                x, y = l
                adj_coords = {
                    (x+1, y),
                    (x, y+1),
                    (x-1, y),
                    (x, y-1)
                }
                adj_coords = {adj for adj in adj_coords if adj in grid}
                for adj in adj_coords:
                    if adj not in basin and adj not in to_check and grid[adj] != 9 and grid[adj] > grid[l]:
                        to_check.append(adj)
            basin_sizes.append(len(basin))
        i += 1
    return math.prod(sorted(basin_sizes, reverse=True)[:3])

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day9_input.txt')
    grid = dict()
    for y, l in enumerate(vals):
        for x, height in enumerate(l):
            grid[(x,y)] = int(height)
    print(f'Part 1 answer: {part1(grid.copy())}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(grid.copy())}')

