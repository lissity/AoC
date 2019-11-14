def read_initial_state():
    input = open('2018/Day12/input.txt','r').readline().split()
    state = '.....' + input[2] + '.....'
    zero_index = 5
    return state, zero_index

def read_rules():
    input = open('2018/Day12/input.txt','r').read().splitlines()[2:]
    rule_dict = dict()
    for rule in input:
        rule_dict[rule[0:5]] = rule[9:10]
    return rule_dict

def add_dots(state, zero_index):
    #add dots at beginning and end if needed
    splited = state.split('#')
    dots = 5 - splited[0].count('.')
    for i in range(dots):
        state = '.' + state
        zero_index += 1
    #count dots at zero_index
    dots = 0
    for i in range(len(state)-5, len(state)):
        if state[i] == '#':
            break   #stop count
        else:
            dots += 1
    dots = 5 - dots
    for i in range(dots):
        state = state + '.'
    return state, zero_index

def calc_pot_sum(state, zero_index):
    sum = 0
    point_value = 0
    if(zero_index >= 0):
        for i in range(zero_index, len(state)):
            if state[i] == '#':
                sum += point_value
            point_value += 1
        point_value = 0
        for i in range(zero_index, -1, -1):
            if state[i] == '#':
                sum += point_value
            point_value -= 1
    elif(zero_index < 0):
        point_value = abs(zero_index)
        for i in range(0, len(state)):
            if(state[i] == '#'):
                sum += point_value
            point_value +=1
    return sum

# Part 1
initial_state, pot_zero_position = read_initial_state()
rules = read_rules()
current_state = initial_state
print('0: ' + initial_state + ', len=' + str(len(initial_state)) + ', i=' + str(pot_zero_position))
for gen in range(1,21):     # 1-20
    new_state = ''
    for i in range(2, len(current_state)-2):
        pattern = current_state[i-2:i+3]
        if pattern in rules:
            new_state += rules[pattern]
        else:
            new_state += '.'
    pot_zero_position -= 2
    new_state, pot_zero_position = add_dots(new_state, pot_zero_position)
    current_state = new_state
    print(str(gen) + ': ' + current_state + ', len=' + str(len(current_state)) + ', i=' +str(pot_zero_position))
s = calc_pot_sum(current_state, pot_zero_position)
print(s)

# Part 2
initial_state, pot_zero_position = read_initial_state()
rules = read_rules()
current_state = initial_state
print('0: ' + initial_state + ', len=' + str(len(initial_state)) + ', i=' + str(pot_zero_position))
for gen in range(1,1001):
    new_state = ''
    for i in range(2, len(current_state)-2):
        pattern = current_state[i-2:i+3]
        if pattern in rules:
            new_state += rules[pattern]
        else:
            new_state += '.'
    pot_zero_position -= 2
    new_state, pot_zero_position = add_dots(new_state, pot_zero_position)
    current_state = new_state
    print(str(gen) + 'i= ' +str(pot_zero_position) + ': ' + current_state + ', len=' + str(len(current_state)) + ', i=' +str(pot_zero_position))
gen_left = 50000000000 - 1000
pot_zero_position = pot_zero_position - gen_left
print(pot_zero_position)
s = calc_pot_sum(current_state, pot_zero_position)
print(s)
