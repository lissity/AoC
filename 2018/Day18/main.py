def read_input(path):
    input = open(path,'r').read().splitlines()
    map = list()
    for line in input:
        listrow = list()
        for c in line:
            listrow.append(c)
        map.append(listrow)
    return map

def print_map(map):
    for row in map:
        line = ''
        for char in row:
            line += char
        print(line)
def count_adj(map, coords, symbol):
    x = coords[0]
    y = coords[1]
    x_range = len(map)
    y_range = len(map[0])
    adjacent_squares = list()
    if((x-1) >= 0):
        if((y-1) >= 0):
            adjacent_squares.append((x-1,y-1))
        adjacent_squares.append((x-1,y))
        if((y+1) < y_range):
            adjacent_squares.append((x-1,y+1))
    if((x+1) < x_range):
        if((y-1) >= 0):
            adjacent_squares.append((x+1,y-1))
        adjacent_squares.append((x+1,y))
        if((y+1) < y_range):
            adjacent_squares.append((x+1,y+1))
    if((y-1) >= 0):
        adjacent_squares.append((x,y-1))
    if((y+1) < y_range):
        adjacent_squares.append((x,y+1))
    count = 0
    for square in adjacent_squares:
        if(map[square[1]][square[0]] == symbol):
            count += 1
    return count

def create_next_map(map):
    new_map = list()
    for y in range(len(map)):
        new_row = list()
        for x in range(len(map[0])):
            acre = map[y][x]
            adj_open = count_adj(map, (x,y), '.')
            adj_tree = count_adj(map, (x,y), '|')
            adj_lumber = count_adj(map, (x,y), '#')
            if(acre == '.'):
                if(adj_tree >= 3):
                    new_row.append('|')
                else:
                    new_row.append('.')
            elif(acre == '|'):
                if(adj_lumber >= 3):
                    new_row.append('#')
                else:
                    new_row.append('|')
            elif(acre == '#'):
                if(adj_tree >= 1 and adj_lumber >= 1):
                    new_row.append('#')
                else:
                    new_row.append('.')
        new_map.append(new_row)
    return new_map

def count_symbol_in_map(map,symbol):
    count = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if(map[y][x] == symbol):
                count += 1
    return count

#map = read_input('2018/Day18/input_sample.txt')
map = read_input('2018/Day18/input.txt')
print_map(map)
current = map
for i in range(10):
    new_map = create_next_map(current)
    current=new_map
print('\n')
print_map(new_map)
trees = count_symbol_in_map(new_map,'|')
lumber = count_symbol_in_map(new_map,'#')
print('Trees:',trees)
print('Lumberyards:',lumber)
print('Resouce value:', trees*lumber)
