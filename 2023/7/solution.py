from collections import Counter

# inp = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# """.splitlines()

inp = open("input.txt").read().splitlines()


class Hand:
    _ALL_CARDS = "AKQJT98765432"

    def __init__(self, cards: str):
        self.cards = cards

    def __gt__(self, other: "Hand"):
        if self._is_same_label(other):
            for i in range(len(self.cards)):
                c1 = self.cards[i]
                c2 = other.cards[i]
                if c1 == c2:
                    continue
                return self._ALL_CARDS.index(c1) < self._ALL_CARDS.index(c2)
        else:
            return self.counts > other.counts

    @property
    def common(self):
        return self.c.most_common()

    @property
    def c(self):
        return Counter(self.cards)

    def _is_same_label(self, other):
        return self.counts == other.counts

    @property
    def counts(self):
        return tuple(v[1] for v in self.common)

    def __repr__(self):
        return self.cards


def get_cards(kls):
    return list(map(lambda x: (kls(x[0]), int(x[1])), (x.split() for x in inp)))


assert Hand("32456") > Hand("2345k")
assert Hand("32TAK") > Hand("32456")
assert Hand("AAAAA") > Hand("AA866")


def calc_ans(_cards):
    return sum(i * rank for i, (_, rank) in enumerate(_cards))


# part1
print(calc_ans(sorted(get_cards(Hand))))

# part2
# QJJQ2 -> QQQQ2
# QJQ22 -> QQQ22
class Hand2(Hand):
    _ALL_CARDS = "AKQT98765432J"

    @property
    def c(self):
        c = Counter(self.cards)
        if "J" in c and c["J"] < 5:
            j_count = c.pop("J")
            _max_card = c.most_common()[0][0]
            c[_max_card] += j_count
        return c


print(calc_ans(sorted(get_cards(Hand2))))
