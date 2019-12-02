import unittest
from typing import List
from operator import add, mul

OP_CODE_POS = 4

OPERATIONS = {
    1: add,
    2: mul,
}

def iterate(ints):
    for pos, i in enumerate(ints):
        if pos % OP_CODE_POS == 0:
            first_int_pos = pos + 1
            last_in_pos = pos + 3

            op_code = ints[pos]

            if op_code in OPERATIONS.keys():
                first_value = ints[ints[pos + 1]]
                last_value = ints[ints[pos + 2]]

                yield op_code, (first_value, last_value), ints[last_in_pos]

def process_memeory(ints):
    for op_code, values, replace_pos in iterate(ints):
        operation = OPERATIONS[op_code]
        ints[replace_pos] = operation(*values)

    return ints


def part1(ints):
    process_memeory(ints)
    return ints


class TestPart1(unittest.TestCase):
    def test_example(self):
        ints: List[int] = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

        result = part1(ints)

        self.assertEqual(result, expected)

    def test_1(self):
        result = part1([1, 0, 0, 0, 99])

        self.assertEqual(result, [2, 0, 0, 0, 99])

    def test_2(self):
        result = part1([2,3,0,3,99])

        self.assertEqual(result, [2,3,0,6,99])

    def test_3(self):
        result = part1([2,4,4,5,99,0])

        self.assertEqual(result, [2,4,4,5,99,9801])

    def test_5(self):
        result = part1([1,1,1,4,99,5,6,0,99])

        self.assertEqual(result, [30,1,1,4,2,5,6,0,99])


# unittest.main(verbosity=2)

ints = list(
    map(int, open("input.txt").read().split(','))
)

ints[1] = 12
ints[2] = 2

# print(part1(ints)[0])

def part2():
    find = 19690720
    noun = range(0, 100)
    verb = range(0, 100)

    for n in noun:
        for v in verb:
            ints[1] = n
            ints[2] = v

            _ints = list(ints)
            res = process_memeory(_ints)
            if res[0] == find:
                answer = 100 * n + v
                return answer

print(part2())
