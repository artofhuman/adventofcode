from collections import Counter


# f_name = "test_input.txt"
f_name = "input.txt"

with open(f_name) as f:
    nums = list(map(int, f.read().split(',')))

def part1_easy(days, nums):
    for _ in range(days):
        for i in range(len(nums)):
            n = nums[i]
            n -= 1
            if n == -1:
                nums[i] = 6
                nums.append(8)
            else:
                nums[i] = n

    return len(nums)

def part2(days, nums):
    counter = Counter(nums)

    for d in range(days):
        counter[d + 7] += counter[d]
        counter[d + 9] += counter[d]
        counter[d] = 0

    return sum(counter.values())

print(part1_easy(18, nums[:]))
print(part2(18, nums[:]))
print(part2(256, nums[:]))
