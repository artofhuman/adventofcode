str_val = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
str_val = open("input.txt").readline().strip()

blocks = str_val.split(",")

# part1
ans = 0


def get_hash(block):
    v = 0
    for ch in block:
        v += ord(ch)
        v *= 17
        v %= 256
    return v


for block in blocks:
    ans += get_hash(block)
print(ans)

# part2


class Lens:
    def __init__(self, value):
        label, val = value.split("=")
        self.label = label
        self.val = int(val)

    def __repr__(self):
        return f"{self.label} {self.val}"

    @property
    def box_num(self):
        return get_hash(self.label)

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.label == other
        return self.label == other.label


boxes = [{} for _ in range(256)]

for block in blocks:
    if block[-1] == "-":  # minus op
        label = block[:-1]
        num = get_hash(label)
        if label in boxes[num]:
            del boxes[num][label]
    else:
        lens = Lens(block)
        num = lens.box_num
        boxes[num][lens.label] = lens

ans = 0
for box_n, box in enumerate(boxes):
    for slot_n, (_, l) in enumerate(box.items()):
        total = (1 + box_n) * (slot_n + 1) * l.val
        # print(total)
        ans += total

print(ans)
