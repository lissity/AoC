def get_new_coord(direction, current_position):
    x = current_position[0]
    y = current_position[1]
    if (direction == '^'):
        y += 1
    elif (direction == 'v'):
        y -= 1
    elif (direction == '>'):
        x += 1
    elif (direction == '<'):
        x -= 1
    return (x, y)


input = open('2015/Day03/input.txt').readline()

# Part 1
current_position = (0, 0)
visited_coords = {(0, 0): True}
for direction in input:
    current_position = get_new_coord(direction, current_position)
    visited_coords[current_position] = True

print("Part 1: " + str(len(visited_coords)) +
      " houses receive at least one present on year 1.")

# Part 2
santa_current_pos = (0, 0)
robo_current_pos = (0, 0)
visited_coords = {(0, 0): True}
for i in range(0, len(input)):
    if (i % 2 == 0):  # Santa moves
        santa_current_pos = get_new_coord(input[i], santa_current_pos)
        visited_coords[santa_current_pos] = True
    else:  # Robo-Santa moves
        robo_current_pos = get_new_coord(input[i], robo_current_pos)
        visited_coords[robo_current_pos] = True

print("Part 2: " + str(len(visited_coords)) +
      " houses receive at least one present on year 2.")
