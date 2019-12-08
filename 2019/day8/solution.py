import collections

input = '123456789012'

w = 3
h = 2


input = open('input.txt').read().split('\n')[0]

w = 25
h = 6

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

for i, layer in enumerate(layers):
    line = ''.join(layer)
    c = collections.Counter(line)

    count_zeros[i] = c['0']

min_line = min(count_zeros, key=count_zeros.get)


print(min_line)
c = collections.Counter(''.join(layers[min_line]))

print(c['1'] * c['2'])
