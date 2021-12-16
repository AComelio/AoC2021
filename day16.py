# https://adventofcode.com/2021/day/16

from utils import time_me, run_tests, tokenise_input_file
from collections import deque
from math import prod

e1 = '8A004A801A8002F478'
e2 = '620080001611562C8802118E34'
e3 = 'C0015000016115A2E0802F182340'
e4 = 'A0016C880162017C3686B18A3D4780'

test_pairs_part1 = [
    #('D2FE28', None),
    (e1, 16),
    (e2, 12),
    (e3, 23),
    (e4, 31)
]
test_pairs_part2 = [
    ('C200B40A82', 3),
    ('04005AC33890', 54),
    ('880086C3E88112', 7),
    ('CE00C43D881120', 9),
    ('D8005AC2A8F0', 1),
    ('F600BC2D8F', 0),
    ('9C005AC2F8F0', 0),
    ('9C0141080250320F1802104A08', 1)
]

int2 = lambda x: int(x, 2)

code_funcs = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    4: lambda l: l[0],
    5: lambda l: int(l[0] > l[1]),
    6: lambda l: int(l[0] < l[1]),
    7: lambda l: int(l[0] == l[1]),
}

@time_me
def part1(hex_str):
    bin_str = bin(int(hex_str, 16))[2:]
    missing_0s = (len(hex_str) * 4) - len(bin_str)
    for _ in range(missing_0s):
        bin_str = '0' + bin_str
    loc = 0
    total = 0
    while len(bin_str) - loc > 11:
        header = bin_str[loc: loc+6]
        ver, type_id = int2(header[:3]), int2(header[3:])
        loc += 6
        if type_id == 4:
            block = bin_str[loc: loc+5]
            literal = block[1:]
            loc += 5
            while block[0] == '1':
                block = bin_str[loc: loc+5]
                literal += block[1:]
                loc += 5
            val = int2(literal)
        else:
            I = bin_str[loc]
            loc += 1
            if I == '0':
                length = int2(bin_str[loc: loc+15])
                loc += 15
            else:
                subpackets = int2(bin_str[loc: loc+11])
                loc += 11
        total += ver
    return total

@time_me
def part2(hex_str):
    bin_str = bin(int(hex_str, 16))[2:]
    missing_0s = (len(hex_str) * 4) - len(bin_str)
    for _ in range(missing_0s):
        bin_str = '0' + bin_str
    loc = 0
    packets = deque()
    while len(bin_str) - loc > 10:
        header = bin_str[loc: loc+6]
        ver, type_id = int2(header[:3]), int2(header[3:])
        start_loc = loc
        loc += 6
        if type_id == 4:
            block = bin_str[loc: loc+5]
            literal = block[1:]
            loc += 5
            while block[0] == '1':
                block = bin_str[loc: loc+5]
                literal += block[1:]
                loc += 5
            val = int2(literal)
            packets.append({
                'Type': 4,
                'Value': val,
                'Length': loc - start_loc
            })
        else:
            I = bin_str[loc]
            loc += 1
            if I == '0':
                length = int2(bin_str[loc: loc+15])
                loc += 15
                packets.append({
                    'Type': type_id,
                    'Length': length + (loc - start_loc)
                })
            else:
                subpackets = int2(bin_str[loc: loc+11])
                loc += 11
                packets.append({
                    'Type': type_id,
                    'args': subpackets
                })
    stack = deque()
    while packets:
        v = packets.pop()
        if v['Type'] == 4:
            stack.append(v)
        elif 'Length' in v:
            args = list()
            args_length = 0
            while args_length < v['Length'] - 22:
                nv = stack.pop()
                args.append(nv['Value'])
                args_length += nv['Length']
            stack.append({
                'Type': 4,
                'Value': code_funcs[v['Type']](args),
                'Length': v['Length']
            })
        else:
            args = list()
            args_length = 0
            for _ in range(v['args']):
                nv = stack.pop()
                args.append(nv['Value'])
                args_length += nv['Length']
            stack.append({
                'Type': 4,
                'Value': code_funcs[v['Type']](args),
                'Length': args_length + 18
            })
    return stack.pop()['Value']

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day16_input.txt')
    print(f'Part 1 answer: {part1(vals[0])}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals[0])}')
