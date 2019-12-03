def create_wire_path(path_instructions):
    coord = [0, 0]     # Starting coordinate
    wire = []
    for instr in path_instructions:
        dir = instr[0]
        distance = int(instr[1:])
        for _ in range(0, distance):
            if(dir == 'R'):
                coord[0] +=1
            elif(dir == 'L'):
                coord[0] -=1
            elif(dir == 'U'):
                coord[1] += 1
            elif(dir == 'D'):
                coord[1] -= 1
            wire.append(tuple(coord))
    return wire

def manhattan_distance(coord):
    return abs(coord[0]) + abs(coord[1])

# Obtain input
with open('2019/Day03/input.txt','r') as file:
    wire_path_1 = file.readline().strip().split(',')
    wire_path_2 = file.readline().strip().split(',')

#---- First star ----
# Create lists of all coordinates where wire 1 and wire 2 are
wire1 = create_wire_path(wire_path_1)
wire2 = create_wire_path(wire_path_2)

intersections = list(set(wire1).intersection(wire2))
closest_intersection = min(intersections, key=lambda t: manhattan_distance(t))
print('[part1] The distance to the closest intersection is {}' \
      .format(manhattan_distance(closest_intersection)))

#---- Second star ----
total_steps = []
for intersec in intersections:
    total_steps.append(wire1.index(intersec) + wire2.index(intersec) + 2)
print('[part2] The fewest combined steps to an intersection is {}'.format(min(total_steps)))
