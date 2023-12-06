from math import prod

# time = list(map(int, "7  15   30".split()))
# distance = list(map(int, "9  40  200".split()))

time = list(map(int, "48     93     84     66".split()))
distance = list(map(int, "261   1192   1019   1063".split()))

def get_distance(press_time: int, initial_time: int):
    speed = press_time
    distance_to_move = speed * (initial_time - press_time)
    # print(speed, distance_to_move)
    return distance_to_move


# part1
cases = []
for t, recored_won in zip(time, distance):
    count_to_win = 0
    for i in range(1, t + 1):
        distance = get_distance(i, t)
        if distance > recored_won:
            count_to_win += 1
    cases.append(count_to_win)

print(prod(cases))

# part2
# time = 71530
# distance = 940200
time = 48938466
distance = 261119210191063

ans = 0
for i in range(1, time + 1):
    d = get_distance(i, time)
    if d > distance:
        ans += 1
print(ans)

