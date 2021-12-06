# https://adventofcode.com/2021/day/4

from utils import time_me, run_tests, tokenise_input_file

example_input = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

example_input = example_input.split('\n\n')
example_nums = list(map(int, example_input[0].split(',')))
example_boards = list()
for str_board in example_input[1:]:
    board = [
        [
            [None, False], [None, False], [None, False], [None, False], [None, False]
        ],
        [
            [None, False], [None, False], [None, False], [None, False], [None, False]
        ],
        [
            [None, False], [None, False], [None, False], [None, False], [None, False]
        ],
        [
            [None, False], [None, False], [None, False], [None, False], [None, False]
        ],
        [
            [None, False], [None, False], [None, False], [None, False], [None, False]
        ]
            ]
    for j, line in enumerate(str_board.split('\n')):
        for i, value in enumerate(line.split()):
            board[i][j][0] = int(value)
    example_boards.append(board)

test_pairs_part1 = [
    ((example_nums, example_boards), 4512),
]
test_pairs_part2 = [
    ((example_nums, example_boards), 1924),
]

def check_board(board):
    verti_win = [True,] * 5
    for i in range(5):
        horiz_win = True
        for j in range(5):
            horiz_win = horiz_win and board[i][j][1]
            verti_win[j] = verti_win[j] and board[i][j][1]
        if horiz_win:
            return horiz_win
    return any(verti_win)

@time_me
def part1(val):
    nums, boards = val
    for num in nums:
        for board in boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j][0] == num:
                        board[i][j][1] = True
            if check_board(board):
                s = 0
                for i in range(5):
                    for j in range(5):
                        if not board[i][j][1]:
                            s += board[i][j][0]
                return s * num

@time_me
def part2(val):
    nums, boards = val
    l = -1
    last_board_won = False
    while len(boards) > 1 or not last_board_won:
        l += 1
        wins = [False,] * len(boards)
        num = nums[l]
        for p, board in enumerate(boards):
            for i in range(5):
                for j in range(5):
                    if board[i][j][0] == num:
                        board[i][j][1] = True
            wins[p] = check_board(board)
        if len(boards) > 1:
            boards = [board for board, win in zip(boards, wins) if not win]
        elif wins[0]:
            last_board_won = True
    board = boards[0]
    print(board)
    print(num)
    s = 0
    for i in range(5):
        for j in range(5):
            if not board[i][j][1]:
                s += board[i][j][0]
    return s * num

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('day4_input.txt', '\n\n')
    nums = list(map(int, vals[0].split(',')))
    boards = list()
    for str_board in vals[1:]:
        board = [
            [
                [None, False], [None, False], [None, False], [None, False], [None, False]
            ],
            [
                [None, False], [None, False], [None, False], [None, False], [None, False]
            ],
            [
                [None, False], [None, False], [None, False], [None, False], [None, False]
            ],
            [
                [None, False], [None, False], [None, False], [None, False], [None, False]
            ],
            [
                [None, False], [None, False], [None, False], [None, False], [None, False]
            ]
                ]
        for j, line in enumerate(str_board.split('\n')):
            for i, value in enumerate(line.split()):
                board[i][j][0] = int(value)
        boards.append(board)
    print(f'Part 1 answer: {part1((nums, boards))}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2((nums, boards))}')

