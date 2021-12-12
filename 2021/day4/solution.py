BOARDS = []

board = []
with open("input.txt") as f:
    nums = [int(i) for i in f.readline().split(",")]
    f.readline() # empty first

    for line in f.readlines():
        line = line.strip()
        if line:
            line_nums = [int(n) for n in line.split(" ") if n]
            board.append(line_nums)
            if len(board) == 5:
                BOARDS.append(board)
                board = []


def is_win_nums(row, nums):
    found = 0
    for _n in row:
        if _n in nums:
            found += 1
    return found == 5


def find_win_boards(nums):
    wins = []
    for board_i, board in enumerate(BOARDS):
        for row in board:
            if is_win_nums(row, nums):
                if board_i not in wins:
                    wins.append(board_i)

        for col_i in range(5):
            col = []
            for i in range(5):
                col.append(board[i][col_i])
            if is_win_nums(col, nums):
                wins.append(board_i)
    return wins


def calc_result(board, nums):
    sum_of_unsign = 0
    for row in board:
        for n in row:
            if n not in nums:
                sum_of_unsign += n
    return sum_of_unsign * nums[-1]


def get_bingo_nums():
    _nums = []
    for n in nums:
        _nums.append(n)
        if len(_nums) >= 5:
            yield _nums


def solve1():
    for bingo in get_bingo_nums():
        if winners := find_win_boards(bingo):
            return calc_result(BOARDS[winners[0]], bingo)


def solve2():
    wins = []
    win_num = None
    for bingo in get_bingo_nums():
        if winners := find_win_boards(bingo):
            for w in winners:
                if w not in wins:
                    wins.append(w)
                    win_num = bingo[:]

    return calc_result(BOARDS[wins[-1]], win_num)

print(solve1())
print(solve2())
