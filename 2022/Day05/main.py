def create_stack_start_state(input_stacks, num_of_stacks):
    crate_letter_index = 1
    for i in range(num_of_stacks):
        for row in reversed(input_stacks):
            crate = row[crate_letter_index]
            if (crate == ' '):
                break
            stacks[i].append(row[crate_letter_index])
        crate_letter_index += 4

# Obtain input
puzzle_input = open('2022/Day05/input.txt').readlines()

# Reading the two-part input into different lists
stacks_input = []
instructions = []
reading_stacks = True
for line in puzzle_input:
    if (line == '\n'):
        reading_stacks = False
    elif (line[1] == '1'):
        tmp = line.strip().split(' ')
        number_of_stacks = int(tmp[-1])
    elif reading_stacks:
        stacks_input.append(line)
    else:
        instructions.append(line.strip().split(' '))

# Creating the empty stacks
stacks = [[] for i in range(number_of_stacks)]

# Reading the input stacks and placing them in the correct stack
create_stack_start_state(stacks_input, number_of_stacks)

# Part 1
# Reading instructions and moving crates between stacks
for instr in instructions:
    crates_to_move = int(instr[1])
    from_stack = int(instr[3])
    to_stack = int(instr[5])

    # Move one crate at the time using pop and push between stacks
    for _ in range(crates_to_move):
        crate = stacks[from_stack-1].pop()
        stacks[to_stack-1].append(crate)

part1answer = ''.join([stack[-1] for stack in stacks])
print(f'Part 1: The crates at the top of each stack are {part1answer}.')

# Part 2
stacks = [[] for i in range(number_of_stacks)]
create_stack_start_state(stacks_input, number_of_stacks)

# Read instructions
for instr in instructions:
    crates_to_move, from_stack, to_stack = int(instr[1]), int(instr[3]), int(instr[5])
    crates = stacks[from_stack-1][-crates_to_move:]     # Get the crates
    del stacks[from_stack-1][-crates_to_move:]          # Remove crates from one stack
    stacks[to_stack-1].extend(crates)                   # Add crates to another stack

part2answer = ''.join([stack[-1] for stack in stacks])
print(f'Part 2: The crates at the top of each stack are {part2answer}.')
