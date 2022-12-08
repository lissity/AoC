def isTreeVisible(row, col, tree_map):
    tree_height = int(tree_map[row][col])
    trees_col = [row[col] for row in tree_map]
    trees_above = trees_col[0:row]
    trees_below = trees_col[row+1:len(trees_col)]
    trees_right = tree_map[row][0:col]
    trees_left = tree_map[row][col+1:len(tree_map[0])]
    
    for trees in [trees_above, trees_below, trees_right, trees_left]:
        isVisible = all(int(tree) < tree_height for tree in trees)
        if (isVisible):
            return True
    return False        # The tree was not visible from any direction

def getScenicScore(row, col, tree_map):
    tree_height = int(tree_map[row][col])
    trees_col = [row[col] for row in tree_map]
    trees_above = reversed(trees_col[0:row])
    trees_below = trees_col[row+1:len(trees_col)]
    trees_right = reversed(tree_map[row][0:col])
    trees_left = tree_map[row][col+1:len(tree_map[0])]
    
    score = 1

    for trees in [trees_above, trees_below, trees_right, trees_left]:
        viewing_distance = 0
        for tree in trees:
            if int(tree) >= tree_height:
                viewing_distance += 1
                break
            viewing_distance += 1
        score *= viewing_distance
    return score

# Obtain input
tree_map = [list(line.strip()) for line in open('2022/Day08/input.txt').readlines()]
rows = len(tree_map)
cols = len(tree_map[0])

# Part 1
num_visible_trees = len(tree_map)*2 + (len(tree_map[0])-2)*2
for row_i in range(1, rows-1):
    for col_i in range(1, cols-1):      # Looping through trees excluding outer trees
        if (isTreeVisible(row_i, col_i, tree_map)):
            num_visible_trees += 1

print(f'Part 1: {num_visible_trees} trees are visible from outside the grid.')

# Part 2'
max_scenic_score = 0
for row_i in range(rows):
    for col_i in range(cols):      # Looping through trees
        score = getScenicScore(row_i, col_i, tree_map)
        if score > max_scenic_score:
            max_scenic_score = score

print(f'Part 2: The highest scenic score possible is {max_scenic_score}.')
