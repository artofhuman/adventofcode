from collections import defaultdict


with open("test_input.txt") as f:
    test_input = f.read().splitlines()

# with open("input.txt") as f:
#     test_input = f.read().splitlines()

def get_cord(char):
    x1, y1 = char.split(",")
    return (int(x1), int(y1))

overlaps = defaultdict(int)

def sign(x):
    if x == 0:
        return 0
    return -1 if x < 0 else 1


def make_range(c1, c2):
    return range(c1, c2 + 1) if c2 >= c1 else range(c2, c1 + 1)


max_x = 0
for line in test_input:
    c1, c2 = line.split(" -> ")
    x1, y1 = get_cord(c1)
    x2, y2 = get_cord(c2)

    if x1 > max_x:
        max_x = x1

    x_inc = sign(x2 - x1)
    y_inc = sign(y2 - y1)

    if x1 == x2:
        while y1 != y2 + y_inc:
            overlaps[(x1, y1)] += 1
            y1 += y_inc
    elif y1 == y2:
        while x1 != x2 + x_inc:
            overlaps[(x1, y1)] += 1
            x1 += x_inc
    else: # + part 2
        while x1 != x2 + x_inc or y1 != y2 + y_inc:
            overlaps[(x1, y1)] += 1
            x1 += x_inc
            y1 += y_inc

result = 0
for i in overlaps.values():
    if i > 1:
        result += 1

# show for test input (do not try for real input =))
for x in range(max_x + 1):
    for y in range(max_x + 1):
        if overlaps[(x, y)] > 0:
            print(overlaps[(x, y)], end=" ")
        else:
            print(".", end=" ")
        if y == max_x:
            print("")

print(result)
