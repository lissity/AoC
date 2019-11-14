input = open('2015/Day1/input.txt').readline()[:-1]

# Part 1
up = 0
down = 0
for paranthesis in input:
    if(paranthesis == '('):
        up += 1
    elif(paranthesis == ')'):
        down += 1

print('Floor: ' + str(up-down))

#Part 2
level = 0
pos = 1
for c in input:
    if(c == '('):
        level += 1
    elif(c == ')'):
        level -= 1
    if(level == -1):
        break
    pos += 1

print('First basement position: ' + str(pos))
