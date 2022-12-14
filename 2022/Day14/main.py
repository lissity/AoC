def points_between(p1, p2):
    stepx = 1 if p1[0] < p2[0] else -1
    stepy = 1 if p1[1] < p2[1] else -1
    xs = range(p1[0] + stepx, p2[0], stepx) or [p1[0]]
    ys = range(p1[1] + stepy, p2[1], stepy) or [p1[1]]
    return [(x,y) for x in xs for y in ys]

def get_path(coord_list, cave):
    for i in range(len(coord_list)-1):
        p1 = coord_list[i]
        p2 = coord_list[i+1]
        points = points_between(p1, p2)
        for p in points:
            if p not in cave:
                cave[p] = 'ROCK'
        for p in [p1, p2]:
            if p not in cave:
                cave[p] = 'ROCK'

def move_sand(coord, cave, max_y=-1, floor_location=-1):
    # Part 1: Check if falling into the abyss
    if max_y != -1 and coord[1] > max_y:
        return False

    # Part 2: Check if hitting the floor
    if floor_location != -1 and coord[1]+1 == floor_location:
        cave[tuple(coord)] = 'SAND'
        return False

    down = (coord[0], coord[1]+1)
    down_left = (coord[0]-1, coord[1]+1)
    down_right = (coord[0]+1, coord[1]+1)
    if down not in cave:
        coord[1] = down[1] 
        return True
    elif down_left not in cave:
        coord[0] = down_left[0]
        coord[1] = down_left[1]
        return True
    elif down_right not in cave:
        coord[0] = down_right[0]
        coord[1] = down_right[1]
        return True
    else:
        cave[tuple(coord)] = 'SAND'
        return False

# Obtain input
rocks = [line.strip().split(' -> ') 
         for line in open('2022/Day14/input.txt').readlines()]
for i in range(len(rocks)):
    for j in range(len(rocks[i])):
        rocks[i][j]= tuple(map(int, rocks[i][j].split(',')))

# Part 1
cave_map = {}
for rock in rocks:
    get_path(rock, cave_map)

max_y = max(cave_map, key=lambda k: k[1])[1]
sand_at_rest = 0
while(True):
    sand_location = [500,0]         # Spawn sand
    while (move_sand(sand_location, cave_map, max_y)):
        pass
    if sand_location[1] > max_y:
        break
    sand_at_rest += 1

print(f'Part 1: {sand_at_rest} units of sand is at rest.')

# Part 2
cave_map = {}           # Resetting the map
for rock in rocks:
    get_path(rock, cave_map)

floor_location = max_y + 2
sand_at_rest = 0
while(True):
    sand_location = [500,0]
    while (move_sand(sand_location, cave_map, -1, floor_location)):
        pass
    sand_at_rest += 1
    if sand_location == [500,0]:
        break

print(f'Part 2: {sand_at_rest} units of sand is at rest.')
