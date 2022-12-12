class Node():
    """A node class for A* Pathfinding"""
    def __init__(self, parent=None, position=None, height='a'):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
        self.height = height

    def __eq__(self, other):
        return self.position == other.position

def manhattan(a, b):
    return sum([abs(a[0] - b[0]), abs(a[1] - b[1])])

def AStar(maze, start, goal):
    """Returns a list of tuples as a path from the given start to the given end
       in the given maze"""

    # Create start end goal nodes
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    start_node.height = ord(maze[start[1]][start[0]])
    goal_node = Node(None, goal)
    goal_node.g = goal_node.h = goal_node.f = 0
    goal_node.height = ord(maze[goal[1]][goal[0]])

    # Init open and closed dictionaries
    open = {}
    closed = {} 
    open[start] = start_node            # Add start node to open

    # Loop until the goal is reached
    while len(open) != 0:
        # Set current node to the node in open_list with the smallest f value
        cur_node = open[next(iter(open))]
        for pos, node in open.items():
            if node.f < cur_node.f:
                cur_node = node

        # Remove the current node from open_list and add it to closed_list
        del open[cur_node.position]
        closed[cur_node.position] = cur_node

        # Check if goal is found/reached
        if cur_node == goal_node:
            path = []
            current = cur_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = getNeighbours(maze, cur_node)
 
        # Loop through children
        for child in children:
            if child.position in closed:
                continue                    # Child is on the closed list

            # Create the f, g, and h values
            child.g = cur_node.g + 1                                    # Distance between child node and start node
            child.h = manhattan(child.position, goal_node.position)     # Estimated distance from child node to goal node (underestimation)
            child.f = child.g + child.h                                 # Total cost of the node, used when selecting which node in open to explore next
            
            # Check if child is already in the open list and has a worse g value
            if child.position in open and child.g > open[child.position].g:
                continue
            open[child.position] = child        # Add the child to the open list

def getNeighbours(maze, cur_node):
    pos = cur_node.position
    maze_max_x = len(maze[0]) - 1
    maze_max_y = len(maze) - 1
    neighbours = []
    for new_pos in [(0, -1), (0,1), (-1,0), (1,0)]: # Up, down, left, right
        node_pos = (pos[0] + new_pos[0],
                    pos[1] + new_pos[1])

        # Make sure node_pos is not outside the maze grid
        if (node_pos[0] < 0 or node_pos[1] < 0 or 
            node_pos[0] > maze_max_x or node_pos[1] > maze_max_y):
            continue

        # Make sure node_pos is traversable based on elevation rules
        cur_height = cur_node.height
        node_height = ord(maze[node_pos[1]][node_pos[0]])
        if (node_height > (cur_height+1)):    # Elevation is at most 1 higher than current
            continue

        # Create a node and append to children
        new_node = Node(cur_node, node_pos, node_height)
        neighbours.append(new_node)
    return neighbours

# Obtain input
heightmap = [list(line.strip()) for line in open('2022/Day12/input.txt').readlines()]
for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        if heightmap[y][x] == 'S':
            start = (x, y)
            heightmap[y][x] = 'a'
        if heightmap[y][x] == 'E':
            end = (x,y)
            heightmap[y][x] = 'z'

# Part 1
path = AStar(heightmap, start, end)
print(f'Part 1: The fewest steps to the goal is {len(path)-1}.')

# Part 2
elevation_a_squares = []
for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        if heightmap[y][x] == 'a':
            elevation_a_squares.append((x,y))

smallest_hike_length = float("inf")
for square in elevation_a_squares:
    path = AStar(heightmap, square, end)
    if path is not None:
        if len(path)-1 < smallest_hike_length:
            smallest_hike_length = len(path)-1
print(f'Part 2: The fewest steps to the goal from any square with elevation ' +
      f'\'a\' is {smallest_hike_length}.')
