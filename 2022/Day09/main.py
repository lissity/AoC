def isAdjacentOrOverlapping(coord1, coord2):
    x_coord, y_coord = coord1[0], coord1[1]
    adjacent_coords = []
    for x,y in [[x_coord+i,y_coord+j] for i in (-1,0,1) for j in (-1,0,1)]:
        adjacent_coords.append([x,y])
    if coord2 in adjacent_coords:
        return True
    else:
        return False

def updateTailPosition(head, tail):
    if isAdjacentOrOverlapping(head, tail):
        return tail                             # Tail does not need to move

    new_tail_x = tail[0]
    new_tail_y = tail[1]

    if head[0] > tail[0]:
        new_tail_x += 1
    if head[0] < tail[0]:
        new_tail_x -= 1
    if head[1] > tail[1]:
        new_tail_y += 1
    if head[1] < tail[1]:
        new_tail_y -= 1

    return [new_tail_x, new_tail_y]

def addToVisited(visited_dict, tail):
    if tail in visited_dict:
        visited_dict[tail] += 1
    else:
        visited_dict[tail] = 1


# Obtain input
move_instructions = [(line.strip().split()[0],  int(line.strip().split()[1]))
                    for line in open('2022/Day09/input.txt').readlines()]

# Part 1
head_pos = [0,0]
tail_pos = [0,0]
visited = {(0,0): 1}

for instr in move_instructions:
    direction, length = instr[0], instr[1]
    for _ in range(length):
        if direction == 'R':
            head_pos[0] += 1 
        elif direction == 'L':
            head_pos[0] -= 1
        elif direction == 'U':
            head_pos[1] += 1
        elif direction == 'D':
            head_pos[1] -= 1
        tail_pos = updateTailPosition(head_pos, tail_pos)
        addToVisited(visited, tuple(tail_pos))

print(f'Part 1: The tail of the rope visits {len(visited)} positions.')

# Part 2
visited.clear()
visited = {(0,0): 1}
head_pos = [0,0]
knot_pos =[[0,0]]*9

for instr in move_instructions:
    direction, length = instr[0], instr[1]
    for _ in range(length):
        if direction == 'R':
            head_pos[0] += 1
        elif direction == 'L':
            head_pos[0] -= 1
        elif direction == 'U':
            head_pos[1] += 1
        elif direction == 'D':
            head_pos[1] -= 1
        knot_pos[0] = updateTailPosition(head_pos, knot_pos[0])
        for i in range(1,len(knot_pos)):
            knot_pos[i] = updateTailPosition(knot_pos[i-1], knot_pos[i])
        addToVisited(visited, tuple(knot_pos[-1]))

print(f'Part 2: The tail of the longer rope visits {len(visited)} positions.')
