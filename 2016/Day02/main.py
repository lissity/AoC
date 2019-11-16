def find_keypad_button(start_pos_x, start_pos_y, instruction):
    # 1 2 3
    # 4 5 6
    # 7 8 9 ( keypad[x][y], keypad[0][0] starts at 7)
    keypad = [[7,4,1],[8,5,2],[9,6,3]]
    x, y = start_pos_x, start_pos_y
    for char in instruction:
        if ((char == 'U' and y == 2) or (char == 'D' and y == 0) or
            (char == 'R' and x == 2) or (char == 'L' and x == 0)):
            pass          # Doesn't lead to a button -> Ignore.
        elif(char == 'U'):
            y += 1          # Move up
        elif(char == 'D'):
            y -=1           # Move down
        elif(char == 'R'):
            x += 1          # Move right
        elif(char == 'L'):
            x -= 1          # Move left
    return (x, y), keypad[x][y];

def find_keypad_button_part2(start_pos_x, start_pos_y, instruction):
    # - - 1 - -
    # - 2 3 4 -
    # 5 6 7 8 9
    # - A B C -
    # - - D - - ( keypad[x][y], keypad[0][0] starts at '-' (bottom-left corner))
    keypad = [['-','-',5,'-','-'],['-','A',6,2,'-'],['D','B','7','3','1'],
              ['-','C',8,4,'-'], ['-','-',9,'-','-']]
    x, y = start_pos_x, start_pos_y
    for char in instruction:
        if ((char == 'U' and (y == 4 or keypad[x][y+1] == '-')) or
            (char == 'D' and (y == 0 or keypad[x][y-1] == '-')) or
            (char == 'R' and (x == 4 or keypad[x+1][y] == '-')) or
            (char == 'L' and (x == 0 or keypad[x-1][y] == '-'))):
            pass          # Doesn't lead to a button -> Ignore.
        elif(char == 'U'):
            y += 1          # Move up
        elif(char == 'D'):
            y -=1           # Move down
        elif(char == 'R'):
            x += 1          # Move right
        elif(char == 'L'):
            x -= 1          # Move left
    return (x, y), keypad[x][y];

#---- First star ----#
# Obtain instructions
instructions = [instr.strip() for instr in open('2016/Day02/input.txt', 'r').readlines()]
pos_x, pos_y = 1, 1                 # starting position at button 5
code = ''
for instr in instructions:
    new_pos, button_value = find_keypad_button(pos_x, pos_y,instr)
    pos_x, pos_y = new_pos[0], new_pos[1]
    code += str(button_value)
print('[part1] The code presumably is {}.'.format(code))

#---- Second star ----#
pos_x, pos_y = 0, 2              # starting position at button 5 (on new keypad)
code = ''
for instr in instructions:
    new_pos, button_value = find_keypad_button_part2(pos_x, pos_y,instr)
    pos_x, pos_y = new_pos[0], new_pos[1]
    code += str(button_value)
print('[part2] The code actually is {}.'.format(code))
