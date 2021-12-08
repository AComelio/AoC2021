# https://adventofcode.com/2021/day/8

from utils import time_me, run_tests, tokenise_input_file

example_input = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''
example_input = example_input.split('\n')
p1_example = list()
for l in example_input:
    p1_example.append(l.split(' | ')[1])

test_pairs_part1 = [
    (p1_example.copy(), 26),
]
test_pairs_part2 = [
    (example_input.copy(), 61229),
]

nums = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

@time_me
def part1(lines):
    count = 0
    for l in lines:
        for num in l.split(' '):
            count += len(num) in {len(nums[1]), len(nums[4]), len(nums[7]), len(nums[8])}
    return count

@time_me
def part2(lines):
    total = 0
    scrambled_nums = set(num for l in lines for num in l.replace(' | ', ' ').split(' '))
    for l in lines:
        scrambled_nums = set(''.join(sorted(num)) for num in l.replace(' | ', ' ').split(' '))

        one_s = set({n for n in scrambled_nums if len(n) == 2}.pop())
        seven_s = set({n for n in scrambled_nums if len(n) == 3}.pop())
        four_s = set({n for n in scrambled_nums if len(n) == 4}.pop())
        eight_s = set({n for n in scrambled_nums if len(n) == 7}.pop())

        cf = one_s
        bd = four_s - cf
        eg = (eight_s - seven_s) - bd
        a = set(seven_s) - cf

        len_5 = {n for n in scrambled_nums if len(n) == 5}
        three_s = set([n for n in len_5 if len(set(n) - cf) == 3][0])
        two_s = set([n for n in len_5 if len((set(n) - three_s) & eg) == 1][0])
        five_s = set([n for n in len_5 if len((set(n) - three_s) & bd) == 1][0])

        len_6 = {n for n in scrambled_nums if len(n) == 6}
        nine_s = set([n for n in len_6 if len(set(n) - three_s) == 1][0])
        six_s = set([n for n in len_6 if len(set(n) - seven_s) == 4][0])
        zero_s = set([n for n in len_6 if set(n) != nine_s and set(n) != six_s][0])

        mapping = {
            ''.join(sorted(zero_s)): '0',
            ''.join(sorted(one_s)): '1',
            ''.join(sorted(two_s)): '2',
            ''.join(sorted(three_s)): '3',
            ''.join(sorted(four_s)): '4',
            ''.join(sorted(five_s)): '5',
            ''.join(sorted(six_s)): '6',
            ''.join(sorted(seven_s)): '7',
            ''.join(sorted(eight_s)): '8',
            ''.join(sorted(nine_s)): '9',
        }
        total += int(''.join([mapping[n] for n in [''.join(sorted(num)) for num in l.split(' | ')[1].split(' ')]]))
    return total

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day8_input.txt', seperator='\n')
    p1_input = list()
    for l in vals:
        p1_input.append(l.split(' | ')[1])
    print(f'Part 1 answer: {part1(p1_input.copy())}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals.copy())}')
