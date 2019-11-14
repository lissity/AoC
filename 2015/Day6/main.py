def read_input():
    input = open('2015/Day6/input.txt', 'r').read().splitlines()
    input_list = list()
    for line in input:
        split_line = line.split()
        if(split_line[0] == 'turn'):
            if(split_line[1]=='on'):
                command = 'on'
            elif(split_line[1]=='off'):
                command = 'off'
            coord1 = split_line[2].split(',')
            coord2 = split_line[4].split(',')
        elif(split_line[0] == 'toggle'):
            command = 'toggle'
            coord1 = split_line[1].split(',')
            coord2 = split_line[3].split(',')
        list_item = [command, coord1, coord2]
        input_list.append(list_item)
    return input_list

input = read_input()
# Two-dimentional list
w, h = 1000, 1000
grid = [[0 for x in range(w)] for y in range(h)]

# Part 1
for item in input:
    for i in range(int(item[1][0]), int(item[2][0])+1):
        for j in range(int(item[1][1]), int(item[2][1])+1):
            #print(i,j)
            if(item[0] == 'on'):
                grid[i][j] = 1
            elif(item[0] == 'off'):
                grid[i][j] = 0
            elif(item[0] == 'toggle'):
                if(grid[i][j] == 0):
                    grid[i][j] = 1
                elif(grid[i][j] == 1):
                    grid[i][j] = 0

lit_lights = 0
for i in range(1000):
    for j in range(1000):
        if(grid[i][j] == 1):
            lit_lights += 1

print('Lit lights: ' + str(lit_lights))

# Part 2
w, h = 1000, 1000
grid2 = [[0 for x in range(w)] for y in range(h)]
for item in input:
    for i in range(int(item[1][0]), int(item[2][0])+1):
        for j in range(int(item[1][1]), int(item[2][1])+1):
            #print(i,j)
            if(item[0] == 'on'):
                grid2[i][j] += 1
            elif(item[0] == 'off'):
                if(grid2[i][j]>0):
                    grid2[i][j] -= 1
            elif(item[0] == 'toggle'):
                grid2[i][j] += 2

brightness = 0
for i in range(1000):
    for j in range(1000):
        brightness += grid2[i][j]

print('Brightness: ' + str(brightness))
