from copy import deepcopy
def read_input(path):
    input = open(path,'r').read().splitlines()
    map = list()
    for y in input:
        row = list()
        for x in y:
            row.append(x)
        map.append(row)
    return map
def print_map(map):
    for y in map:
        row = ''
        for x in y:
            row += str(x)
        print(row)
def find_units(map):
    unit_list = list()
    y = 0
    for row in map:
        x = 0
        for symbol in row:
            if(symbol == 'G'):
                goblin = Unit('G',x,y)
                unit_list.append(goblin)
            elif(symbol == 'E'):
                elf = Unit('E',x,y)
                unit_list.append(elf)
            x +=1
        y +=1
    return unit_list
def get_adjacent_targets(targets, unit):
    x = unit.posX
    y = unit.posY
    adjacent = list()
    for t in targets:
        if(x == t.posX+1  and y == t.posY):
            adjacent.append(t)
        elif(x == t.posX-1 and y == t.posY):
            adjacent.append(t)
        elif(x == t.posX and y == t.posY+1):
            adjacent.append(t)
        elif(x == t.posX and y == t.posY-1):
            adjacent.append(t)
    return adjacent
def get_in_range_squares(targets, map):
    squares = list()
    for t in targets:
        x = t.posX
        y = t.posY
        if(map[y][x+1] == '.'):
            squares.append((x+1,y))
        if(map[y][x-1] == '.'):
            squares.append((x-1,y))
        if(map[y+1][x] == '.'):
            squares.append((x,y+1))
        if(map[y-1][x] == '.'):
            squares.append((x,y-1))
    return squares
def have_neighbor_number(unit, frontier_map):
    x = unit.posX
    y = unit.posY
    up = (x,y-1)
    down = (x,y+1)
    right = (x+1,y)
    left = (x-1,y)
    if(isinstance(frontier_map[up[1]][up[0]], int)):
        return True
    elif(isinstance(frontier_map[down[1]][down[0]], int)):
        return True
    elif(isinstance(frontier_map[right[1]][right[0]], int)):
        return True
    elif(isinstance(frontier_map[left[1]][left[0]], int)):
        return True
    return False
def add_fronts(frontier_map, frontier, current):
    up = (current[0], current[1]-1)
    down = (current[0], current[1]+1)
    right = (current[0]+1, current[1])
    left = (current[0]-1, current[1])
    if(frontier_map[up[1]][up[0]] == '.'):
        frontier.append([up[0], up[1], current[2]+1])
        frontier_map[up[1]][up[0]] = current[2]
    if(frontier_map[down[1]][down[0]] == '.'):
        frontier.append([down[0], down[1], current[2]+1])
        frontier_map[down[1]][down[0]] = current[2]
    if(frontier_map[right[1]][right[0]] == '.'):
        frontier.append([right[0], right[1], current[2]+1])
        frontier_map[right[1]][right[0]] = current[2]
    if(frontier_map[left[1]][left[0]] == '.'):
        frontier.append([left[0], left[1], current[2]+1])
        frontier_map[left[1]][left[0]] = current[2]
    return frontier_map, frontier
def add_neighbor_squares(frontier_map, squares, unit):
    x = unit.posX
    y = unit.posY
    up = (x,y-1)
    down = (x,y+1)
    right = (x+1,y)
    left = (x-1,y)
    if(isinstance(frontier_map[up[1]][up[0]], int)):
        s = Square(up[0], up[1], frontier_map[up[1]][up[0]])
        squares.append(s)
    if(isinstance(frontier_map[down[1]][down[0]], int)):
        s = Square(down[0], down[1], frontier_map[down[1]][down[0]])
        squares.append(s)
    if(isinstance(frontier_map[right[1]][right[0]], int)):
        s = Square(right[0], right[1], frontier_map[right[1]][right[0]])
        squares.append(s)
    if(isinstance(frontier_map[left[1]][left[0]], int)):
        s = Square(left[0], left[1], frontier_map[left[1]][left[0]])
        squares.append(s)
    return squares
def add_neighbor_squares_s(frontier_map, squares, square):
    x = square.x
    y = square.y
    up = (x,y-1)
    down = (x,y+1)
    right = (x+1,y)
    left = (x-1,y)
    if(isinstance(frontier_map[up[1]][up[0]], int)):
        s = Square(up[0], up[1], frontier_map[up[1]][up[0]])
        squares.append(s)
    if(isinstance(frontier_map[down[1]][down[0]], int)):
        s = Square(down[0], down[1], frontier_map[down[1]][down[0]])
        squares.append(s)
    if(isinstance(frontier_map[right[1]][right[0]], int)):
        s = Square(right[0], right[1], frontier_map[right[1]][right[0]])
        squares.append(s)
    if(isinstance(frontier_map[left[1]][left[0]], int)):
        s = Square(left[0], left[1], frontier_map[left[1]][left[0]])
        squares.append(s)
    return squares
def hit_point_sum(unit_list):
    hp_sum = 0
    for unit in unit_list:
        if(unit.alive == True):
            hp_sum += unit.hit_points
    return hp_sum
