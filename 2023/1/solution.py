import re

lines = open("input.txt").readlines()
part1 = 0
for l in lines:
    match = re.findall(r'\d', l)
    val1 = int(match[0])
    val2 = int(match[-1])
    part1 += val1 * 10 + val2

print(part1)

_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

ans = 0
for li in lines:
    curr = ""
    nums = []

    for i, ch in enumerate(li):
        curr += ch
        if any(_ch.isdigit() for _ch in curr):
            nums.append(int(li[i]))
            curr = ""
            continue
        else:
            for w in _map.keys():
                if w in curr:
                    nums.append(_map[w])
                    curr = li[i]
                    continue

    val1 = nums[0]
    val2 = nums[-1]
    ans += val1 * 10 + val2

print(ans)
