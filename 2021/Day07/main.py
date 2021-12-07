import numpy

def calc_fuel_cost(position, crabs, break_condition):
    cost = 0
    for pos in crabs:
        if (break_condition is not None and cost > break_condition):
            break
        steps = abs(pos - position)
        cost += steps * (steps + 1) // 2
    return cost

# Obtain input
input_data = list(map(int, open('2021/Day07/input.txt','r').readline().strip().split(',')))

# Part 1
move_to = int(numpy.median(input_data))
fuel_cost = 0
for crab_pos in input_data:
    fuel_cost += abs(crab_pos - move_to)

print(f'Part 1: The fuel cost to align at position {move_to} is {fuel_cost}.')

# Part 2
min_pos = min(input_data)
max_pos = max(input_data)

fuel_cost = float('inf')
for pos in range(min_pos, max_pos):
    result = calc_fuel_cost(pos, input_data, fuel_cost)
    if result < fuel_cost:
        fuel_cost = result
        cheapest_position = pos

print(f'Part 2: The fuel cost to align at position {cheapest_position} is {fuel_cost}.')
