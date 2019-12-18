import numpy as np
import matplotlib.pyplot as plt

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

def process_int_instructions(int_dict, input, ip_start=0, relative_base=0):
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
        elif(op_code == '03'): # Read input
            if(len(input) != 0):
                int_dict[read_address(int_dict, i+1, first_mode, relative_base)] = input.pop()
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

def move(current_dir, current_pos, direction):
    x = current_pos[0]
    y = current_pos[1]
    if(direction == 0):     # turn left 90 degrees
        if(current_dir == 'up'):
            new_dir = 'left'
            new_pos = [x-1, y]
        elif(current_dir == 'down'):
            new_dir = 'right'
            new_pos = [x+1, y]
        elif(current_dir == 'right'):
            new_dir = 'up'
            new_pos = [x, y+1]
        elif(current_dir == 'left'):
            new_dir = 'down'
            new_pos = [x, y-1]
    elif(direction == 1):   # turn right 90 degrees
        if(current_dir == 'up'):
            new_dir = 'right'
            new_pos = [x+1, y]
        elif(current_dir == 'down'):
            new_dir = 'left'
            new_pos = [x-1, y]
        elif(current_dir == 'right'):
            new_dir = 'down'
            new_pos = [x, y-1]
        elif(current_dir == 'left'):
            new_dir = 'up'
            new_pos = [x, y+1]
    return new_pos, new_dir

def paint_panel(current_pos, color, painted_panels):
    painted_panels[tuple(current_pos)] = color

def get_panel_color(current_pos, painted_panels):
    if(tuple(current_pos) in painted_panels):
        return painted_panels[tuple(current_pos)]
    else:
        return 0    # 0 = black, all panels start out as black.

def runPaintingRobot(instructions, input_value):
    # Initialize robot start values
    direction = 'up'
    painted_panels = {}
    current_pos = [0,0]

    # Initialize intcode computer values
    ip = 0
    rel_base = 0
    input = [input_value]

    # Run robot using intcode computer
    while(True):
        # First output: Paint the panel the outputted color (0:black, 1:white)
        output, ip, rel_base = process_int_instructions(instr_dict, input, ip, rel_base)
        if(ip == -1):
            break
        paint_panel(current_pos, output, painted_panels)

        # Second output: Turn the robot (0:turn left, 1:turn right) and move the robot 1 step forward
        output, ip, rel_base = process_int_instructions(instr_dict, input, ip, rel_base)
        if(ip == -1):
            break
        current_pos, direction = move(direction, current_pos, output)

        # Check color of current panel and use as input
        input = [get_panel_color(current_pos, painted_panels)]
    return painted_panels

# Obtain puzzle input
instructions = list(map(int, open('2019/Day11/input.txt','r').readline().strip().split(',')))
# Convert list to dictionary
instr_dict = {}
i = 0
for integer in instructions:
    instr_dict[i] = integer
    i += 1

# --- Part 1 ---
painted_panels = runPaintingRobot(instr_dict.copy(), 0)
print('[part1] The robot paints {} panels at least once'.format(len(painted_panels)))

# --- Part 2 ---
painted_panels = runPaintingRobot(instr_dict.copy(), 1)

# Restructure data
black_tiles, white_tiles = [], []
for key, value in painted_panels.items():
    if(value == 0):
        black_tiles.append(key)
    elif(value == 1):
        white_tiles.append(key)

# Plot data
fig_size = [5, 0.7]
plt.rcParams["figure.figsize"] = fig_size
plt.scatter(*zip(*white_tiles), color='black')
plt.scatter(*zip(*black_tiles), color='white')
print('[part2] The robot paints the following registration identifier (see graph)')
plt.show()
