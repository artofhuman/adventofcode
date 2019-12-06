input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""


input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

lines = input.splitlines()
lines = open('input.txt').read().splitlines()

tree = {}

for line in lines:
    orb, next_orb = line.split(')')

    if orb not in tree:
        tree[orb] = []

    if next_orb not in tree:
        tree[next_orb] = []


    tree[orb].append(next_orb)



def find_prev(find_orb, acc = None):
    if acc is None:
        acc = []

    for orb, childs in tree.items():
        if find_orb in childs:
            acc.append(orb)
            find_prev(orb, acc)

    return acc

# prev = find_prev("L")

def part1():
    result = 0

    orbs = list(tree.keys())
    orbs.reverse()

    for orb in orbs:
        result += len(find_prev(orb))

    print(result)

# print(tree)


def part2():
    santa_path = find_prev('SAN')
    you_path = find_prev('YOU')

    for orb in you_path:
        if orb in santa_path:
            y = you_path[0:you_path.index(orb) + 1]
            s = santa_path[0:santa_path.index(orb) + 1]
            break

    res = set(y + s)
    print(len(res) - 1)

part2()
