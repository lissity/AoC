import string
def read_input():
    input = open('2015/Day7/input.txt','r').read().splitlines()
    input_list = list()
    for line in input:
        splitted = line.split()
        if(splitted[0] == 'NOT'):
            tmp = [splitted[3], splitted[0], splitted[1]]
        elif(splitted[1] == '->'):
            tmp = [splitted[2], 'ASSIGN', splitted[0]]
        else:
            tmp = [splitted[4], splitted[1], splitted[0], splitted[2]]
        input_list.append(tmp)
    return input_list
def bit_not(n, numbits=16):
    return (1 << numbits) - 1 - n
def bit_and(n,p):
    return n&p
def bit_or(n,p):
    return n|p
def rshift(n, shift):
    return n>>shift
def lshift(n, shift):
    return n<<shift
def do_calc(input, known_values):
    arg1 = None
    arg2 = None
    #if(input[1] in ['NOT','ASSIGN']):
    if(input[2].isdigit()):
        arg1 = int(input[2])
    else:
        arg1 = known_values.get(input[2])
    if(input[1] in ['AND', 'OR', 'RSHIFT', 'LSHIFT']):
        if(input[3].isdigit()):
            arg2 = int(input[3])
        else:
            arg2 = known_values.get(input[3])
    if(input[1] == 'NOT'):
        r = bit_not(arg1)
        known_values[input[0]] = r
    elif(input[1] == 'ASSIGN'):
        r = arg1
        known_values[input[0]] = r
    elif(input[1] == 'AND'):
        r = bit_and(arg1,arg2)
        known_values[input[0]] = r
    elif(input[1] == 'OR'):
        r = bit_or(arg1,arg2)
        known_values[input[0]] = r
    elif(input[1] == 'RSHIFT'):
        r = rshift(arg1,arg2)
        known_values[input[0]] = r
    elif(input[1] == 'LSHIFT'):
        r = lshift(arg1,arg2)
        known_values[input[0]] = r
def check_possible(list_row, known):
    if(known.get(list_row[0]) != None): #already known this value!
        return False
    if(list_row[1] in ['ASSIGN', 'NOT']):
        if(known.get(list_row[2]) != None or list_row[2].isdigit()):
            return True
        else:
            return False
    else:
        if(((known.get(list_row[2])!=None) or (list_row[2].isdigit()) ) and ((known.get(list_row[3]) != None) or (list_row[3].isdigit()))):
            return True
        else:
            return False

input = read_input()

#Part1
known_values = dict()
keepgoing = True
while(keepgoing):
    keepgoing = False
    for u in input:
        if(check_possible(u, known_values)):
            do_calc(u, known_values)
            keepgoing = True
print('Signal to wire a: ' + str(known_values['a']))

#Part 2
known_values = dict()
known_values['b'] = 3176    #override b's value
keepgoing = True
while(keepgoing):
    keepgoing = False
    for u in input:
        if(check_possible(u, known_values)):
            do_calc(u, known_values)
            keepgoing = True

print('New signal to wire a: ' + str(known_values['a']))
