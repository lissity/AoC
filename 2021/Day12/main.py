def find_all_paths(graph, start, end, path=[], isPart2=False, small_cave_visited_twice=False):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if not isPart2: # Part 1
            if node.isupper() or node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        else:   # Part 2
            if node in ['start', 'end'] or node.isupper() or small_cave_visited_twice:
                if node.isupper() or node not in path:
                    newpaths = find_all_paths(graph, node, end, path, True, small_cave_visited_twice)
                    for newpath in newpaths:
                        paths.append(newpath)
            else:
                twice_visited = False
                if node in path:
                    twice_visited = True
                newpaths = find_all_paths(graph, node, end, path, True, twice_visited)
                for newpath in newpaths:
                    paths.append(newpath)
    return paths

# Obtain puzzle input
with open('2021/Day12/input.txt', 'r') as file:
    puzzle_input = [line.strip().split('-') for line in file.readlines()]
graph = {}
for path in puzzle_input:
    if path[0] in graph:
        graph[path[0]].append(path[1])
    else:
        graph[path[0]] = [path[1]]
    if path[1] in graph:
        graph[path[1]].append(path[0])
    else:
        graph[path[1]] = [path[0]]

# Part 1
paths = find_all_paths(graph, 'start', 'end')
print(f'Part 1: There are {len(paths)} paths through the cave system.')

# Part 2
paths = find_all_paths(graph, 'start', 'end', [], True)
print(f'Part 2: There are {len(paths)} paths through the cave system (when ' +
      f'a single small cave can be visited twice).')
