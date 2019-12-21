import arcade

def read_memory(int_dict, position):
    if position not in int_dict:
        return 0
    else:
        return int_dict[position]

def read_address(int_dict, position, mode , relative_base):
    if(mode == 0):
        return int_dict[position]
    elif(mode == 2):
        return int_dict[position] + relative_base
    else:
        print('Wrong')

def read_int(int_dict, position, mode, rel_base):
    int_at_position = read_memory(int_dict, position)
    if mode == 0:       # Position mode
        return read_memory(int_dict, int_at_position)
    elif mode == 1:     # Immediate mode
        return int_at_position
    elif mode == 2:     # Relative mode
        return read_memory(int_dict, int_at_position + rel_base)

def read_opcode(instruction):
    if(len(instruction) == 1):
        return '0' + instruction
    else:
        return instruction[-2:]

def process_int_instructions(int_dict, input_list, ip_start=0, relative_base=0):
    output = 0
    i = ip_start
    while i < len(int_dict):
        instr = str(int_dict[i])
        # print(i, instr, str(int_dict[i+1]))
        op_code = read_opcode(instr)
        # ---Set up parameter modes (0=position mode, 1=immediate mode)---
        first_mode, second_mode, third_mode = 0, 0, 0 # Default: Set all parameter modes to 0
        # If instruction specifies parameter modes - set them accordingly
        if(len(instr) >= 3):
            first_mode = int(instr[-3])
        if(len(instr) >= 4):
            second_mode = int(instr[-4])
        if(len(instr) >= 5):
            third_mode = int(instr[-5])

        # ---Interpret and execute instruction---
        if(op_code == '01'):   # Add
            address = read_address(int_dict, i+3, third_mode, relative_base)
            int_dict[address] = read_int(int_dict, i+1, first_mode, relative_base) \
                                    + read_int(int_dict, i+2, second_mode, relative_base)
            i += 4
        elif(op_code == '02'): # Multiply
            address = read_address(int_dict, i+3, third_mode, relative_base)
            int_dict[address] = read_int(int_dict, i+1, first_mode, relative_base) \
                                    * read_int(int_dict, i+2, second_mode, relative_base)
            i += 4
        elif(op_code == '03'): # Read input_list
            if(len(input_list) == 0):
                return None, i, relative_base
            if(len(input_list) != 0):
                int_dict[read_address(int_dict, i+1, first_mode, relative_base)] = input_list.pop()
            i += 2
        elif(op_code == '04'): # Output
            output = read_int(int_dict, i+1, first_mode, relative_base)
            i += 2
            return output, i, relative_base
        elif(op_code == '05'): # Jump-if-true
            if(read_int(int_dict, i+1, first_mode, relative_base) != 0):
                i = read_int(int_dict, i+2, second_mode, relative_base)
            else:
                i += 3
        elif(op_code == '06'): # Jump-if-false
            if(read_int(int_dict, i+1, first_mode, relative_base) == 0):
                i = read_int(int_dict, i+2, second_mode, relative_base)
            else:
                i += 3
        elif(op_code == '07'): # Less than
            address = read_address(int_dict, i+3, third_mode, relative_base)
            if(read_int(int_dict, i+1, first_mode, relative_base) < read_int(int_dict, i+2, second_mode, relative_base)):
                int_dict[address] = 1
            else:
                int_dict[address] = 0
            i += 4
        elif(op_code == '08'): # Equals
            address = read_address(int_dict, i+3, third_mode, relative_base)
            if(read_int(int_dict, i+1, first_mode, relative_base) == read_int(int_dict, i+2, second_mode, relative_base)):
                int_dict[address] = 1
            else:
                int_dict[address] = 0
            i += 4
        elif(op_code == '09'): # Adjust the relative base
            relative_base += read_int(int_dict, i+1, first_mode, relative_base)
            i += 2
        elif(op_code == '99'): # Halt program
            return output, -1, -1
        else:
            print('Something went wrong...')
            return -1

def list_to_objects(output_list):
    output_instr = []
    for i in range(0, len(output_list), 3):
        instr = [output_list[i], output_list[i+1], output_list[i+2]]
        output_instr.append(instr)
    no_blocks = len([instr[2] for instr in output_instr if instr[2]==2])
    objects = {}
    for object in output_instr:
        objects[(object[0], object[1])] = object[2]
    return objects

def get_ball_location(objects):
    for key, value in objects.items():
        if(value == 4):
            return key


