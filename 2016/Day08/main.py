from collections import deque

def create_rectangle(screen, width, height):
    for row in range(0, height):
        for col in range(0, width):
            screen[row][col] = "#"
    return screen

def rotate_row(screen, row, amount):
    row_copy = deque(screen[row].copy())
    row_copy.rotate(amount)
    screen[row] = list(row_copy)
    return screen

def rotate_col(screen, col, amount):
    col_copy = deque([screen[i][col] for i in range(0, len(screen))])
    col_copy.rotate(amount)
    col_copy = list(col_copy)
    for i in range(0, len(screen)):
        screen[i][col] = col_copy[i]
    return screen

def count_lit_pixels(screen):
    counter = 0
    for i in range(0, len(screen)):
        counter += screen[i].count('#')
    return counter

# Functions for debugging
def print_screen(screen):
    for row in screen:
        print(''.join(row))
    print('\n')

def reset_screen(screen):
    for row in range(0,len(screen)):
        for col in range(0,len(screen[row])):
            screen[row][col] = '.'
    return screen

# Obtain and parse instructions
input = [l.strip() for l in open('2016/Day08/input.txt', 'r').readlines()]
instructions = []
for item in input:
    item = item.split()
    instr = {}
    if(item[0] == 'rect'):
        instr['command'] = 'rect'
        args = item[1].split('x')
        instr['arg1'] = int(args[0])
        instr['arg2'] = int(args[1])
    elif(item[0] == 'rotate'):
        if(item[1] == 'row'):
            instr['command'] = 'rotaterow'
        elif(item[1] == 'column'):
            instr['command'] = 'rotatecol'
        instr['arg1'] = int(item[2].split('=')[1])
        instr['arg2'] = int(item[4])
    instructions.append(instr)

# Create 50x6 screen
screen = [[],[],[],[],[],[]]
for row in screen:
    for _ in range(0, 50):
        row.append('.')


for instr in instructions:
    if(instr['command'] == 'rect'):
        create_rectangle(screen, instr['arg1'], instr['arg2'])
    elif(instr['command'] == 'rotaterow'):
        rotate_row(screen, instr['arg1'], instr['arg2'])
    elif(instr['command'] == 'rotatecol'):
        rotate_col(screen, instr['arg1'], instr['arg2'])
print('[part1] The number of lit pixels are {}'.format(count_lit_pixels(screen)))
print('[part2] The screen is displaying:')
print_screen(screen)
