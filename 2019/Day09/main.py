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
        elif(op_code == '09'): # Adjust the relative relative base
            relative_base += read_int(int_dict, i+1, first_mode, relative_base)
            i += 2
        elif(op_code == '99'): # Halt program
            return output, -1, -1
        else:
            print('Something went wrong...')
            return -1

def runIntComputer(instructions, input_value):
    ip = 0
    rel_base = 0
    input = [input_value]
    output_list = []
    while(True):
        output, ip, rel_base = process_int_instructions(instructions, input, ip, rel_base)
        if(ip == -1):
            break
        output_list.append(output)
    return output_list

# Obtain puzzle input
instructions = list(map(int, open('2019/Day09/input.txt','r').readline().strip().split(',')))

# Convert list to dictionary
instr_dict = {}
i = 0
for integer in instructions:
    instr_dict[i] = integer
    i += 1

#-----Part1-----
output = runIntComputer(instr_dict.copy(), 1)
print('[part1] The BOOST keycode is {}'.format(output))

#-----Part2-----
output = runIntComputer(instr_dict.copy(), 2)
print('[part1] The coordinates of the distress signal are {}'.format(output))
