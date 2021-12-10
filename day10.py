# https://adventofcode.com/2021/day/10

from utils import time_me, run_tests, tokenise_input_file
from collections import deque

example_input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''
example_input = example_input.split('\n')

test_pairs_part1 = [
    (example_input.copy(), 26397),
]
test_pairs_part2 = [
    (example_input.copy(), 288957),
]

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

scores_p2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

openers = {'(', '[', '{', '<'}

@time_me
def part1(lines):
    score = 0
    for line in lines:
        stack = deque()
        for c in line:
            if c in openers:
                stack.append(c)
            elif stack.pop() != pairs[c]:
                score += scores[c]
                break
    return score

@time_me
def part2(lines):
    scores = list()
    for line in lines:
        stack = deque()
        for c in line:
            if c in openers:
                stack.append(c)
            elif stack.pop() != pairs[c]:
                break
        else:
            score = 0
            while len(stack) > 0:
                score *= 5
                c = stack.pop()
                score += scores_p2[c]
            scores.append(score)
    scores.sort()
    return scores[len(scores)//2]

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day10_input.txt')
    print(f'Part 1 answer: {part1(vals.copy())}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals.copy())}')
