# dest range start, source range start, range lenght
# 50 98 2
# 52 50 48

# 98 -> 50
# 99 -> 51
import sys

lines = open("input.txt").readlines()


def to_int_list(values):
    return list(map(int, values))


seeds = to_int_list(lines[0].split(":")[-1].split())

maps = {}

for line in lines[2:]:
    if line[0] == "" or line[0] == "\n":
        continue

    if not line[0].isdigit():
        map_name = line.removesuffix(" map:\n")
        maps[map_name] = []
    else:
        values = to_int_list(line.split())
        maps[map_name].append(values)


def find_map(seed, map_name):
    value = seed
    for dst, src, count in maps[map_name]:
        in_range = src <= seed <= src + count
        if in_range:
            shift = dst - src
            value = seed + shift
            return value
    return value


ans = sys.maxsize
for seed in seeds:
    location = seed
    for map_name in maps:
        location = find_map(location, map_name)
    ans = min(ans, location)
print(ans)

# part 2
# rs.....rs+rl
     # ms.........ms+ml

# seeds_ranges = list(zip(seeds[::2], seeds[1::2]))


seeds_ranges = []

for i in range(0, len(seeds), 2):
    seeds_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))


new = []
for block in maps.values():
    # src, dst, l
    new = []
    while seeds_ranges:
        s, e = seeds_ranges.pop()
        for a, b, c in block:
            shift = b - a
            os = max(s, b)
            oe = min(e, b + c)

            if os < oe:
                new.append((os - shift, oe - shift))
                if os > s:
                    seeds_ranges.append((s, os))
                if e > oe:
                    seeds_ranges.append((oe, e))
                break
        else:
            new.append((s, e))
    seeds_ranges = new

print(sorted(seeds_ranges)[0])
