# https://pypi.org/project/pathfinding/
# pip install pathfinding
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

import queue

class Coord:
    def __init__(self, x, y, steps_taken):
        self.x = x
        self.y = y
        self.steps_taken = steps_taken

def wall_or_open_space(coord, favorite_number):
    x = coord[0]
    y = coord[1]
    num = x*x + 3*x + 2*x*y + y + y*y
    num += favorite_number
    binary_rep = bin(num)[2:]   # Removing inital '0b' in binary representation
    no_one_bits = binary_rep.count('1')
    if(no_one_bits % 2 == 0):    # even
        return 'space'
    elif(no_one_bits % 2 == 1):  # odd
        return 'wall'

def construct_map(map, favorite_number, sizeX, sizeY):
    for row_num in range(0, sizeY):
        map_row = []
        for col_num in range(0, sizeX):
            if(wall_or_open_space([col_num, row_num], favorite_number)=='space'):
                map_row.append(1)
            else:
                map_row.append(0)
        map.append(map_row)

def print_map(map):
    sizeX = len(map[0])
    sizeY = len(map)
    print('  ', end = '')
    for i in range(0, sizeX):
        print(i, end='')
    print('')
    for i in range(0, sizeY):
        print(str(i) + ' ', end='')
        for row_item in map[i]:
            if(row_item==0):
                print('#', end='')
            elif(row_item==1):
                print('.', end='')
        print('')

def get_valid_neighbours(map, coord):
    sizeX = len(map[0])
    sizeY = len(map)
    valid_coords = []
    x = coord[0]
    y = coord[1]
    # Up
    if(y-1 >= 0 and map[y-1][x] != 0):
        valid_coords.append([x,y-1])
    # Left
    if(x-1 >= 0 and map[y][x-1] != 0):
        valid_coords.append([x-1,y])
    # Down
    if(y+1 < sizeY and map[y+1][x]):
        valid_coords.append([x,y+1])
    # Right
    if(x+1 < sizeX and map[y][x+1]):
        valid_coords.append([x+1,y])
    return valid_coords

def explore_map(map, start_coord, visited_coords):
    coord_str = str(start_coord[0])+ ',' + str(start_coord[1])
    visited_coords[coord_str] = True

    q = queue.Queue(0)
    start = Coord(start_coord[0], start_coord[1], 0)
    q.put(start)
    while(not q.empty()):
        coord = q.get()
        if(coord.steps_taken == 50):
            pass    # Don't continue further than 50 steps
        else:
            neighbour_coords = get_valid_neighbours(map, [coord.x, coord.y])    # Get possible neighbour coords
            for c in neighbour_coords:
                coord_str = str(c[0])+','+str(c[1])
                if(coord_str in visited_coords):    # If coord is already in visited coords, do nothing
                    pass
                else:   # Else, add coord to visited_coords and queue.
                    visited_coords[coord_str] = True
                    new_coord = Coord(c[0], c[1], coord.steps_taken+1)
                    q.put(new_coord)

puzzle_input = 1352
map = []
construct_map(map, puzzle_input, 50, 50)

# First star
grid = Grid(matrix=map)
start = grid.node(1, 1)
end = grid.node(31, 39)
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)
print('[part1] The fewest number of steps required to reach (31,39) is {}'.format(len(path)-1)) # subtracting starting position from path

# Second star
visited_coords = {}
explore_map(map, [1,1], visited_coords)
print('[part2] The amount of unique locations that can be reached within 50 steps are {}'.format(len(visited_coords)))
