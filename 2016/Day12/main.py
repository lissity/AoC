def interpret_arg(arg1, registers):
    try:
        arg1 = int(arg1)
        return arg1
    except:
        return registers[arg1]

input = [l.strip().split() for l in open('2016/Day12/input.txt').readlines()]

# Part 1 registers
registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
# Part 2 registers
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

i = 0
while(i < len(input)):
    instr = input[i]
    cmd, arg1 = instr[0], instr[1]
    if (cmd in ['cpy', 'jnz']):
        arg2 = instr[2]
    if(cmd == 'cpy'):
        registers[arg2] = interpret_arg(arg1, registers)
    elif(cmd == 'jnz'):
        if(interpret_arg(arg1,registers) != 0):
            i += int(arg2)
            i -= 1              # To mitigate i+=1 (last in while-loop)
    elif(cmd == 'inc'):
        registers[arg1] += 1
    elif(cmd == 'dec'):
        registers[arg1] -= 1
    i += 1
print('The value in register a is {}'.format(registers['a']))
