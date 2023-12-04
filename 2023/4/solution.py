import re

lines = open("input.txt").read().splitlines()

# part 1

def calc(count):
    sub = 0
    for i in range(count):
        if i == 0:
            sub = 1
        else:
            sub *= 2
    return sub


ans = 0
pattern = re.compile(r"Card *(\d+): *(\d+(?: *\d+)*) \| *(\d+(?: *\d+)*)")
matches = []
for i, line in enumerate(lines):
    match = pattern.search(line)

    wins = set(match[2].split())
    nums = set(match[3].split())
    count = len(nums & wins)

    ans += calc(count)
    matches.append(count)


print(ans)
# part 2

ans = 0
from collections import deque

q = deque()
for i in range(len(matches)):
    q.append(i + 1)

while q:
    ans += 1
    card = q.popleft()
    for k in range(card + 1, card + matches[card - 1] + 1):
        q.append(k)

print(ans)
