# https://adventofcode.com/2021/day/2

from utils import time_me, run_tests, tokenise_input_file

example_input = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''
example_input = [(l.split(' ')[0].lower(), int(l.split(' ')[1])) for l in example_input.split('\n')]

test_pairs_part1 = [
    (example_input, 150),
]
test_pairs_part2 = [
    (example_input, 900),
]

@time_me
def part1(orders):
    loc = [0,0]
    for direction, distance in orders:
        if direction == 'forward': loc[0] += distance
        elif direction == 'down': loc[1] += distance
        elif direction == 'up': loc[1] -= distance
        elif direction == 'backward': loc[0] -= distance
        else: raise ValueError(f'Invalid direction {direction}')
    return loc[0] * loc[1]

@time_me
def part2(orders):
    params = {
        'x': 0,
        'y': 0,
        'aim': 0
    }
    for direction, distance in orders:
        if direction == 'forward':
            params['x'] += distance
            params['y'] += distance * params['aim']
        elif direction == 'backward':
            params['x'] -= distance
            params['y'] -= distance * params['aim']
        elif direction == 'up':
            params['aim'] -= distance
        elif direction == 'down':
            params['aim'] += distance
        else: raise ValueError(f'Invalid direction {direction}')
    return params['x'] * params['y']

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day2_input.txt')
    vals = [(l.split(' ')[0].lower(), int(l.split(' ')[1])) for l in vals]
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