class Unit():
    def __init__(self, type, posX, posY):
        self.type = type
        self.posX = posX
        self.posY = posY
        self.attack_power = 3
        self.hit_points = 200
        self.alive = True
    def print_unit(self):
        print(self.type,'X:',self.posX, 'Y:', self.posY, 'HP:', self.hit_points)
    def __lt__(self, other):
        if(self.posY == other.posY):
            return self.posX < other.posX
        else:
            return self.posY < other.posY
    def make_move(self, new_square, map):
        map[self.posY][self.posX] = '.'
        map[new_square.y][new_square.x] = self.type
        self.posX = new_square.x
        self.posY = new_square.y
        return map
    def move(self, map, targets):
        frontier_map = deepcopy(map)
        frontier = list()
        frontier_map, frontier = add_fronts(frontier_map,frontier,
                                            [unit.posX,unit.posY,1])
        while(len(frontier)>0):
            current = frontier.pop(0)
            frontier_map, frontier = add_fronts(frontier_map, frontier,
                                                current)
        #pick out reachable targets based on the frontier map
        reachable = list()
        for tar in targets:
            if(have_neighbor_number(tar, frontier_map)):
                reachable.append(tar)
        if(len(reachable) == 0):
            return map
        #find the nearest target of the reachable ones.
        squares = list()
        for r in reachable:
            squares = add_neighbor_squares(frontier_map, squares, r)
        squares.sort()
        chosen = squares[0]
        #decide where the current unit should move
        s = Square(chosen.x,chosen.y,chosen.steps_needed)
        current = s
        while(current.steps_needed != 1):
            squares = list()
            squares = add_neighbor_squares_s(frontier_map, squares, current)
            squares.sort()
            current = squares[0]
        #go to current
        map = self.make_move(current, map)
        return map
    def attack(self, other, map):
        other.hit_points -= self.attack_power
        if(other.hit_points <= 0):
            other.alive = False
            map[other.posY][other.posX] = '.'
        return map
class Square():
    def __init__(self, x, y, steps_needed):
        self.x = x
        self.y = y
        self.steps_needed = steps_needed
    def print_square(self):
        print('X:',self.x, 'Y:',self.y, 'Steps:',self.steps_needed)
    def __lt__(self, other):
        if(self.steps_needed == other.steps_needed):
            if(self.y == other.y):
                return self.x < other.x
            else:
                return self.y < other.y
        else:
            return self.steps_needed < other.steps_needed
class Enemy():
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp
    def print_enemy(self):
        print('X:',self.x, 'Y:', self.y, 'HP:', self.hp)
    def __lt__(self, other):
        if(self.hp == other.hp):
            if(self.y == other.y):
                return self.x < other.x
            else:
                return self.y < other.y
        else:
            return self.hp < other.hp
map = read_input('2018/Day15/input.txt')
print_map(map)
units = find_units(map)
units.sort()

combat = True
round = 0
while(combat):
    units.sort()
    no_goblins = sum(u.type == 'G' and u.alive == True for u in units)
    no_elves = sum(u.type == 'E' and u.alive == True for u in units)
    for unit in units:
        end_turn = False
        if (unit.alive == False):
            end_turn = True
        if(not end_turn):
        #1. Identify possible targets
            targets = list()
            if(unit.type == 'E'):
                for u in units:
                    if u.type == 'G' and u.alive == True:
                        targets.append(u)
            elif(unit.type == 'G'):
                for u in units:
                    if u.type == 'E' and u.alive == True:
                        targets.append(u)
            # 1.2 if none remain: combat = False, break;
            if(len(targets) == 0):
                print('No targets remaining, combat is ending! #elves:', no_elves\
                , '#goblins:', no_goblins)
                print('Number of rounds completed:', round)
                print('Hit Point Sum:', hit_point_sum(units))
                print('Battle outcome: ' + str(hit_point_sum(units)) +' * '+ str(round) + ' = ' + str(hit_point_sum(units)*round))
                combat = False
                break
            #2 If not in range of a target:
            adj_targets = get_adjacent_targets(targets, unit)
            if(len(adj_targets) == 0):
                in_range = get_in_range_squares(targets, map)
                # if no open squares: end turn
                if(len(in_range) == 0):
                    end_turn = True
                # else: move
                if(not end_turn):
                    map = unit.move(map,targets)
                    #print_map(map)
        if(not end_turn):
            #3. attack if possible
            adj_targets = get_adjacent_targets(targets, unit)
            if(len(adj_targets) != 0):
            # ATTACK!
                enemies = list()
                for a in adj_targets:
                    enemy = Enemy(a.posX, a.posY, a.hit_points)
                    enemies.append(enemy)
                enemies.sort()
                chosen_target = enemies.pop(0)
                for tar in targets:
                    if(tar.posX == chosen_target.x and tar.posY == chosen_target.y):
                        other = tar
                map = unit.attack(other, map)
    print(round)
    print_map(map)
    round +=1
