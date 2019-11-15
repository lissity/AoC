#---- First star ----#

# Obtain instructions
instructions = [instr.strip() for instr in open('2016/Day01/input.txt','r').read().split(', ')]

# Initial values
coords = {'x': 0, 'y': 0}
direction = 'up'

# Moving logic
for instr in instructions:
    steps = int(instr[1:])
    if(instr[0] == 'R'):
        if(direction == 'up'):
            coords['x'] += steps
            direction = 'right'
        elif(direction == 'right'):
            coords['y'] -= steps
            direction = 'down'
        elif(direction == 'down'):
            coords['x'] -= steps
            direction = 'left'
        elif(direction == 'left'):
            coords['y'] += steps
            direction = 'up'
    elif(instr[0] == 'L'):
        if(direction == 'up'):
            coords['x'] -= steps
            direction = 'left'
        elif(direction == 'left'):
            coords['y'] -= steps
            direction = 'down'
        elif(direction == 'down'):
            coords['x'] += steps
            direction = 'right'
        elif(direction == 'right'):
            coords['y'] += steps
            direction = 'up'

result = abs(coords['x']) + abs(coords['y'])
print('[part1] The distance from (0,0) to ({},{}) is {}'.format(coords['x'], coords['y'], result))

#---- Second star ----#
def check_visited_coords(dict, x1, y1, x2, y2):
    duplicate_coord_found = False
    dup_coord = [];

    if (x1 is not x2):
        for x in range(x1, x2, int(round((x2-x1)/abs(x2-x1)))):
            if((x,y1) in visited_coords):
                duplicate_coord_found = True
                dup_coord = [x, y1]
                break
            else:
                visited_coords[(x, y1)] = True
    elif(y1 is not y2):
        for y in range(y1, y2, int(round(((y2-y1)/abs(y2-y1))))):
            if((x1,y) in visited_coords):
                duplicate_coord_found = True
                dup_coord = [x1, y]
                break
            else:
                visited_coords[(x1, y)] = True
    return duplicate_coord_found, dup_coord

# Initial values
coords = {'x': 0, 'y': 0}
direction = 'up'
visited_coords = {}

# Moving logic
for instr in instructions:
    start_coords = coords.copy();
    steps = int(instr[1:])
    if(instr[0] == 'R'):
        if(direction == 'up'):
            coords['x'] += steps
            direction = 'right'
        elif(direction == 'right'):
            coords['y'] -= steps
            direction = 'down'
        elif(direction == 'down'):
            coords['x'] -= steps
            direction = 'left'
        elif(direction == 'left'):
            coords['y'] += steps
            direction = 'up'
    elif(instr[0] == 'L'):
        if(direction == 'up'):
            coords['x'] -= steps
            direction = 'left'
        elif(direction == 'left'):
            coords['y'] -= steps
            direction = 'down'
        elif(direction == 'down'):
            coords['x'] += steps
            direction = 'right'
        elif(direction == 'right'):
            coords['y'] += steps
            direction = 'up'
    duplicate_coord_found, dup_coord = check_visited_coords(visited_coords, start_coords['x'], start_coords['y'], coords['x'], coords['y'])
    if(duplicate_coord_found):
        result = abs(dup_coord[0]) + abs(dup_coord[1])
        print('[part2] The first coordinate reached twice is ({}, {}). \
The distance from (0,0) to ({},{}) is {}'.format(dup_coord[0], dup_coord[1], dup_coord[0], dup_coord[1], result))
        break;
