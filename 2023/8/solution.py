import re
from dataclasses import dataclass

lines = open("input.txt").read().splitlines()

@dataclass
class Node:
    value: str
    left: str
    right: str


path = lines[0]
unparsed_nodes = list(filter(lambda x: len(x), lines[1:]))

_r = re.compile(r"^(\S+) = \((\S+), (\S+)\)")

nodes = {}

for l in unparsed_nodes:
    parsed_node = _r.search(l)
    value = parsed_node[1]
    left = parsed_node[2]
    right = parsed_node[3]
    node = Node(value, left, right)
    nodes[value] = node

def get_next_node(cur, w):
    if w == "R":
        return nodes[cur.right]
    return nodes[cur.left]


def go():
    i = 0
    while True:
        w = path[i]

        yield w

        i += 1
        if i == len(path):
            i = 0

# part1
START = "AAA"
END = "ZZZ"
ans = 0
cur = nodes[START]
i = 0

for w in go():
    cur = get_next_node(cur, w)
    ans += 1
    print(w, cur)
    if cur.value == END:
        break

print(ans)


# part 2
# not working naive
# ans = 0
# cur_nodes = list(filter(lambda n: n.value.endswith("A"), nodes.values()))

# i = 0
# while True:
#     w = path[i]

#     for _n in range(len(cur_nodes)):
#         cur_node = cur_nodes[_n]
#         next_node = get_next_node(cur_node, w)
#         cur_nodes[_n] = next_node

#     ans += 1
#     if all(nn.value.endswith("Z") for nn in cur_nodes):
#         break

#     i += 1
#     if i == len(path):
#         i = 0

# print(ans)
