# https://adventofcode.com/2021/day/12

from utils import time_me, run_tests, tokenise_input_file
from collections import defaultdict, deque

def input_2_network(lines):
    network = defaultdict(list)
    for line in lines:
        l, r = line.split('-')
        network[l].append(r)
        network[r].append(l)
    return network

example_input_1 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''
example_input_1 = example_input_1.split('\n')
example_network_1 = input_2_network(example_input_1)

example_input_2 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''
example_input_2 = example_input_2.split('\n')
example_network_2 = input_2_network(example_input_2)

example_input_3 = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''
example_input_3 = example_input_3.split('\n')
example_network_3 = input_2_network(example_input_3)

test_pairs_part1 = [
    (example_network_1.copy(), 10),
    (example_network_2.copy(), 19),
    (example_network_3.copy(), 226)
]
test_pairs_part2 = [
    (example_network_1.copy(), 36),
    (example_network_2.copy(), 103),
    (example_network_3.copy(), 3509)
]

@time_me
def part1(network):
    routes = deque()
    stack = deque()
    l1 = {
        'loc': 'start',
        'route': ['start',]
    }
    stack.append(l1)
    while stack:
        info = stack.pop()
        visited = set(info['route'])
        valid_nodes = deque()
        for node in network[info['loc']]:
            if node.isupper() or node not in visited:
                valid_nodes.append(node)
        while valid_nodes:
            node = valid_nodes.pop()
            new_info = {
                'loc': node,
                'route': info['route'].copy()
            }
            new_info['route'].append(node)
            if node == 'end':
                routes.append(new_info['route'])
            else:
                stack.append(new_info)
    return len(routes)

@time_me
def part2(network):
    routes = deque()
    stack = deque()
    l1 = {
        'loc': 'start',
        'route': ['start',],
        'double_done': False
    }
    stack.append(l1)
    while stack:
        info = stack.pop()
        visited = set(info['route'])
        valid_nodes = deque()
        for node in network[info['loc']]:
            if node != 'start' and (node.isupper() or not info['double_done'] or node not in visited):
                valid_nodes.append(node)
        while valid_nodes:
            node = valid_nodes.pop()
            new_info = {
                'loc': node,
                'route': info['route'].copy(),
                'double_done': info['double_done']
            }
            new_info['route'].append(node)
            if not info['double_done']:
                new_info['double_done'] = node.islower() and node in visited
            if node == 'end':
                routes.append(new_info['route'])
            else:
                stack.append(new_info)
    return len(routes)

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day12_input.txt')
    network = input_2_network(vals)
    print(f'Part 1 answer: {part1(network.copy())}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(network.copy())}')