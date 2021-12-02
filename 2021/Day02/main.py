# Obtain input
commands = [line.strip().split() for line in open('2021/Day02/input.txt', 'r').readlines()]
commands = [(c[0], int(c[1])) for c in commands]

# Part 1
horizontal_pos = 0
depth = 0
for command in commands:
    if (command[0] == 'forward'):
        horizontal_pos += command[1]
    elif (command[0] == 'down'):
        depth += command[1]
    elif (command[0] == 'up'):
        depth -= command[1]

print(f'Depth multiplied by horizontal position is {depth * horizontal_pos}.')

# Part 2
horizontal_pos = 0
depth = 0
aim = 0
for command in commands:
    if (command[0] == 'forward'):
        horizontal_pos += command[1]
        depth += aim * command[1]
    elif (command[0] == 'down'):
        aim += command[1]
    elif (command[0] == 'up'):
        aim -= command[1]

print(f'Depth multiplied by horizontal position is {depth * horizontal_pos}.')