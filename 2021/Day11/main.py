def get_adjacent_cells(x_coord, y_coord, max_x, max_y):
    result = []
    for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1)
                if not (i == 0 and j == 0)]:
        if (x >= 0 and x < max_x) and y >= 0 and y < max_y:
            result.append((x,y))
    return result

def grid_indices(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            yield(x,y)

# Obtain puzzle input
with open('2021/Day11/input.txt', 'r') as file:
    puzzle_input = [line.strip() for line in file.readlines()]
    puzzle_input = [[int(char) for char in row] for row in puzzle_input]
energy_levels = puzzle_input.copy()
max_x = len(energy_levels[0])
max_y = len(energy_levels)

# Part 1
flash_count = 0
for _ in range(0, 100):
    # Increase energy levels by 1
    energy_levels = [[num+1 for num in row ]for row in energy_levels]

    # All octopus with energy level > 9 will flash
    will_flash = []
    has_flashed = []
    for (x,y) in grid_indices(energy_levels):
        if (energy_levels[y][x] > 9):
            will_flash.append((x,y))
    
    # Go through octopus that will flash this step
    while len(will_flash) != 0:
        # Increase adjacent squares with 1
        for x,y in get_adjacent_cells(will_flash[0][0], will_flash[0][1], max_x, max_y):
            energy_levels[y][x] += 1
        has_flashed.append(will_flash[0])
        del will_flash[0]
        flash_count += 1

        # Add new octopus to list if their energy level > 9
        for (x,y) in grid_indices(energy_levels):
            if (energy_levels[y][x] > 9) and (x,y) not in has_flashed and (x,y) not in will_flash:
                will_flash.append((x,y))

    # Any octopus that flashed has its energy level set to 0
    for (x,y) in has_flashed:
        energy_levels[y][x] = 0
    has_flashed = []

print(f'Part 1: After 100 steps the total amount of flashes are {flash_count}.')

# Part 2
step = 101      # Continuing at step 101
while(True):
    # Increase energy levels by 1
    energy_levels = [[num+1 for num in row ]for row in energy_levels]

    # All octopus with energy level > 9 will flash
    will_flash = []
    has_flashed = []
    for (x,y) in grid_indices(energy_levels):
        if (energy_levels[y][x] > 9):
            will_flash.append((x,y))

    # Go through octopus that will flash
    while len(will_flash) != 0:
        # Increase adjacent squares with 1
        for x,y in get_adjacent_cells(will_flash[0][0], will_flash[0][1], max_x, max_y):
            energy_levels[y][x] += 1
        has_flashed.append(will_flash[0])
        del will_flash[0]

        # Add new octopus to list if their energy level > 9
        for (x,y) in grid_indices(energy_levels):
            if (energy_levels[y][x] > 9) and (x,y) not in has_flashed and (x,y) not in will_flash:
                will_flash.append((x,y))
    
    # Any octopus that flashed has its energy level set to 0
    count = 0
    for (x,y) in has_flashed:
        energy_levels[y][x] = 0
        count += 1
    has_flashed = []

    # Check if all octopus flashed on this step
    if(count == (max_x * max_y)):
        break
    step += 1

print(f'Part 2: The first step when all octopuses flash is step {step}.')
