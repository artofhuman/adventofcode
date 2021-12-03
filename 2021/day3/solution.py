from collections import defaultdict

# TODO: to utils
def get_lines(file_name: str) -> list[str]:
    with open(file_name) as f:
        return list(map(lambda l: l.strip(), f.readlines()))

numbers = get_lines("input.txt")


def get_counts(numbers, bit):
    counts = defaultdict(int)
    for line_i in range(len(numbers)):
        b = numbers[line_i][bit]
        counts[b] += 1
    return counts


def part1(numbers):
    gamma = []
    epsilon = []

    for i in range(len(numbers[0])):
        counts = get_counts(numbers, i)
        most_common_b = get_most_common(counts)
        less_common = get_less_common(counts)
        gamma.append(most_common_b)
        epsilon.append(less_common)

    gamma = int("".join(gamma), 2)
    epsilon = int("".join(epsilon), 2)

    print(gamma * epsilon)


def get_most_common(counts):
    return '1' if counts['1'] >= counts['0'] else '0'


def get_less_common(counts):
    return '0' if counts['0'] <= counts['1'] else '1'


def _filter(nums, get_bit_func):
    for i in range(len(nums[0])):
        counts = get_counts(nums, i)
        bit = get_bit_func(counts)
        if len(nums) > 1:
            nums = list(filter(lambda line: line[i] == bit, nums))
    return nums[0]


def part2(numbers):
    co2 = _filter(numbers[:], get_most_common)
    rating = _filter(numbers[:], get_less_common)

    print(int(co2, 2) * int(rating, 2))

part1(numbers)
part2(numbers)
