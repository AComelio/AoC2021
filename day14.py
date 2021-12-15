# https://adventofcode.com/2021/day/14

from utils import time_me, run_tests, tokenise_input_file
from collections import Counter

def pairwise(in_str):
    ret = list()
    for l, r in zip(in_str[:-1], in_str[1:]):
        ret.append(l+r)
    return ret

def input_2_init_rules_pairs(in_str_pair):
    start_str, rules_str = in_str_pair
    rules = dict()
    for rule in rules_str.split('\n'):
        l, r = rule.split(' -> ')
        rules[l] = r
    pairs_counts = Counter(pairwise(start_str))
    return pairs_counts, rules, start_str

example_input = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''
example_input = example_input.split('\n\n')

test_pairs_part1 = [
    ((*input_2_init_rules_pairs(example_input), 10), 1588),
]

test_pairs_part2 = [
    ((*input_2_init_rules_pairs(example_input), 40), 2188189693529),
]

@time_me
def part1(vals):
    pair_counts, rules, raw, steps = vals
    char_counts = Counter(raw)
    for _ in range(steps):
        new_pair_counts = Counter(pair_counts)
        for pair in pair_counts:
            if pair not in rules:
                continue
            count = pair_counts[pair]
            lp = pair[0] + rules[pair]
            rp = rules[pair] + pair[1]
            new_pair_counts[lp] += count
            new_pair_counts[rp] += count
            new_pair_counts[pair] -= count
            char_counts[rules[pair]] += count 
        pair_counts = new_pair_counts
    return max(char_counts.values()) - min(char_counts.values())

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day14_input.txt', seperator='\n\n')
    print(f'Part 1 answer: {part1((*input_2_init_rules_pairs(vals), 10))}')
    print()
    run_tests(part1, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part1((*input_2_init_rules_pairs(vals), 40))}')