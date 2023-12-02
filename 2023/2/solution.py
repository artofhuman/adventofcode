from math import prod

lines = open("input.txt").read().splitlines()

rules = {"blue": 14, "green": 13, "red": 12}


def iter_over_colors(game):
    for i in range(1, len(game), 2):
        color = game[i]
        count = int(game[i - 1])
        yield color, count


def is_valid(game):
    game = game.split()
    for color, count in iter_over_colors(game):
        if count > rules[color]:
            return False
    return True


def get_games(line):
    parts = line.replace(",", "").split(":")
    id_ = int(parts[0].split()[-1])
    return id_, parts[1].strip().split(";")


ans = 0
for line in lines:
    id_, games = get_games(line)
    if any(not is_valid(game) for game in games):
        continue
    else:
        ans += id_

print(ans)


def get_set(games):
    counts = {}
    for game in games:
        game = game.split()
        for color, count in iter_over_colors(game):
            if color not in counts or counts[color] < count:
                counts[color] = count
    return counts


ans = 0
for line in lines:
    _, games = get_games(line)

    set_ = get_set(games)
    ans += prod(set_.values())
print(ans)
