import collections

input = '123456789012'

w = 3
h = 2


input = open('input.txt').read().split('\n')[0]

w = 25
h = 6

# input = '0222112222120000'
# w = 2
# h = 2

layers = []
layer = []

count_zeros = {}

for i, step in enumerate(range(0, len(input), w)):
    if i % h == 0:
        layer = []
        layers.append(layer)

    pixel = input[step:step + w]
    layer.append(pixel)

    print(pixel)


# input = '0222112222120000'
# w = 2
# h = 2


def part1():
    for i, layer in enumerate(layers):
        line = ''.join(layer)
        c = collections.Counter(line)

        count_zeros[i] = c['0']

    min_line = min(count_zeros, key=count_zeros.get)


    print(min_line)
    c = collections.Counter(''.join(layers[min_line]))

    print(c['1'] * c['2'])

# part1()

print(layers)

# 0 - black
# 1 - white
# 2 - transparent

result = []
matrix = [['-' for i in range(w)] for i in range(h)]

for layer in layers:
    for p in layer:
        print(p)

layers.reverse()

for num_layer, layer in enumerate(layers):
    print('-------')
    for num_pixel, pixel in enumerate(layer):
        line = num_pixel

        for pos_char, char in enumerate(pixel):
            if char != '2':
                matrix[line][pos_char] = char


for line in matrix:
    _line = []
    for ch in line:
        if ch == '1':
            _line.append('*')
        else:
            _line.append(' ')

    print(''.join(_line))
