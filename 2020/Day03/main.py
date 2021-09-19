from functools import reduce

# Obtain input
mymap = [line.strip() for line in open('2020/Day03/input.txt', 'r').readlines()]
map_width = len(mymap[0])
map_length = len(mymap)

# Part 1
current_location = [0,0]    # Starting location
slope = [3,1]
tree_count = 0

while (current_location[1] < map_length-1):
    current_location[0] += slope[0]
    current_location[1] += slope[1]
    x = current_location[0] % map_width
    if (mymap[current_location[1]][x]) == '#':
        tree_count += 1

print(f"Part 1: Encountered {tree_count} trees.")

# Part 2
current_location = [0,0]    # Starting location
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
tree_counts = []
tree_count = 0

for current_slope in slopes:
    while (current_location[1] < map_length-1):
        current_location[0] += current_slope[0]
        current_location[1] += current_slope[1]
        x = current_location[0] % map_width
        if (mymap[current_location[1]][x]) == '#':
            tree_count += 1
    tree_counts.append(tree_count)
    tree_count = 0              # Reset tree count
    current_location = [0,0]    # Reset starting location

print(f"Part 2: The number of trees encountered multiplied together is "
      f"{reduce(lambda x, y: x*y, tree_counts)}")