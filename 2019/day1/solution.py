import math

masses = list(map(int, open("input.txt")))


def calc_fuel(mass):
    return math.floor((mass / 3) - 2)


def part1():
    return sum(calc_fuel(mass) for mass in masses)


def part2():
    def _calc(mass, acc=0):
        fuel = calc_fuel(mass)

        if fuel <= 0:
            return acc
        acc += fuel
        return _calc(fuel, acc)

    return sum(_calc(mass) for mass in masses)

print(part1(), part2())
