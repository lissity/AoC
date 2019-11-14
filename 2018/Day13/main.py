def read_input(path):
    return open(path,'r').read().splitlines()
def get_map(x,y,map):
    try:
        map_sym = map[y][x]
        return map_sym
    except:
        return ''
def get_map_c(xy, map):
    x = xy[0]
    y = xy[1]
    return map[y][x]
def update_map(xy,sym,map):
    x = xy[0]
    y = xy[1]
    map_row = map[y]
    new = map_row[:x] + sym + map_row[x+1:]
    map[y] = new
    return map
def find_carts(map):
    cart_coords = list()
    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] in ['<','^','>','v']):
                cart_coords.append((x,y))
    return cart_coords
def print_map(map):
    for y in map:
        print(y)
def number_of_carts_left(cart_list):
    counter = 0
    for c in cart_list:
        if c.out_of_order == False:
            counter += 1
    return counter
def find_missing_piece(coords, map):
    if get_map(coords[0], coords[1]+1, map) in ['|','/','\\','+']:
        if get_map(coords[0], coords[1]-1, map) in ['|','/','\\','+']:
            return '|'
    elif get_map(coords[0]+1, coords[1], map) in ['-','/','\\','+']:
        if get_map(coords[0]-1, coords[1], map) in ['-','|','/','\\','+']:
            return '-'
    return 'unknown'
class Cart:
    def __init__(self, coords, symbol):
        self.coords = coords
        self.symbol = symbol
        self.turn = 'L' # L, S, R
        self.standing_on = find_missing_piece(coords, map)
        self.out_of_order = False
    def print_cart(self):
        print(self.coords, ':',self.symbol, ':',self.standing_on)
    def __lt__(self, other):
        if(self.coords[1] == other.coords[1]):
            return self.coords[0] < other.coords[0]
        else:
            return self.coords[1] < other.coords[1]
    def remove_cart(self):
        update_map(self.coords, self.standing_on, map)
        self.out_of_order = True
    def turn_intersection(self):
        if(self.turn == 'S'):
            self.turn = 'R'
            return
        elif(self.turn == 'L'):
            if(self.symbol == '<'):
                self.symbol = 'v'
            elif(self.symbol == '>'):
                self.symbol = '^'
            elif(self.symbol == '^'):
                self.symbol = '<'
            elif(self.symbol == 'v'):
                self.symbol = '>'
            self.turn = 'S'
            return
        elif(self.turn == 'R'):
            if(self.symbol == '<'):
                self.symbol = '^'
            elif(self.symbol == '>'):
                self.symbol = 'v'
            elif(self.symbol == '^'):
                self.symbol = '>'
            elif(self.symbol == 'v'):
                self.symbol = '<'
            self.turn = 'L'
            return
    def turn_curve(self, curve_symbol):
        if(curve_symbol == '/'):
            if(self.symbol == '>'):
                self.symbol = '^'
            elif(self.symbol == 'v'):
                self.symbol = '<'
            elif(self.symbol == '<'):
                self.symbol = 'v'
            elif(self.symbol == '^'):
                self.symbol = '>'
        elif(curve_symbol == '\\'):
            if(self.symbol == '>'):
                self.symbol = 'v'
            elif(self.symbol == 'v'):
                self.symbol = '>'
            elif(self.symbol == '<'):
                self.symbol = '^'
            elif(self.symbol == '^'):
                self.symbol = '<'
        return
    def make_move(self, new_coords, map):
        tmp_sym = get_map_c(new_coords, map)
        update_map(self.coords, self.standing_on, map)
        update_map(new_coords, self.symbol, map)
        self.standing_on = tmp_sym
        self.coords = new_coords
    def move(self, map):
        if(self.symbol == 'v'):
            ahead = get_map(self.coords[0], self.coords[1]+1, map)
            new_coords = (self.coords[0], self.coords[1]+1)
        elif(self.symbol == '^'):
            ahead = get_map(self.coords[0], self.coords[1]-1, map)
            new_coords = (self.coords[0], self.coords[1]-1)
        elif(self.symbol == '<'):
            ahead = get_map(self.coords[0]-1, self.coords[1], map)
            new_coords = (self.coords[0]-1, self.coords[1])
        elif(self.symbol == '>'):
            ahead = get_map(self.coords[0]+1, self.coords[1], map)
            new_coords = (self.coords[0]+1, self.coords[1])
        if(ahead == '|'):
            self.make_move(new_coords, map)
        elif(ahead == '-'):
            self.make_move(new_coords, map)
        elif(ahead == '/'):
            self.turn_curve('/')
            self.make_move(new_coords, map)
        elif(ahead == '\\'):
            self.turn_curve('\\')
            self.make_move(new_coords, map)
        elif(ahead == '+'):
            self.turn_intersection()
            self.make_move(new_coords, map)
        elif(ahead in ['<','>','v','^']):
            print('CRASH', new_coords)
            return True, new_coords
        return False, (-1, -1)

def part1(map):
    #print_map(map)
    cart_coords = find_carts(map)
    cart_list = list()
    for coord in cart_coords:
        cart_sym = get_map_c(coord ,map)
        cart = Cart(coord, cart_sym)
        cart_list.append(cart)
    no_crash = True
    while(no_crash):
        cart_list.sort()
        for cart in cart_list:
            #cart.print_cart()
            ret = cart.move(map)
            if ret[0] == True:
                no_crash = False
                break
        #print_map(map)
def part2(map):
    #print_map(map)
    cart_coords = find_carts(map)
    cart_list = list()
    for coord in cart_coords:
        cart_sym = get_map_c(coord ,map)
        cart = Cart(coord, cart_sym)
        cart_list.append(cart)
    no_crash = True
    while(number_of_carts_left(cart_list)>1):
        cart_list.sort()
        remove_carts_at = list()
        for cart in cart_list:
            if(cart.out_of_order == False):
                ret = cart.move(map)
                if ret[0] == True:
                    cart.remove_cart()                    #remove first cart
                    for cart2 in cart_list:
                        if(cart2.coords == (ret[1][0], ret[1][1])):
                            cart2.remove_cart()           # remove second cart
    # Print answer:
    for cart in cart_list:
        if(cart.out_of_order == False):
            cart.print_cart()

print('Part1')
#map = read_input('2018/Day13/input_sample.txt')
#map = read_input('2018/Day13/input_sample2.txt')
map = read_input('2018/Day13/input.txt')
part1(map)
print('-------------------------------')
print('Part2')
map = read_input('2018/Day13/input.txt')
part2(map)
