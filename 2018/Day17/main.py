import re
from operator import itemgetter
def read_input(path):
    input = open(path,'r').read().splitlines()
    clayCoords = list()
    for line in input:
        x = re.search(r'x=\d+(..\d+)?', line).group(0)
        y = re.search(r'y=\d+(..\d+)?', line).group(0)
        x = x.split('x=')[1]
        y = y.split('y=')[1]
        if(x.isdigit()):
            x = [int(x), int(x)]
        else:
            xs = x.split('..')
            x = [int(xs[0]), int(xs[1])]
        if(y.isdigit()):
            y = [int(y), int(y)]
        else:
            ys = y.split('..')
            y = [int(ys[0]), int(ys[1])]
        for xx in range(x[0], x[1]+1):
            for yy in range(y[0], y[1]+1):
                clayCoords.append((xx,yy))
    return clayCoords
def create_map(clay_coords):
    maxX = max(clay_coords, key=itemgetter(0))[0]+1
    minX = 0-1
    maxY = max(clay_coords, key=itemgetter(1))[1]
    minY = 0
    map = list()
    for y in range(minY,maxY+1):
        row = list()
        for x in range(minX,maxX+1):
            row .append('.')
        map.append(row)
    for coord in clay_coords:
        x = coord[0]
        y = coord[1]
        map[y][x] = '#'
    return map
def print_map(map, minX=494, maxX=507, minY=0, maxY=13):
    for y in range(minY, maxY+1):
        row = ''
        for x in range(minX, maxX+1):
            row += str(map[y][x])
        print(row)
def check_clay_both_sides(map, current):
    x = current[0]
    y = current[1]
    rx, ry = x, y
    lx, ly = x, y
    right_wall_found = False
    continue_look_for_wall = True
    while(continue_look_for_wall):
        if(map[ry+1][rx] in ['#', '~']):    # has floor
            if(map[ry][rx+1] in ['#','~']):     # has wall on right side
                right_wall_found = True
                continue_look_for_wall = False
            else:
                rx = rx + 1                 # move right
        else: # no floor !?!?
            right_wall_found = False
            continue_look_for_wall = False
    left_wall_found = False
    continue_look_for_wall = True
    while(continue_look_for_wall):
        if(map[ry+1][rx] in ['#', '~']):    # has floor
            if(map[ry][rx-1] in ['#','~']):     # has wall on left side
                left_wall_found = True
                continue_look_for_wall = False
            else:
                rx = rx - 1                  # move left
        else: # no floor !?!?
            left_wall_found = False
            continue_look_for_wall = False
    return (right_wall_found and left_wall_found)
def fill_water(map, current):
    x = current[0]
    y = current[1]
    rx, ry = x, y
    lx, ly = x, y
    done = False
    while(not done):            #right side
        map[ry][rx] = '~'
        if(map[ry][rx+1] in ['#','~']):
            done = True
        else:
            rx = rx + 1
    done = False
    while(not done):            #left side
        map[ly][lx] = '~'
        if(map[ly][lx-1] in ['#','~']):
            done = True
        else:
            lx = lx - 1
    return map
def water_overflow(map, current):
    new_water_sources = list()
    x = current[0]
    y = current[1]
    rx, ry = x, y
    lx, ly = x, y
    done = False
    while(not done):            #right side
        if(map[ry][rx] != '#'):
            map[ry][rx] = '|'
        if(map[ry][rx] == '#'):                 #if current tile is a wall
            done = True
        elif(map[ry+1][rx] in ['.', '|']):      #if tile below current is open
            new_water_sources.append([(rx,ry),True])
            done = True
        else:
            rx = rx + 1
    done = False
    while(not done):            #left side
        if(map[ly][lx] != '#'):
            map[ly][lx] = '|'
        if(map[ly][lx] == '#'):
            done = True
        elif(map[ly+1][lx] in ['.', '|']):
            new_water_sources.append([(lx,ly), True])
            done = True
        else:
            lx = lx - 1
    return map, new_water_sources
def add_water(map, start_source):
    continue_water_flow = True
    water_sources = list()
    water_sources.append(start_source)
    counter = 0
    while(continue_water_flow):
        for water_source in water_sources:
            at_rest = False
            current_source = water_source[0]
            current = water_source[0]
            while(not at_rest):
                if(len(map) == current[1]+1):
                    water_source[1] = False
                    at_rest = True
                down = (current[0], current[1]+1)
                right = (current[0]+1, current[1])
                left = (current[0]-1, current[1])
                up = (current[0], current[1]-1)
                # if source is covered in water, move it up
                if(map[water_source[0][1]][water_source[0][0]]=='~'):
                    #water_source[0][1] -= 1
                    if([(water_source[0][0],water_source[0][1]-1), True] not in water_sources):
                        water_sources.append([(water_source[0][0],water_source[0][1]-1), True])
                        water_sources.remove(water_source)
                # move down if possible
                if(not at_rest and map[down[1]][down[0]] in ['.','|']):
                    map[down[1]][down[0]] = '|'
                    current = down
                elif(not at_rest and map[down[1]][down[0]] in ['#','~']):
                    enclosed_space = check_clay_both_sides(map, current)
                    #print('espace:',enclosed_space, water_source)
                    # fill spaces that has clay on both sides
                    if(enclosed_space):
                        map = fill_water(map, current)
                        at_rest = True
                    # overflow, and add new water sources (remove current water souce)
                    else:
                        map, new_water_sources = water_overflow(map, current)
                        water_sources.remove([current_source, True])
                        for s in new_water_sources:
                            if(s not in water_sources):
                                water_sources.append(s)
                        at_rest = True
            #print_map(map)
            #print_map(map,482,594,0,1937)
            #print_map(map,3,50,0,62)
            #print('\n')
        if(counter%1000 == 0):
            print(counter)
        if(counter%10000 == 0):
            print(water_sources)
            #print_map(map,482,594,0,70)
        counter +=1
        if(not any([s[1] for s in water_sources])):
            print('why stop')
            continue_water_flow = False
    return map
def count_water_tiles(map, minX, maxX, minY, maxY):
    count = 0
    for y in range(minY, maxY+1):
        for x in range(minX, maxX):
            if(map[y][x] in ['|','~']):
                count +=1
    return count
def count_remaining_water(map, minX, maxX, minY, maxY):
    count = 0
    for y in range(minY, maxY+1):
        for x in range(minX, maxX):
            if(map[y][x] == '~'):
                count +=1
    return count

#clay = read_input('2018/Day17/input_sample.txt')
#clay= read_input('2018/Day17/input_test.txt')
clay= read_input('2018/Day17/input.txt')
maxX = max(clay, key=itemgetter(0))[0]+1
minX = min(clay, key=itemgetter(0))[0]-1
maxY = max(clay, key=itemgetter(1))[1]
minY = 0
print(minX,maxX,minY,maxY)
map = create_map(clay)
#Place water source
map[0][500] = '+'       #19
print_map(map, minX, maxX, minY, maxY)
add_water(map, [(500,0), True])
print_map(map, minX, maxX, minY, maxY)
minY = min(clay, key=itemgetter(1))[1]

res1 = count_water_tiles(map, minX, maxX, minY, maxY)
print('Number of tiles reachable by water:',res1)
res2 = count_remaining_water(map, minX, maxX, minY, maxY)
print('Number of tiles with remainging water:',res2)
