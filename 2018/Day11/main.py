from operator import itemgetter
def calc_power_level(x, y, serial):
    rackID = x + 10
    power_level = rackID * y
    power_level += serial
    power_level = power_level * rackID
    power_level = str(power_level)
    power_level = power_level[-3]
    power_level = int(power_level)
    power_level -= 5
    return power_level

grid_serial_number = 4151

# Part 1
max_fuel_level = 0
top_left_corner = list()
for x in range(1,298+1):
    for y in range(1, 298+1):
        # left corner: x,y
        fuel_level = 0
        for i in range(x, x+3):
            for j in range(y, y+3):
                fuel_level += calc_power_level(i,j,grid_serial_number)
        if(fuel_level > max_fuel_level):
            max_fuel_level = fuel_level
            top_left_corner = [x, y]

print('Max fuel level: ' + str(max_fuel_level) + ', Top left corner: ' +  str(top_left_corner))

# Part 2
w, h = 300, 300
grid = [[0 for x in range(1, w+2)] for y in range(1, h+2)]
# Populate grid with fuel levels
for x in range(1,300+1):
    for y in range(1,300+1):
        grid[x][y] = calc_power_level(x, y, grid_serial_number)

max_fuel_list = list()
for size in range(1, 300+1):
    print('Size: '+ str(size) + 'x' + str(size))
    max_fuel_level = -1000000000
    top_left_corner = list()
    last_x = 0
    for x in range(1, 300-size+2):
        for y in range(1, 300-size+2):
            # left corner: x,y
            if(last_x == x):                        # Optimization!
                #subtract
                for i in range(x, x+size):
                    fuel_level -= grid[i][y-1]
                #add
                for i in range(x, x+size):
                    fuel_level += grid[i][y+size-1]
            else:
                fuel_level = 0
                for i in range(x, x+size):
                   for j in range(y, y+size):
                       fuel_level += grid[i][j]
            last_x = x
            if(fuel_level > max_fuel_level):
                max_fuel_level = fuel_level
                top_left_corner = [x, y]
    max_fuel_list.append([size, max_fuel_level, top_left_corner[0], top_left_corner[1]])
print(max(max_fuel_list, key=itemgetter(1)))
