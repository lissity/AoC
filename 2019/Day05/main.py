def read_int(int_list, position, mode):
    int_at_position = int_list[position]
    if mode == 0:       # Position mode
        return int_list[int_at_position]
    elif mode == 1:     # Immediate mode
        return int_at_position

def process_int_instructions(int_list, input):
    output = 0
    i = 0
    while i < len(int_list):
        instr = str(int_list[i])
        op_code = int(instr[-1])
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
        if(op_code == 1):   # Add
            int_list[int_list[i+3]] = read_int(int_list, i+1, first_mode) \
                                    + read_int(int_list, i+2, second_mode)
            i += 4
        elif(op_code == 2): # Multiply
            int_list[int_list[i+3]] = read_int(int_list, i+1, first_mode) \
                                    * read_int(int_list, i+2, second_mode)
            i += 4
        elif(op_code == 3): # Read input
            int_list[int_list[i+1]] = input
            i += 2
        elif(op_code == 4): # Output
            output = read_int(int_list, i+1, first_mode)
            i += 2
        elif(op_code == 5): # Jump-if-true
            if(read_int(int_list, i+1, first_mode) != 0):
                i = read_int(int_list, i+2, second_mode)
            else:
                i += 3
        elif(op_code == 6): # Jump-if-false
            if(read_int(int_list, i+1, first_mode) == 0):
                i = read_int(int_list, i+2, second_mode)
            else:
                i += 3
        elif(op_code == 7): # Less than
            if(read_int(int_list, i+1, first_mode) < read_int(int_list, i+2, second_mode)):
                int_list[int_list[i+3]] = 1
            else:
                int_list[int_list[i+3]] = 0
            i += 4
        elif(op_code == 8): # Equals
            if(read_int(int_list, i+1, first_mode) == read_int(int_list, i+2, second_mode)):
                int_list[int_list[i+3]] = 1
            else:
                int_list[int_list[i+3]] = 0
            i += 4
        elif(op_code == 9): # Halt program
            return output
        else:
            print('Something went wrong...')
            return -1

# Obtain puzzle input
instructions = list(map(int, open('2019/Day05/input.txt','r').readline().strip().split(',')))

# Part 1
diagnostic_code = process_int_instructions(instructions.copy(), 1)
print('[part1] The program produces the diagnostic code {}'.format(diagnostic_code))

# Part 2
diagnostic_code = process_int_instructions(instructions.copy(), 5)
print('[part2] The program produces the diagnostic code {}'.format(diagnostic_code))
