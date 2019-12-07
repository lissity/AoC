import itertools

class Amplifier:
    def __init__(self, instructions, ip, input):
        self.instructions = instructions
        self.ip = ip
        self.input = input
        self.finished = False

    def run(self, new_input):
        self.input.append(new_input)
        output, current_ip = process_int_instructions(self.instructions, self.input, self.ip)
        self.ip = current_ip
        if(current_ip == -1):
            self.finished = True
        return output

def read_int(int_list, position, mode):
    int_at_position = int_list[position]
    if mode == 0:       # Position mode
        return int_list[int_at_position]
    elif mode == 1:     # Immediate mode
        return int_at_position

def process_int_instructions(int_list, input, ip_start):
    output = 0
    i = ip_start
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
            if(len(input) != 0):
                int_list[int_list[i+1]] = input.pop(0)
            i += 2
        elif(op_code == 4): # Output
            output = read_int(int_list, i+1, first_mode)
            i += 2
            return output, i
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
            return output, -1
        else:
            print('Something went wrong...')
            return -1

# Obtain puzzle input
instructions = list(map(int, open('2019/Day07/input.txt','r').readline().strip().split(',')))

# -----Part1-----
# Get all possible combinations of phase settings
phase_settings = list(itertools.permutations(range(5), 5))

signals = []
for setting in phase_settings:
    next_input = 0
    for i in range(0,5):
        next_input, ip = process_int_instructions(instructions.copy(), [setting[i], next_input], 0)
    signals.append(next_input)
print('[part1] The highest signal sent to the thrusters is {}'.format(max(signals)))

# -----Part2-----
# Get all possible combinations of phase settings
phase_settings = list(itertools.permutations([5,6,7,8,9], 5))
signals = []
amp = {}
for setting in phase_settings:
    # Set up amplifiers
    amp['A'] = Amplifier(instructions.copy(), 0, [setting[0]])
    amp['B'] = Amplifier(instructions.copy(), 0, [setting[1]])
    amp['C'] = Amplifier(instructions.copy(), 0, [setting[2]])
    amp['D'] = Amplifier(instructions.copy(), 0, [setting[3]])
    amp['E'] = Amplifier(instructions.copy(), 0, [setting[4]])

    # Run amplifiers with feeedback loop
    ampAout = amp['A'].run(0)
    while(True):
        ampBout = amp['B'].run(ampAout)
        ampCout = amp['C'].run(ampBout)
        ampDout = amp['D'].run(ampCout)
        ampEout = amp['E'].run(ampDout)
        ampAout = amp['A'].run(ampEout)
        if(amp['A'].finished == True):
            signals.append(ampEout)
            break
print('[part2] With the feedback loop the highest signal sent to the thrusters'\
      ' is {}'.format(max(signals)))
