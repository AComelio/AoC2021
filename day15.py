# https://adventofcode.com/2021/day/15

from utils import time_me, run_tests, tokenise_input_file
from collections import deque
import networkx as nx

def input_2_grid(in_lines):
    grid = dict()
    for y, line in enumerate(in_lines):
        for x, c in enumerate(line):
            grid[(x+1,y+1)] = int(c)
    return grid

example_input = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''
example_input = example_input.split('\n')

test_pairs_part1 = [
    (input_2_grid(example_input), 40),
]
test_pairs_part2 = [
    (input_2_grid(example_input), 315),
]

def print_grid(grid):
    xmin = min(x for x, _ in grid)
    xmax = max(x for x, _ in grid)
    ymin = min(y for _, y in grid)
    ymax = max(y for _, y in grid)
    for y in range(ymin, ymax+1):
        l = ''
        for x in range(xmin, xmax+1):
            if (x, y) in grid:
                l += str(grid[(x,y)])
            else:
                l += '.'
        print(l)

@time_me
def part1(grid):
    G = nx.DiGraph()
    for coord in grid:
        x, y = coord
        l = (x-1, y)
        r = (x+1, y)
        u = (x, y-1)
        d = (x, y+1)
        for n in {l, r, u, d}:
            if n in grid:
                G.add_edge(coord, n, weight=grid[n])
    start = (1,1)
    end = (max(x for x, y in grid), max(y for x, y in grid))
    route = nx.shortest_path(G, source=start, target=end, weight='weight')
    return sum(grid[n] for n in route) - grid[start]

@time_me
def part2(grid):
    start = (1,1)
    xmax, ymax = (max(x for x, y in grid), max(y for x, y in grid))
    big_grid = dict()
    for xm in range(5):
        for ym in range(5):
            for coord in grid:
                x, y = coord
                v = grid[coord] + xm + ym
                while v > 9:
                    v -= 9
                big_grid[(x+(xmax*xm), y+(ymax*ym))] = v
    grid = big_grid
    #print_grid(grid)
    end = (max(x for x, y in grid), max(y for x, y in grid))
    G = nx.DiGraph()
    for coord in grid:
        x, y = coord
        l = (x-1, y)
        r = (x+1, y)
        u = (x, y-1)
        d = (x, y+1)
        for n in {l, r, u, d}:
            if n in grid:
                G.add_edge(coord, n, weight=grid[n])
    route = nx.shortest_path(G, source=start, target=end, weight='weight')
    return sum(grid[n] for n in route) - grid[start]

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day15_input.txt')
    print(f'Part 1 answer: {part1(input_2_grid(vals))}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(input_2_grid(vals))}')
