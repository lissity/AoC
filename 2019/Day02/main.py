def process_int_instructions(int_instructions_original, noun, verb):
    int_instructions = int_instructions_original.copy()     # Reset memory
    int_instructions[1] = noun
    int_instructions[2] = verb
    i = 0
    while i < len(int_instructions):
        instr = int_instructions[i]
        input_pos_1 = int_instructions[i+1]
        input_pos_2 = int_instructions[i+2]
        output_pos = int_instructions[i+3]
        if(instr == 1):
            int_instructions[output_pos] = int_instructions[input_pos_1] + int_instructions[input_pos_2]
        elif(instr == 2):
            int_instructions[output_pos] = int_instructions[input_pos_1] * int_instructions[input_pos_2]
        elif(instr == 99):
            return int_instructions[0]
        else:
            print('Something went wrong')
            return -1
        i += 4

# Obtain puzzle input
int_instructions_original = list(map(int, open('2019/Day02/input.txt','r').readline().strip().split(',')))

# First star
ret = process_int_instructions(int_instructions_original, 12, 2)
print('[part1] When the program halts the value at position 0 is {}'.format(ret))

# Second star
for noun in range(0, 100):
    for verb in range(0, 100):
        ret = process_int_instructions(int_instructions_original, noun, verb)
        if(ret == 19690720):
            print('[part2] 100 * noun + verb is {}'.format(100*noun+verb))
