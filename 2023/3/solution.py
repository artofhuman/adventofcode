lines = open("input.txt").read().splitlines()

n = len(lines)
m = len(lines[0])

# cur (l=0, pos=0)
# (l=0, pos=-1)
# (l=0, pos=+1)
# (l=-1, pos=0)
# (l=+1, pos=0)
#
# (l=-1, pos=-1)
# (l=-1, pos=+1)
# (l=+1, pos=-1)
# (l=+1, pos=+1)
def has_symbol(l, pos):
    for i in range(l - 1, l + 2):
        for j in range(pos - 1, pos + 2):
            if (i < 0 or j < 0) or (i == l and j == pos) or (j > m - 1):
                continue

            try:
                if lines[i][j] != "." and not lines[i][j].isdigit():
                    return True, (i, j)
            except IndexError:
                continue
    return False, None


class CurrDigit:
    def __init__(self):
        self.chars = []
        self.has_symb = False
        self.gear_pos = []

    def __repr__(self):
        return f"{self.chars} {self.has_symb}"

    def to_int(self):
        return int("".join(self.chars))


# part1
cur = CurrDigit()
digits = []
ans = 0
for l, line in enumerate(lines):
    for pos, ch in enumerate(line):
        if ch.isdigit():
            res, coords = has_symbol(l, pos)
            cur.chars.append(ch)
            if res:
                cur.has_symb = True
                if lines[coords[0]][coords[1]] == "*":
                    cur.gear_pos = coords
        else:
            if cur.chars:
                if cur.has_symb:
                    digits.append(cur)
                    ans += cur.to_int()
            cur = CurrDigit()

print(ans)

# part2
from collections import defaultdict
from math import prod

res = defaultdict(list)
for d in digits:
    if d.gear_pos:
        res[d.gear_pos].append(d)

ans = 0
for ds in res.values():
    if len(ds) > 1:
        ans += prod(x.to_int() for x in ds)
print(ans)
