input_line = open("2015/Day01/input.txt", "r").readline()

# Part 1
up = input_line.count('(')
down = input_line.count(')')
dest_floor = up - down
print('Part 1: The instructions takes Santa to floor #' + str(dest_floor))

# Part 2
floor_no = 0
index = 0
for char in input_line:
    if (char == '('):
        floor_no += 1
    if (char == ')'):
        floor_no -= 1
    if (floor_no == -1):
        print('Part 2: The position of the character that causes Sant to enter the basement is ' + str(index+1))
        break
    index += 1
