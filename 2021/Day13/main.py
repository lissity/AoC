from operator import itemgetter

def render_img(coordinates):
    max_x = max(coordinates, key=itemgetter(0))[0]
    max_y = max(coordinates, key=itemgetter(1))[1]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in coordinates:
                print('#', end='')
            else:
                print(' ', end='')
        print()

# Obtain puzzle input
with open('2021/Day13/input.txt', 'r') as file:
    dots = []
    line = file.readline()
    while line != '\n':
        dots.append(line)
        line = file.readline()
    instructions = [l.strip()[11::].split('=') for l in file.readlines()]

instructions = [(i[0], int(i[1])) for i in instructions]
dots = [tuple(map(int, d.strip().split(','))) for d in dots]

# Part 1 & 2
for i in range(0, len(instructions)):
    fold_axis = instructions[i][0]
    fold_location = instructions[i][1]

    for dot in dots.copy():
        x, y = dot[0], dot[1]
        if (fold_axis == 'x'):
            if (x > fold_location):
                dots.append((fold_location - ( x-fold_location), y))
                dots.remove((x,y))
        elif (fold_axis == 'y'):
            if (y > fold_location):
                dots.append((x, fold_location - (y-fold_location)))
                dots.remove((x,y))
    if (i == 0):
        print(f'Part 1: The number of visible dots after first fold is {len(set(dots))}.')
print(f'Part 2: The code is:')
render_img(dots)
