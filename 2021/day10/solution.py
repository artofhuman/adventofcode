SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


LINES = open("input.txt").read().splitlines()

BRACKETS = { ")": "(", "]": "[",  "}": "{", ">": "<" }


def error_in_line(line):
    brackets_stack = []
    for ch in line:
        if ch in BRACKETS.values():
            brackets_stack.append(ch)
        else:
            last_open_bracket = brackets_stack.pop()
            if BRACKETS[ch] != last_open_bracket:
                return ch
    return "".join(brackets_stack)


PART2_SCORES = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def solve1():
    score = 0
    errors = []

    for line in LINES:
        if error := error_in_line(line):
            if len(error) == 1:
                score += SCORES[error]
            errors.append(error)

    return score


def solve2():
    scores = []

    for line in LINES:
        score = 0
        if error := error_in_line(line):
            if len(error) > 1:
                for ch in reversed(error):
                    score *= 5
                    score += PART2_SCORES[ch]
                scores.append(score)

    return sorted(scores)[int(len(scores) / 2)]


print(solve1())
print(solve2())
