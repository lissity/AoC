# https://pypi.org/project/pathfinding/
# pip install pathfinding
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def get_grid_value(x,y):
    grid_x = x % len(puzzle_input)
    grid_y = y % len(puzzle_input)
    increase_x = x // len(puzzle_input)
    increase_y = y // len(puzzle_input)
    value = puzzle_input[grid_y][grid_x] + increase_x + increase_y
    if (value > 9):
        value = (value % 10) + 1
    return value

# Obtain puzzle input
with open('2021/Day15/input.txt', 'r') as file:
    puzzle_input = [[int(char) for char in line.strip()] for line in file.readlines()]

# Part 1
grid = Grid(matrix=puzzle_input)
start = grid.node(0, 0)
end = grid.node(len(puzzle_input[0])-1, len(puzzle_input)-1)
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)
risk = sum([puzzle_input[y][x] for x,y in path if (not(x==0 and y==0))])

print(f'Part 1: The lowest risk path has a risk of {risk}.')

# Part 2
large_grid = [[get_grid_value(x, y) for x in range(len(puzzle_input[0])*5)] for y in range(len(puzzle_input)*5)]

grid = Grid(matrix=large_grid)
start = grid.node(0, 0)
end = grid.node(len(puzzle_input[0])*5-1, len(puzzle_input)*5-1)
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)
risk =sum([get_grid_value(x,y) for x,y in path if (not(x==0 and y==0))])

# Takes ~50s for part 2 answer
print(f'Part 2: The lowest risk path has a risk of {risk}.')
