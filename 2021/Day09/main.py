import numpy

def is_low_point(x, y, heightmap):
    current_height = heightmap[y][x]
    for loc in get_adjacent_locations(x, y, heightmap):
        if current_height >= heightmap[loc[1]][loc[0]]:
            return False
    return True

def get_adjacent_locations(x, y, grid):
    locations = []
    max_x = len(grid[0])
    max_y = len(grid)
    if (y-1) >= 0:
        locations.append((x, y-1))
    if (y+1) < max_y:
        locations.append((x, y+1))
    if (x-1) >= 0:
        locations.append((x-1, y))
    if (x+1) < max_x:
        locations.append((x+1, y))
    return locations

def calc_basin_size(x, y, heightmap):
    visited_locations = []

    to_visit = [(x,y)]
    while (len(to_visit) != 0):
        current_x = to_visit[0][0]
        current_y = to_visit[0][1]
        neighbours = get_adjacent_locations(current_x, current_y, heightmap)

        # Add new neighbours that are not 9
        for n in neighbours:
            if heightmap[n[1]][n[0]] != '9' and n not in visited_locations and n not in to_visit:
                to_visit.append(n)

        to_visit.remove((current_x, current_y))
        visited_locations.append((current_x, current_y))
    return len(visited_locations)

# Obtain puzzle input
heightmap = []
with open('2021/Day09/input.txt','r') as file:
    heightmap = [line.strip() for line in file.readlines()]

# Part 1
risk_level_sum = 0
low_points = []
for y in range(0, len(heightmap)):
    for x in range(0, len(heightmap[0])):
        if (is_low_point(x, y, heightmap)):
            risk_level_sum += int(heightmap[y][x]) + 1
            low_points.append((x,y))

print(f'Part 1: The sum of the risk levels is {risk_level_sum}.')

# Part 2
basin_sizes = []
for point in low_points:
    basin_sizes.append(calc_basin_size(point[0], point[1], heightmap))

basin_sizes = sorted(basin_sizes, reverse=True)
print(f'Part 2: The product of the 3 largest basin sizes is ' + 
      f'{numpy.prod(basin_sizes[0:3])}.')
