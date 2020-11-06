def parseInputLine(line):
    words = line.split()
    if (words[0] == 'toggle'):
        coords1 = tuple(map(int, words[1].split(',')))
        coords2 = tuple(map(int, words[3].split(',')))
        return 'toggle', coords1, coords2
    else:
        coords1 = tuple(map(int, words[2].split(',')))
        coords2 = tuple(map(int, words[4].split(',')))
        if (words[1] == 'on'):
            return 'enable', coords1, coords2
        if(words[1] == 'off'):
            return 'disable', coords1, coords2


def controlLight(action, state):
    if(action == "enable"):
        return True
    elif(action == "disable"):
        return False
    elif(action == "toggle"):
        if (state == True):
            return False
        elif (state == False):
            return True


def controlLightBrightness(action, state):
    if (action == "enable"):
        return state + 1
    elif (action == "disable"):
        if ((state - 1) <= 0):
            return 0
        else:
            return state - 1
    elif (action == "toggle"):
        return state + 2


lines = open('2015/Day06/input.txt').read().splitlines()

# Part 1
light_grid = [[False] * 1000 for i in range(1000)]  # 1000x1000 grid

for line in lines:
    action, coord1, coord2 = parseInputLine(line)
    for y in range(coord1[0], coord2[0]+1):
        for x in range(coord1[1], coord2[1]+1):
            light_grid[y][x] = controlLight(action, light_grid[y][x])

light_counter = sum(map(sum, light_grid))
print('Part 1:', light_counter, 'lights are lit')

# Part 2
light_grid = [[0] * 1000 for i in range(1000)]  # 1000x1000 grid

for line in lines:
    action, coord1, coord2 = parseInputLine(line)
    for y in range(coord1[0], coord2[0]+1):
        for x in range(coord1[1], coord2[1]+1):
            light_grid[y][x] = controlLightBrightness(action, light_grid[y][x])


light_sum = sum(map(sum, light_grid))
print('Part 2: The total brightness is', light_sum)
