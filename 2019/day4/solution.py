import collections

rng = range(264793, 803935 + 1)

print(len(rng))


def part1():
    candidates = []

    for candidate in rng:
        digits = list(map(int, list(str(candidate))))

        is_valid = True
        has_pairs = False

        for i, d in enumerate(digits):
            if i != 5:
                next_d = digits[i + 1]
                if next_d < d:
                    is_valid = False
                    break

                if d == next_d:
                    has_pairs = True

        if is_valid and has_pairs:
            candidates.append(candidate)


    print('--Part1---')
    print(len(candidates))


def part2():
    candidates = []

    for candidate in rng:
        digits = list(map(int, list(str(candidate))))

        is_valid = True
        counter = None

        for i, d in enumerate(digits):
            if i != 5:
                next_d = digits[i + 1]
                if next_d < d:
                    is_valid = False
                    break

                if d == next_d:
                    counter = collections.Counter(digits)

        if not counter or 2 not in counter.values():
            continue

        if is_valid:
            candidates.append(candidate)

    print('--Part2---')
    for c in candidates:
        print(c)
    print(len(candidates))

part1()
part2()
