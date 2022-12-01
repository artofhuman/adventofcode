LINES = open("test_input.txt").read().splitlines()

POSITIONS = []

for line in LINES:
    POSITIONS.append(list(map(int, line)))


class Point:
    def __init__(self, right, down):
        self.right = right
        self.down = down

    @property
    def num(self):
        return POSITIONS[self.down][self.right]

    @property
    def next_right(self):
        if self.right < len(POSITIONS) - 1:
            return Point(self.right + 1, self.down)

    @property
    def next_down(self):
        if self.down < len(POSITIONS) - 1:
            return Point(self.right, self.down + 1)

    def __str__(self):
        return str(self.num)
        # if self.next_right:
        #     res += " "

        # return f"<{self.num} -> {self.next_right.num} ↓ {self.next_down.num}, [{self.right}, {self.down}], is_last: {self.is_last}>"

    def __repr__(self):
        return str(self)

    @property
    def is_last(self):
        return self.next_right is None and self.next_down is None

    def __lt__(self, other):
        return self.num < other.num

def go(point, score = 0):
    print(point)

    score += point.num

    if point.is_last:
        print(score)
        return score

    if point.right == 0 and point.down == 0:
        score_down = go(point.next_down, score)
        score_right = go(point.next_right, score)
    else:
        if point.next_right is None:
            return go(point.next_down, score)
        if point.next_down is None:
            return go(point.next_right, score)
        elif point.next_right > point.next_down:
            return go(point.next_down, score)
        else:
            return go(point.next_right, score)

go(Point(0, 0))
