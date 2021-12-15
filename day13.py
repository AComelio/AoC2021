# https://adventofcode.com/2021/day/13

from utils import time_me, run_tests, tokenise_input_file
from collections import deque

def input_2_grid_instr_pairs(in_str_pair):
    grid_str, instrs = in_str_pair
    grid = set()
    instructions = deque()
    for coord_str in grid_str.split('\n'):
        x, y = map(int, coord_str.split(','))
        grid.add((x,y))
    for instr in instrs.split('\n'):
        l, r = instr.split('=')
        r = int(r)
        if 'x' in l:
            instructions.append(('x', r))
        else:
            instructions.append(('y', r))
    return (grid, instructions)

example_input = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''
example_input = example_input.split('\n\n')
example_input = input_2_grid_instr_pairs(example_input)

test_pairs_part1 = [
    ((example_input[0], example_input[1].copy()), 17),
]

test_pairs_part2 = [
    ((example_input[0], example_input[1].copy()), None),
]

def print_grid(grid):
    xmin = min(x for x, _ in grid)
    xmax = max(x for x, _ in grid)
    ymin = min(y for _, y in grid)
    ymax = max(y for _, y in grid)
    for y in range(ymin, ymax+1):
        l = ''
        for x in range(xmin, xmax+1):
            if (x,y) in grid:
                l += '#'
            else:
                l += '.'
        print(l)

def fold_grid(grid, fold):
    new_grid = set()
    if fold[0] == 'y':
        for x, y in grid:
            if y > fold[1]:
                new_grid.add((x, fold[1] - (abs(fold[1] - y))))
            else:
                new_grid.add((x, y))
    else:
        for x, y in grid:
            if x > fold[1]:
                new_grid.add((fold[1] - (abs(fold[1] - x)), y))
            else:
                new_grid.add((x, y))
    return new_grid

def part1(vals):
    grid, instrs = vals
    fold1 = instrs.popleft()
    grid = fold_grid(grid, fold1)
    #print_grid(grid)
    return len(grid)

def part2(vals):
    grid, instrs = vals
    while instrs:
        fold = instrs.popleft()
        grid = fold_grid(grid, fold)
    print_grid(grid)

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day13_input.txt', seperator='\n\n')
    vals = input_2_grid_instr_pairs(vals)
    print(f'Part 1 answer: {part1((vals[0], vals[1].copy()))}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2((vals[0], vals[1].copy()))}')
