test_input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

input = list(map(int, open("data.txt")))

def part1(input: list):
    m = input[0]
    increased = 0

    for i in range(1, len(input)):
        if input[i] > m:
            increased += 1
        m = input[i]
    return increased

result = part1(input)

print("result1", result)

def part2(input):
    m = sum(input[0:3])
    result = 0

    for i in range(len(input)):
        if i > 0:
            res = sum(input[i:i+3])
            if res > m:
                result += 1
            m = res
    return result

result = part2(input)
print("result2", result)