def get_paddle_location(objects):
    for key, value in objects.items():
        if(value == 3):
            return key

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        self.timer = 0
        self.draw_objects = {}
        self.ball_location = []
        self.paddle_location = []

    def setup(self, instr_dict):
        # Set up your game here
        self.instr_dict_copy = instr_dict.copy()
        self.instr_dict_copy[0] = 2
        self.ip = 0
        self.rel_base = 0
        self.input_list = []
        self.output_list = []
        self.score = 0
        self.object_dict = {}
        self.gameEnd = False

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        arcade.set_viewport(-5,45,-5,45)

        # Create rectangles for all items in draw_objects
        for key, value in self.draw_objects.items():
            x = key[0]
            y = key[1]
            tile_id = value
            if(x == -1 and y == 0):
                self.score = tile_id
            elif(tile_id == 0):   # Empty tile
                rec = arcade.create_rectangle(x, y, 1, 1, arcade.color.WHITE)
                self.object_dict[(x,y)] = rec
            elif(tile_id == 1): # Wall
                rec = arcade.create_rectangle(x, y, 1, 1, arcade.color.BLACK)
                self.object_dict[(x,y)] = rec
            elif(tile_id == 2): # Block
                rec = arcade.create_rectangle(x, y, 1, 1, arcade.color.BROWN)
                self.object_dict[(x,y)] = rec
            elif(tile_id == 3): # Paddle
                self.paddle_location = [x,y]
                rec = arcade.create_rectangle(x, y, 1, 1, arcade.color.BLUE)
                self.object_dict[(x,y)] = rec
            elif(tile_id == 4): # Ball
                self.ball_location = [x, y]
                rec = arcade.create_rectangle(x, y, 1, 1, arcade.color.PINK)
                self.object_dict[(x,y)] = rec

        # Draw score on screen
        arcade.draw_text(str(self.score), 0, 30, arcade.color.BLACK, font_size=12)

        # Draw all rectangles in object_dict
        shape_list = arcade.ShapeElementList()
        for key, value in self.object_dict.items():
            shape_list.append(value)
        shape_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        if(self.gameEnd == False):      # Only update while game is in session
            runIntCode = True
            output_list = []
            while(runIntCode):
                self.output, self.ip, self.rel_base = process_int_instructions(self.instr_dict_copy, self.input_list, self.ip, self.rel_base)
                if(self.ip == -1):
                    changed_objects = list_to_objects(output_list)
                    self.draw_objects = changed_objects
                    self.score = changed_objects[(-1,0)]
                    print('[part2] Game ended! Score:', self.score)
                    self.gameEnd = True
                    runIntCode = False
                    break
                if(self.output == None and len(output_list) == 0):
                    if (self.ball_location[0] < self.paddle_location[0]):
                        self.input_list = [-1]
                    elif (self.ball_location[0] > self.paddle_location[0]):
                        self.input_list = [1]
                    else:
                        self.input_list = [0]
                    runIntCode = False
                elif(self.output == None):
                    break
                else:
                    output_list.append(self.output)
            changed_objects = list_to_objects(output_list)
            self.draw_objects = changed_objects

# Obtain puzzle input_list
instructions = list(map(int, open('2019/Day13/input.txt','r').readline().strip().split(',')))
# Convert list to dictionary
instr_dict = {}
i = 0
for integer in instructions:
    instr_dict[i] = integer
    i += 1

# --- Part 1 ---
# Initialize intcode computer values
ip = 0
rel_base = 0
input_list = []
output_list = []
instr_dict_copy = instr_dict.copy()

while(True):
    output, ip, rel_base = process_int_instructions(instr_dict_copy, input_list, ip, rel_base)
    if(ip == -1):
        break
    output_list.append(output)

output_instr = []
for i in range(0, len(output_list), 3):
    instr = [output_list[i], output_list[i+1], output_list[i+2]]
    output_instr.append(instr)
no_blocks = len([instr[2] for instr in output_instr if instr[2]==2])

print('[part1] The number of blocks tiles when the game exits is {}'.format(no_blocks))

# --- Part 2 ---

# Solution without graphics
instr_dict_copy = instr_dict.copy()
instr_dict_copy[0] = 2              # Insert 2 quarters to play for free
ip = 0
rel_base = 0
input_list = []
output_list = []
score = 0

while(True):
    output, ip, rel_base = process_int_instructions(instr_dict_copy, input_list, ip, rel_base)
    if(ip == -1):   # Game ended
        changed_objects = list_to_objects(output_list)
        score = changed_objects[(-1,0)]
        print('[part2] The score when the last block is broken is {}'.format(score))
        break
    if(output == None):     # Intcode computer needs input to continue
        changed_objects = list_to_objects(output_list)
        score = changed_objects[(-1,0)]
        ball_location = list(get_ball_location(changed_objects))
        paddle_location = list(get_paddle_location(changed_objects))
        if (ball_location[0] < paddle_location[0]):
            input_list = [-1]
        elif (ball_location[0] > paddle_location[0]):
            input_list = [1]
        else:
            input_list = [0]
    else:
        output_list.append(output)

# Solution with graphics
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
game.setup(instr_dict)
arcade.run()
