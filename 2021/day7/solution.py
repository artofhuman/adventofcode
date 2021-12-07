from collections import defaultdict


nums = [int(n) for n in open('input.txt').read().split(',')]

def cost(n):
    return int(((1 + n) / 2) * n) # faster
    # return sum(range(1, n + 1))

def find_fuel(target, crabs, cost_f):
    fuel = 0
    for n in crabs:
        if n != target:
            fuel += cost_f(abs(n - target))
    return fuel


def solve(cost_f):
    result = float('inf')
    for c in range(1, max(nums) + 1):
        # print(c, max(nums) + 1)

        fuel = find_fuel(c, nums, cost_f)
        if fuel < result:
            result = fuel
    return result

print("Part 1", solve(lambda x: x))
print("Part 2", solve(cost))

