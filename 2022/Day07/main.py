from anytree import Node, RenderTree

def calc_size(current_node, dirs):
    name = current_node.name.split()
    if len(name) == 2:                  # A file
        return int(name[0])
    else:                               # A directory
        size = 0
        for child in current_node.children:
            s = calc_size(child, dirs)
            size += s
        dirs.append((current_node.name, size))
        return size

# Obtain input
terminal_output = [line.strip() for line in open('2022/Day07/input.txt').readlines()]

# Creating a tree structure based on the terminal output
root = Node("/")
current_directory = None

for line in terminal_output:
    line = line.split()
    if line[0] == '$':          # Executed command
        if (line[1] == 'cd'):
            if (line[2] == '/'):
                current_directory = root
            elif (line[2] == '..'):
                current_directory = current_directory.parent
            else: 
                for child in current_directory.children:
                    if child.name == line[2]:
                        current_directory = child
                        break
    else:                       # Process output from 'ls'
        if line[0] == 'dir':    # Create new dir
            new_dir = Node(line[1], parent=current_directory)
        else:                   # Create new file
            filename = line[0] + ' ' + line[1]
            new_file = Node(filename, parent=current_directory)

# Part 1: Find directories with a total size of at most 100000
dirs = []
root_size = calc_size(root, dirs)
total_size = sum([d[1] for d in dirs if d[1] <= 100000])
print(f'Part 1: The sum of total sizes is {total_size}.')

# Part 2
total_space = 70000000
req_space = 30000000
free_space = total_space - root_size
needed_space = req_space - free_space

dirs_sorted_by_size = sorted(dirs, key=lambda tup: tup[1])
for directory in dirs_sorted_by_size:
    # Finding the smallest directory with a size is at least needed_disk_space
    if directory[1] >= needed_space:
        print(f'Part 2: The smallest directory to delete has a size of {directory[1]}.')
        break
