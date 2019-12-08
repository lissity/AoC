from operator import itemgetter

def count_digit(layer, digit):
    counter = 0
    for row in layer:
        counter += row.count(digit)
    return counter

def get_pixel_value(data_stack):
    # 0 black, 1 white, 2 transparent
    for i in data_stack:
        if(i == '0'):
            return ' '
        if(i == '1'):
            return '#'

def render_img(img_data, width, height):
    current_pos = 0
    for _ in range(0, height):
        for _ in range(0, width):
            print(get_pixel_value(img_data[current_pos]), end='')
            current_pos += 1
        print('')

# Obtain input
digits = open('2019/Day08/input.txt', 'r').readline().strip()
width, height = 25, 6

# Create layers
digits_per_layer = width * height
no_layers = int(len(digits)/digits_per_layer)
layers = []
current_pos = 0
for i in range(0, no_layers):
    layer = []
    for _ in range(0, height):
        layer.append(digits[current_pos:current_pos+width])
        current_pos += width
    layers.append(layer)

# Part 1
layer_with_fewest_0 = min(((count_digit(layer,'0'), layer) for layer in layers),key=itemgetter(0))[1]
print('[part1] On the layer with fewest 0s, the number of 1s multiplied with' \
        ' the number of 2s is {}'.format(count_digit(layer_with_fewest_0, '1') \
        * count_digit(layer_with_fewest_0, '2')))

# Part 2
img_data = []
current_pos = 0

for _ in range(0, digits_per_layer):
    data = []
    data = digits[current_pos::digits_per_layer]
    current_pos += 1
    img_data.append(data)

print('[part2] The message that the image produces is: ')
render_img(img_data, width, height)
